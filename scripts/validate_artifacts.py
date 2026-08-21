import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "data" / "ecr_summary.csv"


def rate(numerator: int, denominator: int) -> float:
    if denominator <= 0:
        raise ValueError("Denominator must be positive.")
    return numerator / denominator


def main() -> None:
    with SUMMARY.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))

    required = {
        "dataset_name",
        "text_only_errors",
        "corrected_errors",
        "ecr",
        "text_only_high_conf_errors",
        "high_conf_corrected_errors",
        "hc_ecr",
    }
    if not rows or set(rows[0]) != required:
        raise RuntimeError("Unexpected ecr_summary.csv schema.")

    for row in rows:
        errors = int(row["text_only_errors"])
        corrected = int(row["corrected_errors"])
        high_conf_errors = int(row["text_only_high_conf_errors"])
        high_conf_corrected = int(row["high_conf_corrected_errors"])
        if not 0 <= corrected <= errors:
            raise RuntimeError(f"Invalid correction counts for {row['dataset_name']}.")
        if not 0 <= high_conf_corrected <= high_conf_errors:
            raise RuntimeError(f"Invalid high-confidence counts for {row['dataset_name']}.")
        if abs(rate(corrected, errors) - float(row["ecr"])) > 1e-12:
            raise RuntimeError(f"ECR mismatch for {row['dataset_name']}.")
        if abs(rate(high_conf_corrected, high_conf_errors) - float(row["hc_ecr"])) > 1e-12:
            raise RuntimeError(f"HC-ECR mismatch for {row['dataset_name']}.")
        print(
            f"{row['dataset_name']}: ECR={float(row['ecr']) * 100:.4f}% "
            f"({corrected}/{errors}), HC-ECR={float(row['hc_ecr']) * 100:.4f}% "
            f"({high_conf_corrected}/{high_conf_errors})"
        )


if __name__ == "__main__":
    main()
