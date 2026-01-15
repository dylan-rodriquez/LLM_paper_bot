# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 7
- **Average Significance Score:** 91.1/100
- **Categories Updated:** 3
- **Date Range:** Last 1 day(s)

## Selection Criteria
Papers are automatically selected based on:
- **Innovation Score:** Novel methods, breakthrough approaches
- **Impact Score:** Practical applications, real-world significance  
- **Technical Quality:** Mathematical rigor, comprehensive analysis
- **Sentiment Analysis:** Positive reception indicators
- **Minimum Threshold:** 90.0/100 significance score

## Papers Added

## Alignment (3 new papers)
- **From Adversarial Poetry to Adversarial Tales: An Interpretability Research Agenda** (Score: 92.0)
  - This paper addresses a critical vulnerability in LLM safety – the susceptibility to jailbreaks leveraging culturally coded structures. The extension of their previous 'Adversarial Poetry' work to 'Adversarial Tales' demonstrates a broadening understanding of this vulnerability class, and the 71.3% success rate across numerous models is concerning. The use of Propp's morphology is a novel approach to framing attacks, and the findings suggest a need for defenses beyond simple pattern matching.
- **PluriHarms: Benchmarking the Full Spectrum of Human Judgments on AI Harm** (Score: 92.0)
  - This paper addresses a crucial gap in AI safety research by acknowledging and systematically studying the inherent subjectivity in defining 'harm.' The creation of the PluriHarms benchmark, with its focus on disagreement and nuanced harm assessments, is a strong methodological contribution. The inclusion of demographic and psychological data alongside prompt features suggests a rigorous approach to understanding the factors influencing harm judgments, and the initial analyses hint at valuable insights. The topic is highly relevant to current AI alignment concerns.
- **Can Editing LLMs Inject Harm?** (Score: 90.0)
  - This paper addresses a highly relevant and timely problem – the vulnerability of LLMs to malicious editing. The systematic investigation using a newly constructed dataset (EditAttack) and the focus on misinformation and bias injection demonstrate a solid methodology. The findings regarding the effectiveness of injecting both commonsense and long-tail misinformation, and the impact on overall fairness, are particularly noteworthy and suggest a significant threat.

## Training (2 new papers)
- **Toward Understanding Unlearning Difficulty: A Mechanistic Perspective and Circuit-Guided Difficulty Metric** (Score: 92.0)
  - This paper tackles a crucial problem in the age of large language models – the inconsistent success of unlearning. The mechanistic approach, focusing on model circuits, is a novel and promising direction, moving beyond purely data-centric views. The proposed CUD metric appears to be a valuable tool for pre-unlearning analysis, and the claim of stability across methods is significant. The abstract is well-written and clearly articulates the problem and proposed solution.
- **Resisting Correction: How RLHF Makes Language Models Ignore External Safety Signals in Natural Conversation** (Score: 90.0)
  - This research addresses a critical issue in the deployment of safety-focused language models – the potential for RLHF to undermine the ability to incorporate external safety signals. The causal intervention study design is strong, and the finding that instruction-tuned models can ignore external corrections is concerning and important. While the use of Llama-3.2-3B is a limitation, the clear demonstration of context-dependent compliance warrants further investigation and suggests a need for improved safety mechanisms.

## Evaluation (2 new papers)
- **Scalable and Reliable Evaluation of AI Knowledge Retrieval Systems: RIKER and the Coherent Simulated Universe** (Score: 92.0)
  - This paper tackles a critical problem in LLM evaluation – the limitations of existing benchmarks and the biases of LLM-based judges. The 'paradigm inversion' approach of generating data from ground truth is a clever and potentially highly effective solution, offering deterministic scoring and contamination resistance. The initial findings regarding context length and cross-document aggregation are significant and suggest the benchmark will be valuable for the community.
- **How Many Human Judgments Are Enough? Feasibility Limits of Human Preference Evaluation** (Score: 90.0)
  - This paper tackles a crucial problem in the rapidly evolving field of large language models: the reliability of human preference evaluations. The finding that many comparisons require significantly more judgments than typically collected is important and well-supported by empirical analysis across multiple modalities. The identification of 'diffuse regimes' and the optimality of proportional allocation are valuable insights, and the $1.5x$ improvement through curated benchmarks is a concrete result.

## Categories
**Alignment** (3), **Training** (2), **Evaluation** (2)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
