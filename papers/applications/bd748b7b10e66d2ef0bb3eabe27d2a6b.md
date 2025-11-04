# Can SAEs reveal and mitigate racial biases of LLMs in healthcare?

**Authors:** Hiba Ahsan, Byron C. Wallace

**Published:** 2025-11-04 | **Source:** arXiv RSS

**Categories:** cs.LG

**Significance Score:** 90.0/100

## Abstract

arXiv:2511.00177v1 Announce Type: cross 
Abstract: LLMs are increasingly being used in healthcare. This promises to free physicians from drudgery, enabling better care to be delivered at scale. But the use of LLMs in this space also brings risks; for example, such models may worsen existing biases. How can we spot when LLMs are (spuriously) relying on patient race to inform predictions? In this work we assess the degree to which Sparse Autoencoders (SAEs) can reveal (and control) associations the model has made between race and stigmatizing concepts. We first identify SAE latents in Gemma-2 models which appear to correlate with Black individuals. We find that this latent activates on reasonable input sequences (e.g., "African American") but also problematic words like "incarceration". We then show that we can use this latent to steer models to generate outputs about Black patients, and further that this can induce problematic associations in model outputs as a result. For example, activating the Black latent increases the risk assigned to the probability that a patient will become "belligerent". We evaluate the degree to which such steering via latents might be useful for mitigating bias. We find that this offers improvements in simple settings, but is less successful for more realistic and complex clinical tasks. Overall, our results suggest that: SAEs may offer a useful tool in clinical applications of LLMs to identify problematic reliance on demographics but mitigating bias via SAE steering appears to be of marginal utility for realistic tasks.

## Analysis

**Innovation Score:** 75.0/100
**Impact Score:** 85.0/100  
**Sentiment Score:** 88.0/100

**Justification:** This research tackles a crucial problem – racial bias in healthcare LLMs – with a novel approach using Sparse Autoencoders. The finding that SAE latents correlate with both race and stigmatizing concepts is concerning and highlights a real risk. The ability to steer model outputs based on these latents, and the demonstration of induced problematic associations, strengthens the argument for proactive bias mitigation. The work is well-motivated and the initial results are compelling.

## Keywords

llms, black, latent, models, problematic, saes, associations, associations model, bias, biases

## Links

- [Paper URL](https://arxiv.org/abs/2511.00177)

---
*Auto-generated on 2025-11-04 09:30:39 UTC*
