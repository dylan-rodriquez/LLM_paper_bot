# Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs

**Authors:** Mohammad Tavakoli, Alireza Salemi, Carrie Ye, Mohamed Abdalla, Hamed Zamani, J Ross Mitchell

**Published:** 2025-11-03 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2510.27246v1 Announce Type: new 
Abstract: Evaluating the abilities of large language models (LLMs) for tasks that require long-term memory and thus long-context reasoning, for example in conversational settings, is hampered by the existing benchmarks, which often lack narrative coherence, cover narrow domains, and only test simple recall-oriented tasks. This paper introduces a comprehensive solution to these challenges. First, we present a novel framework for automatically generating long (up to 10M tokens), coherent, and topically diverse conversations, accompanied by probing questions targeting a wide range of memory abilities. From this, we construct BEAM, a new benchmark comprising 100 conversations and 2,000 validated questions. Second, to enhance model performance, we propose LIGHT-a framework inspired by human cognition that equips LLMs with three complementary memory systems: a long-term episodic memory, a short-term working memory, and a scratchpad for accumulating salient facts. Our experiments on BEAM reveal that even LLMs with 1M token context windows (with and without retrieval-augmentation) struggle as dialogues lengthen. In contrast, LIGHT consistently improves performance across various models, achieving an average improvement of 3.5%-12.69% over the strongest baselines, depending on the backbone LLM. An ablation study further confirms the contribution of each memory component.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper tackles a crucial bottleneck in LLM development – long-term memory and context handling. The creation of BEAM, a benchmark designed to specifically address the shortcomings of existing evaluations, is a strong contribution. The proposed LIGHT framework, inspired by human cognition, suggests a thoughtful approach to improving LLM memory capabilities, and the focus on episodic, working, and scratchpad memory is promising. The potential for advancing conversational AI and other long-context applications is significant.

## Keywords

memory, long, llms, term, long term, abilities, beam, context, conversations, framework

## Links

- [Paper URL](https://arxiv.org/abs/2510.27246)

---
*Auto-generated on 2025-11-03 09:31:59 UTC*
