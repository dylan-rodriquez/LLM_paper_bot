# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 7
- **Average Significance Score:** 92.0/100
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

## Multimodal (1 new papers)
- **The Thiomi Dataset: A Large-Scale Multimodal Corpus for Low-Resource African Languages** (Score: 92.0)
  - This paper addresses a crucial gap in NLP research – the lack of resources for low-resource African languages. The creation of a large-scale, multimodal dataset with a robust quality assurance pipeline is a significant achievement. While the ASR, MT, and TTS baselines are valuable, the primary contribution lies in the dataset itself, and the innovation is primarily in the scale and breadth of language coverage rather than novel algorithmic approaches.

## Evaluation (4 new papers)
- **Beyond Idealized Patients: Evaluating LLMs under Challenging Patient Behaviors in Medical Consultations** (Score: 92.0)
  - This paper addresses a crucial gap in medical LLM evaluation – the lack of realism in testing scenarios. By focusing on challenging patient behaviors, it moves beyond idealized inputs and towards a more practical assessment of model safety and reliability. The creation of the CPB-Bench dataset, particularly its bilingual nature, is a strong methodological contribution, and the defined failure criteria add rigor to the evaluation process.
- **Perfecting Human-AI Interaction at Clinical Scale. Turning Production Signals into Safer, More Human Conversations** (Score: 92.0)
  - This research addresses a crucial gap in healthcare AI – moving beyond benchmark accuracy to real-world performance and safety. The scale of data (115M+ interactions, 7K+ clinicians) is impressive and suggests a robust methodology. The focus on 'in-the-wild' cues and the argument against relying on a single LLM for healthcare-grade safety are particularly strong points, indicating a well-considered and potentially impactful approach.
- **Habibi: Laying the Open-Source Foundation of Unified-Dialectal Arabic Speech Synthesis** (Score: 92.0)
  - This paper tackles a significant problem – the lack of unified Arabic TTS – with a well-defined methodology. The repurposing of ASR data and the curriculum learning strategy are clever solutions to data scarcity and dialectal divergence. The release of a standardized benchmark is a particularly valuable contribution, and the reported performance matching specialized models is encouraging. The work is clearly presented and addresses key challenges in the field.
- **AgentDrift: Unsafe Recommendation Drift Under Tool Corruption Hidden by Ranking Metrics in LLM Agents** (Score: 92.0)
  - This paper tackles a critical vulnerability in LLM agents – the potential for unsafe recommendations despite seemingly good ranking metrics. The paired-trajectory protocol and decomposition into information/memory channels are strong methodological contributions. The findings of 'evaluation blindness' and the persistence of unsafe recommendations are concerning and highlight a significant gap in current evaluation practices. The focus on financial dialogues adds to the practical relevance.

## Training (1 new papers)
- **Trojan-Speak: Bypassing Constitutional Classifiers with No Jailbreak Tax via Adversarial Finetuning** (Score: 92.0)
  - This research addresses a critical vulnerability in deployed LLMs – the susceptibility to adversarial fine-tuning that bypasses safety classifiers. The reported low degradation in reasoning benchmarks alongside high classifier evasion rates is particularly impressive. The focus on a real-world scenario (CBRN queries from a bug bounty program) strengthens the paper's relevance and demonstrates practical implications. While the methods build upon existing techniques (curriculum learning, GRPO), the combination and application to this specific problem are novel.

## Alignment (1 new papers)
- **Script Gap: Evaluating LLM Triage on Indian Languages in Native vs Romanized Scripts in a Real World Setting** (Score: 92.0)
  - This research addresses a crucial and often overlooked issue in LLM deployment – the impact of script variation in multilingual contexts, specifically focusing on Indian languages. The identification of a significant performance gap between native and romanized scripts, coupled with a proposed solution and quantification of potential errors, demonstrates strong methodological rigor and practical relevance. The scale of potential errors (2 million) highlights the importance of this work, and the focus on maternal healthcare adds to its societal impact.

## Categories
**Multimodal** (1), **Evaluation** (4), **Training** (1), **Alignment** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
