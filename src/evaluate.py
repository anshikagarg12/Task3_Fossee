"""
evaluate.py

Read model outputs and evaluate them for:
- Diagnosticity
- Conceptual focus
- Solution-neutrality

Outputs a CSV summary per student file.
"""

import json
from pathlib import Path
import pandas as pd

# Paths
RAW_RESULTS_DIR = Path("results/raw")
EVAL_RESULTS_DIR = Path("results/processed")
EVAL_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Models
MODELS = ["chatgpt", "gemini", "claude", "perplexity", "starcoder"]


# Evaluation Functions


def score_diagnosticity(text):
    """
    Placeholder scoring: 
    Count number of reflective questions / prompt indicators.
    """
    return text.count("?")  # simplistic heuristic

def score_conceptual_focus(text):
    """
    Placeholder: check for keywords like 'variable', 'loop', 'function', 'logic'
    """
    keywords = ["variable", "loop", "function", "logic", "error", "condition", "algorithm"]
    return sum(1 for kw in keywords if kw.lower() in text.lower())

def score_solution_neutrality(text):
    """
    Placeholder: penalize presence of actual code fixes
    """
    if "def " in text or "return " in text or "print(" in text:
        return 0  # contains code = less solution-neutral
    return 1  # no code snippets = solution-neutral


# Main Evaluation Pipeline

def evaluate_results():
    summary = []

    for file_path in RAW_RESULTS_DIR.glob("*_results.json"):
        with open(file_path, "r", encoding="utf-8") as f:
            results = json.load(f)

        row = {"filename": file_path.stem.replace("_results", "")}

        for model in MODELS:
            text = results.get(model, "")
            row[f"{model}_diagnosticity"] = score_diagnosticity(text)
            row[f"{model}_conceptual_focus"] = score_conceptual_focus(text)
            row[f"{model}_solution_neutrality"] = score_solution_neutrality(text)

        summary.append(row)

    # Save summary to CSV
    df = pd.DataFrame(summary)
    output_csv = EVAL_RESULTS_DIR / "evaluation_summary.csv"
    df.to_csv(output_csv, index=False)
    print(f"[✅] Evaluation complete. Summary saved to {output_csv}")

if __name__ == "__main__":
    evaluate_results()
