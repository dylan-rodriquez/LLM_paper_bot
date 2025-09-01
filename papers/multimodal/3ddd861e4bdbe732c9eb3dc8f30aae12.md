# AHELM: A Holistic Evaluation of Audio-Language Models

**Authors:** Tony Lee, Haoqin Tu, Chi Heem Wong, Zijun Wang, Siwei Yang, Yifan Mai, Yuyin Zhou, Cihang Xie, Percy Liang

**Published:** 2025-09-01 | **Source:** arXiv RSS

**Categories:** cs.AI

**Significance Score:** 90.0/100

## Abstract

arXiv:2508.21376v1 Announce Type: cross 
Abstract: Evaluations of audio-language models (ALMs) -- multimodal models that take interleaved audio and text as input and output text -- are hindered by the lack of standardized benchmarks; most benchmarks measure only one or two capabilities and omit evaluative aspects such as fairness or safety. Furthermore, comparison across models is difficult as separate evaluations test a limited number of models and use different prompting methods and inference parameters. To address these shortfalls, we introduce AHELM, a benchmark that aggregates various datasets -- including 2 new synthetic audio-text datasets called PARADE, which evaluates the ALMs on avoiding stereotypes, and CoRe-Bench, which measures reasoning over conversational audio through inferential multi-turn question answering -- to holistically measure the performance of ALMs across 10 aspects we have identified as important to the development and usage of ALMs: audio perception, knowledge, reasoning, emotion detection, bias, fairness, multilinguality, robustness, toxicity, and safety. We also standardize the prompts, inference parameters, and evaluation metrics to ensure equitable comparisons across models. We test 14 open-weight and closed-API ALMs from 3 developers and 3 additional simple baseline systems each consisting of an automatic speech recognizer and a language model. Our results show that while Gemini 2.5 Pro ranks top in 5 out of 10 aspects, it exhibits group unfairness ($p=0.01$) on ASR tasks whereas most of the other models do not. We also find that the baseline systems perform reasonably well on AHELM, with one ranking 5th overall despite having only speech-to-text capabilities. For transparency, all raw prompts, model generations, and outputs are available on our website at https://crfm.stanford.edu/helm/audio/v1.0.0. AHELM is intended to be a living benchmark and new datasets and models will be added over time.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a crucial gap in the ALM field – the lack of standardized and holistic evaluation. The introduction of AHELM, along with the new datasets PARADE and CoRe-Bench, demonstrates a strong methodological approach. The focus on aspects beyond simple accuracy, such as fairness and reasoning, is particularly commendable and suggests a high likelihood of positive reception within the community.

## Keywords

models, audio, alms, ahelm, text, aspects, datasets, language, 10, 10 aspects

## Links

- [Paper URL](https://arxiv.org/abs/2508.21376)

---
*Auto-generated on 2025-09-01 09:30:48 UTC*
