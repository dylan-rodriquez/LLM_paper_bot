# Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks

**Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla

**Published:** 2025-11-10 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2511.04689v1 Announce Type: new 
Abstract: Large language model evaluation requires thousands of benchmark items, making evaluations expensive and slow. Existing methods compute average accuracy across fixed item sets, treating all items equally despite varying quality and informativeness. We present ATLAS an adaptive testing framework using Item Response Theory (IRT) to estimate model ability through Fisher information-guided item selection. Our analysis of five major benchmarks reveals that 3-6% of items exhibit negative discrimination, indicating annotation errors that corrupt static evaluation. ATLAS achieves 90% item reduction while maintaining measurement precision: on HellaSwag (5,608 items), we match full-benchmark estimates using only 42 items with 0.154 MAE. Our framework maintains item exposure rates below 10% and test overlap at 16-27%, compared to static benchmarks where every model sees all items (100% exposure). Among 4,000+ tested models, IRT ranks differ from accuracy ranks: models with the same accuracy get different IRT scores, and 23-31% of all models shift by more than 10 rank positions. Code and calibrated item banks are available at https://github.com/Peiyu-Georgia-Li/ATLAS.git.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 92.0/100

**Justification:** This paper addresses a critical bottleneck in LLM evaluation – the cost and inefficiency of static benchmarks. The application of Item Response Theory (IRT) to adaptive testing is a clever and well-justified approach, and the reported results (90% item reduction with maintained precision) are impressive. The discovery of annotation errors within existing benchmarks is also a significant finding, suggesting a broader issue with data quality.

## Keywords

item, items, accuracy, atlas, benchmarks, evaluation, irt, model, models, static

## Links

- [Paper URL](https://arxiv.org/abs/2511.04689)

---
*Auto-generated on 2025-11-10 09:31:22 UTC*
