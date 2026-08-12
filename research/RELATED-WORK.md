# Related Work and Protocol Positioning

## Status and Scope

This document positions MSB relative to earlier agent communication languages,
current agent interoperability protocols, and multi-agent deliberation
research. It is informative. It does not claim priority, compatibility,
replacement, endorsement, or IETF consensus.

MSB addresses a narrow question: how can heterogeneous systems exchange an
append-only, inspectable deliberation state containing claims, evidence,
objections, revisions, decisions, failures, and termination without requiring
private reasoning disclosure?

## Layer Position

| System or family | Primary layer | Relationship to MSB |
|---|---|---|
| KQML | Agent communication acts and knowledge exchange | Historical foundation for typed message intent and separation of content, language, and ontology |
| FIPA ACL | Communicative acts, message structure, and interaction protocols | Historical foundation for explicit semantics and protocol discipline |
| MCP | AI application access to tools, resources, prompts, and context | Complementary tool and context layer |
| A2A | Discovery, task exchange, and interoperability among agentic applications | Complementary agent application and task layer |
| ACP | Multimodal communication among agents, applications, and humans | Historical related protocol; its project has joined A2A |
| Multi-Agent Debate | Iterative model interaction intended to improve answers | Motivates structured deliberation but does not define a portable artifact protocol |
| MSB | Shared, auditable deliberation artifacts and closure | Candidate model-independent deliberation-state layer |

A transport or agent protocol can carry MSB artifacts without adopting MSB
semantics. MSB does not define discovery, task routing, tool invocation,
transport security, or application lifecycle.

## KQML

Tim Finin, Richard Fritzson, Don McKay, and Robin McEntire described KQML as a
language and protocol for exchanging information and knowledge among intelligent
systems. KQML introduced performatives and separated message intent from content
language and ontology.

MSB differs in its focus on immutable deliberation artifacts, explicit
objection and revision history, privacy boundaries for black-box models, and
decision closure.

Reference: Tim Finin, Richard Fritzson, Don McKay, and Robin McEntire, "KQML as
an Agent Communication Language", CIKM 1994, DOI 10.1145/191246.191322.

## FIPA ACL

The Foundation for Intelligent Physical Agents standardized ACL message
structure, communicative acts, content languages, ontologies, and interaction
protocols. FIPA ACL demonstrates the value of explicit communicative semantics
and also records the difficulty of unambiguous semantic conformance testing.

MSB narrows its conformance target to externally inspectable artifacts and
graph invariants. It does not require access to a participant's beliefs,
intentions, private cognition, or internal ontology.

References: FIPA ACL Message Structure Specification SC00061 and FIPA
Communicative Act Library Specification SC00037.

## Model Context Protocol

The Model Context Protocol defines standardized interaction between AI
applications and external capabilities such as tools, resources, prompts, and
context.

- MCP exposes or invokes external capabilities.
- MSB represents the public state of a deliberation.
- MCP tool results may become evidence inputs to MSB.
- MSB treats those results as data and does not grant them authority to mutate
  role, system, privacy, or authorization policy.

MSB is not an MCP replacement or extension. A future binding could define how
MSB artifacts are transported through MCP without changing either protocol's
core semantics.

Reference: https://modelcontextprotocol.io/specification/.

## Agent2Agent

Agent2Agent is an open protocol for discovery, communication, task delegation,
and interoperability among opaque agentic applications. It originated at
Google and is hosted by the Linux Foundation.

A2A operates at the agent application and task layer. MSB does not duplicate
Agent Cards, task lifecycle, discovery, or remote-agent interaction. MSB defines
a candidate representation for inspectable deliberation state that an agent
task might produce or consume.

Reference: https://a2a-protocol.org/.

## Agent Communication Protocol

ACP was developed in the BeeAI community as an open protocol for communication
among agents, applications, and humans. The ACP project subsequently announced
that it became part of A2A under the Linux Foundation.

ACP is therefore recorded as relevant protocol lineage, not as a separate
current competitor to A2A. Its goals are adjacent to MSB, but it did not define
MSB's append-only artifact graph, blocking-objection closure, or privacy
boundary.

Reference: https://github.com/i-am-bee/acp.

## Multi-Agent Debate

Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch
studied iterative multi-agent debate as a method for improving factuality and
reasoning. This work demonstrates that interaction among model instances can be
useful, but it does not itself provide a transport-independent artifact schema,
canonical identity, provenance model, failure semantics, or verifiable closure.

Later evaluations caution that debate does not reliably outperform simple
single-agent baselines across all tasks. MSB therefore does not claim that
multi-model deliberation is inherently more accurate.

References:

- Du et al., "Improving Factuality and Reasoning in Language Models through
  Multiagent Debate", arXiv:2305.14325.
- Hangfan Zhang et al., "If Multi-Agent Debate Is the Answer, What Is the
  Question?", arXiv:2502.08788.

## Free-MAD

Yu Cui, Hang Fu, Haibin Zhang, Licheng Wang, and Cong Zuo proposed Free-MAD,
which challenges consensus-driven debate and evaluates a debate trajectory
instead of relying only on final-round majority voting.

Free-MAD is directly relevant to MSB's decision not to treat majority agreement
as sufficient closure. MSB preserves reachable blocking objections and requires
explicit disposition. Revision `-00` does not standardize trajectory scores,
role reliability, or adjudication thresholds.

Reference: "Free-MAD: Consensus-Free Multi-Agent Debate",
arXiv:2509.11035.

## CIPHER

Chau Pham, Boyi Liu, Yingxiang Yang, Zhengyu Chen, Tianyi Liu, Jianbo Yuan,
Bryan A. Plummer, Zhaoran Wang, and Hongxia Yang studied embedding-mediated
multi-agent debate in "Let Models Speak Ciphers".

CIPHER illustrates that sampled natural-language tokens are not the only
communication surface. MSB does not standardize latent or embedding exchange
because cross-model semantic alignment, auditability, portability, and privacy
boundaries remain unresolved.

Reference: "Let Models Speak Ciphers: Multiagent Debate through Embeddings",
ICLR 2024.

## G2CP

Karim Ben Khaled and Davy Monticolo proposed G2CP, a graph-grounded
communication protocol in which agents exchange graph operations rather than
free text.

G2CP is architecturally close to MSB in its use of structured graph exchange.
G2CP operates over a shared knowledge graph and graph operations; MSB operates
over immutable deliberation artifacts and explicit references and includes
objection disposition, failure, termination, provenance, and closure semantics.
MSB does not inherit G2CP's reported performance results.

Reference: "G2CP: A Graph-Grounded Communication Protocol for Verifiable and
Efficient Multi-Agent Reasoning", arXiv:2602.13370.

## Positioning Summary

MSB does not propose a universal language for every agent interaction. It
proposes a candidate shared record for auditable deliberation. Whether this
combination produces measurable interoperability, efficiency, or
decision-quality gains remains an experimental question.
