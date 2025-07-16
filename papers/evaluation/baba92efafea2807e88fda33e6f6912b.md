# Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing

**Authors:** Han Jiang, Xiaoyuan Yi, Zhihua Wei, Ziang Xiao, Shu Wang, Xing Xie

**Published:** 2025-06-12 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2406.14230v5 Announce Type: replace 
Abstract: Warning: Contains harmful model outputs. Despite significant advancements, the propensity of Large Language Models (LLMs) to generate harmful and unethical content poses critical challenges. Measuring value alignment of LLMs becomes crucial for their regulation and responsible deployment. Although numerous benchmarks have been constructed to assess social bias, toxicity, and ethical issues in LLMs, those static benchmarks suffer from evaluation chronoeffect, in which, as models rapidly evolve, existing benchmarks may leak into training data or become saturated, overestimating ever-developing LLMs. To tackle this problem, we propose GETA, a novel generative evolving testing approach based on adaptive testing methods in measurement theory. Unlike traditional adaptive testing methods that rely on a static test item pool, GETA probes the underlying moral boundaries of LLMs by dynamically generating test items tailored to model capability. GETA co-evolves with LLMs by learning a joint distribution of item difficulty and model value conformity, thus effectively addressing evaluation chronoeffect. We evaluated various popular LLMs with GETA and demonstrated that 1) GETA can dynamically create difficulty-tailored test items and 2) GETA's evaluation results are more consistent with models' performance on unseen OOD and i.i.d. items, laying the groundwork for future evaluation paradigms.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 85.0/100  
**Sentiment Score:** 78.0/100

**Justification:** This paper tackles a crucial problem in LLM development – the stagnation of benchmarks due to model evolution. The proposed GETA approach, leveraging adaptive testing, is a clever solution to dynamically assess LLM values and avoid benchmark saturation. While the abstract doesn't detail implementation specifics, the core idea is strong and addresses a significant limitation of current evaluation methods. The warning about harmful outputs is concerning but highlights the importance of the research.

## Keywords

llms, geta, evaluation, models, testing, benchmarks, items, model, test, adaptive

## Links

- [Paper URL](https://arxiv.org/abs/2406.14230)

---
*Auto-generated on 2025-06-12 09:29:11 UTC*
