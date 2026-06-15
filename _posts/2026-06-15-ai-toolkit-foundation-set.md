---
layout: post
title: "AI Toolkit — The Foundation Set"
date: 2026-06-15
---

This beat is only a couple of weeks old, so think of this less as a six-month retrospective and more as the foundation set — the ready-to-use AI assets to start from if you're building a working toolkit for Claude, ChatGPT and Gemini today. A few are long-standing staples that have earned their place; a few genuinely shipped this fortnight. Here are the strongest, weighted toward the prompts and skills first.

## Skills worth installing

**[A skill that rewrites your prompt for you (Claude)](https://github.com/Li-Bailiang/prompt-refine-skill)**  
An Agent Skill that quietly refines whatever you type for the model currently running — a rare skill that is itself about better prompting.  
*GitHub · created Jun 5*

**[Make your agent think like a blunt senior dev (Claude)](https://github.com/DietrichGebert/ponytail)**  
Gives an agent the instincts of a no-nonsense senior engineer. It went viral this fortnight — thousands of stars in days — which says something about the appetite for opinionated defaults.  
*GitHub · created Jun 12*

**[Pressure-test a product idea before you build it (Claude)](https://github.com/TexasBedouin/vibe-check)**  
A skill from a long-time product manager that interrogates a beginner's product idea and surfaces the holes early, before you've written any code.  
*GitHub · created Jun 5*

**[Patterns and starters for agent loops (Claude)](https://github.com/cobusgreyling/loop-engineering)**  
Practical patterns, starter templates and CLI tools for "loop engineering" an agent, from prolific LLM practitioner Cobus Greyling.  
*GitHub · created Jun 9*

## Prompts and rules worth keeping

**[A library of ready-to-run prompt patterns (Claude, ChatGPT, Gemini)](https://github.com/danielmiessler/Fabric)**  
An open-source collection of curated prompts for everyday tasks — summarise, extract, analyse, write — that you can run from the command line or lift into any assistant. The single best starting point for reusable prompts.  
*GitHub · 42k★ · evergreen*

**[The system prompts behind the major AI tools (any assistant)](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)**  
The actual system prompts of Claude Code, Cursor and the rest, collected in one place. Less a prompt to copy than a masterclass in how the best tools instruct a model — well worth borrowing from.  
*GitHub · 140k★ · evergreen*

**[A browsable library of reusable agent "rules" (coding agents)](https://cursor.directory)**  
A community catalogue of rule files — system-prompt-style instruction sets — for coding agents, sorted by language and framework. A faster way to pick up a battle-tested setup than writing one from scratch.  
*Cursor Directory · evergreen*

## Tools and servers to install

**[Keep your assistant's docs current (Claude, Cursor — MCP)](https://github.com/upstash/context7)**  
An MCP server that injects up-to-date library documentation into your editor, so the model stops writing against APIs that changed months ago.  
*GitHub · 57k★*

**[Give a coding agent real eyes on the page (coding agents — MCP)](https://github.com/ChromeDevTools/chrome-devtools-mcp)**  
The official server that lets an agent inspect and debug live web pages through Chrome DevTools — invaluable for front-end work.  
*GitHub · 44k★*

**[Path-scoped rules and skills for a whole team (coding agents — MCP)](https://glama.ai/mcp/servers/pathrule/mcp)**  
An MCP server that gives a team shared, path-scoped memories, rules and skills, so the agent picks up the right conventions for whichever part of the repo it's working in.  
*Glama registry · updated Jun 9*

## Directories worth bookmarking

**[The running catalogue of MCP servers](https://github.com/punkpeye/awesome-mcp-servers)**  
The community's go-to index of Model Context Protocol servers, sorted by category — the fastest way to find a server for a given tool or data source.  
*GitHub · 89k★*

**[A large, browsable prompt collection (any assistant)](https://github.com/f/prompts.chat)**  
Formerly "Awesome ChatGPT Prompts": a huge, searchable community library you can copy from, across assistants and use-cases.  
*GitHub · 164k★*
