# Stats Mastery

> **The complete interactive visual curriculum for statistical mastery.**
>
> 31 comprehensive, self-contained interactive modules covering probability, classical inference, regression, causal inference, Bayesian modeling, and specialist depth — with interactive simulations, formula proofs, and self-assessment exams.

---

## 🚀 Quick Start

**No build tools, bundlers, or server runtimes required.**

Simply open `index.html` in any modern web browser:

```bash
# Windows
start index.html

# macOS
open index.html

# Linux
xdg-open index.html
```

Or serve locally with any static web server:

```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000`.

---

## 📊 Curriculum Overview

The curriculum is structured across 7 progressive stages comprising **31 modules**, **386 chapters**, **364 interactive simulation labs**, and **552 exam questions**.

### Stage 1 · Foundations & Probability Theory
1. [`random-variables-mastery.html`](random-variables-mastery.html) — **Random Variables, Expectation, Variance & Covariance** (15 chapters, 14 labs, 16 exam questions)
2. [`core-distributions.html`](core-distributions.html) — **Core Distributions and How They Relate** (14 chapters, 17 labs, 16 exam questions)
3. [`bayes-conditional-probability.html`](bayes-conditional-probability.html) — **Conditional Probability and Bayes’ Theorem** (12 chapters, 12 labs, 16 exam questions)
4. [`lln-clt-mastery.html`](lln-clt-mastery.html) — **Law of Large Numbers & Central Limit Theorem** (14 chapters, 14 labs, 18 exam questions)

### Stage 2 · Classical Estimation & Inference
5. [`sampling-estimators-mastery.html`](sampling-estimators-mastery.html) — **Sampling Distributions, Standard Errors & Estimators** (13 chapters, 12 labs, 18 exam questions)
6. [`mle-mastery.html`](mle-mastery.html) — **Maximum Likelihood Estimation (MLE)** (12 chapters, 11 labs, 18 exam questions)
7. [`confidence-intervals-mastery.html`](confidence-intervals-mastery.html) — **Confidence Intervals** (12 chapters, 11 labs, 18 exam questions)
8. [`bootstrap-resampling-mastery.html`](bootstrap-resampling-mastery.html) — **Bootstrap and Resampling Methods** (12 chapters, 11 labs, 18 exam questions)
9. [`p-value-mastery.html`](p-value-mastery.html) — **P-Values from Scratch to Expert** (14 chapters, 15 labs, 20 exam questions)
10. [`power-design-mastery.html`](power-design-mastery.html) — **Hypothesis Testing, Power & Experimental Design** (12 chapters, 11 labs, 18 exam questions)

### Stage 3 · Regression & Linear Models
11. [`linear-regression-mastery.html`](linear-regression-mastery.html) — **Linear Regression Done Properly** (12 chapters, 11 labs, 18 exam questions)
12. [`collinearity-interactions-mastery.html`](collinearity-interactions-mastery.html) — **Multicollinearity, Interactions & Nonlinearity** (12 chapters, 11 labs, 18 exam questions)
13. [`glm-mastery.html`](glm-mastery.html) — **Generalized Linear Models (GLM)** (12 chapters, 11 labs, 18 exam questions)
14. [`regularisation-mastery.html`](regularisation-mastery.html) — **Regularisation: Ridge, Lasso & Elastic Net** (12 chapters, 11 labs, 18 exam questions)
15. [`model-selection-mastery.html`](model-selection-mastery.html) — **Model Selection** (12 chapters, 11 labs, 18 exam questions)

### Stage 4 · Real-World Data Complexity
16. [`calibration-scoring-mastery.html`](calibration-scoring-mastery.html) — **Calibration and Proper Scoring Rules** (12 chapters, 11 labs, 18 exam questions)
17. [`imbalanced-rare-events-mastery.html`](imbalanced-rare-events-mastery.html) — **Imbalanced Data & Rare Events** (12 chapters, 11 labs, 18 exam questions)
18. [`survival-analysis-mastery.html`](survival-analysis-mastery.html) — **Survival & Time-to-Event Analysis** (12 chapters, 11 labs, 18 exam questions)
19. [`missing-data-mastery.html`](missing-data-mastery.html) — **Missing Data Mechanisms & Imputation** (12 chapters, 11 labs, 18 exam questions)
20. [`dependent-data-mastery.html`](dependent-data-mastery.html) — **Dependent Data: Time Series, Panels & Mixed Models** (12 chapters, 11 labs, 18 exam questions)

### Stage 5 · Causal Inference & Experimentation
21. [`multiple-testing-mastery.html`](multiple-testing-mastery.html) — **Multiple Testing and Selective Inference** (12 chapters, 11 labs, 18 exam questions)
22. [`confounding-selection-mastery.html`](confounding-selection-mastery.html) — **Confounding, Selection Bias & Simpson’s Paradox** (12 chapters, 11 labs, 18 exam questions)
23. [`experiments-ab-mastery.html`](experiments-ab-mastery.html) — **Potential Outcomes, A/B Testing & CUPED** (12 chapters, 11 labs, 18 exam questions)
24. [`observational-causal-mastery.html`](observational-causal-mastery.html) — **Observational Causal Methods (Matching, IPW, DiD, IV, RDD)** (12 chapters, 11 labs, 18 exam questions)
25. [`uplift-heterogeneous-mastery.html`](uplift-heterogeneous-mastery.html) — **Uplift & Heterogeneous Treatment Effects** (12 chapters, 11 labs, 18 exam questions)

### Stage 6 · Bayesian & Probabilistic Modelling
26. [`bayesian-inference-mastery.html`](bayesian-inference-mastery.html) — **Bayesian Inference & Conjugate Updating** (12 chapters, 11 labs, 18 exam questions)
27. [`mcmc-variational-mastery.html`](mcmc-variational-mastery.html) — **MCMC and Variational Inference** (12 chapters, 11 labs, 18 exam questions)
28. [`hierarchical-models-mastery.html`](hierarchical-models-mastery.html) — **Hierarchical (Partial Pooling) Models** (12 chapters, 11 labs, 18 exam questions)
29. [`bayesian-decision-theory-mastery.html`](bayesian-decision-theory-mastery.html) — **Bayesian Decision Theory & Utility** (12 chapters, 11 labs, 18 exam questions)

### Stage 7 · Specialist Depth
30. [`multivariate-methods-mastery.html`](multivariate-methods-mastery.html) — **Multivariate Methods (PCA, Factor Analysis, Mixtures & Mahalanobis)** (12 chapters, 11 labs, 18 exam questions)
31. [`extreme-value-theory-mastery.html`](extreme-value-theory-mastery.html) — **Extreme Value Theory and Heavy Tails** (12 chapters, 11 labs, 18 exam questions)

---

## 📁 Repository Structure

```
stats-mastery/
├── index.html                           # Main entry point and curriculum dashboard
├── *.html                               # 31 interactive mastery learning modules
├── README.md                            # Project documentation
├── .gitignore                           # Repository exclusions
└── .snapshots/                          # Archived incremental ZIP snapshots (ignored)
```

---

## 📜 License & Acknowledgments

All rights reserved by the author. Created and iteratively developed from October to November 2026.

