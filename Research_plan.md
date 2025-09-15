# Research Plan: Evaluating Open Source Models for Student Competence Analysis

## 1. Approach to Identifying and Evaluating Models

I will be using and comparing five LLMs — **ChatGPT (OpenAI)**, **Gemini (Google DeepMind)**, **Claude (Anthropic)**, **Perplexity AI**, and **StarCoder (BigCode)**. These models were selected based on:

- Established reasoning and natural language capabilities.  
- Accessibility via APIs or web interfaces for research and educational use.  
- Support for multi-turn conversation and large context windows, enabling evaluation of complete code submissions.  
- Existing examples of educational/pedagogical applications.

The evaluation will focus on using **Python student code submissions** to:

1. Analyze code for conceptual understanding.  
2. Generate prompts that highlight reasoning gaps without giving away solutions.  
3. Identify misconceptions or missing logic.  
4. Encourage deeper reflection and learning.



## 2. Testing and Validation

The evaluation process will follow staged validation:

1. **Static Checks**  
   - Provide representative Python code snippets (correct, partially-correct, misconception-prone).  
   - Record each model's feedback.

2. **Prompt-Generation Task**  
   - Instruct models to produce reflective, non-solution prompts.

3. **Comparative Analysis**  
   - Score prompts for clarity, diagnosticity, solution-neutrality, and conceptual focus.

4. **Human Evaluation**  
   - Teachers rate outputs using defined rubrics.

5. **Student Pilot**  
   - A/B testing to measure post-test learning gains using model-generated prompts versus baseline hints.



## 3. Reasoning and Decision-Making

- **Suitability Criteria**: Ability to reason about Python code, follow instructions, maintain context, provide safe and pedagogical prompts.  
- **Prompt Evaluation**: Compare against teacher-created gold standards for diagnosticity, conceptual focus, and solution-neutrality.  
- **Trade-Offs**: Balance accuracy, interpretability, cost, and accessibility of models.  
- **Model Selection**:  
  - ChatGPT / Gemini: Technical reasoning depth.  
  - Claude: Safe scaffolding and alignment.  
  - Perplexity: Grounded answers with citations.  
  - StarCoder: Open-source code-aware baseline.



**Conclusion:**  
The research plan aims to systematically evaluate multiple LLMs for generating pedagogically meaningful prompts for Python student code, with validation through teacher scoring and small-scale student pilot studies.
