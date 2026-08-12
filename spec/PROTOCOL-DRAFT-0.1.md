# Model-Independent Structured Deliberation Protocol

## Research Draft 0.1

- **Status:** Experimental Research Draft
- **Author:** Mohsen Mashayekhi
- **Date:** 11 August 2026
- **Intended use:** Open technical review and interoperability research

This document is not an adopted Internet Standard, IETF Internet-Draft, or standards-body publication.

---

## Abstract

AI systems can exchange messages, invoke tools, and participate in shared workflows without agreeing on how a deliberation itself is represented.

That distinction matters when heterogeneous models must challenge one another, revise claims, evaluate evidence, and reach decisions that remain auditable after the models, providers, or orchestration systems are no longer available.

This document defines a research protocol for representing deliberation as a graph of immutable public artifacts. The protocol separates interoperable public state from private model computation. It does not require, transport, or standardize chain-of-thought, hidden model state, system prompts, private memory, or model weights.

The draft defines semantics for claims, evidence, objections, revisions, decisions, failures, termination, content-addressed identity, append-only history, evidence provenance, versioned extensions, and decision closure.

The goal is not to standardize how models think. The goal is to standardize the minimum public record required for one implementation to inspect and challenge another.

## 1. Introduction

### 1.1 Problem Statement

Interoperability at the messaging layer does not imply interoperability at the deliberation layer.

A system may successfully deliver a message from Model A to Model B while leaving fundamental questions undefined:

- Is the message a claim, evidence, or objection?
- What prior artifact does it challenge?
- Is the evidence observed, external, hypothetical, or model-generated?
- Has a prior claim been mutated or superseded?
- Which objections remain blocking?
- Is a final decision actually closed over the public record?
- Did the process complete, fail, deadlock, or merely stop?

When these semantics exist only in prompts, orchestration code, or conversational convention, an independent implementation cannot reliably reconstruct the deliberation.

This draft defines a public artifact layer for that purpose.

### 1.2 Protocol Objective

A conforming deliberation should produce a public record from which an independent reviewer can determine:

1. what propositions were introduced;
2. what evidence was offered;
3. what objections were raised;
4. how claims changed;
5. what failures occurred;
6. whether termination was legitimate; and
7. why the final decision is or is not supported by the public record.

No requirement depends on access to private model reasoning.

### 1.3 Scope

This draft specifies protocol semantics and conformance invariants.

It does not standardize:

- transport;
- model inference;
- agent orchestration;
- tool execution;
- prompt construction;
- model selection;
- provider authentication; or
- private reasoning representation.

Any transport capable of preserving the required public artifacts may carry the protocol.

### 1.4 Non-Goals

The protocol does not attempt to:

- expose chain-of-thought;
- make models deterministic;
- guarantee agreement;
- guarantee factual correctness;
- replace security policy;
- replace authorization systems;
- define a universal agent runtime; or
- establish a consensus algorithm for arbitrary distributed systems.

Disagreement and non-convergence are valid protocol outcomes.

## 2. Conventions and Terminology

### 2.1 Requirement Language

Uppercase normative terms such as `MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `RECOMMENDED`, `NOT RECOMMENDED`, `MAY`, and `OPTIONAL` follow BCP 14 as defined by [RFC2119] and clarified by [RFC8174].

Lowercase uses of those words are descriptive rather than normative unless the surrounding text explicitly states otherwise.

Because this is a research draft, normative language defines the intended conformance contract of this document; it does not imply adoption by a standards body.

### 2.2 Public Artifact

A **public artifact** is an inspectable protocol object intended to cross the interoperability boundary.

A public artifact is not a transcript of private model cognition.

### 2.3 Private Model State

Private model state includes implementation-internal material that the protocol does not require for interoperability, including:

- chain-of-thought;
- hidden activations or state;
- system prompts;
- private memory;
- model weights; and
- provider-specific private reasoning payloads.

### 2.4 Deliberation

A **deliberation** is a set of public artifacts and references whose semantics permit claims to be challenged, revised, and decided.

### 2.5 Closure

**Closure** is the set of artifacts transitively reachable from the declared decision or tip set through protocol references.

## 3. Architectural Invariant

The core interoperability invariant is:

> A decision MUST be auditable from public artifacts without requiring private model state.

An implementation MAY use arbitrary private computation to produce an artifact.

An implementation MUST NOT require another participant to disclose private chain-of-thought as a condition of protocol interoperability.

## 4. Core Artifact Semantics

### 4.1 CLAIM

A `CLAIM` introduces a public proposition that can be referenced, supported, challenged, revised, or decided upon.

A claim SHOULD be specific enough that another participant can identify what is being contested.

### 4.2 EVIDENCE

An `EVIDENCE` artifact provides public support relevant to one or more claims.

Evidence MUST carry explicit provenance classification.

The research profile defines four provenance classes:

- `TRACE_VERIFIED_OBSERVATION`
- `MODEL_GENERATED_ANALYSIS`
- `EXTERNAL_EVIDENCE`
- `HYPOTHESIS`

A model-generated analysis does not become an observed fact merely because it contains numbers, a simulation, or benchmark-like language.

### 4.3 OBJECTION

An `OBJECTION` records a challenge to a claim, evidence item, revision, decision, or protocol assumption.

An objection MAY be marked blocking.

A blocking objection MUST either receive a public disposition or remain visible as unresolved when a decision is issued.

### 4.4 REVISION

A `REVISION` represents a change to a prior public position.

A revision MUST create a new artifact.

It MUST NOT mutate the historical artifact it revises.

The revision SHOULD reference the artifact or artifacts that it supersedes or modifies.

### 4.5 DECISION

A `DECISION` records a public disposition over the deliberation state.

A decision SHOULD identify:

- the outcome;
- the public basis;
- relevant artifact references;
- dispositions of blocking objections; and
- unresolved issues.

A decision MUST NOT claim closure while silently omitting a blocking objection reachable from its declared closure set.

### 4.6 FAILURE

A `FAILURE` records that a requested protocol operation could not be completed.

The research profile includes failure classes for:

- malformed artifacts;
- unsupported versions;
- unsupported extensions;
- unresolved references;
- integrity failures;
- policy refusals;
- capability limits;
- timeouts; and
- resource limits.

Failure is a protocol outcome. It MUST NOT be silently converted into success.

### 4.7 TERMINATION

A `TERMINATION` artifact records the terminal state of a deliberation.

The research profile distinguishes:

- `completed`
- `suspended`
- `cancelled`
- `deadlock`
- `exhausted`

A `completed` termination MUST identify a final decision.

A `deadlock` or `exhausted` termination MUST preserve the unresolved blocking objections relevant to termination.

### 4.8 Abstract Artifact Model

The core protocol is defined as an abstract data model rather than as a transport-specific wire format.

A published artifact in the current research profile consists conceptually of:

- `protocol_version` — identifies the protocol profile under which the artifact is interpreted;
- `artifact_id` — binds the published artifact to its content-addressed identity when the active profile requires content addressing;
- `artifact_type` — identifies the core semantic type;
- `payload` — contains type-specific public data;
- `references` — contains zero or more references to other public artifacts; and
- `extensions` — optionally contains namespaced extension data.

A profile MAY define additional metadata, but additional metadata MUST NOT silently change the semantics of a core artifact field.

The abstract model intentionally does not require transport addresses, provider identifiers, model names, or tool invocation metadata as core protocol fields.

#### 4.8.1 References

A reference MUST identify a target artifact.

A reference MAY also identify a semantic relation between the source and target artifacts.

A reference relation does not replace artifact-type semantics. For example, an `OBJECTION` remains an objection even when a relation identifies the claim to which it objects.

#### 4.8.2 Extensions

Extension data MUST be distinguishable from core protocol fields.

Unknown extension data MUST NOT be interpreted as modifying core semantics unless the active compatibility profile explicitly permits that interpretation.

### 4.9 Processing Model

A conforming implementation is expected to process public artifacts through an explicit validation boundary.

The current research profile follows this conceptual sequence:

1. Produce a public artifact from private computation.
2. Apply the privacy boundary before persistence or forwarding.
3. Validate core structure and artifact semantics.
4. Validate evidence provenance where evidence is present.
5. Validate version and extension compatibility.
6. Derive or verify content-addressed identity under the active identity profile.
7. Append the artifact without mutating prior history.
8. Resolve required references.
9. Evaluate blocking objections and closure before final decision completion.
10. Represent failure or termination explicitly when processing cannot continue.

An implementation MAY combine these operations internally.

It MUST preserve the externally observable invariants defined by the active protocol profile.

## 5. Artifact Identity

### 5.1 Content Addressing

A protocol profile SHOULD provide a deterministic method of deriving artifact identity from artifact content.

The active research profile computes a SHA-256 digest over the restricted canonical JSON representation defined by [MSB Restricted Canonical JSON Profile 0.1](CANONICAL-JSON-PROFILE-0.1.md). The identifier calculation removes exactly the top-level `artifact_id` member before canonicalization.

The identifier form for that profile is:

`sha256:<64-lowercase-hex>`

The canonical JSON profile is the controlling specification for identifier calculation and verification. The earlier experimental `urn:sdap:sha256:` form is not used by this profile.

### 5.2 Restricted Canonical JSON Profile

The complete serialization, normalization, member-ordering, duplicate-key, normalization-collision, numeric-domain, encoding, and failure requirements are defined by [MSB Restricted Canonical JSON Profile 0.1](CANONICAL-JSON-PROFILE-0.1.md).

This restricted profile is not a claim of compatibility with RFC 8785 JSON Canonicalization Scheme.

Independent positive and negative test vectors are required before the profile is treated as an interoperability result.

## 6. Immutable History

An artifact identifier MUST bind to one artifact body.

Once accepted into an append-only history, an artifact MUST NOT be silently replaced.

An implementation MAY treat an identical re-submission as idempotent.

A changed artifact body MUST receive a new identity.

Corrections and updates MUST be represented as new artifacts with explicit references to prior artifacts.

## 7. References

A protocol reference identifies another public artifact and MAY additionally identify the semantic relationship to that artifact.

Examples of relations include:

- supports;
- objects-to;
- revises;
- supersedes;
- considers; and
- decides.

The final vocabulary remains open to review.

An implementation performing closure verification MUST detect references to unavailable artifacts.

## 8. Decision Closure

A verifier evaluates a decision against the transitive closure of its declared artifact references.

A closure calculation MUST fail if a required referenced artifact is unavailable.

The current prototype rejects reference cycles during closure calculation. Whether all cycles are invalid at the protocol level remains an open design question.

A final decision MUST NOT hide unresolved blocking objections that are within its audited closure.

## 9. Evidence Provenance

### 9.1 Trace-Verified Observation

`TRACE_VERIFIED_OBSERVATION` identifies evidence directly supported by an explicitly admitted execution or trace source.

The evidence MUST reference an admissible source identifier.

### 9.2 External Evidence

`EXTERNAL_EVIDENCE` identifies evidence supplied from outside the deliberation.

The evidence MUST reference an explicit external source admitted by the protocol context or experiment.

### 9.3 Model-Generated Analysis

`MODEL_GENERATED_ANALYSIS` identifies calculations, critiques, proof sketches, simulations, estimates, or other analytical products generated by a participant.

Such material MAY be useful and MAY contain quantitative content.

It MUST NOT be represented as independently observed empirical evidence unless separately grounded.

### 9.4 Hypothesis

`HYPOTHESIS` identifies a proposition offered for future validation rather than as an observed result.

### 9.5 Empirical Claims

A benchmark, simulation result, accuracy claim, latency claim, or percentage MUST NOT be promoted to trace-verified or external empirical evidence without an admissible source.

Classification is a provenance property, not a lexical property.

## 10. Failure and Recovery

A protocol participant SHOULD distinguish protocol failure from transport failure.

Examples include:

- valid artifact rejected by a local policy;
- malformed public artifact;
- unavailable reference;
- model provider timeout;
- unsupported protocol version; and
- deliberation deadlock.

A retry MUST NOT silently erase the existence of a prior canonical failure when that failure is part of an auditable research or operational record.

## 11. Versioning

The research profile uses major and minor version components.

A participant:

- MUST reject an unsupported major version;
- MAY accept a different minor version when the applicable compatibility profile permits it;
- MUST preserve unknown extensions when the profile requires transparent forwarding; and
- MUST NOT interpret unknown extensions as changing core semantics without an explicit compatibility rule.

The final standards-track version requires a complete compatibility matrix before protocol freeze.

## 12. Extensions

Extensions MUST be namespaced under the current restricted profile.

An unknown namespaced extension MAY be preserved without interpretation when doing so cannot alter the meaning of a core protocol artifact.

A future specification will need to define:

- namespace ownership;
- collision handling;
- critical versus non-critical extensions;
- extension discovery; and
- registration policy.

## 13. Conformance

A conforming implementation of the current research profile MUST demonstrate, at minimum:

1. provenance-aware evidence validation;
2. deterministic artifact identity;
3. append-only artifact history;
4. explicit failure semantics;
5. explicit termination semantics;
6. major-version rejection behavior;
7. namespaced extension handling;
8. missing-reference detection;
9. blocking-objection closure checks; and
10. protection against silent overwrite of canonical trace artifacts where traces are used as evidence.

The EXP-003 prototype currently exercises seven grouped deterministic tests covering these areas.

Passing those tests does not establish interoperability with an independent implementation.

## 14. Security Considerations

Structured deliberation introduces security properties that do not disappear merely because the artifact format is public.

A production profile will need to address at least:

- artifact forgery;
- author impersonation;
- replay;
- equivocation;
- malicious references;
- provenance spoofing;
- prompt injection carried as evidence;
- denial of service through unbounded artifact graphs;
- adversarial extension use;
- decision manipulation through omitted artifacts; and
- trust assumptions around external evidence.

Content addressing provides integrity detection for artifact content but does not by itself establish author identity, authorization, or trustworthiness.

Those properties require separate mechanisms.

## 15. Privacy Considerations

The protocol is designed to minimize the information required to cross the model boundary.

A conforming interoperability profile MUST NOT require disclosure of private chain-of-thought.

Implementations SHOULD minimize unnecessary provider metadata and SHOULD apply an explicit sanitization boundary before persisting model responses as public artifacts.

A public artifact can still contain sensitive user information even when it contains no chain-of-thought. Application-level data minimization and disclosure policy therefore remain necessary.

## 16. Operational Considerations

Implementations should place explicit limits on:

- artifact size;
- graph depth;
- total closure size;
- reference fan-out;
- retry behavior; and
- resource consumption.

Failure caused by such a limit SHOULD be represented explicitly rather than appearing as silent truncation.

## 17. IANA Considerations

This research draft requests no IANA actions.

The experimental identifier prefix used by the prototype is not presented as an IANA-registered namespace.

Any future request for registries, media types, URI schemes, or protocol parameters would require a separate standards-track analysis.

## 18. Experimental Evidence

The current protocol draft was informed by three study stages.

EXP-001-R2 completed a heterogeneous twelve-round public-artifact relay but used single-hop direct history.

EXP-002 introduced complete accumulated public history and stricter validation but stopped fail-closed at Round 2. It is not a full structured-vs-structured quality comparison.

EXP-003 performed targeted deterministic conformance validation without paid model execution.

The evidence is documented separately in the research ledger.

Experimental evidence is informative. Protocol requirements are not considered proven solely because one or more models proposed or endorsed them.

## 19. Open Issues

Before a standards-track freeze, the project should resolve at least:

1. final canonical serialization;
2. artifact author authentication;
3. signature and verification profiles;
4. reference-cycle semantics;
5. concurrent branches and merge behavior;
6. partition behavior;
7. bounded-history and checkpoint profiles;
8. extension registration;
9. transport bindings;
10. external evidence trust semantics;
11. independent implementation test vectors; and
12. formal threat analysis.

## 20. References

### 20.1 Normative References

**[RFC2119]** Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

**[RFC8174]** Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017.

### 20.2 Informative References

**[RFC8785]** Rundgren, A., Jordan, B., and S. Erdtman, "JSON Canonicalization Scheme (JCS)", RFC 8785, June 2020.

The current prototype does not claim RFC 8785 conformance.

## 21. Document Status

Research Draft 0.1 is a protocol-design artifact intended for public review.

It should be read as a precise statement of the current research profile, not as a declaration that the interoperability problem is solved.

The next meaningful milestone is independent implementation and cross-implementation conformance evidence.
