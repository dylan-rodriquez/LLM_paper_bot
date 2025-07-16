# DCR: Quantifying Data Contamination in LLMs Evaluation

**Authors:** Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, M-Tahar Kechadi

**Published:** 2025-07-16 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2507.11405v1 Announce Type: new 
Abstract: The rapid advancement of large language models (LLMs) has heightened concerns about benchmark data contamination (BDC), where models inadvertently memorize evaluation data, inflating performance metrics and undermining genuine generalization assessment. This paper introduces the Data Contamination Risk (DCR) framework, a lightweight, interpretable pipeline designed to detect and quantify BDC across four granular levels: semantic, informational, data, and label. By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. Validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, the DCR framework reliably diagnoses contamination severity and with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline. Emphasizing computational efficiency and transparency, DCR provides a practical tool for integrating contamination assessment into routine evaluations, fostering fairer comparisons and enhancing the credibility of LLM benchmarking practices.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 90.0/100

**Justification:** This paper tackles a crucial problem in LLM evaluation – data contamination – with a novel framework (DCR) that quantifies contamination at multiple granularities. The reported accuracy adjustment within 4% of a baseline is a strong result, suggesting the method is both effective and practical. The use of a fuzzy inference system for synthesizing contamination scores is a clever approach, and the validation across diverse tasks and model sizes strengthens the findings. The work is well-aligned with current concerns in the field and likely to be well-received.

## Keywords

contamination, dcr, data, data contamination, llms, accuracy, assessment, bdc, dcr factor, dcr framework

## Links

- [Paper URL](https://arxiv.org/abs/2507.11405)

---
*Auto-generated on 2025-07-16 09:34:05 UTC*
