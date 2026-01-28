# Unsupervised Elicitation of Language Models

**Authors:** Jiaxin Wen, Zachary Ankner, Arushi Somani, Peter Hase, Samuel Marks, Jacob Goldman-Wetzler, Linda Petrini, Henry Sleight, Collin Burns, He He, Shi Feng, Ethan Perez, Jan Leike

**Published:** 2026-01-28 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2506.10139v2 Announce Type: replace 
Abstract: To steer pretrained language models for downstream tasks, today's post-training paradigm relies on humans to specify desired behaviors. However, for models with superhuman capabilities, it is difficult or impossible to get high-quality human supervision. To address this challenge, we introduce a new unsupervised algorithm, Internal Coherence Maximization (ICM), to fine-tune pretrained language models on their own generated labels, \emph{without external supervision}. On GSM8k-verification, TruthfulQA, and Alpaca reward modeling tasks, our method matches the performance of training on golden labels and outperforms training on crowdsourced human supervision. On tasks where LMs' capabilities are strongly superhuman, our method can elicit those capabilities significantly better than training on human labels. Finally, we show that our method can improve the training of frontier LMs: we use our method to train an unsupervised reward model and use reinforcement learning to train a Claude 4 Sonnet-based assistant. The resulting assistant matches its counterpart trained on production-grade human labels on average, with higher scores on chat and safety yet lower scores on math and coding.

## Analysis

**Innovation Score:** 80.0/100
**Impact Score:** 85.0/100  
**Sentiment Score:** 92.0/100

**Justification:** This paper addresses a crucial bottleneck in scaling language models – the difficulty of obtaining high-quality human supervision, especially for highly capable models. The proposed Internal Coherence Maximization (ICM) method is a novel approach to self-training that demonstrably matches or exceeds performance compared to human-labeled data, and even outperforms it in scenarios where LMs have superhuman capabilities. The results on GSM8k-verification, TruthfulQA, and Alpaca reward modeling are compelling, suggesting a significant advancement in unsupervised alignment techniques.

## Keywords

training, human, labels, method, models, capabilities, language, language models, supervision, tasks

## Links

- [Paper URL](https://arxiv.org/abs/2506.10139)

---
*Auto-generated on 2026-01-28 09:58:15 UTC*
