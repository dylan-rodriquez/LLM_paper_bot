# From Detection to Diagnosis: Advancing Hallucination Analysis with Automated Data Synthesis

**Authors:** Yanyi Liu, Qingwen Yang, Tiezheng Guo, Feiyu Qu, Jun Liu, Yingyou Wen

**Published:** 2026-01-16 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2601.09734v1 Announce Type: new 
Abstract: Hallucinations in Large Language Models (LLMs), defined as the generation of content inconsistent with facts or context, represent a core obstacle to their reliable deployment in critical domains. Current research primarily focuses on binary "detection" approaches that, while capable of identifying hallucinations, fail to provide interpretable and actionable feedback for model improvement, thus limiting practical utility. To address this limitation, a new research paradigm is proposed, shifting from "detection" to "diagnosis". The Hallucination Diagnosis Task is introduced, a task which requires models to not only detect hallucinations, but also perform error localization, causal explanation, and content correction. We develop the Hallucination Diagnosis Generator (HDG), an automated pipeline that systematically generates high-quality training samples with rich diagnostic metadata from raw corpora through multi-dimensional augmentation strategies including controlled fact fabrication and reasoning chain perturbation. Using HDG-generated data, we train HDM-4B-RL, a 4-billion-parameter hallucination diagnosis model, employing Group Relative Policy Optimization (GRPO) with a comprehensive reward function incorporating structural, accuracy, and localization signals. Experimental results demonstrate that our model surpasses previous state-of-the-art detection models on the HaluEval benchmark while achieving comparable performance to advanced general-purpose models. In comprehensive diagnosis tasks, HDM-4B-RL matches the capabilities of larger general models while maintaining a smaller size. This work validates the feasibility and value of hallucination diagnosis, providing an effective methodology for building more trustworthy and reliable generative AI systems.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 85.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a crucial problem in LLM deployment – hallucinations – and proposes a shift from simple detection to a more useful diagnostic approach. The introduction of the 'Hallucination Diagnosis Task' and the HDG pipeline demonstrate a clear methodology for generating training data to improve model understanding and correction capabilities. While the abstract doesn't detail the specifics of the augmentation techniques, the overall framing and proposed task are well-defined and likely to resonate with the research community.

## Keywords

diagnosis, hallucination, models, detection, hallucination diagnosis, hallucinations, model, 4b, 4b rl, automated

## Links

- [Paper URL](https://arxiv.org/abs/2601.09734)

---
*Auto-generated on 2026-01-16 09:44:30 UTC*
