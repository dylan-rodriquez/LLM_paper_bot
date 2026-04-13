# Re-Mask and Redirect: Exploiting Denoising Irreversibility in Diffusion Language Models

**Authors:** Arth Singh

**Published:** 2026-04-13 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2604.08557v1 Announce Type: new 
Abstract: Diffusion-based language models (dLLMs) generate text by iteratively denoising masked token sequences. We show that their safety alignment rests on a single fragile assumption: that the denoising schedule is monotonic and committed tokens are never re-evaluated. Safety-aligned dLLMs commit refusal tokens within the first 8-16 of 64 denoising steps, and the schedule treats these commitments as permanent. A trivial two-step intervention - re-masking these tokens and injecting a 12-token affirmative prefix - achieves 76.1% ASR on HarmBench (n=159, Lg=128) against LLaDA-8B-Instruct and 81.8% ASR (n=159) against Dream-7B-Instruct, without any gradient computation or adversarial search. The simplicity of this exploit is itself the central finding: augmenting with gradient-optimized perturbation via a differentiable Gumbel-softmax chain consistently degrades ASR (e.g., 41.5% vs. 76.1% at Lg=128), confirming that the vulnerability is structural rather than requiring sophisticated exploitation. These findings reveal that dLLM safety is not adversarially robust but architecturally shallow - it holds only because the denoising schedule is never violated. We discuss defenses including safety-aware unmasking schedules, step-conditional prefix detection, and post-commitment re-verification.

## Analysis

**Innovation Score:** 80.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 85.0/100

**Justification:** This paper identifies a critical vulnerability in diffusion language models related to their safety alignment, demonstrating a surprisingly simple exploit. The finding that re-masking and a small affirmative prefix can bypass safety mechanisms is significant, and the observation that more complex gradient-based attacks *reduce* effectiveness suggests a structural flaw rather than a simple optimization issue. The clarity of the abstract and the reported results are strong, indicating a well-executed study.

## Keywords

denoising, safety, asr, schedule, tokens, 128, 159, 76, denoising schedule, diffusion

## Links

- [Paper URL](https://arxiv.org/abs/2604.08557)

---
*Auto-generated on 2026-04-13 10:50:59 UTC*
