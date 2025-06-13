# Unsupervised Elicitation of Language Models

**Authors:** Jiaxin Wen, Zachary Ankner, Arushi Somani, Peter Hase, Samuel Marks, Jacob Goldman-Wetzler, Linda Petrini, Henry Sleight, Collin Burns, He He, Shi Feng, Ethan Perez, Jan Leike

**Published:** 2025-06-13 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2506.10139v1 Announce Type: new 
Abstract: To steer pretrained language models for downstream tasks, today's post-training paradigm relies on humans to specify desired behaviors. However, for models with superhuman capabilities, it is difficult or impossible to get high-quality human supervision. To address this challenge, we introduce a new unsupervised algorithm, Internal Coherence Maximization (ICM), to fine-tune pretrained language models on their own generated labels, \emph{without external supervision}. On GSM8k-verification, TruthfulQA, and Alpaca reward modeling tasks, our method matches the performance of training on golden supervision and outperforms training on crowdsourced human supervision. On tasks where LMs' capabilities are strongly superhuman, our method can elicit those capabilities significantly better than training on human labels. Finally, we show that our method can improve the training of frontier LMs: we use our method to train an unsupervised reward model and use reinforcement learning to train a Claude 3.5 Haiku-based assistant. Both the reward model and the assistant outperform their human-supervised counterparts.

## Analysis

**Innovation Score:** 80.0/100
**Impact Score:** 85.0/100  
**Sentiment Score:** 92.0/100

**Justification:** This paper addresses a crucial bottleneck in scaling language models – the difficulty of obtaining high-quality human supervision, especially for highly capable models. The proposed 'Internal Coherence Maximization' (ICM) method is a novel approach to fine-tuning LMs without external labels, and the reported results, matching or exceeding human-supervised training, are compelling. The ability to elicit superhuman capabilities is particularly noteworthy, suggesting a significant advancement in LM training paradigms. The positive results on frontier LMs further strengthen the paper's potential.

## Keywords

training, human, method, models, supervision, capabilities, language, language models, reward, tasks

## Links

- [Paper URL](https://arxiv.org/abs/2506.10139)

---
*Auto-generated on 2025-06-13 09:29:22 UTC*
