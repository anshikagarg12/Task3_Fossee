# ⚙️ Setup Instructions for Student Competence Analysis

This guide explains how to set up your Python environment and run evaluations for the following AI models:

- ChatGPT (OpenAI)
- Gemini (Google DeepMind)
- Claude (Anthropic)
- Perplexity AI
- StarCoder (BigCode Project, HuggingFace)


## 1️⃣ Prerequisites

- Python 3.10+ installed
- Git installed
- A terminal or command prompt
- API keys for proprietary models:
  - **OpenAI**: [https://platform.openai.com](https://platform.openai.com)
  - **Gemini**: [https://console.cloud.google.com/](https://console.cloud.google.com/)
  - **Claude**: [https://www.anthropic.com/](https://www.anthropic.com/)
  - **Perplexity AI**: API token (if applicable)


## 2️⃣ Clone the Repository

```bash

git clone https://github.com/anshikagarg12/Task3\_Fossee

cd Task3\_Fossee



\##3️⃣ Install Dependencies

pip install -r requirements.txt





This will install:



Core utilities (numpy, pandas, requests)



Jupyter notebooks (notebook, ipython)



Model libraries (openai, google-generativeai, anthropic, transformers, torch)



Optional code analysis and visualization tools (black, flake8, matplotlib, seaborn)



\##4️⃣ Configure API Keys



Create a .env file in the root folder:



\# .env

OPENAI\_API\_KEY=your\_openai\_api\_key

GOOGLE\_API\_KEY=your\_gemini\_api\_key

ANTHROPIC\_API\_KEY=your\_claude\_api\_key

PERPLEXITY\_API\_KEY=your\_perplexity\_api\_key





Make sure you never commit your .env to public repositories.



\##5️⃣ Running Model Evaluation Scripts



Run each model’s evaluation script to generate prompts and feedback on student Python code:



python src/chatgpt\_eval.py

python src/gemini\_eval.py

python src/claude\_eval.py

python src/perplexity\_eval.py

python src/starcoder\_eval.py





Each script will read Python files from data/student\_submissions/.



Outputs will be saved in results/raw/ and results/processed/.



\##6️⃣ Jupyter Notebook Testing (Optional)



You can also run the notebooks in the notebooks/ folder for step-by-step analysis:



jupyter notebook





01\_data\_prep.ipynb → Load and inspect student submissions



02\_model\_queries.ipynb → Query all 5 models



03\_analysis.ipynb → Compare outputs and visualize results



\##7️⃣ Notes



StarCoder is fully open-source and requires no API key.



Proprietary models (ChatGPT, Gemini, Claude, Perplexity) require valid API keys and may incur costs.



Ensure Python environment has sufficient RAM for StarCoder (>8GB recommended).



For reproducibility, always use the provided data/student\_submissions/ folder or add new student code in the same format.





