# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 12
- **Average Significance Score:** 91.3/100
- **Categories Updated:** 7
- **Date Range:** Last 1 day(s)

## Selection Criteria
Papers are automatically selected based on:
- **Innovation Score:** Novel methods, breakthrough approaches
- **Impact Score:** Practical applications, real-world significance  
- **Technical Quality:** Mathematical rigor, comprehensive analysis
- **Sentiment Analysis:** Positive reception indicators
- **Minimum Threshold:** 90.0/100 significance score

## Papers Added

## Theoretical (1 new papers)
- **Multi-Method Validation of Large Language Model Medical Translation Across High- and Low-Resource Languages** (Score: 92.0)
  - This research addresses a highly significant problem – access to medical translation – and employs a robust, multi-faceted validation framework. The use of multiple LLMs and a five-layer validation approach, including back-translation and lexical borrowing analysis, demonstrates methodological rigor. While the core idea of applying LLMs to translation isn't novel, the comprehensive evaluation across diverse resource languages and the scale of the study (704 translation pairs) are strong points.

## Architectures (2 new papers)
- **Detecting Non-Membership in LLM Training Data via Rank Correlations** (Score: 92.0)
  - This paper tackles a crucial and currently under-explored problem in the LLM space – verifying *non*-membership in training data. The approach of using rank correlations in logits is a clever and relatively simple method that appears effective. The focus on grey-box access makes it practical for real-world scenarios where full training data access isn't available, and the initial results suggest strong performance.
- **Sparser, Faster, Lighter Transformer Language Models** (Score: 90.0)
  - This paper addresses a critical bottleneck in LLM scaling – computational cost. The combination of sparsity techniques, a new packing format, and optimized CUDA kernels suggests a rigorous approach to improving efficiency. The reported 99% sparsity with minimal performance impact is particularly promising, and the focus on practical implementation via GPU optimization strengthens the work's potential.

## Evaluation (4 new papers)
- **When AI Shows Its Work, Is It Actually Working? Step-Level Evaluation Reveals Frontier Language Models Frequently Bypass Their Own Reasoning** (Score: 92.0)
  - This paper tackles a crucial issue in the rapidly evolving field of LLMs: the reliability of 'reasoning' steps. The proposed 'step-level evaluation' is a simple yet powerful method for uncovering potentially superficial reasoning, and the low cost of implementation makes it widely accessible. The breadth of models and tasks tested strengthens the findings, suggesting a systemic problem with current LLM reasoning capabilities.
- **Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy** (Score: 92.0)
  - This research tackles a crucial problem – the unreliability of AI-generated text detectors despite high benchmark scores. The use of explainable AI to investigate *why* detectors fail, rather than just *that* they fail, is a strong methodological choice. The reported F1 score is competitive, but the key finding of generalization failure is particularly important and suggests a need for more robust detection methods. The focus on linguistic features and systematic evaluation across datasets and generators adds to the rigor.
- **From Static Templates to Dynamic Runtime Graphs: A Survey of Workflow Optimization for LLM Agents** (Score: 92.0)
  - This survey tackles a highly relevant and rapidly evolving area – workflow optimization for LLM agents. The framing of workflows as 'agentic computation graphs' and the categorization based on workflow structure determination (static vs. dynamic) provides a valuable organizational lens. While a survey doesn't inherently present novel *methods*, the synthesis and categorization of existing work is strong, and the topic's importance ensures a positive reception within the AI community.
- **LLM Olympiad: Why Model Evaluation Needs a Sealed Exam** (Score: 92.0)
  - This paper addresses a critical issue in LLM evaluation – the increasing unreliability of benchmarks due to gaming and data contamination. The proposed 'Olympiad' style evaluation offers a compelling solution by emphasizing sealed exams and standardized harnesses, promoting more trustworthy results. While the core idea isn't entirely novel (closed benchmarks exist), the combination of sealing, freezing, and full release post-evaluation is a strong and practical approach. The paper is well-focused and clearly articulates the problem and proposed solution.

## Alignment (1 new papers)
- **Steering LLMs for Culturally Localized Generation** (Score: 90.0)
  - This paper tackles a crucial problem in LLM deployment – cultural bias – with a novel and rigorous approach. The use of mechanistic interpretability and sparse autoencoders to identify and manipulate 'Cultural Embeddings' is a significant step beyond existing prompting or post-training alignment methods. The reported improvements in cultural faithfulness and elicitation of long-tail concepts suggest a promising path forward for more inclusive and globally relevant LLMs. The complementary nature of their approach to existing methods further strengthens its potential.

## Agents (2 new papers)
- **T-MAP: Red-Teaming LLM Agents with Trajectory-aware Evolutionary Search** (Score: 92.0)
  - This paper addresses a crucial and timely problem in LLM security – red-teaming agents in complex environments like MCP. The trajectory-aware evolutionary search (T-MAP) approach appears novel and effectively targets agent-specific vulnerabilities beyond simple text-based attacks. The reported performance against frontier models like GPT-5.2 and Gemini-3-Pro suggests a significant contribution to the field, and the focus on attack *realization* rather than just eliciting harmful text is a strong point.
- **The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration** (Score: 92.0)
  - This paper addresses a highly relevant and rapidly evolving area in LLM research – moving beyond single-tool use to complex orchestration. The comprehensive review approach, unifying task formulations and outlining core dimensions, suggests a rigorous and well-structured analysis. Given the practical challenges of safety, cost, and verifiability in real-world agent deployments, this work is poised to be influential and well-received by the community.

## General (1 new papers)
- **Between Rules and Reality: On the Context Sensitivity of LLM Moral Judgment** (Score: 90.0)
  - This paper addresses a crucial gap in LLM morality research by moving beyond static scenarios to explore context sensitivity, mirroring human moral reasoning. The introduction of the Contextual MoralChoice dataset is a strong methodological contribution, and the finding that models and humans react differently to contextual shifts is insightful. The proposed activation steering approach offers a potential path towards better alignment, suggesting practical implications for responsible AI development. The work is well-scoped and clearly presented.

## Multimodal (1 new papers)
- **MedObvious: Exposing the Medical Moravec's Paradox in VLMs via Clinical Triage** (Score: 90.0)
  - This paper addresses a crucial and often overlooked problem in medical VLMs: the ability to perform basic sanity checks on input data *before* attempting complex reasoning. The 'MedObvious' benchmark is a clever way to isolate this capability, and the progressive tiers suggest a thoughtful approach to evaluating model robustness. The framing of the problem as a 'Medical Moravec's Paradox' is insightful and highlights the potential for models to excel at complex tasks while failing at seemingly simple ones.

## Categories
**Theoretical** (1), **Architectures** (2), **Evaluation** (4), **Alignment** (1), **Agents** (2), **General** (1), **Multimodal** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
