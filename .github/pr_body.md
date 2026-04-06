# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 13
- **Average Significance Score:** 91.7/100
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
- **Using LLM-as-a-Judge/Jury to Advance Scalable, Clinically-Validated Safety Evaluations of Model Responses to Users Demonstrating Psychosis** (Score: 92.0)
  - This research tackles a crucial and timely problem – the safety of LLMs for vulnerable populations, specifically those experiencing psychosis. The combination of clinician-informed criteria, human consensus dataset creation, and LLM-as-a-Judge/Jury methodology demonstrates a rigorous approach. While using LLMs for evaluation isn't entirely novel, applying it to this specific, high-stakes clinical context and validating against human experts is a strong contribution. The reported Cohen's Kappa suggests promising alignment.
- **Xpertbench: Expert Level Tasks with Rubrics-Based Evaluation** (Score: 92.0)
  - This paper addresses a critical bottleneck in LLM research – robust evaluation of complex, expert-level tasks. The use of tasks curated by domain experts and detailed rubrics significantly improves upon existing benchmarks prone to bias and limited scope. The scale of the benchmark (1,346 tasks, 80 categories) is impressive and suggests a substantial contribution to the field. The focus on ecological validity is particularly strong.
- **StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs** (Score: 90.0)
  - This paper addresses a crucial and timely problem in the LLM space – the reliable generation of structured data. The introduction of StructEval, with its dual paradigm (generation and conversion) and comprehensive format coverage, represents a significant step forward in benchmarking. While the core idea of benchmarking isn't novel, the systematic approach and focus on structural fidelity are strong points, suggesting a positive reception within the community.

## Alignment (3 new papers)
- **SocioEval: A Template-Based Framework for Evaluating Socioeconomic Status Bias in Foundation Models** (Score: 92.0)
  - This paper addresses a crucial and currently under-explored area of LLM bias – socioeconomic status. The systematic framework (SocioEval) with its hierarchical themes and prompt generation is well-defined and the rigorous three-stage annotation protocol strengthens the validity of the findings. The reported variation in bias rates across models is significant and highlights the need for further investigation and mitigation strategies. While template-based evaluation isn't entirely novel, its application to socioeconomic bias is a valuable contribution.
- **Redirected, Not Removed: Task-Dependent Stereotyping Reveals the Limits of LLM Alignments** (Score: 92.0)
  - This paper addresses a crucial and timely problem in LLM research – the nuanced nature of bias and the limitations of current alignment techniques. The introduction of a hierarchical taxonomy of bias types and the demonstration of task-dependent stereotyping are strong methodological contributions. The findings, showing a divergence between explicit and implicit bias responses, are significant and suggest current safety alignments are incomplete, warranting further investigation.
- **An Independent Safety Evaluation of Kimi K2.5** (Score: 92.0)
  - This paper addresses a crucial gap in the release of Kimi K2.5 – a lack of safety evaluation for a powerful, open-weight LLM. The focus on dual-use risks (CBRNE, cybersecurity) and the finding of fewer refusals on dangerous requests are particularly concerning and valuable. While the methodology appears sound for a preliminary assessment, the work doesn't present novel techniques, but rather applies existing safety evaluation frameworks to a new model.

## Applications (2 new papers)
- **Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Research Agents** (Score: 92.0)
  - This research addresses a critical issue with LLMs and research agents – the reliability of their citations. The systematic measurement across multiple models and datasets (DRBench and ExpertQA) using the Wayback Machine is a strong methodological approach. The findings regarding hallucination rates and domain-specific effects are significant and will likely resonate with the NLP community, particularly those working on information retrieval and trustworthy AI.
- **IndustryCode: A Benchmark for Industry Code Generation** (Score: 92.0)
  - This paper addresses a crucial gap in LLM evaluation – the lack of benchmarks tailored to complex, multi-domain industrial code generation. The creation of IndustryCode, with its 579 sub-problems and focus on real-world challenges, is a significant contribution. While the core idea of a benchmark isn't novel, the scope and focus on industrial applications elevate its value, suggesting a positive reception within the community.

## Reasoning (2 new papers)
- **Beyond the Parameters: A Technical Survey of Contextual Enrichment in Large Language Models: From In-Context Prompting to Causal Retrieval-Augmented Generation** (Score: 92.0)
  - This survey tackles a highly relevant and rapidly evolving area in LLMs – contextual enrichment. The inclusion of a literature-screening protocol, claim-audit framework, and evidence synthesis suggests a rigorous approach, going beyond a simple conceptual overview. The focus on a deployment-oriented decision framework further enhances its practical value, indicating a strong potential for positive reception within the NLP community.
- **Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems** (Score: 92.0)
  - This research addresses a critical and emerging security vulnerability in LLM-based coding agents – supply chain attacks via skill marketplaces. The 'Document-Driven Implicit Payload Execution' (DDIPE) attack vector is novel and concerning, given the privileged access these skills often have. The scale of the experimentation (1,070 adversarial skills) and coverage across frameworks/models suggests a rigorous approach, making this work highly relevant and likely to be well-received by the community.

## Training (2 new papers)
- **Mitigating LLM biases toward spurious social contexts using direct preference optimization** (Score: 92.0)
  - This research tackles a highly significant problem – bias in LLMs, particularly in high-stakes applications like teacher evaluation. The use of a large, real-world dataset (NCTE transcripts) is a strong point, and the finding that larger models *can* be more sensitive to spurious contexts is counterintuitive and noteworthy. While the abstract doesn't detail the mitigation strategy, the problem framing and initial findings suggest solid work, though the innovation appears to be in the application and scale of analysis rather than a fundamentally new technique.
- **Be Careful When Fine-tuning On Open-Source LLMs: Your Fine-tuning Data Could Be Secretly Stolen!** (Score: 92.0)
  - This paper addresses a critical and previously unrecognised security vulnerability in the increasingly common practice of fine-tuning open-source LLMs with private data. The experimental results demonstrating high extraction rates are concerning and well-quantified. While the detection-based defense is bypassed, the identification of the vulnerability itself is a significant contribution, and the work is clearly presented and rigorous based on the abstract.

## Agents (1 new papers)
- **APEX-EM: Non-Parametric Online Learning for Autonomous Agents via Structured Procedural-Episodic Experience Replay** (Score: 90.0)
  - This paper addresses a crucial limitation of current LLM-based agents – their inability to learn from past experiences. The proposed APEX-EM framework, with its structured experience representation and PRGII workflow, appears well-designed to tackle this problem. The combination of semantic, structural, and DAG-based retrieval is particularly promising for cross-domain transfer, suggesting a robust and adaptable system. The focus on procedural memory is highly relevant to the current trajectory of autonomous agent research.

## Categories
**Evaluation** (3), **Alignment** (3), **Applications** (2), **Reasoning** (2), **Training** (2), **Agents** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
