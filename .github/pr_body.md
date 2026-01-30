# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 7
- **Average Significance Score:** 91.4/100
- **Categories Updated:** 5
- **Date Range:** Last 1 day(s)

## Selection Criteria
Papers are automatically selected based on:
- **Innovation Score:** Novel methods, breakthrough approaches
- **Impact Score:** Practical applications, real-world significance  
- **Technical Quality:** Mathematical rigor, comprehensive analysis
- **Sentiment Analysis:** Positive reception indicators
- **Minimum Threshold:** 90.0/100 significance score

## Papers Added

## Reasoning (1 new papers)
- **Large Language Models Naively Recover Ethnicity from Individual Records** (Score: 92.0)
  - This research addresses a critical ethical concern regarding the potential for LLMs to reveal sensitive demographic information. The finding that LLMs outperform established methods like BISG, and the demonstration of reduced bias, are significant. While the methodology appears sound based on the abstract, a full review would be needed to assess the robustness of the stratified sampling and the generalizability of the results. The high accuracy and potential for misuse suggest a strong positive, yet cautious, community reception.

## Alignment (1 new papers)
- **SHARP: Social Harm Analysis via Risk Profiles for Measuring Inequities in Large Language Models** (Score: 92.0)
  - This paper addresses a crucial problem in LLM evaluation – the inadequacy of scalar scores for capturing complex social harms. The proposed SHARP framework, with its multidimensional, distribution-aware approach and focus on worst-case behavior via CVaR, appears well-motivated and technically sound. The decomposition into bias, fairness, ethics, and reliability is a strong methodological choice, and the application to eleven frontier LLMs suggests a rigorous empirical evaluation.

## Evaluation (2 new papers)
- **The Compliance Paradox: Semantic-Instruction Decoupling in Automated Academic Code Evaluation** (Score: 92.0)
  - This paper tackles a crucial and timely problem in the burgeoning field of LLM-assisted education: the reliability of automated code evaluation. The identification of the 'Compliance Paradox' and the development of SPACI and AST-ASIP demonstrate a strong methodological approach and a clear understanding of the vulnerabilities within LLMs. The large-scale evaluation across multiple models and submissions adds to the rigor of the work, suggesting a high likelihood of positive reception within the research community.
- **FIT: Defying Catastrophic Forgetting in Continual LLM Unlearning** (Score: 92.0)
  - This paper tackles a very important and timely problem – continual unlearning in LLMs – which is crucial for addressing privacy, copyright, and safety concerns. The proposed 'FIT' framework, with its filtering, importance-aware updates, and targeted layer attribution, appears well-reasoned and designed to mitigate catastrophic forgetting. The focus on realistic, high-volume deletion requests is a strong point, suggesting a practical approach. The abstract is clear and concise, outlining the problem and solution effectively.

## Theoretical (1 new papers)
- **RAG-E: Quantifying Retriever-Generator Alignment and Failure Modes** (Score: 90.0)
  - This paper tackles a crucial problem in RAG systems – the misalignment between retriever and generator – with a novel explainability framework. The adaptation of Integrated Gradients and introduction of PMCSHAP demonstrate methodological rigor, and the WARG metric provides a quantifiable measure of alignment. The reported misalignment rates (47.4%-66.7%) are significant and highlight a real-world challenge for RAG deployment, particularly in sensitive applications.

## Training (2 new papers)
- **Learn-to-Distance: Distance Learning for Detecting LLM-Generated Text** (Score: 92.0)
  - The paper addresses a highly relevant and urgent problem – detecting LLM-generated text. The geometric approach to understanding rewrite-based detection and the introduction of an adaptively learned distance function suggest a solid methodological foundation. The extensive experimental setup (over 100 settings) indicates rigor, and the claim of superior performance is promising, though details are limited by the abstract alone. The topic is very 'hot' right now, suggesting a positive reception.
- **SONIC: Segmented Optimized Nexus for Information Compression in Key-Value Caching** (Score: 90.0)
  - This paper addresses a critical bottleneck in deploying large language models – the KV cache size. The proposed SONIC framework, with its 'Nexus' tokens and dynamic budget training, appears to be a novel and effective approach to compression, as evidenced by the substantial performance improvements on MTBench101. The clear focus on multi-turn dialogue context and the ability to adapt to varying memory constraints are particularly strong points, suggesting a high likelihood of positive reception within the LLM community.

## Categories
**Reasoning** (1), **Alignment** (1), **Evaluation** (2), **Theoretical** (1), **Training** (2)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
