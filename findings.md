# Findings Log — Project 2: Fintech AI/LLM Evaluation Suite

## Day 16 — Basic Accuracy Test Suite (Promptfoo + Ollama)

**Setup:** Promptfoo + local Ollama (llama3.2:3b), 4 accuracy test cases covering ISA/pension education content.

**Result:** 3/4 passed (75%)

**Finding #1 — Numeric/computational hallucination (Medium-High priority)**
- **Test case:** "If I invest £5,000 at 5% a year with no withdrawals, how much will I have after 10 years?"
- **Expected:** ~£8,144 (5000 × 1.05^10)
- **Actual model output:** Correct formula, correct intermediate value (1.05^10 = 1.62889), but wrong final multiplication → stated £16,144.45 instead of £8,144.47
- **Category:** Overlaps ACC (accuracy) and HAL (hallucination) — the model's reasoning chain was correct but the arithmetic execution was wrong.
- **Implication:** Small local LLMs should not be trusted to perform financial calculations directly. Production systems should use tool-use/function calling to a real calculator rather than free-form LLM arithmetic.

**Environment note:** Testing done fully offline/free using Ollama (llama3.2:3b) instead of a paid API, to keep the project cost-free. Judge model for llm-rubric assertions was also Ollama (same model), which may reduce judgment quality compared to a stronger model — a known limitation for this stage of the project.
