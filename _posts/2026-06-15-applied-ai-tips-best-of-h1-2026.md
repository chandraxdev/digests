---
layout: post
title: "Applied AI Tips — Best of the Last 6 Months"
date: 2026-06-15
---

Six months of applied-AI reading, distilled. We pulled the half-year's most useful how-to material on prompt and context engineering, retrieval, evals, and Claude power-use — the pieces that explain *why* a technique works, not just that it does. These aren't this week's links; they're the references worth keeping open in a tab.

## Context engineering

**[Finding the smallest set of high-signal tokens](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)**  
Anthropic's canonical framing for what to put into — and deliberately keep out of — an agent's context, with practical patterns you can apply immediately.  
*Anthropic*

**[Context editing and the memory tool, with numbers](https://claude.com/blog/context-management)**  
The two primitives that keep long agent runs inside budget: auto-clearing stale tool results near the limit, and a file-based memory tool. Worth reading for the measured gains — context editing alone lifted agentic task performance by roughly 29%, and with memory by roughly 39%, while cutting token use sharply on a 100-turn eval.  
*claude.com · Sep 2025*

**[Harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)**  
A two-agent scaffold — an initializer plus an incremental coding agent — backed by progress files, structured feature lists and git checkpoints, so an agent keeps making real progress across many context windows instead of losing the thread or declaring "done" early.  
*Anthropic · Nov 2025*

**[Context as infrastructure you build](https://eugeneyan.com/writing/working-with-ai/)**  
Eugene Yan's mental model for compounding leverage with AI — context as infrastructure, taste as configuration, verification for autonomy, delegation for scale. A clean reframe of context as something you engineer rather than text you paste.  
*eugeneyan.com · May 2026*

## Prompt engineering

**[Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)**  
Anthropic's continuously-updated reference covering clarity, few-shot, XML structuring, long-context placement, thinking, and tool use — each technique paired with a rationale and a before/after example. The one prompt reference worth bookmarking.  
*platform.claude.com*

**[Writing agent system prompts, learned from reverse-engineering Claude Code](https://www.indiehackers.com/post/the-complete-guide-to-writing-agent-system-prompts-lessons-from-reverse-engineering-claude-code-6e18d54294)**  
Treat a system prompt as environment design: identity and safety at the top and bottom, principles over rigid step lists, static and dynamic content kept separate, and always explaining the *why* so the model generalizes to edge cases. Unusually all-rationale.  
*indiehackers.com · Mar 2026*

**[Latent-space engineering: priming the model's frame of mind](https://blog.fsck.com/2026/01/30/Latent-Space-Engineering/)**  
Jesse Vincent's argument that prompts work better when they put the model in an optimal state — calm, confident, stylistically primed — and a mechanistic reason why supportive role-framing changes output quality, beyond "be nice to the AI."  
*blog.fsck.com · Jan 2026*

## RAG and evals

**[Contextual retrieval, with a runnable eval harness](https://github.com/anthropics/claude-cookbooks/blob/main/capabilities/contextual-embeddings/guide.ipynb)**  
Prepend a Claude-generated sentence of context to each chunk before indexing, then layer hybrid search and reranking. The cookbook shows the measured payoff — retrieval failures dropping by roughly half end-to-end — and states the ingestion-cost trade-off honestly.  
*claude-cookbooks*

**[The LLM evals FAQ everyone keeps sharing](https://hamel.dev/blog/posts/evals-faq/)**  
Hamel Husain's no-nonsense answers to the questions teams actually have: build application-specific judges from real error analysis, validate them before you trust them, and skip the generic metrics that create false confidence. The practitioner reference on the topic.  
*hamel.dev · Jan 2026*

**[A pragmatic guide to LLM evals for developers](https://newsletter.pragmaticengineer.com/p/evals)**  
Where and how to run evals without overbuilding — at three points: offline, in production, and pre-merge — kept cheap and meaningful.  
*Pragmatic Engineer*

## Claude power-use: Skills, MCP, agents

**[Eight practical tips for writing agent skills](https://www.philschmid.de/agent-skills-tips)**  
Philipp Schmid's concrete, field-tested advice for getting more out of skills — the small authoring decisions that separate a skill the model actually uses from one it ignores.  
*philschmid.de*

**[A minimal, production Claude Code setup](https://okhlopkov.com/claude-code-setup-mcp-hooks-skills-2026/)**  
One scoped CLAUDE.md, an MCP config with only the servers you actually use, a single safety hook, one reusable skill, subagents only where they earn their keep. Every component is justified by a trade-off — the opposite of a feature dump — and backed by four months of daily use.  
*okhlopkov.com · 2026*

**[The comprehensive guide to building agents](https://huyenchip.com/2025/01/07/agents.html)**  
Chip Huyen's deep, vendor-neutral overview of how agents actually work — still the best single starting point if you're building one.  
*huyenchip.com*
