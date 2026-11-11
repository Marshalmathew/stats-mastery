"""
ingest_checkpoint.py
====================
Automated tool to ingest, organize, and commit incoming stats-mastery checkpoint ZIPs.

Usage:
    python ingest_checkpoint.py                     # Auto-detects newest unprocessed ZIP
    python ingest_checkpoint.py path/to/file.zip    # Ingests specific ZIP file
"""

import os
import sys
import glob
import shutil
import zipfile
import re
import subprocess
from datetime import datetime

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
SNAPSHOTS_DIR = os.path.join(WORKSPACE, ".snapshots")
os.makedirs(SNAPSHOTS_DIR, exist_ok=True)

def get_item_order_key(tag):
    m = re.search(r"Stage\s*(\d+)\s*·\s*item[s]?\s*([\d–-]+)", tag, re.IGNORECASE)
    if not m:
        return 9999.0
    stage = int(m.group(1))
    item_str = m.group(2)
    first_num = float(re.match(r'\d+', item_str).group(0))
    has_range = '–' in item_str or '-' in item_str
    return stage * 1000 + first_num + (0.5 if has_range else 0.0)

def fix_and_sort_index_html(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Sort COURSES array
    courses_match = re.search(r'const COURSES=\[\s*(.*?)\s*\];', content, re.DOTALL)
    if courses_match:
        courses_str = courses_match.group(1)
        raw_entries = []
        for line in courses_str.splitlines():
            line_s = line.strip()
            if line_s:
                if line_s.endswith(','):
                    line_s = line_s[:-1]
                raw_entries.append(line_s)

        def entry_sort_key(line):
            tag_m = re.search(r"tag:'([^']+)'", line)
            return get_item_order_key(tag_m.group(1)) if tag_m else 9999.0

        sorted_entries = sorted(raw_entries, key=entry_sort_key)
        new_courses_str = 'const COURSES=[\n ' + ',\n '.join(sorted_entries) + '\n];'
        content = content[:courses_match.start()] + new_courses_str + content[courses_match.end():]

    # 2. Ensure runtime sort exists before render
    if "COURSES.sort(" not in content:
        render_target = "document.getElementById('courses').innerHTML=COURSES.map"
        sort_snippet = ("function itemKey(tag){const m=tag.match(/Stage\\s*(\\d+)\\s*·\\s*items?\\s*([\\d–-]+)/i);"
                        "if(!m)return 9999;const s=parseInt(m[1],10),p=m[2].split(/[–-]/);"
                        "return s*1000+parseFloat(p[0])+(p.length>1?0.5:0)}\n"
                        "COURSES.sort((a,b)=>itemKey(a.tag)-itemKey(b.tag));\n"
                        + render_target)
        content = content.replace(render_target, sort_snippet)

    # 3. Ensure Multiple Testing is in Stage 5, not Stage 4 in roadmap ST
    bad_st = "['Multiple testing and selective inference',{f:'multiple-testing-mastery.html'}]]],"
    if bad_st in content:
        # Move from Stage 4 to Stage 5
        content = content.replace(bad_st, "]]],")
        stage5_marker = "['Stage 5 · Causal thinking',[\n"
        if stage5_marker in content and "['Multiple testing" not in content.split(stage5_marker)[1]:
            content = content.replace(stage5_marker, stage5_marker + "  ['Multiple testing and selective inference',{f:'multiple-testing-mastery.html'}],")

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_readme(workspace):
    index_path = os.path.join(workspace, "index.html")
    if not os.path.exists(index_path):
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        idx_content = f.read()

    cards = re.findall(r"\{f:'([^']+)',key:'([^']+)',tag:'([^']+)',t:'([^']+)',d:'([^']+)',m:\[([^\]]+)\]\}", idx_content)
    total_chapters = 0
    total_labs = 0
    total_questions = 0
    for f, k, tag, t, d, m in cards:
        ch = re.search(r'(\d+)\s*chapters?', m)
        lb = re.search(r'(\d+)\s*labs?', m)
        qu = re.search(r'(\d+)\s*(-question|\s*questions?)', m)
        if ch: total_chapters += int(ch.group(1))
        if lb: total_labs += int(lb.group(1))
        if qu: total_questions += int(qu.group(1))

    readme_path = os.path.join(workspace, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme = f.read()

        # Update numbers in overview
        pattern = r"comprising \*\*\d+ modules\*\*, \*\*\d+ chapters\*\*, \*\*\d+ interactive simulation labs\*\*, and \*\*\d+ exam questions\*\*"
        repl = f"comprising **{len(cards)} modules**, **{total_chapters} chapters**, **{total_labs} interactive simulation labs**, and **{total_questions} exam questions**"
        readme = re.sub(pattern, repl, readme)

        # Update top badge
        top_pattern = r">\s*\d+ comprehensive, self-contained interactive modules"
        top_repl = f"> {len(cards)} comprehensive, self-contained interactive modules"
        readme = re.sub(top_pattern, top_repl, readme)

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme)

def find_unprocessed_zips():
    # Any zip in workspace root is newly arrived
    root_zips = [os.path.join(WORKSPACE, f) for f in os.listdir(WORKSPACE) if f.endswith('.zip')]
    return sorted(root_zips, key=os.path.getmtime)

def ingest_zip(zip_path):
    print(f"\n==========================================")
    print(f"Ingesting checkpoint: {os.path.basename(zip_path)}")
    print(f"==========================================")

    mtime = os.path.getmtime(zip_path)
    dt_iso = datetime.fromtimestamp(mtime).strftime('%Y-%m-%dT%H:%M:%S')

    extracted_new = []
    with zipfile.ZipFile(zip_path, 'r') as z:
        for member in z.infolist():
            if member.is_dir() or member.filename.endswith('/'):
                continue
            rel_name = member.filename
            if rel_name.startswith("stats-mastery/"):
                rel_name = rel_name[len("stats-mastery/"):]

            target_path = os.path.join(WORKSPACE, rel_name)
            is_new = not os.path.exists(target_path)
            with open(target_path, 'wb') as out_f:
                out_f.write(z.read(member.filename))

            if is_new and rel_name.endswith('.html') and rel_name != 'index.html':
                extracted_new.append(rel_name)

    print(f"Extracted files. New modules detected: {len(extracted_new)}")
    for mod in extracted_new:
        print(f"  + {mod}")

    # Fix and sort index.html
    index_path = os.path.join(WORKSPACE, "index.html")
    fix_and_sort_index_html(index_path)
    print("index.html sorted and verified.")

    # Update README
    update_readme(WORKSPACE)
    print("README.md metrics updated.")

    # Move zip to .snapshots
    dst_snap = os.path.join(SNAPSHOTS_DIR, os.path.basename(zip_path))
    if os.path.abspath(zip_path) != os.path.abspath(dst_snap):
        shutil.move(zip_path, dst_snap)
    print(f"Archived snapshot into {dst_snap}")

    # Git commit
    env = os.environ.copy()
    env["GIT_AUTHOR_DATE"] = dt_iso
    env["GIT_COMMITTER_DATE"] = dt_iso

    msg = f"Ingest checkpoint {os.path.basename(zip_path)}"
    if extracted_new:
        msg += f": add {', '.join(extracted_new)}"

    subprocess.run(["git", "add", "-A"], cwd=WORKSPACE, check=True)
    res = subprocess.run(["git", "commit", "-m", msg], cwd=WORKSPACE, env=env, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Committed to Git: {msg}")
    else:
        print(f"Git status: {res.stdout.strip() or res.stderr.strip()}")

def main():
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if os.path.exists(target):
            ingest_zip(target)
        else:
            print(f"File not found: {target}")
    else:
        zips = find_unprocessed_zips()
        if not zips:
            print("No pending ZIP files found in workspace root.")
            print("To re-sort and verify the current workspace, checking index.html...")
            fix_and_sort_index_html(os.path.join(WORKSPACE, "index.html"))
            update_readme(WORKSPACE)
            res = subprocess.run(["git", "status", "--porcelain"], cwd=WORKSPACE, capture_output=True, text=True)
            if res.stdout.strip():
                subprocess.run(["git", "add", "-A"], cwd=WORKSPACE, check=True)
                subprocess.run(["git", "commit", "-m", "Ensure runtime sort and index order consistency"], cwd=WORKSPACE, check=True)
                print("Applied and committed verification updates.")
            else:
                print("Workspace is already up to date and clean.")
            return

        for z in zips:
            ingest_zip(z)

if __name__ == "__main__":
    main()
