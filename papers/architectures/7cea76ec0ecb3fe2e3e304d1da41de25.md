# Detecting Non-Membership in LLM Training Data via Rank Correlations

**Authors:** Pranav Shetty, Mirazul Haque, Zhiqiang Ma, Xiaomo Liu

**Published:** 2026-03-25 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2603.22707v1 Announce Type: new 
Abstract: As large language models (LLMs) are trained on increasingly vast and opaque text corpora, determining which data contributed to training has become essential for copyright enforcement, compliance auditing, and user trust. While prior work focuses on detecting whether a dataset was used in training (membership inference), the complementary problem -- verifying that a dataset was not used -- has received little attention. We address this gap by introducing PRISM, a test that detects dataset-level non-membership using only grey-box access to model logits. Our key insight is that two models that have not seen a dataset exhibit higher rank correlation in their normalized token log probabilities than when one model has been trained on that data. Using this observation, we construct a correlation-based test that detects non-membership. Empirically, PRISM reliably rules out membership in training data across all datasets tested while avoiding false positives, thus offering a framework for verifying that specific datasets were excluded from LLM training.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 90.0/100

**Justification:** This paper tackles a crucial and currently under-explored problem in the LLM space – verifying *non*-membership in training data. The approach of using rank correlations in logits is a clever and relatively simple method that appears effective. The focus on grey-box access makes it practical for real-world scenarios where full training data access isn't available, and the initial results suggest strong performance.

## Keywords

membership, training, data, dataset, non, non membership, correlation, dataset used, datasets, detecting

## Links

- [Paper URL](https://arxiv.org/abs/2603.22707)

---
*Auto-generated on 2026-03-25 10:09:33 UTC*
