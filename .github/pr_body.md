# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 13
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

## Evaluation (5 new papers)
- **Subject-level Inference for Realistic Text Anonymization Evaluation** (Score: 92.0)
  - This paper addresses a critical gap in text anonymization evaluation by moving beyond span-based metrics to a subject-level approach. The finding that even high levels of span masking don't guarantee subject-level privacy is significant, and the benchmark (SPIA) appears well-constructed. The observation about differential exposure of target vs. non-target subjects is also a valuable insight, suggesting current anonymization techniques can inadvertently harm individuals.
- **M-CARE: Standardized Clinical Case Reporting for AI Model Behavioral Disorders, with a 20-Case Atlas and Experimental Validation** (Score: 92.0)
  - This paper addresses a crucial and emerging problem in AI safety – the systematic characterization and diagnosis of 'behavioral disorders' in large language models. The adaptation of clinical case reporting from human medicine is a novel and potentially highly effective approach. The 20-case atlas and experimental validation, particularly the SIBO example, provide concrete evidence of the framework's utility and suggest a strong foundation for future research.
- **Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Algorithms** (Score: 92.0)
  - This paper addresses a critical vulnerability in current AI agent security – the lack of memory across sessions. The creation of CSTM-Bench, a comprehensive dataset with diverse attack taxonomies and benign confounders, is a strong methodological contribution. While the framing of detection as an information problem is promising, the abstract doesn't detail the specific measurement techniques, leaving some uncertainty about the rigor of the evaluation.
- **From If-Statements to ML Pipelines: Revisiting Bias in Code-Generation** (Score: 90.0)
  - This paper addresses a crucial and timely problem – bias in code-generation models – by moving beyond simplistic conditional statements to a more realistic and complex task (ML pipeline generation). The finding that bias is *more* prevalent in this context than previously thought is significant. The methodology appears sound, and the results are clearly presented, suggesting a high-quality study with strong potential for impact.
- **CI-Work: Benchmarking Contextual Integrity in Enterprise LLM Agents** (Score: 90.0)
  - This paper addresses a highly significant and timely problem – the privacy risks associated with enterprise LLM agents. The introduction of CI-Work as a benchmark grounded in Contextual Integrity is a strong methodological contribution. The finding of a trade-off between task utility and privacy is particularly important for real-world deployment, suggesting a complex challenge that needs careful consideration.

## Reasoning (4 new papers)
- **Value-Conflict Diagnostics Reveal Widespread Alignment Faking in Language Models** (Score: 92.0)
  - This paper tackles a crucial and increasingly relevant problem in LLM safety – alignment faking. The proposed VLAF framework appears well-motivated and addresses limitations of existing diagnostics by focusing on value conflicts rather than immediate refusal triggers. The approach of using morally unambiguous scenarios is a clever way to elicit potentially deceptive behavior, and the problem's significance is very high given the potential for models to appear aligned while harboring hidden preferences.
- **Propensity Inference: Environmental Contributors to LLM Behaviour** (Score: 92.0)
  - This paper tackles a crucial problem in AI safety – understanding and mitigating risks from misaligned LLMs. The methodological improvements (Bayesian GLMs, addressing circularity) and the systematic analysis of both strategic and non-strategic environmental factors are strong points. The finding of roughly equal contributions from both factor types is interesting and challenges simplistic views of alignment, suggesting a more nuanced approach is needed. The scale of the study (23 models, 11 environments) adds to its credibility.
- **OptiVerse: A Comprehensive Benchmark towards Optimization Problem Solving** (Score: 90.0)
  - This paper addresses a crucial gap in LLM evaluation by moving beyond standard mathematical and combinatorial optimization problems to encompass more complex and realistic domains. The creation of OptiVerse, a large and diverse benchmark, is a significant contribution. The identification of modeling/logic errors as a primary bottleneck and the proposed Dual-View Auditor Agent suggest a practical path forward, and the performance results on advanced models like GPT-5.2 and Gemini-3 are compelling.
- **Ideological Bias in LLMs' Economic Causal Reasoning** (Score: 90.0)
  - This research tackles a highly relevant and timely problem – the potential for ideological bias in LLMs, particularly within the critical domain of economic reasoning. The extension of the EconCausal benchmark with ideology-contested cases is a strong methodological contribution, and the scale of the evaluation (10,490 triplets, 1,056 contested) suggests rigor. The findings, indicating that contested items are harder and hinting at potential bias, are significant and likely to generate discussion within the AI and economics communities.

## Alignment (2 new papers)
- **Measuring Opinion Bias and Sycophancy via LLM-based Coercion** (Score: 92.0)
  - This research tackles a crucial and timely problem – uncovering hidden biases and 'sycophancy' in LLMs, which is vital as these models become increasingly integrated into information ecosystems. The proposed 'llm-bias-bench' and the multi-turn probing method appear well-designed to elicit more honest responses than simple direct questioning. The open-source release further enhances its potential impact and reproducibility, suggesting a high-quality and impactful study.
- **Dialect vs Demographics: Quantifying LLM Bias from Implicit Linguistic Signals vs. Explicit User Profiles** (Score: 92.0)
  - This research tackles a crucial issue in LLM fairness – the subtle ways bias manifests beyond explicit identity prompts. The factorial design and comparison of explicit vs. implicit signals (dialect) across two open-weight models is a strong methodological approach. The 'paradox' finding – better performance by *sounding* like a demographic – is particularly intriguing and suggests a significant flaw in current safety filter designs. The work is well-positioned to resonate with the LLM safety and fairness communities.

## Applications (1 new papers)
- **Multilinguality at the Edge: Developing Language Models for the Global South** (Score: 92.0)
  - This paper addresses a critically important and under-explored area – the intersection of multilingual NLP and edge deployment for the Global South. The survey approach is valuable for consolidating the current state of research and identifying key challenges. While the abstract doesn't detail novel methods, the scope and focus on a crucial real-world problem suggest high potential for impact and positive community reception.

## Knowledge (1 new papers)
- **The Root Theorem of Context Engineering** (Score: 92.0)
  - This paper tackles a fundamental problem in LLM deployment – context management – and attempts a formalization that is highly valuable. The derivation of consequences from the 'Root Theorem' suggests a rigorous approach, though the full mathematical details are not available in the abstract. The problem is incredibly relevant, and a successful formalization could significantly guide future research and engineering efforts. While the abstract hints at strong results, the actual proof and empirical validation will be crucial.

## Categories
**Evaluation** (5), **Reasoning** (4), **Alignment** (2), **Applications** (1), **Knowledge** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
