# IS-Bench: Evaluating Interactive Safety of VLM-Driven Embodied Agents in Daily Household Tasks

**Authors:** Xiaoya Lu, Zeren Chen, Xuhao Hu, Yijin Zhou, Weichen Zhang, Dongrui Liu, Lu Sheng, Jing Shao

**Published:** 2025-12-08 | **Source:** arXiv RSS

**Categories:** cs.AI

**Significance Score:** 92.0/100

## Abstract

arXiv:2506.16402v3 Announce Type: replace-cross 
Abstract: Flawed planning from VLM-driven embodied agents poses significant safety hazards, hindering their deployment in real-world household tasks. However, existing static, non-interactive evaluation paradigms fail to adequately assess risks within these interactive environments, since they cannot simulate dynamic risks that emerge from an agent's actions and rely on unreliable post-hoc evaluations that ignore unsafe intermediate steps. To bridge this critical gap, we propose evaluating an agent's interactive safety: its ability to perceive emergent risks and execute mitigation steps in the correct procedural order. We thus present IS-Bench, the first multi-modal benchmark designed for interactive safety, featuring 161 challenging scenarios with 388 unique safety risks instantiated in a high-fidelity simulator. Crucially, it facilitates a novel process-oriented evaluation that verifies whether risk mitigation actions are performed before/after specific risk-prone steps. Extensive experiments on leading VLMs, including the GPT-4o and Gemini-2.5 series, reveal that current agents lack interactive safety awareness, and that while safety-aware Chain-of-Thought can improve performance, it often compromises task completion. By highlighting these critical limitations, IS-Bench provides a foundation for developing safer and more reliable embodied AI systems. Code and data are released under https://github.com/AI45Lab/IS-Bench.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 80.0/100

**Justification:** This paper addresses a crucial problem in deploying VLMs for embodied agents – interactive safety – which is currently underserved by existing evaluation methods. The proposal of IS-Bench, a multi-modal benchmark focused on *interactive* safety, is a strong contribution. The focus on 'process-oriented evaluation' and identifying risks *before* they occur is a significant step forward, and the scale of the benchmark (161 scenarios, 388 risks) suggests substantial effort and potential utility. While the abstract doesn't detail the specific mitigation techniques evaluated, the problem framing is compelling.

## Keywords

safety, interactive, bench, interactive safety, risks, agents, embodied, steps, actions, agent

## Links

- [Paper URL](https://arxiv.org/abs/2506.16402)

---
*Auto-generated on 2025-12-08 09:36:00 UTC*
