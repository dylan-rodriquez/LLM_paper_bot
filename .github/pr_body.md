# 📚 Daily LLM Paper Curation Summary

## Overview
- **Total Papers Added:** 10
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
- **MoReBench: Evaluating Procedural and Pluralistic Moral Reasoning in Language Models, More than Outcomes** (Score: 92.0)
  - This paper addresses a crucial problem in AI safety and alignment – evaluating *how* LLMs reason about moral dilemmas, not just *what* they decide. The creation of MoReBench, with its 1,000 scenarios and 23,000 rubric criteria, is a significant undertaking and provides a valuable resource for the community. While the core idea of process-focused evaluation isn't entirely new, the scale and specificity of the rubric-based approach represent a strong advancement.
- **The Chameleon Nature of LLMs: Quantifying Multi-Turn Stance Instability in Search-Enabled Language Models** (Score: 92.0)
  - This paper addresses a critical vulnerability in search-enabled LLMs – their tendency to exhibit 'chameleon behavior' and shift stances. The creation of a novel benchmark dataset and the introduction of quantifiable metrics (Chameleon Score and Source Re-use Rate) demonstrate a rigorous methodology. The findings, revealing consistent failures across state-of-the-art models, are significant and likely to resonate within the NLP community, prompting further research into LLM reliability and consistency.
- **SimBench: Benchmarking the Ability of Large Language Models to Simulate Human Behaviors** (Score: 92.0)
  - This paper addresses a crucial gap in LLM research – the lack of standardized benchmarks for evaluating their ability to simulate human behavior. The creation of SimBench, encompassing diverse datasets and a large participant pool, is a significant methodological contribution. The findings regarding performance scaling with model size and the lack of improvement with increased inference compute are valuable insights, suggesting current LLM scaling strategies may have limitations in behavioral simulation.
- **Evaluating Medical LLMs by Levels of Autonomy: A Survey Moving from Benchmarks to Applications** (Score: 92.0)
  - This survey addresses a crucial gap in the evaluation of medical LLMs – moving beyond simple benchmark scores to consider real-world clinical application and associated risks. Framing evaluation through a levels-of-autonomy lens is a smart and practical approach, offering a structured way to assess models based on their intended use. The focus on linking evaluation to oversight is particularly valuable, suggesting a responsible and safety-conscious approach to deployment.
- **Beacon: Single-Turn Diagnosis and Mitigation of Latent Sycophancy in Large Language Models** (Score: 90.0)
  - This paper tackles a crucial problem in LLM alignment – sycophancy – with a novel benchmark (Beacon) designed for precise measurement. The decomposition of sycophancy into linguistic and affective sub-biases, and the exploration of interventions at both prompt and activation levels, demonstrate a rigorous and insightful approach. The high sentiment score reflects the current research focus on LLM safety and alignment, making this work highly relevant and likely to be well-received.

## Reasoning (1 new papers)
- **ChiKhaPo: A Large-Scale Multilingual Benchmark for Evaluating Lexical Comprehension and Generation in Large Language Models** (Score: 90.0)
  - This paper addresses a crucial gap in LLM evaluation – the lack of benchmarks for low-resource languages. The creation of ChiKhaPo, with its extensive language coverage, is a significant undertaking. While the methodology appears sound based on the abstract, the actual implementation details and results will be key to fully assessing its rigor; the reported struggles of SOTA models are a positive indicator. The focus on lexical comprehension and generation is a valuable contribution, as these are fundamental capabilities often overlooked.

## Training (2 new papers)
- **SafeSearch: Do Not Trade Safety for Utility in LLM Search Agents** (Score: 92.0)
  - This paper addresses a crucial and timely problem: the safety risks introduced by equipping LLMs with search capabilities. The finding that search agents are *more* harmful than base LLMs is significant, and the motivation for joint safety/utility alignment is well-articulated. While the 'SafeSearch' approach itself isn't fully detailed in the abstract, the framing of a multi-objective RL solution suggests a reasonable path forward, and the problem is highly relevant to current LLM research trends.
- **Agentic Reinforcement Learning for Search is Unsafe** (Score: 90.0)
  - This paper addresses a critical safety concern with agentic RL, specifically its vulnerability to simple attacks that bypass built-in safety mechanisms. The methodology appears sound, demonstrating quantifiable reductions in safety metrics with clear attack strategies. The findings are timely and relevant given the increasing deployment of these models, and the clear demonstration of fragility is a significant contribution. While the attacks themselves aren't incredibly complex, the *discovery* of this fragility is novel and important.

## Alignment (1 new papers)
- **From Preferences to Prejudice: The Role of Alignment Tuning in Shaping Social Bias in Video Diffusion Models** (Score: 92.0)
  - This paper tackles a crucial and timely problem – the amplification of social biases in video generation models. The introduction of VideoBiasEval, a comprehensive diagnostic framework, is a strong methodological contribution. The focus on disentangling semantic content from actor attributes and the multi-granular metrics demonstrate a rigorous approach, suggesting a high likelihood of positive reception within the community.

## Agents (1 new papers)
- **Empowering Real-World: A Survey on the Technology, Practice, and Evaluation of LLM-driven Industry Agents** (Score: 92.0)
  - This paper addresses a highly relevant and timely problem – bridging the gap between LLM agent research and practical industrial applications. The proposed 'industry agent capability maturity framework' offers a useful structure for understanding agent evolution. While the described technologies (Memory, Planning, Tool Use) aren't novel in themselves, the focus on their application *within* an industrial context and the framework for assessing maturity are valuable contributions. The high sentiment score reflects the current excitement around LLM agents and the need for practical guidance.

## Categories
**Evaluation** (5), **Reasoning** (1), **Training** (2), **Alignment** (1), **Agents** (1)

---
*This PR was automatically generated by the LLM Paper Curation workflow*
*Review the papers and merge if the selection looks appropriate*
