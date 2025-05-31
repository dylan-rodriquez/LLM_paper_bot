# How Do Diffusion Models Improve Adversarial Robustness?

**Authors:** Liu Yuezhang, Xue-Xin Wei

**Published:** 2025-05-31 | **Source:** arXiv RSS

**Categories:** cs.LG

**Significance Score:** 85.0/100

## Abstract

arXiv:2505.22839v1 Announce Type: new 
Abstract: Recent findings suggest that diffusion models significantly enhance empirical adversarial robustness. While some intuitive explanations have been proposed, the precise mechanisms underlying these improvements remain unclear. In this work, we systematically investigate how and how well diffusion models improve adversarial robustness. First, we observe that diffusion models intriguingly increase, rather than decrease, the $\ell_p$ distance to clean samples--challenging the intuition that purification denoises inputs closer to the original data. Second, we find that the purified images are heavily influenced by the internal randomness of diffusion models, where a compression effect arises within each randomness configuration. Motivated by this observation, we evaluate robustness under fixed randomness and find that the improvement drops to approximately 24% on CIFAR-10--substantially lower than prior reports approaching 70%. Importantly, we show that this remaining robustness gain strongly correlates with the model's ability to compress the input space, revealing the compression rate as a reliable robustness indicator without requiring gradient-based analysis. Our findings provide novel insights into the mechanisms underlying diffusion-based purification, and offer guidance for developing more effective and principled adversarial purification systems.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 75.0/100  
**Sentiment Score:** 80.0/100

**Justification:** This paper tackles a crucial question regarding the observed adversarial robustness of diffusion models. The counter-intuitive finding that diffusion models *increase* distance to clean samples, and the subsequent analysis of randomness influencing robustness, are strong points. The observed drop in robustness when fixing randomness is particularly compelling and suggests a fragility in the reported gains, indicating a need for more careful evaluation of these models. The work is well-motivated and the initial results are presented clearly.

## Keywords

diffusion, robustness, diffusion models, models, adversarial, adversarial robustness, purification, randomness, based, compression

## Links

- [Paper URL](https://arxiv.org/abs/2505.22839)

---
*Auto-generated on 2025-05-31 09:25:12 UTC*
