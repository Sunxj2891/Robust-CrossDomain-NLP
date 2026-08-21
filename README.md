# Robust Cross-Domain NLP: Artifact Review and Reproduction Plan

This repository is a course-project artifact about binary sentiment transfer from GoEmotions to IMDb. It contains the course report, an appendix of experimental code blocks, an illustrative browser walkthrough, and a compact error-correction summary.

## What is currently verifiable

- The archived course report is in [docs/NLP4Health_assignment3.pdf](docs/NLP4Health_assignment3.pdf).
- The artifact-level error-correction summary is in [data/ecr_summary.csv](data/ecr_summary.csv).
- The browser page is an explanatory rule-based visualisation. It does not load DistilBERT, trained residual-fusion weights, or a held-out dataset.
- The appendix source needs extraction into executable training/evaluation scripts before an end-to-end benchmark can be reproduced from this repository.

## Verified error-correction artifact

The following values are read directly from [data/ecr_summary.csv](data/ecr_summary.csv):

| Split | Text-only errors | Corrected errors | ECR | High-confidence errors | High-confidence corrected | HC-ECR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| GoEmotions validation | 302 | 4 | 1.3245% | 241 | 0 | 0.0000% |
| IMDb test | 7,527 | 53 | 0.7041% | 6,147 | 1 | 0.0163% |

These values are not sufficient to substantiate a model-F1 comparison, an 18.7% high-confidence correction rate, or a claim of deployed model performance. Those statements have been removed from this project copy until training outputs, predictions, split manifests, and executable evaluation code are released together.

## Verify the checked-in artifact

~~~bash
python3 scripts/validate_artifacts.py
~~~

The validator uses only the Python standard library and checks the recorded numerators, denominators, and derived rates.

## Next work required for an end-to-end research project

1. Extract the notebook appendix into versioned preprocessing, training, and evaluation scripts.
2. Add fixed split manifests, random seeds, model configuration, predictions, and per-split metrics.
3. Recompute source and target F1 plus high-confidence error correction from those predictions.
4. Replace the browser walkthrough with real, exported inference results or label it permanently as a visual explanation.

## Portfolio wording

Accurate current wording: analysed domain-shift artefacts and built a transparent visual explanation of residual-error correction; full end-to-end model reproduction remains planned work.

Do not claim a completed residual-fusion benchmark or the previous F1/HC-ECR figures until the missing reproducibility assets are added.
