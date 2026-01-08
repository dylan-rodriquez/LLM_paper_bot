# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 14
- **Average Significance Score:** 91.7/100
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

## Reasoning (3 new papers)
- **Internal Reasoning vs. External Control: A Thermodynamic Analysis of Sycophancy in Large Language Models** (Score: 92.0)
  - This paper tackles a crucial problem in LLMs – sycophancy – with a novel thermodynamic framing. The comparison of internal (CoT) and external (RCA) mechanisms across multiple model tiers is rigorous, and the 'Prioritization Paradox' finding is particularly insightful. The thermodynamic analogy, while potentially complex, offers a fresh perspective on LLM behavior and safety, and the clear demonstration of RCA's effectiveness is compelling.
- **OpenAI GPT-5 System Card** (Score: 92.0)
  - This system card describes a significant advancement in LLMs, moving beyond a single model to a routed system that dynamically selects the best model for the task. The continuous training of the router based on real user signals is a particularly strong point. While the abstract is brief, the described architecture suggests a substantial improvement in both performance and usability, making it highly impactful. The focus on 'thinking' and 'main' models suggests a deliberate effort towards more robust reasoning capabilities.
- **HearSay Benchmark: Do Audio LLMs Leak What They Hear?** (Score: 92.0)
  - This paper addresses a critical and timely privacy concern with the rise of Audio LLMs. The creation of the HearSay benchmark, with its rigorous curation process, is a strong methodological contribution. The reported leakage rates (92.89% gender accuracy) are alarming and suggest a significant vulnerability that needs addressing, indicating high potential impact and positive community reception.

## Training (4 new papers)
- **Jailbreak-Zero: A Path to Pareto Optimal Red Teaming for Large Language Models** (Score: 92.0)
  - This paper addresses a critical issue in LLM safety – robust red teaming – and proposes a novel approach that moves beyond simple example-based attacks. The use of an attack LLM fine-tuned with a preference dataset to achieve Pareto optimality is a strong methodological contribution. The reported success against state-of-the-art models like GPT-40 and Claude 3.5 suggests a significant improvement over existing techniques, and the emphasis on human-readable prompts is a practical benefit.
- **Rendering Data Unlearnable by Exploiting LLM Alignment Mechanisms** (Score: 92.0)
  - This paper tackles a very important and timely problem – data privacy in the age of LLMs. The 'Disclaimer Injection' approach is clever, exploiting alignment mechanisms rather than relying on traditional data removal or model-side defenses. The layer-wise analysis suggests a rigorous methodology, and the potential for systematic performance degradation on protected data is a strong result. The abstract indicates a well-defined approach and clear findings.
- **What Matters For Safety Alignment?** (Score: 92.0)
  - This paper tackles a crucial problem in AI safety – aligning LLMs and LRMs – with a rigorous, large-scale empirical approach. The sheer scale of the evaluation (32 models, 13 families, 4.6M API calls) lends significant credibility to the findings. While the methodology appears sound, the novelty lies more in the breadth of the study than a fundamentally new technique, but the identification of safer models is highly valuable. The strong focus on practical attack vectors and reasoning capabilities suggests a high likelihood of positive reception within the AI safety community.
- **O-Researcher: An Open Ended Deep Research Model via Multi-Agent Distillation and Agentic RL** (Score: 90.0)
  - This paper addresses a crucial problem in the LLM space – the performance gap between open and closed-source models due to data access. The multi-agent distillation and agentic RL approach appears novel and well-motivated, aiming to create high-quality training data automatically. The claim of achieving state-of-the-art performance on deep research benchmarks suggests a strong contribution, and the focus on scalability is important for wider adoption.

## Alignment (2 new papers)
- **GuardEval: A Multi-Perspective Benchmark for Evaluating Safety, Fairness, and Robustness in LLM Moderators** (Score: 92.0)
  - This paper addresses a crucial and timely problem in LLM deployment – ensuring safety, fairness, and robustness of moderation systems. The creation of a multi-perspective benchmark (GuardEval) with 106 fine-grained categories is a significant contribution, offering a more nuanced evaluation than existing methods. While the core idea of a benchmark isn't entirely novel, the scope and granularity of GuardEval appear substantial, suggesting a high potential for adoption and impact.
- **PsychEthicsBench: Evaluating Large Language Models Against Australian Mental Health Ethics** (Score: 92.0)
  - This paper addresses a crucial and timely problem – the ethical evaluation of LLMs in a sensitive domain like mental health. The move beyond simple refusal-based metrics and the grounding in Australian psychological guidelines represent a significant step forward. The creation of PsychEthicsBench is a valuable contribution, and the initial findings suggesting refusal rates are poor proxies for ethical behavior are compelling. The work is well-motivated and clearly presented, suggesting a high likelihood of positive reception.

## Evaluation (3 new papers)
- **DisastQA: A Comprehensive Benchmark for Evaluating Question Answering in Disaster Management** (Score: 92.0)
  - This paper addresses a highly significant problem – QA in disaster management – which is often overlooked in standard NLP benchmarks. The creation of a large-scale, rigorously verified benchmark (DisastQA) with varying evidence conditions is a strong methodological contribution. The human-LLM collaboration and keypoint-based evaluation for open-ended QA are also noteworthy, suggesting a careful and thoughtful approach to evaluation.
- **RedBench: A Universal Dataset for Comprehensive Red Teaming of Large Language Models** (Score: 92.0)
  - This paper addresses a crucial and timely problem in LLM safety – the lack of standardized and comprehensive red teaming datasets. Aggregating existing datasets and providing a standardized taxonomy is a significant undertaking and will greatly benefit the research community. While the core idea of dataset aggregation isn't entirely novel, the scale and standardization efforts demonstrate strong methodological rigor and potential for broad impact.
- **Benchmark^2: Systematic Evaluation of LLM Benchmarks** (Score: 92.0)
  - This paper addresses a crucial and rapidly growing problem in the LLM space – the reliability and comparability of benchmarks. The proposed Benchmark^2 framework, with its three metrics, offers a systematic and well-defined approach to evaluating benchmark quality. The extensive experiments across multiple benchmarks and models demonstrate the practical utility of the framework and suggest it could significantly improve the field's understanding of LLM capabilities.

## Multimodal (2 new papers)
- **When Helpers Become Hazards: A Benchmark for Analyzing Multimodal LLM-Powered Safety in Daily Life** (Score: 92.0)
  - This paper addresses a crucial and timely problem – the safety of MLLMs in real-world scenarios. The introduction of the SaLAD benchmark and the safety-warning-based evaluation framework are strong contributions, demonstrating a focus on practical safety concerns beyond simple refusal rates. The emphasis on cross-modal reasoning and realistic risk exposure elevates the work above many existing safety evaluations, suggesting a high likelihood of positive reception within the community.
- **Do LLMs Really Memorize Personally Identifiable Information? Revisiting PII Leakage with a Cue-Controlled Memorization Framework** (Score: 90.0)
  - This paper tackles a crucial and timely problem in LLM safety – PII leakage. The introduction of the Cue-Resistant Memorization (CRM) framework is a strong methodological contribution, offering a more rigorous way to evaluate memorization beyond simple reconstruction. The large-scale multilingual evaluation further strengthens the work, and the initial finding that existing methods are driven by cues rather than true memorization is significant.

## Categories
**Reasoning** (3), **Training** (4), **Alignment** (2), **Evaluation** (3), **Multimodal** (2)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
