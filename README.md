# Fintech AI/LLM Evaluation Suite

A self-built evaluation suite for a fintech investment/financial-advisor chatbot, testing accuracy, hallucination handling, bias/fairness, and adversarial robustness.

## Purpose

This project moves beyond manual, one-off chatbot testing toward an automated, repeatable evaluation pipeline for the failure modes that matter most in a regulated space: hallucination, unreliable arithmetic, bias, security/injection vulnerabilities, and unsafe advice.

## Approach

Started with a risk-based manual test plan (32 test cases across 9 categories: accuracy, advice boundaries, hallucination, vulnerable users, security, privacy, illegal activity, bias, robustness — see `docs/test-plan.md`), then progressively automated coverage using different tools, each suited to a different category of risk.

This approach is informed by the UK FCA's "AI Live Testing" principles and Consumer Duty expectations: clear governance, human-in-the-loop review of high-risk outputs, and fair, understandable outcomes for retail customers. This is a personal learning project, not a compliance audit — the regulatory framing is used here as a quality lens.

## Tools used

- **Promptfoo** (Node.js) — prompt/output accuracy testing and automated adversarial/red-team
cat > README.md << 'ENDOFREADME'
# Fintech AI/LLM Evaluation Suite

A self-built evaluation suite for a fintech investment/financial-advisor chatbot, testing accuracy, hallucination handling, bias/fairness, and adversarial robustness.

## Purpose

This project moves beyond manual, one-off chatbot testing toward an automated, repeatable evaluation pipeline for the failure modes that matter most in a regulated space: hallucination, unreliable arithmetic, bias, security/injection vulnerabilities, and unsafe advice.

## Approach

Started with a risk-based manual test plan (32 test cases across 9 categories: accuracy, advice boundaries, hallucination, vulnerable users, security, privacy, illegal activity, bias, robustness — see `docs/test-plan.md`), then progressively automated coverage using different tools, each suited to a different category of risk.

This approach is informed by the UK FCA's "AI Live Testing" principles and Consumer Duty expectations: clear governance, human-in-the-loop review of high-risk outputs, and fair, understandable outcomes for retail customers. This is a personal learning project, not a compliance audit — the regulatory framing is used here as a quality lens.

## Tools used

- **Promptfoo** (Node.js) — prompt/output accuracy testing and automated adversarial/red-team testing
- **DeepEval** (Python) — hallucination and toxicity metrics, using a custom local LLM-judge wrapper
- **scikit-learn + Hugging Face Datasets** — bias/fairness testing on a credit-scoring-style classification model
- **Ollama** — free, fully local LLM runtime, used both as the system under test and as an LLM-judge

## Key findings

Full details in [`findings.md`](./findings.md). Summary:

- **Accuracy:** the model made a compound interest calculation error (stated ~£16,144 instead of the correct ~£8,144 for a standard illustration).
- **Hallucination:** the model correctly refused to invent details about a fictional fund, but a small local model struggled to reliably judge more nuanced hallucination cases.
- **Bias:** a large gender demographic parity gap was found in a credit-scoring-style classifier (18.3% predicted high income for men vs. 2.9% for women).
- **Adversarial/Red-team:** 87% of 70 automated attack prompts were defended; the weakest area was resistance to instruction-hijacking (40% attack success rate), while direct PII extraction and illegal-activity requests were fully defended.

## Limitations

- Testing was done against a small, local, open-source model (llama3.2) — not a production-grade commercial LLM — so absolute results should not be generalised, but the *methodology* and *category-level findings* are transferable.
- This is a personal training project, not a compliance audit or a substitute for a real firm's model risk management process.
