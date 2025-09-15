# 📊 Evaluating AI Models for Student Competence Analysis

This repository evaluates the potential of **AI models** for analyzing student-written Python code and assessing competence. The objective is to explore how different models can:
- Analyze and interpret student Python code
- Generate prompts to test conceptual understanding
- Identify reasoning gaps or misconceptions
- Encourage deeper learning without directly providing solutions



## 🔍 Models Evaluated

| Model | Type | Key Strengths | Limitations |
|-------|------|---------------|-------------|
| **ChatGPT (OpenAI)** | Proprietary LLM | Strong reasoning, reliable coding feedback, high-quality prompts | Paid API, not open-source |
| **Gemini (Google DeepMind)** | Proprietary LLM | Multimodal (text + code), integrates with Google ecosystem | Early-stage API, limited interpretability |
| **Claude (Anthropic)** | Proprietary LLM | Safe, structured explanations, strong reasoning alignment | Context window constraints |
| **Perplexity AI** | AI Search + LLM | Real-time retrieval, contextual knowledge integration | Less code-specialized, web-reliant |
| **StarCoder (BigCode Project)** | **Open-Source LLM** | Code-focused, trained on GitHub repositories, customizable & free | Requires fine-tuning for educational use |


## 🛠️ Research Plan

**Approach**
- Use student-written Python code samples as input.
- Evaluate model outputs for correctness, reasoning, and educational guidance.
- Compare how prompts encourage exploration rather than giving direct answers.

**Evaluation Criteria**
- **Accuracy**: Detection of errors and misconceptions.
- **Educational Value**: Prompts that foster deeper understanding.
- **Interpretability**: Transparency in reasoning.
- **Cost & Accessibility**: Free vs proprietary APIs.

**Testing**
- Prepare Python scripts with common student mistakes.
- Query each model for feedback.
- Collect structured metrics (accuracy, quality of prompts, cost-efficiency).



## ⚖️ Reasoning

- **Suitability**: The best model should explain *why* mistakes occur, not just correct them.
- **Meaningful Prompts**: Prompts should guide reflection (e.g., “What happens if the loop runs one more time?”).
- **Trade-offs**:
  - Proprietary models → higher accuracy, less transparency, paid.
  - Open-source (StarCoder) → customizable, transparent, free, but needs tuning.



## 📂 Folder Structure

student-competence-analysis/
│── data/ # Sample student Python code
│── notebooks/ # Jupyter notebooks for experiments
│── src/ # Scripts for each model evaluation
│ ├── chatgpt_eval.py
│ ├── gemini_eval.py
│ ├── claude_eval.py
│ ├── perplexity_eval.py
│ ├── starcoder_eval.py
│── results/ # Outputs & analysis reports
│── README.md # Project overview



## 🚀 Setup & Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/anshikagarg12/Task3_Fossee
   cd Task3_Fossee

2. Install Dependencies

pip install -r requirements.txt

3. Run Model Evaluations

python src/chatgpt_eval.py
python src/gemini_eval.py
python src/claude_eval.py
python src/perplexity_eval.py
python src/starcoder_eval.py

📌 References

OpenAI ChatGPT

Google Gemini

Anthropic Claude

Perplexity AI

StarCoder (BigCode Project)