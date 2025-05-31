# Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference

**Authors:** Donghyeon Joo, Helya Hosseini, Ramyad Hadidi, Bahar Asgari

**Published:** 2025-05-31 | **Source:** arXiv RSS

**Categories:** cs.LG

**Significance Score:** 88.0/100

## Abstract

arXiv:2505.22913v1 Announce Type: new 
Abstract: We demonstrate that unstructured sparsity significantly improves KV cache compression for LLMs, enabling sparsity levels up to 70% without compromising accuracy or requiring fine-tuning. We conduct a systematic exploration of pruning strategies and find per-token magnitude-based pruning as highly effective for both Key and Value caches under unstructured sparsity, surpassing prior structured pruning schemes. The Key cache benefits from prominent outlier elements, while the Value cache surprisingly benefits from a simple magnitude-based pruning despite its uniform distribution. KV cache size is the major bottleneck in decode performance due to high memory overhead for large context lengths. To address this, we use a bitmap-based sparse format and a custom attention kernel capable of compressing and directly computing over compressed caches pruned to arbitrary sparsity patterns, significantly accelerating memory-bound operations in decode computations and thereby compensating for the overhead of runtime pruning and compression. Our custom attention kernel coupled with the bitmap-based format delivers substantial compression of KV cache upto 45% of dense inference and thereby enables longer context length and increased tokens/sec throughput of upto 2.23x compared to dense inference. Our pruning mechanism and sparse attention kernel is available at https://github.com/dhjoo98/mustafar.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 82.0/100  
**Sentiment Score:** 90.0/100

**Justification:** This paper addresses a critical bottleneck in LLM inference – KV cache size – and proposes a novel solution using unstructured sparsity. The systematic exploration of pruning strategies and the development of a custom attention kernel are strong points. The claim of achieving 70% sparsity without accuracy loss is significant, and the bitmap-based sparse format is a practical contribution. The positive framing and relevance to current LLM optimization trends suggest a favorable reception.

## Keywords

pruning, cache, sparsity, based, kv, kv cache, attention, attention kernel, compression, inference

## Links

- [Paper URL](https://arxiv.org/abs/2505.22913)

---
*Auto-generated on 2025-05-31 09:25:12 UTC*
