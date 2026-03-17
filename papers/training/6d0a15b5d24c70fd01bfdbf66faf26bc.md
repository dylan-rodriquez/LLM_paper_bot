# FLUX: Data Worth Training On

**Authors:** Gowtham, Sai Rupesh, Sanjay Kumar,  Saravanan, Venkata Chaithanya

**Published:** 2026-03-17 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2603.13972v1 Announce Type: new 
Abstract: Modern large language model training is no longer limited by data availability, but by the inability of existing preprocessing pipelines to simultaneously achieve massive scale and high data quality. Current approaches are forced to sacrifice one for the other: either aggressively filtering to improve quality at the cost of severe token loss, or retaining large volumes of data while introducing substantial noise. In this work, we introduce FLUX, a preprocessing pipeline specifically designed to break this long-standing trade-off by maximizing token retention while enforcing rigorous quality control. Models trained on FLUX-curated data consistently outperform prior methods. A 3B-parameter model trained on 60B tokens with FLUX achieves 32.14% MMLU accuracy, surpassing the previous state-of-the-art pipeline DCLM (31.98%) and significantly outperforming FineWeb (29.88%). FLUX achieves the same aggregate score as a model trained on DCLM data using only 39B tokens, resulting in a 34.4% reduction in training compute. At the data level, FLUX extracts 50B usable tokens from a single dump (CC-MAIN-2025-51), compared to 40B from DCLM (+25% retention). FLUX-Base yields 192B tokens, exceeding FineWeb's 170B while still maintaining superior quality. Overall, FLUX establishes a new state of the art in web-scale data preprocessing by demonstrating that high retention, strong quality control, and computational efficiency can be achieved simultaneously, redefining the limits of scalable dataset construction for modern language models.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 92.0/100

**Justification:** This paper addresses a crucial bottleneck in LLM training – the trade-off between data quality and quantity. The reported performance gains (surpassing DCLM and significantly outperforming FineWeb on MMLU) suggest a robust and effective pipeline. The clear articulation of the problem and the quantifiable results contribute to a strong overall quality and high potential for positive reception within the community.

## Keywords

data, flux, quality, tokens, dclm, model, preprocessing, retention, trained, training

## Links

- [Paper URL](https://arxiv.org/abs/2603.13972)

---
*Auto-generated on 2026-03-17 10:12:24 UTC*
