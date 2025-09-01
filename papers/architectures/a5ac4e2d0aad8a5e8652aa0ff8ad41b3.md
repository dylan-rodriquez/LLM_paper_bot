# CrossTL: A Universal Programming Language Translator with Unified Intermediate Representation

**Authors:** Nripesh Niketan, Vaatsalya Shrivastva

**Published:** 2025-09-01 | **Source:** arXiv RSS

**Categories:** cs.PL

**Significance Score:** 92.0/100

## Abstract

arXiv:2508.21256v1 Announce Type: cross 
Abstract: We present CrossTL, a universal programming language translator enabling bidirectional translation between multiple languages through a unified intermediate representation called CrossGL. Traditional approaches require separate translators for each language pair, leading to exponential complexity growth. CrossTL uses a single universal IR to facilitate translations between CUDA, HIP, Metal, DirectX HLSL, OpenGL GLSL, Vulkan SPIR-V, Rust, and Mojo, with Slang support in development. Our system consists of: language-specific lexers/parsers converting source code to ASTs, bidirectional CrossGL translation modules implementing ToCrossGLConverter classes for importing code and CodeGen classes for target generation, and comprehensive backend implementations handling full translation pipelines. We demonstrate effectiveness through comprehensive evaluation across programming domains, achieving successful compilation and execution across all supported backends. The universal IR design enables adding new languages with minimal effort, requiring only language-specific frontend/backend components. Our contributions include: (1) a unified IR capturing semantics of multiple programming paradigms, (2) a modular architecture enabling extensibility, (3) a comprehensive framework supporting GPU compute, graphics programming, and systems languages, and (4) empirical validation demonstrating practical viability of universal code translation. CrossTL represents a significant step toward language-agnostic programming, enabling write-once, deploy-everywhere development.

## Analysis

**Innovation Score:** 78.0/100
**Impact Score:** 88.0/100  
**Sentiment Score:** 80.0/100

**Justification:** This paper addresses a significant challenge in heterogeneous computing – the complexity of translating code between different accelerator languages. The use of a unified intermediate representation (CrossGL) is a promising approach to reduce the exponential complexity of pairwise translators. While the concept of IRs isn't novel, the scope of languages supported (CUDA, HIP, Metal, etc.) and the bidirectional translation capability suggest a substantial engineering effort and potential impact.

## Keywords

language, programming, universal, crosstl, translation, code, comprehensive, enabling, ir, languages

## Links

- [Paper URL](https://arxiv.org/abs/2508.21256)

---
*Auto-generated on 2025-09-01 09:30:48 UTC*
