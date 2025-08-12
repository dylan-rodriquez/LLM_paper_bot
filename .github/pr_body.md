# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 13
- **Average Significance Score:** 91.5/100
- **Categories Updated:** 7
- **Date Range:** Last 1 day(s)

## Selection Criteria
Papers are automatically selected based on:
- **Innovation Score:** Novel methods, breakthrough approaches
- **Impact Score:** Practical applications, real-world significance  
- **Technical Quality:** Mathematical rigor, comprehensive analysis
- **Sentiment Analysis:** Positive reception indicators
- **Minimum Threshold:** 90.0/100 significance score

## Papers Added

## Training (4 new papers)
- **CarbonScaling: Extending Neural Scaling Laws for Carbon Footprint in Large Language Models** (Score: 92.0)
  - This paper addresses a critically important and timely issue – the carbon footprint of LLMs – by extending established scaling laws. The integration of multiple models (neural scaling, hardware evolution, parallelism, carbon estimation) demonstrates a rigorous approach. While the concept of linking accuracy to carbon isn't entirely novel, the analytical framework 'CarbonScaling' and the quantification of inefficiencies represent a valuable contribution. The diminishing returns observation regarding hardware scaling for very large models is particularly insightful.
- **Assessing LLM Text Detection in Educational Contexts: Does Human Contribution Affect Detection?** (Score: 92.0)
  - This paper tackles a highly relevant and timely problem – detecting LLM-generated text in education. The introduction of the GEDE dataset is a significant contribution, and the concept of 'contribution levels' offers a nuanced approach to understanding LLM usage. While benchmarking existing detectors isn't groundbreaking, the focus on educational contexts and the dataset's size suggest strong potential for impact and positive reception within the learning analytics community.
- **SAEMark: Multi-bit LLM Watermarking with Inference-Time Scaling** (Score: 92.0)
  - This paper addresses a very important and timely problem – LLM watermarking – with a novel approach that overcomes limitations of existing methods. The post-hoc, inference-time scaling technique is particularly promising as it doesn't require model access or modification, making it applicable to API-based models and multilingual settings. The theoretical guarantees add to the rigor, and the focus on preserving text quality is crucial for practical adoption.
- **Gradient Surgery for Safe LLM Fine-Tuning** (Score: 90.0)
  - This paper addresses a very important and timely problem – the vulnerability of LLM fine-tuning to malicious data. The proposed 'SafeGrad' method, employing gradient surgery, appears to be a novel and potentially effective solution to mitigate the harmful ratio sensitivity issue. The framing of the problem as conflicting gradients is insightful, and the approach of projecting onto the orthogonal plane is a clever idea. The abstract suggests a rigorous approach, and the problem's relevance to the growing 'Fine-tuning-as-a-Service' paradigm is high.

## Evaluation (3 new papers)
- **Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models** (Score: 92.0)
  - This paper addresses a crucial gap in the safety evaluation of rapidly evolving Omni-modal Large Language Models. The creation of a dedicated benchmark, Omni-SafetyBench, with comprehensive modality combinations and tailored metrics like C-ASR and C-RR, demonstrates a strong methodological approach. The focus on cross-modal consistency is particularly valuable, and the problem is highly relevant given the increasing capabilities and deployment of OLLMs. The work appears well-motivated and likely to be well-received by the community.
- **Can You Trick the Grader? Adversarial Persuasion of LLM Judges** (Score: 92.0)
  - This paper addresses a highly relevant and timely problem – the susceptibility of LLMs used as evaluators to persuasive manipulation. The grounding in rhetorical principles and formalization of persuasion techniques is a strong methodological approach. The finding that model size doesn't mitigate the vulnerability is particularly concerning and highlights a critical flaw in relying on LLMs for objective assessment. The work is well-scoped and the results are clearly presented, suggesting a high likelihood of positive reception within the community.
- **Schema Lineage Extraction at Scale: Multilingual Pipelines, Composite Evaluation, and Language-Model Benchmarks** (Score: 90.0)
  - This paper tackles a very important problem – semantic drift in data pipelines – which is increasingly relevant with the rise of complex data ecosystems and applications like RAG. The introduction of SLiCE as a composite evaluation metric is a strong methodological contribution, and the multilingual focus is valuable. While the core idea of schema lineage extraction isn't entirely novel, the scale and the focus on composite evaluation elevate the work.

## Alignment (2 new papers)
- **"Pull or Not to Pull?'': Investigating Moral Biases in Leading Large Language Models Across Ethical Dilemmas** (Score: 92.0)
  - This research tackles a highly relevant and timely problem – the ethical reasoning of LLMs – with a robust methodology involving 14 models and 27 scenarios. The factorial prompting and analysis across multiple moral philosophies demonstrate a strong commitment to rigor. While the use of trolley problems isn't entirely novel, the scale and depth of the analysis, coupled with the focus on decisiveness and justification consistency, are commendable. The identification of 'sweet zones' suggests potentially valuable insights for alignment.
- **Jinx: Unlimited LLMs for Probing Alignment Failures** (Score: 92.0)
  - This paper addresses a critical gap in LLM safety research – the lack of publicly available 'unlimited' models for probing alignment failures. Providing an open-weight alternative like Jinx is a significant contribution, enabling broader research into safety boundaries and failure modes. The approach of adapting existing open-weight models appears sound, and the potential for impact on the alignment research community is high.

## Reasoning (1 new papers)
- **HealthBranches: Synthesizing Clinically-Grounded Question Answering Datasets via Decision Pathways** (Score: 90.0)
  - This paper addresses a crucial need for robust medical Q&A datasets that test complex reasoning. The semi-automated pipeline leveraging clinical decision pathways is a strong methodological approach, and the inclusion of reasoning paths is a significant benefit for interpretability and evaluation. The scale of the dataset (4,063 cases) and coverage of 17 topics further enhance its value, suggesting a high likelihood of positive reception within the medical NLP community.

## Knowledge (1 new papers)
- **IBPS: Indian Bail Prediction System** (Score: 92.0)
  - This research addresses a critical societal problem – fairness and efficiency in bail decisions – within the Indian legal system. The creation and release of a large, annotated dataset is a significant contribution, and the application of LLMs to this domain is promising. While fine-tuning LLMs isn't inherently novel, the specific application to bail prediction and rationale generation, coupled with the dataset, elevates the work. The potential for reducing bias and backlog in the courts is substantial.

## Architectures (1 new papers)
- **Large Language Models for Subjective Language Understanding: A Survey** (Score: 92.0)
  - This survey paper addresses a highly relevant and timely topic – the application of LLMs to subjective language understanding. The scope, covering sentiment analysis, sarcasm detection, and more, is comprehensive. While a survey isn't inherently innovative, a well-executed one provides significant value by consolidating knowledge and identifying research gaps, which this abstract suggests it does. The potential impact is high given the growing importance of subjective language processing in real-world applications.

## Multimodal (1 new papers)
- **Capabilities of GPT-5 on Multimodal Medical Reasoning** (Score: 92.0)
  - This paper addresses a highly significant problem – applying LLMs to complex medical reasoning with multimodal inputs. The systematic evaluation across multiple established medical benchmarks, including both text and visual QA, suggests a rigorous methodology. While leveraging the power of GPT-5 itself isn't inherently novel, demonstrating its capabilities and outperformance against baselines is valuable, and the unified evaluation protocol is a strength. The potential for improving medical decision support is substantial.

## Categories
**Training** (4), **Evaluation** (3), **Alignment** (2), **Reasoning** (1), **Knowledge** (1), **Architectures** (1), **Multimodal** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
