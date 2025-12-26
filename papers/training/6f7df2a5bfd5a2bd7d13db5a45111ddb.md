# Safety Alignment of LMs via Non-cooperative Games

**Authors:** Anselm Paulus, Ilia Kulikov, Brandon Amos, R\'emi Munos, Ivan Evtimov, Kamalika Chaudhuri, Arman Zharmagambetov

**Published:** 2025-12-26 | **Source:** arXiv RSS

**Categories:** cs.AI

**Significance Score:** 90.0/100

## Abstract

arXiv:2512.20806v1 Announce Type: new 
Abstract: Ensuring the safety of language models (LMs) while maintaining their usefulness remains a critical challenge in AI alignment. Current approaches rely on sequential adversarial training: generating adversarial prompts and fine-tuning LMs to defend against them. We introduce a different paradigm: framing safety alignment as a non-zero-sum game between an Attacker LM and a Defender LM trained jointly via online reinforcement learning. Each LM continuously adapts to the other's evolving strategies, driving iterative improvement. Our method uses a preference-based reward signal derived from pairwise comparisons instead of point-wise scores, providing more robust supervision and potentially reducing reward hacking. Our RL recipe, AdvGame, shifts the Pareto frontier of safety and utility, yielding a Defender LM that is simultaneously more helpful and more resilient to adversarial attacks. In addition, the resulting Attacker LM converges into a strong, general-purpose red-teaming agent that can be directly deployed to probe arbitrary target models.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 85.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper tackles a crucial problem in AI safety – aligning LMs – with a novel approach using a non-cooperative game framework. Framing safety alignment as an adversarial game with joint reinforcement learning is a promising direction, and the use of preference-based rewards is a strong methodological choice. The reported shift in the Pareto frontier suggests tangible improvements in both safety and utility, indicating a well-executed study with potential for significant impact.

## Keywords

lm, safety, adversarial, alignment, lms, attacker, attacker lm, defender, defender lm, models

## Links

- [Paper URL](https://arxiv.org/abs/2512.20806)

---
*Auto-generated on 2025-12-26 09:33:18 UTC*
