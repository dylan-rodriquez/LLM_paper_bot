# MisSpans: Fine-Grained False Span Identification in Cross-Domain Fake News

**Authors:** Zhiwei Liu, Paul Thompson, Jiaqi Rong, Baojie Qu, Runteng Guo, Min Peng, Qianqian Xie, Sophia Ananiadou

**Published:** 2026-01-09 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 90.0/100

## Abstract

arXiv:2601.04857v1 Announce Type: new 
Abstract: Online misinformation is increasingly pervasive, yet most existing benchmarks and methods evaluate veracity at the level of whole claims or paragraphs using coarse binary labels, obscuring how true and false details often co-exist within single sentences. These simplifications also limit interpretability: global explanations cannot identify which specific segments are misleading or differentiate how a detail is false (e.g., distorted vs. fabricated). To address these gaps, we introduce MisSpans, the first multi-domain, human-annotated benchmark for span-level misinformation detection and analysis, consisting of paired real and fake news stories. MisSpans defines three complementary tasks: MisSpansIdentity for pinpointing false spans within sentences, MisSpansType for categorising false spans by misinformation type, and MisSpansExplanation for providing rationales grounded in identified spans. Together, these tasks enable fine-grained localisation, nuanced characterisation beyond true/false and actionable explanations. Expert annotators were guided by standardised guidelines and consistency checks, leading to high inter-annotator agreement. We evaluate 15 representative LLMs, including reasoning-enhanced and non-reasoning variants, under zero-shot and one-shot settings. Results reveal the challenging nature of fine-grained misinformation identification and analysis, and highlight the need for a deeper understanding of how performance may be influenced by multiple interacting factors, including model size and reasoning capabilities, along with domain-specific textual features. This project will be available at https://github.com/lzw108/MisSpans.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a crucial gap in fake news detection by moving beyond whole-claim verification to fine-grained span-level analysis. The introduction of the MisSpans benchmark, with its three complementary tasks, is a significant contribution. While the core idea isn't entirely novel (span-level analysis exists in other NLP tasks), applying it specifically to misinformation with a multi-domain dataset and task definition is a strong advancement. The potential for interpretability and understanding *how* information is false is highly valuable.

## Keywords

false, misinformation, misspans, domain, fine, fine grained, grained, reasoning, spans, analysis

## Links

- [Paper URL](https://arxiv.org/abs/2601.04857)

---
*Auto-generated on 2026-01-09 09:40:14 UTC*
