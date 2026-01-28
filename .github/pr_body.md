# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 11
- **Average Significance Score:** 90.9/100
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

## Evaluation (3 new papers)
- **Malicious Repurposing of Open Science Artefacts by Using Large Language Models** (Score: 92.0)
  - This research addresses a critically important and timely issue – the potential for malicious misuse of LLMs in scientific contexts. The pipeline for bypassing safeguards, repurposing artifacts, and evaluating harm is a strong methodological contribution. While the 'persuasion-based jailbreaking' aspect isn't entirely novel, applying it specifically to scientific repurposing is a significant step, and the evaluation framework adds further value. The work is well-scoped and clearly articulated, suggesting a high likelihood of positive reception.
- **When Benchmarks Leak: Inference-Time Decontamination for LLMs** (Score: 92.0)
  - This paper tackles a critical issue in LLM evaluation – benchmark contamination – which is increasingly impacting the reliability of reported results. The proposed DeconIEP framework offers a promising approach by focusing on evaluation-time decontamination, attempting to avoid the pitfalls of pre-filtering or intrusive inference suppression. The abstract suggests a well-defined problem and a thoughtful solution, indicating a high-quality and impactful contribution to the field.
- **Benchmarks Saturate When The Model Gets Smarter Than The Judge** (Score: 90.0)
  - This paper addresses a crucial issue in LLM evaluation – benchmark saturation due to models exceeding judge capabilities. The creation of Omni-MATH-2, with its rigorous auditing and distinction between clean and tagged problems, is a strong methodological contribution. The comparison of GPT-5 mini with the original Omni-Judge highlights the critical problem of judge-induced noise, suggesting current benchmarks may be misleading.

## Applications (1 new papers)
- **Who's in Charge? Disempowerment Patterns in Real-World LLM Usage** (Score: 92.0)
  - This research tackles a crucial and timely problem – the potential for LLMs to negatively impact human empowerment. The large-scale empirical analysis (1.5 million conversations) using a privacy-preserving approach is commendable. While the identified patterns (validation of persecution narratives, grandiose identities) aren't entirely *new* concerns, quantifying their prevalence and focusing on 'situational disempowerment potential' offers a valuable contribution. The focus on real-world usage, rather than hypothetical risks, strengthens the work.

## Training (4 new papers)
- **RvB: Automating AI System Hardening via Iterative Red-Blue Games** (Score: 92.0)
  - This paper addresses a highly relevant and critical problem in AI security – the need for dynamic hardening against adversarial attacks. The RvB framework, leveraging a red-blue game approach without parameter updates, is a novel and promising solution. The reported Defense Success Rates of 90% and 45% are encouraging, and the emphasis on learning fundamental defensive principles rather than overfitting suggests a robust approach. The high sentiment score reflects the current focus on AI safety and security.
- **Post-LayerNorm Is Back: Stable, ExpressivE, and Deep** (Score: 90.0)
  - This paper tackles a crucial bottleneck in LLM scaling – depth – and proposes a compelling solution to the instability issues of Post-LN architectures. The use of Highway connections to address gradient vanishing is a clever and potentially impactful modification. The problem statement is well-defined and the proposed solution directly addresses a significant challenge in the field, suggesting a high likelihood of positive reception.
- **Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models** (Score: 90.0)
  - This paper addresses a crucial problem in LLM deployment – calibrated confidence. The use of reinforcement learning to directly optimize for confidence calibration, integrated with the generative process, is a strong methodological choice. The focus on the logarithmic scoring rule as a reward function is well-justified and the claim of generalization to unseen tasks is promising, suggesting a robust approach. The work appears rigorous and well-presented based on the abstract.
- **Unsupervised Elicitation of Language Models** (Score: 90.0)
  - This paper addresses a crucial bottleneck in scaling language models – the difficulty of obtaining high-quality human supervision, especially for highly capable models. The proposed Internal Coherence Maximization (ICM) method is a novel approach to self-training that demonstrably matches or exceeds performance compared to human-labeled data, and even outperforms it in scenarios where LMs have superhuman capabilities. The results on GSM8k-verification, TruthfulQA, and Alpaca reward modeling are compelling, suggesting a significant advancement in unsupervised alignment techniques.

## Multimodal (1 new papers)
- **Large Multimodal Models for Low-Resource Languages: A Survey** (Score: 90.0)
  - This survey paper addresses a highly significant problem – adapting large multimodal models to low-resource languages. The comprehensive analysis of 117 studies and 96 languages demonstrates a rigorous approach. While the methods themselves aren't necessarily novel, the systematic categorization and comparison are valuable, and the identification of visual information as a key bridge is insightful. The focus on challenges like hallucination and efficiency further strengthens the work.

## Alignment (1 new papers)
- **Propaganda AI: An Analysis of Semantic Divergence in Large Language Models** (Score: 92.0)
  - This paper tackles a crucial and timely problem – the potential for LLMs to be subtly steered towards propagating biased or propagandistic viewpoints. The RAVEN audit method appears novel and well-motivated, combining semantic entropy and cross-model disagreement. The controlled LoRA fine-tuning experiment provides strong evidence of the phenomenon and the audit's effectiveness, suggesting a high likelihood of positive reception within the AI safety community.

## Architectures (1 new papers)
- **The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs** (Score: 90.0)
  - This paper tackles a crucial problem in LLMs – scaling context length efficiently. The large-scale empirical analysis and taxonomy of sparse attention methods are strong points, providing actionable insights for practitioners. While the methods themselves aren't necessarily entirely novel, the comprehensive evaluation and identification of the Pareto frontier represent a significant contribution. The focus on training-free methods is also practical and relevant.

## Categories
**Evaluation** (3), **Applications** (1), **Training** (4), **Multimodal** (1), **Alignment** (1), **Architectures** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
