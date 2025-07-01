# Generalist Reward Models: Found Inside Large Language Models

**Authors:** Yi-Chen Li, Tian Xu, Yang Yu, Xuqin Zhang, Xiong-Hui Chen, Zhongxiang Ling, Ningjing Chao, Lei Yuan, Zhi-Hua Zhou

**Published:** 2025-07-01 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2506.23235v1 Announce Type: new 
Abstract: The alignment of Large Language Models (LLMs) is critically dependent on reward models trained on costly human preference data. While recent work explores bypassing this cost with AI feedback, these methods often lack a rigorous theoretical foundation. In this paper, we discover that a powerful generalist reward model is already latently present within any LLM trained via standard next-token prediction. We prove that this endogenous reward is not a heuristic, but is theoretically equivalent to a reward function learned through offline inverse reinforcement learning. This connection allows us to directly elicit a high-quality reward signal from a base (pre-trained or supervised fine-tuned) model without any further training. Critically, we also prove that subsequent reinforcement learning using this endogenous reward leads to a policy with a provably superior error bound compared to the base model. To our best knowledge, this is the first theoretical proof of the effectiveness of reinforcement learning for LLMs. Our experiments validate this theory, demonstrating that our method not only outperforms existing LLM-as-a-judge approaches but can also surpass explicitly trained reward models. These findings suggest that the reward modeling stage can be replaced by a principled method of eliciting the knowledge already captured during pre-training, heralding a more efficient, powerful, and scalable paradigm for LLMs alignment as well as multi-modal models.

## Analysis

**Innovation Score:** 88.0/100
**Impact Score:** 90.0/100  
**Sentiment Score:** 95.0/100

**Justification:** This paper tackles a crucial problem in LLM alignment – the cost of human preference data. The theoretical grounding of an 'endogenous reward' within LLMs, equivalent to offline IRL, is a significant advancement. The claim of a provably superior error bound for RL using this reward further strengthens the work, suggesting a potentially paradigm-shifting approach to LLM alignment.

## Keywords

reward, models, trained, learning, llms, model, reinforcement, reinforcement learning, reward models, alignment

## Links

- [Paper URL](https://arxiv.org/abs/2506.23235)

---
*Auto-generated on 2025-07-01 09:31:02 UTC*
