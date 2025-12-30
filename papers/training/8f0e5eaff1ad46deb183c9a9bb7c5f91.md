# Learning from Negative Examples: Why Warning-Framed Training Data Teaches What It Warns Against

**Authors:** Tsogt-Ochir Enkhbayar

**Published:** 2025-12-30 | **Source:** arXiv RSS

**Categories:** cs.LG

**Significance Score:** 90.0/100

## Abstract

arXiv:2512.22293v1 Announce Type: cross 
Abstract: Warning-framed content in training data (e.g., "DO NOT USE - this code is vulnerable") does not, it turns out, teach language models to avoid the warned-against behavior. In experiments reported here, models exposed to such warnings reproduced the flagged content at rates statistically indistinguishable from models given the content directly (76.7% vs. 83.3%). Why? Sparse autoencoder analysis points to a failure of orthogonalization: "describing X" and "performing X" activate overlapping latent features. Feature #8684, which tracks code execution patterns, fires at comparable magnitude in both warning and exploitation contexts. A related phenomenon, what I call "stealth slip", allows conversational preambles to rotate activations into subspaces that linear probes miss entirely. Prompting and inference-time steering do not fix this; training-time feature ablation does. The upshot is that statistical co-occurrence dominates over pragmatic interpretation in current architectures. Models learn what tends to follow a context, not why it appeared there.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 80.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This paper addresses a crucial and often overlooked problem in training language models – the counterintuitive effect of warning-framed data. The use of sparse autoencoders to identify overlapping latent features is a clever methodological approach, and the 'stealth slip' phenomenon is a particularly interesting observation. The finding that warnings don't prevent reproduction of harmful content has significant implications for responsible AI development and data curation.

## Keywords

models, content, training, warning, code, data, does, feature, framed, time

## Links

- [Paper URL](https://arxiv.org/abs/2512.22293)

---
*Auto-generated on 2025-12-30 09:41:24 UTC*
