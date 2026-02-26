# Black-Box Reliability Certification for AI Agents via Self-Consistency Sampling and Conformal Calibration

**Authors:** Charafeddine Mouzouni

**Published:** 2026-02-26 | **Source:** arXiv RSS

**Categories:** cs.LG

**Significance Score:** 92.0/100

## Abstract

arXiv:2602.21368v1 Announce Type: cross 
Abstract: Given a black-box AI system and a task, at what confidence level can a practitioner trust the system's output? We answer with a reliability level -- a single number per system-task pair, derived from self-consistency sampling and conformal calibration, that serves as a black-box deployment gate with exact, finite-sample, distribution-free guarantees. Self-consistency sampling reduces uncertainty exponentially; conformal calibration guarantees correctness within 1/(n+1) of the target level, regardless of the system's errors -- made transparently visible through larger answer sets for harder questions. Weaker models earn lower reliability levels (not accuracy -- see Definition 2.4): GPT-4.1 earns 94.6% on GSM8K and 96.8% on TruthfulQA, while GPT-4.1-nano earns 89.8% on GSM8K and 66.5% on MMLU. We validate across five benchmarks, five models from three families, and both synthetic and real data. Conditional coverage on solvable items exceeds 0.93 across all configurations; sequential stopping reduces API costs by around 50%.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 80.0/100

**Justification:** This paper tackles a crucial problem in AI deployment – reliably quantifying the trustworthiness of black-box models. The combination of self-consistency sampling and conformal calibration appears novel and provides strong theoretical guarantees. The empirical validation across multiple models and benchmarks strengthens the findings, suggesting a practical and impactful approach to AI reliability certification.

## Keywords

black, black box, box, calibration, conformal, conformal calibration, consistency, consistency sampling, level, reliability

## Links

- [Paper URL](https://arxiv.org/abs/2602.21368)

---
*Auto-generated on 2026-02-26 09:56:05 UTC*
