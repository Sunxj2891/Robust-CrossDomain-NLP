# Robust Cross-Domain NLP Generalisation with Residual Fusion

Code and experimental data for cross-domain text classification under domain shift. This project evaluates domain-invariant feature stability across heterogeneous corpora (GoEmotions to IMDb) and implements an Out-Of-Fold (OOF) residual fusion layer to calibrate overconfident misclassifications.

[Interactive Demo](https://sunxj2891.github.io/Robust-CrossDomain-NLP/) | [Paper PDF](docs/NLP4Health_assignment3.pdf)

---

## Benchmark Results

Evaluation on GoEmotions (Source) and IMDb (Target):

| Model | Source Val F1 | Target Test F1 | High-Confidence Error Correction Rate (HC-ECR, Conf > 0.90) |
| :--- | :---: | :---: | :---: |
| DistilBERT (Text-only Baseline) | 87.2% | 73.7% | 0.0% |
| Early Fusion Model | 88.6% | 73.7% | 10.2% |
| **Residual Fusion (Ours)** | **89.5%** | **74.1%** | **18.7%** |

### Key Observations
* **Feature Stability**: 42 stylistic and structural features were evaluated using Kolmogorov-Smirnov (KS) tests, Benjamini-Hochberg FDR corrections, and Jensen-Shannon Divergence (JSD). Structural and stylistic features showed substantially lower distribution shift (mean JSD: 0.04) compared to surface lexical terms (mean JSD: 0.21).
* **Error Calibration**: The OOF residual fusion meta-learner intercepted and corrected 18.7% of false-positive errors in the high-confidence region (>0.90) without requiring target-domain re-annotation.

---

## Repository Structure

```text
Robust-CrossDomain-NLP/
├── index.html                  # Standalone interactive demo (GitHub Pages)
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── docs/                       # Research report PDF
├── data/                       # Summary metrics and statistical test outputs
└── notebooks/                  # Feature analysis and visualization notebooks
```

---

## Quickstart

```bash
git clone [https://github.com/Sunxj2891/Robust-CrossDomain-NLP.git](https://github.com/Sunxj2891/Robust-CrossDomain-NLP.git)
cd Robust-CrossDomain-NLP
pip install -r requirements.txt
```

---

## Citation & Contact
Author: Xingjian Sun (The University of Melbourne)  
Contact: cdex1200000@gmail.com