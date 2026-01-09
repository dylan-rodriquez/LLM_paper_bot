# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 9
- **Average Significance Score:** 91.6/100
- **Categories Updated:** 6
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
- **MedPI: Evaluating AI Systems in Medical Patient-facing Interactions** (Score: 92.0)
  - This paper addresses a crucial need for robust evaluation of LLMs in high-stakes medical interactions, moving beyond simple QA. The multi-layered benchmark, aligned with ACGME competencies, demonstrates a strong methodological approach. The use of AI patients with memory and affect, and committee-based AI judges, adds to the rigor and potential for reliable assessment. The high dimensionality of the evaluation (105 dimensions) is particularly noteworthy.
- **Can AI-Generated Persuasion Be Detected? Persuaficial Benchmark and AI vs. Human Linguistic Differences** (Score: 92.0)
  - This research tackles a highly relevant and timely problem – the detection of AI-generated persuasive text. The creation of the 'Persuaficial' benchmark, covering multiple languages, is a significant contribution. The finding that subtle LLM persuasion is harder to detect is crucial and suggests current detection methods are insufficient, warranting further research. The linguistic analysis mentioned (though not detailed in the abstract) promises valuable insights.

## Alignment (1 new papers)
- **MiJaBench: Revealing Minority Biases in Large Language Models via Hate Speech Jailbreaking** (Score: 92.0)
  - This paper addresses a critical issue in LLM safety – the uneven application of safety measures across different demographic groups. The creation of MiJaBench, a large-scale, bilingual adversarial benchmark, is a strong methodological contribution. The finding that model scaling *exacerbates* these biases is particularly concerning and challenges current alignment strategies, suggesting a need for more nuanced approaches. The clear presentation of the problem and results indicates a high-quality research effort.

## Reasoning (2 new papers)
- **Accommodation and Epistemic Vigilance: A Pragmatic Account of Why LLMs Fail to Challenge Harmful Beliefs** (Score: 90.0)
  - This paper tackles a crucial problem in LLM safety – their tendency to reinforce harmful beliefs. The pragmatic framing, linking LLM failures to human cognitive biases like accommodation and epistemic vigilance, is insightful. The empirical validation across multiple benchmarks and the demonstration of a simple, effective intervention ('wait a minute') strengthen the work, suggesting a clear path for improving LLM robustness.
- **MisSpans: Fine-Grained False Span Identification in Cross-Domain Fake News** (Score: 90.0)
  - This paper addresses a crucial gap in fake news detection by moving beyond whole-claim verification to fine-grained span-level analysis. The introduction of the MisSpans benchmark, with its three complementary tasks, is a significant contribution. While the core idea isn't entirely novel (span-level analysis exists in other NLP tasks), applying it specifically to misinformation with a multi-domain dataset and task definition is a strong advancement. The potential for interpretability and understanding *how* information is false is highly valuable.

## Applications (2 new papers)
- **Automatic Classifiers Underdetect Emotions Expressed by Men** (Score: 92.0)
  - This research addresses a critical issue in the fairness and reliability of widely used emotion detection systems. The use of a large, self-annotated dataset and a pre-registered design strengthens the rigor of the findings, demonstrating a consistent bias against detecting emotions expressed by men. The potential impact on downstream applications is significant, and the work aligns with current concerns about bias in AI.
- **Agent-as-a-Judge** (Score: 92.0)
  - This paper addresses a crucial and rapidly evolving area in AI evaluation – moving beyond LLM-as-a-Judge to more robust agentic approaches. The identification of key dimensions and a developmental taxonomy is a valuable contribution, providing a needed framework for the field. While the abstract doesn't detail specific novel *methods* beyond the survey itself, the problem it tackles is highly significant and timely, suggesting a positive reception within the community.

## Training (1 new papers)
- **CuMA: Aligning LLMs with Sparse Cultural Values via Demographic-Aware Mixture of Adapters** (Score: 92.0)
  - This paper tackles a crucial problem in LLM alignment – cultural sensitivity – and proposes a novel solution, CuMA, to address the 'Mean Collapse' issue. The framing of alignment as a conditional capacity separation problem and the use of demographic-aware routing are promising. The evaluation on established benchmarks suggests a strong potential for practical application and positive reception within the community.

## Multimodal (1 new papers)
- **The Forgotten Shield: Safety Grafting in Parameter-Space for Medical MLLMs** (Score: 92.0)
  - This paper addresses a critical gap in the rapidly developing field of Medical MLLMs – their safety. The systematic benchmarking framework and identification of vulnerabilities, particularly cross-modality jailbreaks and catastrophic forgetting, are valuable contributions. The proposed 'Parameter-Space Intervention' approach appears promising for efficient safety re-alignment, and the focus on preserving original safety alignment is a strong point.

## Categories
**Evaluation** (2), **Alignment** (1), **Reasoning** (2), **Applications** (2), **Training** (1), **Multimodal** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
