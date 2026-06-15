---
layout: post
title: "Networking — Best of the Last 6 Months"
date: 2026-06-15
---

A look back at the networking writing worth keeping from the first half of 2026 — the pieces our beat kept returning to across service-provider routing, data-centre fabric, and the automation and telemetry that hold it all together. Nothing here is breaking news; these are the explainers, postmortems and design arguments that earned a second read.

## Routing & security

**[Cloudflare: enforce the first AS in BGP paths to shut a hijack class](https://blog.cloudflare.com/enforce-first-as-bgp/)**  
A concrete, deployable control — verifying a peer always lists its own ASN first in the AS_PATH — and a clear account of the forged-path misdirection it prevents. Drop-in for any operator.  
*Cloudflare · Jun 3*

**[Catching short-lived BGP route leaks automatically](https://blog.apnic.net/2026/05/25/ephemeral-leaks-and-automated-bgp-route-leak-detection/)**  
Doug Madory on the ephemeral leaks that slip past manual review, and how to detect them without a human in the loop — measurement-backed routing-security automation.  
*APNIC · May 24*

**[RADIUS isn't going away, so let's fix it properly](https://blog.apnic.net/2026/05/26/radius-isnt-going-away-so-lets-fix-it-properly/)**  
The FreeRADIUS maintainer makes the case for modernising a load-bearing piece of legacy AAA, and lays out the security roadmap from the primary source.  
*APNIC · May 25*

**[Stop designing route reflectors like it's 2005](https://medium.com/@herve.hildenbrand/stop-designing-route-reflectors-like-its-2005-part-2-the-fast-twitch-muscle-a939fcd8d23d)**  
Opinionated, current guidance on iBGP route-reflector placement and scaling, challenging design habits that have outlived their justification.  
*Medium · May 13*

## Fabric & architecture

**[Goodbye, leaf-and-spine networks?](https://blog.ipspace.net/2026/06/goodbye-leaf-spine-networks/)**  
Ivan Pepelnjak weighs AWS's random-graph-theory fabric claims against the established Clos default — a sharp, skeptical look at whether the new design actually replaces the old one.  
*ipSpace · Jun 10*

**[EVPN centralized routing with Arista EOS](https://blog.ipspace.net/2026/06/arista-eos-evpn-central-routing/)**  
A lab-validated deep-dive into EVPN route-generation patterns for centralized routing, with mechanics that carry across vendors.  
*ipSpace · Jun 3*

**[How Discord moved voice to the edge](https://discord.com/blog/how-we-moved-discord-voice-to-the-edge)**  
A first-party account of re-architecting real-time UDP voice onto edge points-of-presence with anycast and steering — a large-scale deployment told with its trade-offs intact.  
*Discord Engineering · Jun 11*

## Automation & telemetry

**[Scaling Akvorado's routing store with sharding](https://vincent.bernat.ch/en/blog/2026-akvorado-rib-sharding)**  
Vincent Bernat shards the BMP-fed routing store to push flow-enrichment past a single-store bottleneck — a reusable pattern for anyone building telemetry pipelines, straight from the tool's author.  
*vincent.bernat.ch · May 25*

**[Understanding traceroute by reimplementing it in Rust](https://blog.apnic.net/2026/05/25/understanding-traceroute-by-re-implementing-it-in-rust/)**  
George Michaelson teaches the internals — and how to read traceroute output correctly — by rebuilding it from scratch. Diagnostic literacy you'll reuse constantly.  
*APNIC · May 25*

**[Managing MikroTik RouterOS in natural language with MikroMCP](https://medium.com/@ali.karami.m/using-claude-and-mcp-to-manage-mikrotik-routeros-with-natural-language-introducing-mikromcp-321bedc259bc)**  
A working MCP server that exposes a real network OS to AI-native control — one of the more concrete uses of LLMs for network operations to surface this half, rather than another think-piece.  
*Medium · May 20*
