# Online Experiential Learning for Language Models

**Authors:** Tianzhu Ye, Li Dong, Qingxiu Dong, Xun Wu, Shaohan Huang, Furu Wei

**Published:** 2026-03-18 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2603.16856v1 Announce Type: new 
Abstract: The prevailing paradigm for improving large language models relies on offline training with human annotations or simulated environments, leaving the rich experience accumulated during real-world deployment entirely unexploited. We propose Online Experiential Learning (OEL), a framework that enables language models to continuously improve from their own deployment experience. OEL operates in two stages: first, transferable experiential knowledge is extracted and accumulated from interaction trajectories collected on the user side; second, this knowledge is consolidated into model parameters via on-policy context distillation, requiring no access to the user-side environment. The two stages are iterated to form an online learning loop, where the improved model collects higher-quality trajectories that yield richer experiential knowledge for subsequent rounds. We evaluate OEL on text-based game environments across multiple model scales and both thinking and non-thinking variants. OEL achieves consistent improvements over successive iterations, enhancing both task accuracy and token efficiency while preserving out-of-distribution performance. Our analysis further shows that extracted experiential knowledge is significantly more effective than raw trajectories, and that on-policy consistency between the knowledge source and the policy model is critical for effective learning.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a crucial limitation in current LLM training – the inability to learn from deployment data. The proposed Online Experiential Learning (OEL) framework is a promising approach to continuous improvement, leveraging real-world interactions. The use of context distillation for parameter updates without requiring access to user data is particularly clever, and the iterative loop suggests a robust learning process. The evaluation on text-based games provides a good starting point, though broader testing will be needed.

## Keywords

experiential, knowledge, learning, model, oel, experiential knowledge, language, language models, models, online

## Links

- [Paper URL](https://arxiv.org/abs/2603.16856)

---
*Auto-generated on 2026-03-18 10:05:04 UTC*
