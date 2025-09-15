"""
utils.py

Reusable helper functions for the Student Competence Analysis project.
"""

import os
from pathlib import Path
import json


# File Utilities


def load_student_files(data_dir="data/student_submissions"):
    """
    Load all Python files from the given directory.
    Returns a dict {filename: code}.
    """
    data_path = Path(data_dir)
    submissions = {}
    for file in data_path.glob("*.py"):
        with open(file, "r", encoding="utf-8") as f:
            submissions[file.name] = f.read()
    return submissions

def save_model_results(results, filename, results_dir="results/raw"):
    """
    Save model results dictionary as JSON.
    """
    results_path = Path(results_dir)
    results_path.mkdir(parents=True, exist_ok=True)
    output_file = results_path / f"{filename}_results.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    return output_file


# Text Scoring Utilities


def score_diagnosticity(text):
    """
    Count the number of reflective questions in text.
    Simple heuristic: count '?' characters.
    """
    return text.count("?")

def score_conceptual_focus(text):
    """
    Count presence of Python/concept keywords.
    """
    keywords = ["variable", "loop", "function", "logic", "error", "condition", "algorithm"]
    return sum(1 for kw in keywords if kw.lower() in text.lower())

def score_solution_neutrality(text):
    """
    Returns 1 if no code is given in the prompt, 0 otherwise.
    """
    code_indicators = ["def ", "return ", "print(", "import "]
    return 0 if any(ci in text for ci in code_indicators) else 1

# Directory Utilities

def ensure_dir(path):
    """
    Create directory if it does not exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)

