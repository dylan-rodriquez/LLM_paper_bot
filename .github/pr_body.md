# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 8
- **Average Significance Score:** 91.2/100
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

## Architectures (1 new papers)
- **PADBen: A Comprehensive Benchmark for Evaluating AI Text Detectors Against Paraphrase Attacks** (Score: 92.0)
  - This paper addresses a highly relevant and timely problem – the vulnerability of AI text detectors to paraphrasing attacks. The introduction of PADBen, a benchmark specifically designed to evaluate robustness against these attacks, is a significant contribution. The analysis of 'laundering regions' and categorization of attack types demonstrates a strong methodological approach and clear presentation, suggesting high potential for positive reception within the community.

## Training (1 new papers)
- **Friend or Foe: How LLMs' Safety Mind Gets Fooled by Intent Shift Attack** (Score: 90.0)
  - This paper addresses a critical vulnerability in LLMs – their susceptibility to jailbreaking – and proposes a novel attack vector (Intent Shift Attack) that is more subtle and effective than existing methods. The reported 70% improvement in attack success rate is significant, and the focus on minimal edits leading to human-readable prompts is a strong point. The research appears rigorous, and the problem is highly relevant to the ongoing efforts to build safe and reliable LLMs.

## Evaluation (2 new papers)
- **HPLT~3.0: Very Large-Scale Multilingual Resources for LLM and MT. Mono- and Bi-lingual Data, Multilingual Evaluation, and Pre-Trained Models** (Score: 92.0)
  - This paper addresses a crucial need in the LLM community: large-scale, high-quality multilingual data. The scale (30 trillion tokens) is impressive, and the inclusion of a complete pipeline for data processing – from web crawling to filtering – demonstrates a strong methodological approach. While the core idea of creating a large multilingual dataset isn't entirely novel, the size, quality control measures, and open-source nature of the pipeline are significant advancements. The paper's focus on data quality probes and multilingual evaluation further strengthens its credibility.
- **Towards Robust Mathematical Reasoning** (Score: 92.0)
  - This paper addresses a critical bottleneck in evaluating mathematical reasoning in large language models – the lack of challenging benchmarks. The creation of IMO-Bench, vetted by experts and targeting the IMO level, is a significant step forward. The reported 'historic achievement' with Gemini Deep Think further strengthens the paper's impact and suggests a robust evaluation framework.

## Alignment (1 new papers)
- **Surfacing Subtle Stereotypes: A Multilingual, Debate-Oriented Evaluation of Modern LLMs** (Score: 92.0)
  - This paper addresses a crucial and timely problem – the persistence of biases in LLMs, particularly in multilingual contexts. The use of a debate-oriented benchmark is a clever approach to surface subtle stereotypes that classification tasks might miss. The scale of the dataset (8,400 prompts, 100,000+ responses) and inclusion of diverse languages strengthens the findings, suggesting a robust evaluation.

## Applications (2 new papers)
- **"Give a Positive Review Only": An Early Investigation Into In-Paper Prompt Injection Attacks and Defenses for AI Reviewers** (Score: 92.0)
  - This paper addresses a highly relevant and timely problem – the vulnerability of AI-assisted peer review to prompt injection attacks. The systematic investigation of both static and iterative attacks, and the demonstration of their effectiveness against frontier models, is strong. While the described defense is only mentioned as 'simple detection-based', the identification of the attack vectors themselves is a significant contribution, and the high scores achieved suggest a real-world threat.
- **Can SAEs reveal and mitigate racial biases of LLMs in healthcare?** (Score: 90.0)
  - This research tackles a crucial problem – racial bias in healthcare LLMs – with a novel approach using Sparse Autoencoders. The finding that SAE latents correlate with both race and stigmatizing concepts is concerning and highlights a real risk. The ability to steer model outputs based on these latents, and the demonstration of induced problematic associations, strengthens the argument for proactive bias mitigation. The work is well-motivated and the initial results are compelling.

## Reasoning (1 new papers)
- **KV Cache Transform Coding for Compact Storage in LLM Inference** (Score: 90.0)
  - This paper addresses a crucial bottleneck in LLM deployment – KV cache size. The application of classical media compression techniques (PCA, quantization, entropy coding) to this problem is a clever and practical approach. The reported compression ratios (up to 20x, and higher in specific cases) with maintained accuracy suggest a significant advancement, and testing across multiple models strengthens the findings. The positive sentiment is driven by the relevance to current LLM scaling challenges.

## Categories
**Architectures** (1), **Training** (1), **Evaluation** (2), **Alignment** (1), **Applications** (2), **Reasoning** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
