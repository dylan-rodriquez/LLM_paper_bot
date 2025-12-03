# An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation

**Authors:** Daiki Shirafuji, Tatsuhiko Saito, Yasutomo Kimura

**Published:** 2025-12-03 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2512.02689v1 Announce Type: new 
Abstract: Large language models (LLMs) are known to inherit and even amplify societal biases present in their pre-training corpora, threatening fairness and social trust. To address this issue, recent work has explored ``editing'' LLM parameters to mitigate social bias with model merging approaches; however, there is no empirical comparison. In this work, we empirically survey seven algorithms: Linear, Karcher Mean, SLERP, NuSLERP, TIES, DELLA, and Nearswap, applying 13 open weight models in the GPT, LLaMA, and Qwen families. We perform a comprehensive evaluation using three bias datasets (BBQ, BOLD, and HONEST) and measure the impact of these techniques on LLM performance in downstream tasks of the SuperGLUE benchmark. We find a trade-off between bias reduction and downstream performance: methods achieving greater bias mitigation degrade accuracy, particularly on tasks requiring reading comprehension and commonsense and causal reasoning. Among the merging algorithms, Linear, SLERP, and Nearswap consistently reduce bias while maintaining overall performance, with SLERP at moderate interpolation weights emerging as the most balanced choice. These results highlight the potential of model merging algorithms for bias mitigation, while indicating that excessive debiasing or inappropriate merging methods may lead to the degradation of important linguistic abilities.

## Analysis

**Innovation Score:** 65.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a highly significant problem – mitigating social bias in LLMs – and provides a much-needed empirical comparison of existing model merging techniques. The comprehensive evaluation across multiple models, bias datasets, and downstream tasks strengthens the rigor of the work. While the methods themselves aren't entirely novel, the systematic comparison and identification of trade-offs between bias reduction and performance are valuable contributions. The clear finding of a performance degradation with increased bias mitigation is important for practitioners.

## Keywords

bias, merging, algorithms, bias mitigation, merging algorithms, mitigation, model, model merging, performance, slerp

## Links

- [Paper URL](https://arxiv.org/abs/2512.02689)

---
*Auto-generated on 2025-12-03 09:33:03 UTC*
