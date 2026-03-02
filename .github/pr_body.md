# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 11
- **Average Significance Score:** 91.3/100
- **Categories Updated:** 4
- **Date Range:** Last 1 day(s)

## Selection Criteria
Papers are automatically selected based on:
- **Innovation Score:** Novel methods, breakthrough approaches
- **Impact Score:** Practical applications, real-world significance  
- **Technical Quality:** Mathematical rigor, comprehensive analysis
- **Sentiment Analysis:** Positive reception indicators
- **Minimum Threshold:** 90.0/100 significance score

## Papers Added

## Evaluation (6 new papers)
- **CiteAudit: You Cited It, But Did You Read It? A Benchmark for Verifying Scientific References in the LLM Era** (Score: 92.0)
  - This paper addresses a highly relevant and increasingly critical problem – the hallucination of citations by LLMs. The proposed benchmark and multi-agent verification pipeline represent a significant step towards addressing this issue, offering a structured approach to detection. The work is well-motivated and the problem is timely, given the growing reliance on LLMs in research and the documented instances of fabricated references.
- **Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning** (Score: 92.0)
  - This paper addresses a crucial bottleneck in ML research – the lack of readily available code for published papers. The multi-agent LLM framework, PaperCoder, appears well-structured with distinct planning, analysis, and generation stages, suggesting a rigorous approach. The use of specialized agents for each phase is a promising design choice, and the problem's importance is high given the reproducibility crisis and the desire to accelerate research.
- **Beyond Accuracy: Risk-Sensitive Evaluation of Hallucinated Medical Advice** (Score: 92.0)
  - This paper addresses a crucial and often overlooked aspect of LLM evaluation in a high-stakes domain – medical advice. The shift from purely factual correctness to risk-sensitive evaluation is a significant improvement, and the proposed framework seems well-reasoned. The combination of risk scoring and relevance is a particularly strong point, and the application to instruction-tuned models is timely. The work is clearly presented and addresses a very important problem.
- **HLE-Verified: A Systematic Verification and Structured Revision of Humanity's Last Exam** (Score: 92.0)
  - This paper addresses a critical issue in LLM evaluation – benchmark quality. The systematic verification and revision process, coupled with a transparent protocol, significantly improves the reliability of HLE. While the core idea of benchmark verification isn't entirely novel, the scale and rigor applied to HLE, and the two-stage workflow, are commendable. The work is likely to be well-received by the LLM community, as reliable benchmarks are essential for progress.
- **Jailbreak Foundry: From Papers to Runnable Attacks for Reproducible Benchmarking** (Score: 90.0)
  - This paper addresses a critical issue in LLM security – the rapidly evolving nature of jailbreak attacks and the difficulty in maintaining comparable benchmarks. The JBF system offers a robust and reproducible framework for evaluating LLM robustness, significantly improving upon existing fragmented approaches. The reported fidelity and code reuse metrics demonstrate the system's effectiveness and practicality, suggesting a positive reception within the research community.
- **DeepQuestion: Systematic Generation of Real-World Challenges for Evaluating LLMs Performance** (Score: 90.0)
  - This paper addresses a crucial issue in LLM evaluation – the overestimation of capabilities due to simplistic benchmarks. The systematic approach of elevating cognitive complexity using Bloom's taxonomy and generating realistic, scenario-based problems is well-conceived. The reported 70% accuracy drop highlights a significant gap between benchmark performance and real-world application, suggesting a strong potential for impact and positive reception within the community.

## Knowledge (2 new papers)
- **Multi-Agent Causal Reasoning for Suicide Ideation Detection Through Online Conversations** (Score: 92.0)
  - This paper tackles a critically important problem – suicide ideation detection – with a novel approach that addresses limitations of existing methods. The use of a multi-agent system incorporating causal reasoning and bias mitigation is promising. While the abstract is concise, the proposed framework appears well-motivated and potentially rigorous, suggesting a strong contribution to the field. The focus on hidden influences like conformity and copycat behavior is particularly noteworthy.
- **Tracing and Reversing Edits in LLMs** (Score: 92.0)
  - This paper tackles a crucial and timely problem in the age of LLMs – the potential for malicious knowledge editing. The reported accuracy (99% for tracing, 94% for reversing) is impressive, suggesting a robust methodology. The ability to perform these tasks *without* access to the editing prompt is a significant advantage, making the approach more practical in real-world scenarios. The dual-use risk framing is well-articulated, and the work directly addresses a growing concern within the field.

## Training (2 new papers)
- **SWE-rebench V2: Language-Agnostic SWE Task Collection at Scale** (Score: 90.0)
  - This paper addresses a critical bottleneck in SWE agent development – the lack of large-scale, diverse, and reproducible training data. The language-agnostic approach and automated pipeline for task harvesting are strong points, and the use of LLM judges for filtering adds a layer of robustness. The scale (32,000+ tasks, 20 languages) is impressive and suggests a significant contribution to the field. The high sentiment score reflects the current trend towards SWE agents and the need for better benchmarks.
- **Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric** (Score: 90.0)
  - This paper tackles a crucial problem in LLM alignment – the brittleness and reward hacking stemming from scalar reward models. The proposed Open Rubric System (OpenRS) with Pairwise Adaptive Meta-Rubrics (PAMR) and Pointwise Verifiable Rubrics (PVRs) offers a promising alternative by focusing on explicit reasoning and inspectable principles. The approach appears well-motivated and addresses a significant limitation of current alignment techniques, suggesting strong potential for positive reception within the community.

## Reasoning (1 new papers)
- **Toward Guarantees for Clinical Reasoning in Vision Language Models via Formal Verification** (Score: 92.0)
  - This paper tackles a crucial problem in the deployment of VLMs in high-stakes clinical settings – ensuring logical consistency and reasoning. The neurosymbolic verification framework, leveraging SMT solvers and knowledge bases, is a strong methodological contribution. While the approach isn't entirely novel (neurosymbolic methods exist), applying it specifically to VLM clinical reasoning and exposing failure modes is valuable. The potential for improving the reliability of AI-assisted radiology is significant.

## Categories
**Evaluation** (6), **Knowledge** (2), **Training** (2), **Reasoning** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
