# Evaluating Temporal Consistency in Multi-Turn Language Models

**Authors:** Yash Kumar Atri, Steven L. Johnson, Tom Hartvigsen

**Published:** 2026-04-28 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2604.23051v1 Announce Type: new 
Abstract: Language models are increasingly deployed in interactive settings where users reason about facts over time rather than in isolation. In such scenarios, correct behavior requires models to maintain and update implicit temporal assumptions established earlier in a conversation. We study this challenge through the lens of temporal scope stability: the ability to preserve, override, or transfer time-scoped factual context across dialogue turns. We introduce ChronoScope, a large-scale diagnostic benchmark designed to isolate temporal scope behavior in controlled multi-turn interactions, comprising over one million deterministically generated question chains grounded in Wikidata. ChronoScope evaluates whether models can correctly retain inferred temporal scope when follow-up questions omit explicit time references, spanning implicit carryover, explicit scope switching, cross-entity transfer, and longer temporal trajectories. Through extensive evaluation of state-of-the-art language models, we find that temporal scope stability is frequently violated in controlled multi-turn settings, with models often drifting toward present-day assumptions despite correct underlying knowledge. These failures intensify with interaction length and persist even under oracle context conditions, revealing a gap between single-turn factual accuracy and coherent temporal reasoning under sequential interaction. We make our dataset and evaluation suite publicly available at https://github.com/yashkumaratri/ChronoScope

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper tackles a crucial problem in the deployment of LLMs – maintaining temporal consistency in multi-turn dialogues. The introduction of ChronoScope, a large-scale diagnostic benchmark, is a strong methodological contribution. The focus on temporal scope stability and the controlled generation of question chains using Wikidata suggest a rigorous approach, and the problem is highly relevant to the current trajectory of conversational AI research. The potential for improving LLM reliability in real-world applications is significant.

## Keywords

temporal, models, scope, temporal scope, turn, chronoscope, language, language models, multi, multi turn

## Links

- [Paper URL](https://arxiv.org/abs/2604.23051)

---
*Auto-generated on 2026-04-28 11:14:14 UTC*
