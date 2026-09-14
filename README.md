# Project 2 – LLM Evaluation

## Overview
This project showcases AI/LLM testing skills: building an evaluation framework to assess large language model outputs for correctness, safety, consistency, and regression across prompt versions — a core skill for an AI Tester role.

## Objectives
- Build a repeatable evaluation harness for LLM responses
- Cover accuracy, hallucination detection, bias/safety checks, and consistency
- Compare outputs across models or prompt versions
- Present results in a clear, reviewable report format

## Tech Stack
- Language: Python
- LLM access: Anthropic / OpenAI API (TBD)
- Eval framework: custom scripts, or promptfoo / DeepEval (TBD)
- Data: curated test prompt sets + expected criteria
- Reporting: Markdown / HTML report output

## Evaluation Scope
- [ ] Define evaluation criteria (accuracy, safety, tone, hallucination)
- [ ] Build test prompt dataset
- [ ] Automate scoring / grading logic
- [ ] Regression testing across prompt or model versions
- [ ] Generate summary report

## Setup
\```bash
# TBD once implementation starts
pip install -r requirements.txt
python run_eval.py
\```

## Status
🚧 Skeleton — implementation not yet started.

## Roadmap
1. Define evaluation criteria & metrics
2. Build/curate test dataset
3. Implement evaluation harness
4. Run baseline evaluation
5. Document findings & methodology
