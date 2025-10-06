# Leave No TRACE: Black-box Detection of Copyrighted Dataset Usage in Large Language Models via Watermarking

**Authors:** Jingqi Zhang, Ruibo Chen, Yingqing Yang, Peihua Mai, Heng Huang, Yan Pang

**Published:** 2025-10-06 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2510.02962v1 Announce Type: new 
Abstract: Large Language Models (LLMs) are increasingly fine-tuned on smaller, domain-specific datasets to improve downstream performance. These datasets often contain proprietary or copyrighted material, raising the need for reliable safeguards against unauthorized use. Existing membership inference attacks (MIAs) and dataset-inference methods typically require access to internal signals such as logits, while current black-box approaches often rely on handcrafted prompts or a clean reference dataset for calibration, both of which limit practical applicability. Watermarking is a promising alternative, but prior techniques can degrade text quality or reduce task performance. We propose TRACE, a practical framework for fully black-box detection of copyrighted dataset usage in LLM fine-tuning. \texttt{TRACE} rewrites datasets with distortion-free watermarks guided by a private key, ensuring both text quality and downstream utility. At detection time, we exploit the radioactivity effect of fine-tuning on watermarked data and introduce an entropy-gated procedure that selectively scores high-uncertainty tokens, substantially amplifying detection power. Across diverse datasets and model families, TRACE consistently achieves significant detections (p<0.05), often with extremely strong statistical evidence. Furthermore, it supports multi-dataset attribution and remains robust even after continued pretraining on large non-watermarked corpora. These results establish TRACE as a practical route to reliable black-box verification of copyrighted dataset usage. We will make our code available at: https://github.com/NusIoraPrivacy/TRACE.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 85.0/100

**Justification:** This paper tackles a very important and timely problem – protecting copyright in the age of LLM fine-tuning. The proposed TRACE framework addresses limitations of existing black-box detection methods by focusing on distortion-free watermarking, which is a significant improvement. While watermarking isn't entirely novel, the emphasis on practicality (text quality, downstream utility) and black-box operation suggests a strong contribution. The high scores reflect the relevance and potential of the work.

## Keywords

dataset, trace, black, black box, box, copyrighted, datasets, detection, copyrighted dataset, dataset usage

## Links

- [Paper URL](https://arxiv.org/abs/2510.02962)

---
*Auto-generated on 2025-10-06 09:31:18 UTC*
