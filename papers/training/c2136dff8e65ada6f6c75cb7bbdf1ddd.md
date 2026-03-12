# Measuring and Eliminating Refusals in Military Large Language Models

**Authors:** Jack FitzGerald, Dylan Bates, Aristotelis Lazaridis, Aman Sharma, Vincent Lu, Brian King, Yousif Azami, Sean Bailey, Jeremy Cao, Peter Damianov, Kevin de Haan, Joseph Madigan, Jeremy McLaurin, Luke Kerbs, Jonathan Tainer, Dave Anderson, Jonathan Beck, Jamie Cuticello, Colton Malkerson, Tyler Saltsman

**Published:** 2026-03-12 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2603.10012v1 Announce Type: new 
Abstract: Military Large Language Models (LLMs) must provide accurate information to the warfighter in time-critical and dangerous situations. However, today's LLMs are imbued with safety behaviors that cause the LLM to refuse many legitimate queries in the military domain, particularly those related to violence, terrorism, or military technology. Our gold benchmark for assessing refusal rates, which was developed by veterans of the US Army and special forces, is to our knowledge the first dataset of its kind. We present results for refusal and deflection rates on 31 public models and 3 military models. We observe hard rejection rates as high as 98.2% and soft deflection rates ranging from 0% to 21.3%. We also present results on two additional synthetic datasets and show their correlations with the gold dataset. Finally, we perform abliteration using the Heretic library on a military-tuned gpt-oss-20b model, showing an absolute increase in answer rate of 66.5 points but an average relative decrease of 2% on other military tasks. In our concluding remarks, we argue for deeper specialization, including with mid-training and end-to-end post-training, to achieve zero refusals and maximum military task accuracy for closed military models.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 85.0/100

**Justification:** This research addresses a critical issue – the unreliability of LLMs in military contexts due to excessive safety constraints. The creation of a gold benchmark dataset developed with veteran input is a significant strength, and the empirical results demonstrating high refusal rates are compelling. While the ablation study using Heretic is promising, the abstract doesn't detail the magnitude of improvement, leaving some questions about the effectiveness of the approach.

## Keywords

military, models, rates, dataset, deflection, deflection rates, end, gold, language, language models

## Links

- [Paper URL](https://arxiv.org/abs/2603.10012)

---
*Auto-generated on 2026-03-12 09:50:07 UTC*
