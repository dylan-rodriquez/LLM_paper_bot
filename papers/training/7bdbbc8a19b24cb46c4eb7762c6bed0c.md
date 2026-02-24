# MANATEE: Inference-Time Lightweight Diffusion Based Safety Defense for LLMs

**Authors:** Chun Yan Ryan Kan, Tommy Tran, Vedant Yadav, Ava Cai, Kevin Zhu, Ruizhe Li, Maheep Chaudhary

**Published:** 2026-02-24 | **Source:** arXiv RSS

**Categories:** cs.CR

**Significance Score:** 90.0/100

## Abstract

arXiv:2602.18782v1 Announce Type: cross 
Abstract: Defending LLMs against adversarial jailbreak attacks remains an open challenge. Existing defenses rely on binary classifiers that fail when adversarial input falls outside the learned decision boundary, and repeated fine-tuning is computationally expensive while potentially degrading model capabilities. We propose MANATEE, an inference-time defense that uses density estimation over a benign representation manifold. MANATEE learns the score function of benign hidden states and uses diffusion to project anomalous representations toward safe regions--requiring no harmful training data and no architectural modifications. Experiments across Mistral-7B-Instruct, Llama-3.1-8B-Instruct, and Gemma-2-9B-it demonstrate that MANATEE reduce Attack Success Rate by up to 100\% on certain datasets, while preserving model utility on benign inputs.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a critical problem in LLM safety – adversarial jailbreaking – with a novel approach that avoids the pitfalls of traditional defenses. The use of diffusion models for inference-time safety is a clever idea, and the reported results of up to 100% attack success rate reduction are impressive. While the abstract doesn't detail the complexity of implementation, the core concept appears sound and well-motivated, suggesting a high likelihood of positive reception within the community.

## Keywords

manatee, benign, adversarial, defense, diffusion, inference, inference time, instruct, llms, manatee inference

## Links

- [Paper URL](https://arxiv.org/abs/2602.18782)

---
*Auto-generated on 2026-02-24 09:58:26 UTC*
