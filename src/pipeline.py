"""
pipeline.py

Central pipeline to evaluate student Python submissions using:
- ChatGPT (OpenAI)
- Gemini (Google DeepMind)
- Claude (Anthropic)
- Perplexity AI
- StarCoder (HuggingFace)
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")
ANTHROPIC_KEY = os.getenv("ANTHROPIC_API_KEY")
PERPLEXITY_KEY = os.getenv("PERPLEXITY_API_KEY")

# Paths
DATA_DIR = Path("data/student_submissions")
RESULTS_DIR = Path("results/raw")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Import model clients
import openai
import anthropic
# For Gemini, assuming google-generativeai installed
import google.generativeai as genai
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


# StarCoder Setup

STARCODER_MODEL = "bigcode/starcoder"
tokenizer = AutoTokenizer.from_pretrained(STARCODER_MODEL)
model = AutoModelForCausalLM.from_pretrained(STARCODER_MODEL)


# Helper functions


def load_student_files():
    """Load all student Python submissions as dict {filename: code}"""
    submissions = {}
    for file in DATA_DIR.glob("*.py"):
        with open(file, "r", encoding="utf-8") as f:
            submissions[file.name] = f.read()
    return submissions

def query_chatgpt(code):
    openai.api_key = OPENAI_KEY
    prompt = f"Analyze this Python code and generate three reflective, non-solution prompts:\n\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    return response.choices[0].message["content"]

def query_gemini(code):
    genai.configure(api_key=GOOGLE_KEY)
    prompt = f"Analyze this Python code and generate three reflective, non-solution prompts:\n\n{code}"
    response = genai.chat.create(
        model="gemini-1.5",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.last_response

def query_claude(code):
    client = anthropic.Client(ANTHROPIC_KEY)
    prompt = f"Analyze this Python code and generate three reflective, non-solution prompts:\n\n{code}"
    response = client.completions.create(
        model="claude-2",
        prompt=prompt,
        max_tokens_to_sample=500
    )
    return response.completion

def query_perplexity(code):
    # Placeholder function: replace with your actual Perplexity API call
    return f"Perplexity AI response placeholder for code:\n{code[:50]}..."

def query_starcoder(code):
    inputs = tokenizer(code, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Main Pipeline


def main():
    submissions = load_student_files()
    for filename, code in submissions.items():
        results = {
            "chatgpt": query_chatgpt(code),
            "gemini": query_gemini(code),
            "claude": query_claude(code),
            "perplexity": query_perplexity(code),
            "starcoder": query_starcoder(code)
        }

        # Save results
        output_file = RESULTS_DIR / f"{filename}_results.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)

        print(f" Processed {filename}, results saved to {output_file}")

if __name__ == "__main__":
    main()
