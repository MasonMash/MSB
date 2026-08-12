# Design Rationale

## Status

This document explains the research rationale behind the MSB artifact model. It
is informative and does not add normative requirements to the Internet-Draft.

## Problem Boundary

Message exchange, tool invocation, and task delegation do not by themselves
provide a stable, auditable deliberation record. MSB studies the narrower
problem of how heterogeneous systems can expose enough shared state for claims,
evidence, objections, revisions, failures, decisions, and termination to be
independently inspected.

A shared artifact is public to the interoperability boundary. The term does not
mean that the artifact is suitable for unrestricted Internet publication.

## Six Persistent Barriers

### Application-layer focus

Many modern protocols focus on model-to-tool integration, remote agent
discovery, task delegation, or application workflows. Those capabilities are
valuable but do not define an append-only deliberation record or decision
closure.

### Natural-language cost and ambiguity

Natural language is broadly usable, but repeated narrative restatement can be
token-expensive and semantically ambiguous. A typed artifact layer can reduce
the amount of meaning that must be reconstructed from prose.

MSB does not claim that compact encoding is already proven to reduce cost.
Compact wire forms remain a future evaluation subject.

### No portable embedding space

Embeddings from different model families are not assumed to share a stable,
portable, or independently verifiable semantic space. Core interoperability
therefore cannot depend on private vectors or provider-specific latent state.

### Unresolved ontology alignment

A common syntax does not guarantee common meaning. MSB limits its initial
semantic vocabulary, defines explicit reference relations, and leaves
domain-specific ontologies outside the core.

### Incentives favor application integration

Most deployed interoperability work has immediate value at the application,
tool, and workflow layers. Deliberation semantics have fewer mature deployment
anchors. MSB therefore remains experimental and separates its artifact layer
from transport and orchestration.

### Security and privacy are structural constraints

Prompt injection, evidence poisoning, role hijacking, provenance spoofing,
omitted objections, graph exhaustion, and disclosure of sensitive data cannot
be repaired solely by changing transport. They influence the artifact boundary,
validation rules, closure behavior, and deployment policy.

## Research Contributions

The project investigates five separable contributions:

1. a model-independent shared-artifact boundary;
2. typed, immutable deliberation artifacts and explicit relations;
3. evidence provenance and objection-aware decision closure;
4. fail-closed failure and termination semantics; and
5. a deterministic restricted JSON and content-identifier profile.

These are research contributions, not claims of novelty over every prior
agent-communication system and not proof of interoperability.

## Relationship to Existing Protocol Families

KQML and FIPA ACL established important agent-communication concepts,
including performatives and formal communication semantics. They also
demonstrated that syntax alone does not solve ontology alignment, pragmatic
interpretation, or conformance assessment.

The Model Context Protocol standardizes connections between AI applications
and external context, resources, prompts, and tools. Agent2Agent standardizes
communication and task-oriented interoperability between opaque agentic
applications. These protocols can carry or support MSB artifacts, but they do
not define MSB's append-only deliberation graph and closure rules.

Earlier and emerging agent-communication protocols informed the research
question. MSB does not claim to replace, extend, or be compatible with them
unless a future binding specification demonstrates that relationship.

## Conceptual Primitives

The research model uses these conceptual operations:

- introduce a claim;
- attach provenance-bearing evidence;
- object to an artifact or assumption;
- revise without mutating history;
- record an explicit failure;
- decide over a declared closure; and
- terminate with a visible terminal state.

The seven core artifact types are the current realization of these operations.
Whether this vocabulary is minimal remains an open research question.

## Privacy Classification Model

The research program uses four conceptual privacy classes:

| Class | Research meaning |
|---|---|
| P0 | Material intended for unrestricted disclosure |
| P1 | Material shareable with authorized deliberation participants |
| P2 | Sensitive internal material that must not cross the interoperability boundary |
| P3 | Secret or highly restricted material that must not be placed in shared artifacts |

These classes are useful for threat analysis and evaluation. Revision `-00`
does not standardize them as mandatory wire labels because authorization,
deployment boundaries, and regulatory meaning vary by application.

Implementations still need explicit disclosure, authorization, minimization,
retention, logging, and deletion policies.

## Role Model

Roles such as orchestrator, proposer, objector, verifier, risk reviewer, and
synthesizer can improve an orchestration policy. They are not core artifact
identity fields in revision `-00`.

A transport or orchestration profile may bind authenticated actors to roles.
Untrusted artifact content must never assign itself authority to mutate role,
system, privacy, or authorization policy.

## Typed Deliberation Graph

The proposed model is a directed graph whose nodes are immutable artifacts and
whose edges carry explicit relations. Revision `-00` requires an acyclic graph
and preserves concurrent tips.

Decision quality is not defined as raw majority vote. A decision must expose
its basis and the disposition of reachable blocking objections. Reliability
scores, adjudication weights, and decision thresholds remain experimental.

## Compact Runtime Grammar

A delimiter-based compact runtime form may reduce repeated narrative overhead,
but it introduces escaping, extensibility, debugging, internationalization, and
security risks.

It is therefore not part of revision `-00`. Any future compact or binary
encoding must preserve the same abstract artifact semantics and demonstrate
measurable benefit against JSON and natural-language baselines.

## Conformance Layers

The research program distinguishes possible implementation layers:

- human-readable structured artifacts;
- compact textual encoding;
- JSON-compatible envelopes;
- binary encoding; and
- independently verified implementations.

Revision `-00` does not standardize an L0-L4 ladder. Conformance claims instead
identify the exact tested surface: canonical representation, artifact semantic
validation, or closure verification.

## Design Principles

The active design principles are:

- shared artifacts over private cognition;
- explicit types over inferred conversational intent;
- immutable revision over silent overwrite;
- provenance over unsupported authority;
- explicit failure over fabricated success;
- objection-aware closure over transcript completion;
- privacy minimization at the interoperability boundary;
- transport independence;
- bounded resource use; and
- claims limited to available evidence.

## Deferred Questions

The following remain outside the normative `-00` core:

- role reliability and adjudication thresholds;
- mandatory privacy-class wire labels;
- compact delimiter and binary encodings;
- transport bindings and media types;
- signatures and actor authentication;
- ontology negotiation;
- bounded-history checkpoint profiles;
- extension registries; and
- final protocol naming.
