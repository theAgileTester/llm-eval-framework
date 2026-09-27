# Manual Test Plan: Investment / Financial Advisor Chatbot

**Author:** Banu Sencan | **Version:** 1.0

---

## 1. Purpose

Define how to evaluate a simple LLM-based investment/financial advisor chatbot: what to ask, what to expect, and how to decide pass or fail.

A financial chatbot is high-risk. A wrong or overconfident answer can cost a real person real money. So this plan is risk-based: the most dangerous behaviours are tested first and have the strictest pass criteria.

## 2. System Under Test (assumptions)

| Item | Assumption |
|---|---|
| Type | Text chatbot backed by an LLM |
| Audience | UK retail users (beginners) |
| Purpose | General investment guidance and education (ISAs, pensions, funds, risk, compound growth) |
| Not its purpose | Regulated, personalised investment advice; executing trades; accessing user accounts |

**Regulatory context (UK):** The FCA expects firms to communicate clearly and treat retail customers fairly (Consumer Duty). Used here as a quality lens, not legal advice.

## 3. Scope

**In scope:** factual accuracy, advice boundary, risk disclosure, hallucination handling, vulnerable-user/scam scenarios, prompt injection/jailbreaks, privacy of personal data, bias/fairness, robustness.

**Out of scope:** performance/load testing, UI/accessibility, real trading integrations, legal sign-off.

## 4. Test Categories

32 test cases across 9 categories: Accuracy (ACC), Advice boundary/Risk (ADV/RSK), Hallucination (HAL), Vulnerable users (VUL), Security/injection (SEC), Privacy (PRV), Illegal/out-of-scope (OOS), Bias (BIA), Robustness (ROB).

Severity: Critical: 12, High: 12, Medium: 8.

## 5. Automated Coverage

This manual plan was progressively automated — see the project [README](../README.md) and [findings.md](../findings.md) for the automated Promptfoo, DeepEval, scikit-learn/Hugging Face, and adversarial/red-team suites built from these categories.

## 6. Exit Criteria

- 100% of Critical cases pass
- ≥90% of High cases pass
- All failures logged with prompt, response, severity
