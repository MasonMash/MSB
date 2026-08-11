# MSB

**A research project for interoperable, auditable deliberation between heterogeneous AI models.**

Modern AI systems increasingly combine models from different providers, architectures, and capability classes. Transport and tool invocation can be standardized, yet the reasoning process between models is still commonly represented as free-form conversation, provider-specific state, or an opaque sequence of agent messages.

That creates a practical interoperability problem.

When one model challenges another, an external reviewer should be able to determine:

- what was claimed;
- what evidence supported the claim;
- what was challenged;
- what changed after the challenge;
- which objections remain unresolved; and
- why the final decision follows from the public record.

Doing that should not require access to private chain-of-thought, hidden state, system prompts, model weights, or provider-specific internal memory.

MSB investigates a protocol layer for that public record.

## The Problem

A multi-model system can exchange text without having a shared semantics for deliberation.

Two models may be able to communicate while still lacking a provider-neutral contract for:

- claims;
- evidence provenance;
- objections;
- revisions;
- decisions;
- failures;
- termination;
- immutable history; and
- verifiable reference closure.

Without such a contract, interoperability at the transport layer does not automatically produce interoperability at the deliberation layer.

MSB treats this as a protocol problem.

### Why a Chat Log Is Not Enough

A transcript can show that messages were exchanged, but it does not necessarily provide stable protocol semantics.

Free-form conversation does not inherently define:

- immutable artifact identity;
- evidence provenance;
- explicit challenge relationships;
- supersession without history mutation;
- machine-verifiable failure states;
- terminal-state semantics; or
- proof that a final decision considered every blocking objection in scope.

Those properties must be represented explicitly if independently implemented systems are expected to interoperate and audit one another.

### Interoperability Boundary

The intended architecture is deliberately narrow:

```text
private model computation
          |
          v
    public artifact
          |
          v
schema + provenance + privacy validation
          |
          v
content-addressed append-only artifact graph
          |
          v
challenge / revision / decision
          |
          v
auditable closure and termination
```

Models may differ internally at every step above the public-artifact boundary.

The protocol exists so that they do not need to agree on their private reasoning representation in order to share an auditable deliberation state.

## Design Thesis

The protocol boundary should contain **public artifacts, not private reasoning traces**.

A conforming model may perform arbitrary private computation internally. What crosses the interoperability boundary is a compact artifact that another implementation can inspect, challenge, reference, supersede, or decide upon.

The research draft currently defines seven core public semantics:

1. `CLAIM`
2. `EVIDENCE`
3. `OBJECTION`
4. `REVISION`
5. `DECISION`
6. `FAILURE`
7. `TERMINATION`

The associated protocol work includes evidence provenance, content-addressed identity, append-only history, versioned extensions, failure semantics, and closure verification.

## What Success Would Mean

A successful standard would allow independently implemented models to participate in the same deliberation without requiring a shared vendor, model family, orchestration framework, or private reasoning format.

A third party should be able to audit the resulting decision from the public artifact graph alone.

That is the central invariant of this project.

## What MSB Is Not

MSB is not intended to be:

- an agent framework;
- a workflow engine;
- an MCP replacement;
- a tool-calling protocol;
- a model-control API;
- a transport protocol;
- a hidden language between models; or
- a mechanism for extracting private chain-of-thought.

Those systems may carry MSB artifacts, but they are outside the protocol's core scope.

## Current Status

The repository contains **Research Draft 0.1**.

It is an experimental research draft and **not an adopted standard**.

Three study stages inform the current specification:

### EXP-001-R2

A heterogeneous twelve-round model panel completed 12 of 12 planned calls.

It demonstrated that structured public artifacts can carry useful design proposals, objections, revisions, and final judgment across heterogeneous models.

Its direct deliberation context was **single-hop**: each participant received the experiment specification and the immediately preceding public artifact rather than the complete accumulated history.

### EXP-002

EXP-002 introduced stricter schema enforcement, explicit evidence provenance, and complete accumulated public history.

The canonical run stopped fail-closed at Round 2 after a validation rejection.

**EXP-002 is not a full structured-vs-structured quality comparison.** Its scientific value is as a harness-stress result that exposed validation, accounting, and forensic-persistence defects.

### EXP-003

EXP-003 used no paid model calls.

Seven deterministic conformance tests passed for the targeted semantics introduced in response to the earlier findings:

- provenance-aware evidence validation;
- content addressing;
- append-only artifact history;
- failure and termination;
- version and extension behavior;
- closure verification; and
- immutable canonical trace storage.

These tests verify the implemented research profile. They do not establish universal interoperability, security, or performance.

## Repository Map

- [`spec/PROTOCOL-DRAFT-0.1.md`](spec/PROTOCOL-DRAFT-0.1.md) — protocol research draft
- [`research/EVIDENCE_LEDGER.md`](research/EVIDENCE_LEDGER.md) — deduplicated scientific evidence
- [`research/METHODOLOGY.md`](research/METHODOLOGY.md) — experimental design and evidence policy
- [`evidence/manifest.json`](evidence/manifest.json) — cryptographic evidence lineage
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and review requirements
- [`CITATION.cff`](CITATION.cff) — citation metadata

## Evidence Policy

The project keeps several categories deliberately separate:

- harness-observed experimental facts;
- trace-verified observations;
- model-generated analysis;
- methodological limitations;
- harness failures;
- deterministic conformance results; and
- unsupported empirical-sounding model output.

A model-generated benchmark is not an experimental result merely because a model presented it as one.

The evidence ledger is the publication-facing index for these distinctions.

## Public Data Boundary

Raw canonical traces are not included in this initial public snapshot.

The repository publishes cryptographic lineage for the canonical local evidence sets. A raw or sanitized trace dataset requires a separate disclosure and privacy review before publication.

## Standards Direction

The current draft is written as a research protocol document rather than as a claim of completed standardization.

The intended progression is:

1. public technical review;
2. independent implementation feedback;
3. interoperable test vectors;
4. refinement of normative requirements;
5. specification freeze; and
6. evaluation of an appropriate standards-track venue.

The project will not treat model consensus as a substitute for implementation evidence or independent review.

## Contributing

Technical criticism is encouraged.

The highest-value contributions are those that expose ambiguity, interoperability failure, security risk, privacy leakage, or a missing conformance condition.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This repository is licensed under the Apache License 2.0.

See [`LICENSE`](LICENSE).
