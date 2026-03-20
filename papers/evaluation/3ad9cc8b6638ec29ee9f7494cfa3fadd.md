# When Names Change Verdicts: Intervention Consistency Reveals Systematic Bias in LLM Decision-Making

**Authors:** Abhinaba Basu, Pavan Chakraborty

**Published:** 2026-03-20 | **Source:** arXiv RSS

**Categories:** cs.CL

**Significance Score:** 92.0/100

## Abstract

arXiv:2603.18530v1 Announce Type: new 
Abstract: Large language models (LLMs) are increasingly used for high-stakes decisions, yet their susceptibility to spurious features remains poorly characterized. We introduce ICE-Guard, a framework applying intervention consistency testing to detect three types of spurious feature reliance: demographic (name/race swaps), authority (credential/prestige swaps), and framing (positive/negative restatements). Across 3,000 vignettes spanning 10 high-stakes domains, we evaluate 11 LLMs from 8 families and find that (1) authority bias (mean 5.8%) and framing bias (5.0%) substantially exceed demographic bias (2.2%), challenging the field's narrow focus on demographics; (2) bias concentrates in specific domains -- finance shows 22.6% authority bias while criminal justice shows only 2.8%; (3) structured decomposition, where the LLM extracts features and a deterministic rubric decides, reduces flip rates by up to 100% (median 49% across 9 models). We demonstrate an ICE-guided detect-diagnose-mitigate-verify loop achieving cumulative 78% bias reduction via iterative prompt patching. Validation against real COMPAS recidivism data shows COMPAS-derived flip rates exceed pooled synthetic rates, suggesting our benchmark provides a conservative estimate of real-world bias. Code and data are publicly available.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 90.0/100

**Justification:** This paper addresses a critical issue in LLM deployment – the reliance on spurious features leading to biased decisions. The introduction of ICE-Guard provides a novel and systematic framework for identifying these biases, going beyond the typical focus on demographics. The findings regarding the prevalence of authority and framing biases are particularly significant, and the demonstrated effectiveness of structured decomposition is promising for mitigation.

## Keywords

bias, authority, rates, shows, authority bias, compas, consistency, data, demographic, detect

## Links

- [Paper URL](https://arxiv.org/abs/2603.18530)

---
*Auto-generated on 2026-03-20 09:51:15 UTC*
