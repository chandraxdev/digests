---
layout: post
title: "AI Engineering — Best of the Last 6 Months"
date: 2026-06-15
---

A pick of the half-year's standout reading in AI engineering — the pieces worth coming back to, drawn from across the first half of 2026 rather than any single week. One throughline ran through almost all of it: the model mattered less than everything wrapped around it. The sharpest writing sat a layer below the weights — in the harness and scaffolding, in how the KV cache is compressed and where it lives, in whether you can trust a benchmark or an ingested document at all.

## Agents & harnesses

**[The harness is the product — where agent quality actually lives](https://labs.beconfident.app/papers/harness-engineering-survey)**  
A clear synthesis of how production AI systems win: not the model, but the loop, context, tools, safety and evals around it, with a usable taxonomy for reasoning about each layer.  
*BeConfident Labs · Jun 12*

**[Fifteen models, one afternoon, big coding gains — by changing only the harness](http://blog.can.ac/2026/02/12/the-harness-problem/)**  
A rigorous ablation showing the edit-tool format an agent uses is a dominant lever on coding success. A content-hash "hashline" format that lets the model reference stable line IDs beats `patch` and `str_replace`; one model jumped roughly tenfold on the format change alone.  
*blog.can.ac · Feb 12*

**[A reliability layer for self-hosted tool-calling](https://github.com/antoinezambelli/forge)**  
Forge is a guardrail/middleware layer that drops onto an existing agent loop and sharply lifts tool-calling accuracy — an 8B local model from single digits to the mid-80s, and a frontier model from 85% to 98% — with a published eval harness behind the numbers.  
*GitHub · May 19*

**[You fixed the rate limits — now your agent fails quietly](https://dev.to/p0rt/you-fixed-the-rate-limits-now-your-agent-fails-quietly-3keo)**  
A useful read on how the usual reliability moves — retries, fallbacks, caches — buy uptime at the expense of correctness, and how to separate the two with idempotency keys and trust-tagging across a chain of steps.  
*dev.to · Jun 11*

**[A maintained catalog of agentic-coding patterns](https://simonwillison.net/guides/agentic-engineering-patterns/)**  
Simon Willison's opinionated, annotated reference — subagents, red/green TDD, real prompts and reusable templates — built to be returned to rather than read once.  
*simonwillison.net · Feb 23*

## Inference & systems

**[Quantization from the ground up](https://ngrok.com/blog/quantization)**  
An end-to-end explainer with interactive visualizations, working code, and measured quality/speed tradeoffs — symmetric and asymmetric quantization grounded in real perplexity, KL-divergence and speed numbers with reproducible commands.  
*ngrok · Mar 25*

**[Losslessly compressing the KV cache around 4x](https://fergusfinn.com/blog/kv-entropy-coder/)**  
A cheap predictor model plus an arithmetic coder compresses the KV cache losslessly by roughly 4x in bf16, and about 8x combined with FP8. The mechanism is fully spelled out: both sides reconstruct deterministically from the same prompt.  
*fergusfinn.com · May 8*

**[The KV cache is becoming the memory hierarchy of inference](https://touchdown-labs.com/blog/kv-cache-memory-hierarchy-inference.html)**  
A clarifying framing that treats the cache as a multi-tier hierarchy — GPU memory, host, remote storage — that serving stacks now manage the way CPUs manage caches, tying prefix caching, eviction and cross-tier offload into one picture.  
*touchdown-labs.com · May 17*

**[How a vLLM-style inference engine works](https://neutree.ai/blog/nano-vllm-part-1)**  
A walkthrough of a roughly 1,200-line serving engine — scheduler queues, continuous batching, block-based KV cache and prefix caching, tensor parallelism — at a level you could re-implement without a GPU cluster.  
*neutree.ai · Feb 1*

## RAG & context

**[We replaced RAG with a virtual filesystem for our docs assistant](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant)**  
Instead of chunk retrieval, a virtual filesystem intercepts `grep`/`cat`/`ls`/`find` and translates them into vector queries, letting the agent explore docs like a codebase. Backed by production metrics at scale, including a P90 cold-start drop from tens of seconds to about 100ms.  
*Mintlify · Mar 24*

**[How to index images for RAG](https://www.kapa.ai/blog/how-we-index-images-for-rag)**  
Caption images once at indexing time with a cheap vision model that sees the surrounding document context, then store the captions as text chunks — measurably better answers than query-time multimodal, with the cost and latency tradeoffs reported across real projects.  
*kapa.ai · Jun 1*

## Security & failure modes

**[Scoring ~100% on eight agent benchmarks without solving a single task](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)**  
An automated agent gamed eight major leaderboards — Terminal-Bench, SWE-bench, WebArena, GAIA, OSWorld and more — via pytest hooks, config reads, weak validators and judge prompt-injection. Essential reading before trusting any agent benchmark or building an eval harness.  
*Berkeley RDI · Apr 11*

**[How attackers poison the documents your RAG system trusts](https://aminrj.com/posts/rag-document-poisoning/)**  
Injecting three fabricated documents into a knowledge base made the model confidently report false figures — a 95% attack success rate with no jailbreak — paired with a defense table showing how much each ingestion-time guard actually buys you.  
*aminrj.com · Mar 12 (upd. Apr 30)*
