# Reasoning for Model Evaluation: Student Competence Analysis

## 1. Model Suitability for High-Level Competence Analysis

A model is considered suitable if it can:

- **Explain reasoning in natural language**: Translate Python code into conceptual understanding.
- **Follow instructions**: Generate Socratic prompts rather than providing full solutions.
- **Handle context**: Maintain long context windows for complete code files + instructions.
- **Ground responses**: Use retrieval or factual knowledge (e.g., Perplexity AI) to support reasoning.
- **Ensure safety/alignment**: Avoid misleading, unsafe, or solution-revealing prompts.


## 2. Testing for Meaningful Prompt Generation

To validate model effectiveness:

1. Provide each model with identical student Python code examples.
2. Ask: *“Generate three diagnostic, non-solution prompts to help the student reflect.”*
3. Compare outputs to a **gold set** created by teachers.
4. Teachers rate outputs on:
   - Diagnosticity (does it identify gaps or misconceptions?)  
   - Solution-neutrality (does it avoid giving the answer?)  
   - Conceptual focus (does it test understanding?)  
   - Pedagogical depth (does it encourage reflection?)  
5. Optional student pilots: measure post-test gains using model-generated prompts versus baseline hints.

## 3. Trade-Offs: Accuracy vs Interpretability vs Cost

| Factor             | Observations |
|-------------------|--------------|
| Accuracy           | ChatGPT & Gemini provide precise reasoning; Claude excels at safe pedagogy; Perplexity provides grounded citations. |
| Interpretability   | Claude & Perplexity are transparent; ChatGPT & Gemini can hallucinate but often provide detailed explanations. |
| Cost & Access      | Perplexity (free plan) is cheapest; ChatGPT/Claude moderate; Gemini depends on API tier. Interpretability may reduce reasoning breadth. |

## 4. Model Strengths and Limitations

| Model       | Strengths | Limitations |
|------------|-----------|-------------|
| ChatGPT    | Instruction-following, strong reasoning | May reveal solutions instead of scaffolding |
| Gemini     | Excellent reasoning, search grounding | Less clear citations, higher API costs |
| Claude     | Safe, alignment-oriented, long context | Too cautious; may not probe technical depth |
| Perplexity | Grounded answers, citation-rich | Limited Socratic pedagogy, may be less reflective |
| StarCoder  | Open-source, code-aware | No natural-language scaffolding, limited prompt design |



## 5. Evaluation Decision

- **Pedagogical prompts** → Claude is preferred for safe, scaffolded questioning.
- **Technical accuracy** → ChatGPT & Gemini excel at deep code reasoning.
- **Interpretability / citations** → Perplexity adds value for grounded insights.
- **Hybrid approach** → Use Claude for scaffolding questions + ChatGPT/Gemini for deeper technical interrogation.

**Conclusion:**  
The evaluation prioritizes models that generate reflective, non-solution prompts to help students understand Python concepts while balancing accuracy, interpretability, and practical cost.
