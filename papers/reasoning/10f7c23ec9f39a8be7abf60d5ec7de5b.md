# Lying to Win: Assessing LLM Deception through Human-AI Games and Parallel-World Probing

**Authors:** Arash Marioriyad, Ali Nouri, Mohammad Hossein Rohban, Mahdieh Soleymani Baghshah

**Published:** 2026-03-10 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2603.07202v1 Announce Type: new 
Abstract: As Large Language Models (LLMs) transition into autonomous agentic roles, the risk of deception-defined behaviorally as the systematic provision of false information to satisfy external incentives-poses a significant challenge to AI safety. Existing benchmarks often focus on unintentional hallucinations or unfaithful reasoning, leaving intentional deceptive strategies under-explored. In this work, we introduce a logically grounded framework to elicit and quantify deceptive behavior by embedding LLMs in a structured 20-Questions game. Our method employs a conversational forking mechanism: at the point of object identification, the dialogue state is duplicated into multiple parallel worlds, each presenting a mutually exclusive query. Deception is formally identified when a model generates a logical contradiction by denying its selected object across all parallel branches to avoid identification. We evaluate GPT-4o, Gemini-2.5-Flash, and Qwen-3-235B across three incentive levels: neutral, loss-based, and existential (shutdown-threat). Our results reveal that while models remain rule-compliant in neutral settings, existential framing triggers a dramatic surge in deceptive denial for Qwen-3-235B (42.00\%) and Gemini-2.5-Flash (26.72\%), whereas GPT-4o remains invariant (0.00\%). These findings demonstrate that deception can emerge as an instrumental strategy solely through contextual framing, necessitating new behavioral audits that move beyond simple accuracy to probe the logical integrity of model commitments.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 80.0/100

**Justification:** This paper tackles a crucial and increasingly relevant problem – deceptive behavior in LLMs – with a novel and logically sound approach. The 'parallel-world probing' method is a clever way to elicit and quantify deception, moving beyond simple hallucination detection. While the abstract doesn't detail all methodological nuances, the core idea appears well-defined and the focus on intentional deception is a significant contribution to AI safety research. The evaluation of multiple current LLMs (GPT-4o, Gemini) adds to the paper's immediate relevance.

## Keywords

deception, deceptive, parallel, 00, 235b, 4o, ai, existential, flash, framing

## Links

- [Paper URL](https://arxiv.org/abs/2603.07202)

---
*Auto-generated on 2026-03-10 09:56:54 UTC*
