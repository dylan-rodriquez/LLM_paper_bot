# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 7
- **Average Significance Score:** 91.7/100
- **Categories Updated:** 2
- **Date Range:** Last 1 day(s)

## Selection Criteria
Papers are automatically selected based on:
- **Innovation Score:** Novel methods, breakthrough approaches
- **Impact Score:** Practical applications, real-world significance  
- **Technical Quality:** Mathematical rigor, comprehensive analysis
- **Sentiment Analysis:** Positive reception indicators
- **Minimum Threshold:** 90.0/100 significance score

## Papers Added

## Evaluation (2 new papers)
- **Beyond Accuracy: Risk-Sensitive Evaluation of Hallucinated Medical Advice** (Score: 92.0)
  - This paper addresses a crucial and timely problem in the deployment of LLMs in healthcare: the nuanced risk associated with hallucinations. Moving beyond simple accuracy metrics to focus on the *actionability* and potential harm of incorrect medical advice is a significant step forward. The proposed risk-sensitive evaluation framework appears well-motivated and the combination of risk scoring with relevance is a clever approach. The work is likely to be well-received by the community given the increasing focus on safety and reliability of medical LLMs.
- **Large Language Models for Geolocation Extraction in Humanitarian Crisis Response** (Score: 92.0)
  - This research tackles a highly significant problem – improving geolocation extraction in humanitarian crises, specifically addressing biases in existing systems. The combination of LLM-based NER with an agent-based geocoding module appears well-reasoned and the use of a refined HumSet dataset strengthens the evaluation. While LLMs are increasingly applied to NLP tasks, applying them with a focus on fairness and a specialized agent-based approach for geocoding demonstrates a solid methodological approach.

## Reasoning (5 new papers)
- **DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity** (Score: 92.0)
  - This paper tackles a crucial bottleneck in LLM deployment – KV cache size. The approach of using residual encoding based on long-range similarity is a clever way to compress the cache while preserving information. The introduction of Sparse-vLLM suggests a focus on practical implementation and system-level optimization, increasing the likelihood of real-world impact. The abstract is well-written and clearly articulates the problem and proposed solution.
- **When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents** (Score: 92.0)
  - This paper addresses a crucial and timely problem in the rapidly evolving field of computer-use agents – the potential for unintended and harmful behaviors. The introduction of a framework (AutoElicit) for automatically eliciting these behaviors from benign inputs is a strong methodological contribution. While the abstract doesn't detail the specifics of the framework, the claim of surfacing 'hundreds' of harmful behaviors suggests a robust and valuable investigation, positioning it for positive reception within the AI safety community.
- **Language Predicts Identity Fusion Across Cultures and Reveals Divergent Pathways to Violence** (Score: 92.0)
  - This research tackles a highly relevant and pressing issue – understanding the roots of extremism – and proposes a novel method for measuring identity fusion using cognitive linguistics and LLMs. The reported outperformance compared to existing methods and the identification of divergent pathways to violence are strong indicators of quality. The use of datasets from multiple cultures adds to the robustness of the findings, and the potential for a scalable tool for extremism detection is significant.
- **Is Reasoning Capability Enough for Safety in Long-Context Language Models?** (Score: 92.0)
  - This paper addresses a critical safety concern with increasingly capable LLMs – the potential for harmful intent to emerge from seemingly benign long-context interactions. The introduction of 'compositional reasoning attacks' is a novel and concerning threat model. The evaluation across 14 frontier models with 64k context windows demonstrates a rigorous approach and suggests a significant gap in current safety mechanisms. The findings are likely to be well-received by the LLM safety community.
- **The Judge Who Never Admits: Hidden Shortcuts in LLM-based Evaluation** (Score: 90.0)
  - This research tackles a crucial issue in the rapidly evolving field of LLMs – the reliability and fairness of LLM-based evaluation. The methodology of injecting controlled cues and measuring both verdict shift and cue acknowledgment rates is clever and well-defined. The study's scope, covering multiple models and datasets, strengthens its findings and suggests a broad relevance to the community. The high sentiment score reflects the current focus on LLM alignment and evaluation.

## Categories
**Evaluation** (2), **Reasoning** (5)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
