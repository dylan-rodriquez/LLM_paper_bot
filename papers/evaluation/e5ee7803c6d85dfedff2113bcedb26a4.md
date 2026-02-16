# ProbeLLM: Automating Principled Diagnosis of LLM Failures

**Authors:** Yue Huang, Zhengzhe Jiang, Yuchen Ma, Yu Jiang, Xiangqi Wang, Yujun Zhou, Yuexing Hao, Kehan Guo, Pin-Yu Chen, Stefan Feuerriegel, Xiangliang Zhang

**Published:** 2026-02-16 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2602.12966v1 Announce Type: new 
Abstract: Understanding how and why large language models (LLMs) fail is becoming a central challenge as models rapidly evolve and static evaluations fall behind. While automated probing has been enabled by dynamic test generation, existing approaches often discover isolated failure cases, lack principled control over exploration, and provide limited insight into the underlying structure of model weaknesses. We propose ProbeLLM, a benchmark-agnostic automated probing framework that elevates weakness discovery from individual failures to structured failure modes. ProbeLLM formulates probing as a hierarchical Monte Carlo Tree Search, explicitly allocating limited probing budgets between global exploration of new failure regions and local refinement of recurring error patterns. By restricting probing to verifiable test cases and leveraging tool-augmented generation and verification, ProbeLLM grounds failure discovery in reliable evidence. Discovered failures are further consolidated into interpretable failure modes via failure-aware embeddings and boundary-aware induction. Across diverse benchmarks and LLMs, ProbeLLM reveals substantially broader, cleaner, and more fine-grained failure landscapes than static benchmarks and prior automated methods, supporting a shift from case-centric evaluation toward principled weakness discovery.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a crucial problem in the rapidly evolving LLM landscape – understanding *why* models fail, not just *that* they fail. The proposed ProbeLLM framework, leveraging hierarchical Monte Carlo Tree Search and verifiable test cases, appears to be a principled and automated approach to failure mode discovery. The focus on structured failure modes and reliable evidence is a strong point, suggesting a rigorous methodology and potential for significant impact. The use of tool-augmented generation and verification further strengthens the approach.

## Keywords

failure, probellm, probing, automated, discovery, failures, principled, automated probing, aware, benchmarks

## Links

- [Paper URL](https://arxiv.org/abs/2602.12966)

---
*Auto-generated on 2026-02-16 09:59:08 UTC*
