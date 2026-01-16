# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 10
- **Average Significance Score:** 91.8/100
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

## Reasoning (2 new papers)
- **ReasAlign: Reasoning Enhanced Safety Alignment against Prompt Injection Attack** (Score: 92.0)
  - This paper addresses a highly relevant and critical problem – the vulnerability of LLM-based agents to prompt injection attacks. The proposed ReasAlign approach, leveraging structured reasoning and a preference-optimized judge model, appears well-reasoned and potentially effective. The mention of comprehensive evaluations suggests a rigorous methodology, and the focus on safety alignment aligns with current research trends. While the core idea of reasoning isn't entirely novel, the specific implementation and test-time scaling mechanism seem promising.
- **Syntactic Framing Fragility: An Audit of Robustness in LLM Ethical Decisions** (Score: 90.0)
  - This research addresses a critical vulnerability in LLMs – their sensitivity to syntactic framing – which is crucial as these models are deployed in high-stakes scenarios. The introduction of 'Syntactic Framing Fragility' (SFF) and 'Logical Polarity Normalization' (LPN) provides a novel and rigorous framework for evaluating this robustness. The large-scale audit across diverse models and scenarios strengthens the findings and suggests a significant problem requiring attention. The high sentiment score reflects the current focus on LLM safety and alignment.

## Generation (1 new papers)
- **From Detection to Diagnosis: Advancing Hallucination Analysis with Automated Data Synthesis** (Score: 92.0)
  - This paper addresses a crucial problem in LLM deployment – hallucinations – and proposes a shift from simple detection to a more useful diagnostic approach. The introduction of the 'Hallucination Diagnosis Task' and the HDG pipeline demonstrate a clear methodology for generating training data to improve model understanding and correction capabilities. While the abstract doesn't detail the specifics of the augmentation techniques, the overall framing and proposed task are well-defined and likely to resonate with the research community.

## Training (2 new papers)
- **Alignment Pretraining: AI Discourse Causes Self-Fulfilling (Mis)alignment** (Score: 92.0)
  - This paper tackles a crucial and timely problem in AI alignment – the influence of pretraining data on model behavior. The controlled study design, upsampling alignment/misalignment discourse, and observed effects are strong evidence supporting the self-fulfilling alignment hypothesis. While the 6.9B parameter size isn't state-of-the-art, the clear results and implications for data curation are highly valuable.
- **Representation-Aware Unlearning via Activation Signatures: From Suppression to Knowledge-Signature Erasure** (Score: 92.0)
  - This paper tackles a crucial problem in LLMs – genuine unlearning versus superficial suppression – with a novel approach focusing on activation signatures. The reported results (FQ approx 0.99, MU = 0.62) are impressive, suggesting a significant improvement over existing methods and breaking the stability-erasure tradeoff. The combination of representation-aware architecture and parameter-efficient adaptation is a strong methodological contribution, and the focus on GDPR compliance and model safety adds to its relevance.

## Evaluation (3 new papers)
- **coTherapist: A Behavior-Aligned Small Language Model to Support Mental Healthcare Experts** (Score: 92.0)
  - This paper addresses a highly significant problem – the strain on mental healthcare resources – with a promising solution leveraging small language models. The use of domain-specific fine-tuning, retrieval augmentation, and agentic reasoning, coupled with a novel evaluation rubric (T-BARS) and expert validation, suggests a rigorous and well-executed study. The focus on safety, trustworthiness, and empathy is particularly commendable, and the deployment with clinical experts adds substantial weight to the findings.
- **Contextual StereoSet: Stress-Testing Bias Alignment Robustness in Large Language Models** (Score: 92.0)
  - This paper addresses a crucial issue in LLM deployment – the context-dependent nature of bias. The introduction of Contextual StereoSet and CSF provides a robust methodology for evaluating bias alignment beyond controlled lab settings. The statistically significant findings and replication across different vignettes suggest a strong and impactful contribution to the field, and the focus on practical evaluation tracks is commendable.
- **DR-Arena: an Automated Evaluation Framework for Deep Research Agents** (Score: 92.0)
  - This paper addresses a crucial bottleneck in the rapidly evolving field of LLM-powered agents – reliable and dynamic evaluation. The DR-Arena framework, with its focus on real-time information trees and adaptive task complexity, represents a significant step beyond static benchmarks. The orthogonal capabilities testing (deep reasoning and wide coverage) is a thoughtful design choice, and the automated Examiner is a key component for scalability. The approach is well-motivated and appears rigorous, though full evaluation requires seeing the implementation details and experimental results.

## Architectures (1 new papers)
- **Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale** (Score: 92.0)
  - This research addresses a highly relevant and timely problem – the security of AI agent skills. The large-scale empirical analysis and development of SkillScan demonstrate a solid methodology. The findings of pervasive vulnerabilities are concerning and highlight a critical gap in the current agent ecosystem, suggesting strong potential for positive reception within the AI security community.

## Multimodal (1 new papers)
- **A Safety Report on GPT-5.2, Gemini 3 Pro, Qwen3-VL, Doubao 1.8, Grok 4.1 Fast, Nano Banana Pro, and Seedream 4.5** (Score: 92.0)
  - This research addresses a critically important and timely problem – the safety of increasingly powerful LLMs and MLLMs. The integrated evaluation protocol across multiple modalities and threat models is a strong methodological point. While the abstract doesn't detail *how* novel the evaluation methods are, the scope of models tested and the unified approach suggest a valuable contribution to the field. The heterogeneous safety landscape hinted at in the abstract suggests potentially impactful findings.

## Categories
**Reasoning** (2), **Generation** (1), **Training** (2), **Evaluation** (3), **Architectures** (1), **Multimodal** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
