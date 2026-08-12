# Evdran-to-MSB Research Traceability

## 1. Purpose

This document records how concepts from the paper *Evdran Protocol: A
Standardization Proposal for Compact, Auditable, Privacy-Preserving Inter-Model
Deliberation* relate to MSB Research Draft 0.1.

The paper is a protocol position paper and standardization proposal. It does
not report a completed empirical benchmark. MSB does not treat illustrative
paper traces, proposed metrics, or model-generated design claims as measured
project evidence.

This document preserves research lineage. It does not make Evdran the final
name of a future Internet-Draft.

## 2. Concept Disposition

| Evdran concept | MSB disposition | Current MSB representation |
|---|---|---|
| Public deliberation state | Adopted | Public artifacts separated from private model computation |
| Claim | Adopted | `CLAIM` |
| Evidence vector | Adopted and generalized | `EVIDENCE` with explicit provenance |
| Objection | Adopted | `OBJECTION`, including blocking behavior |
| Delta | Adopted and generalized | `REVISION` with immutable supersession |
| Rebuttal or resolution | Transformed | Revision and explicit objection disposition in `DECISION` |
| Risk marker | Transformed | `OBJECTION`, `FAILURE`, or application policy |
| Decision | Adopted | `DECISION` with closure requirements |
| Explicit halt or error | Strengthened | `FAILURE` and `TERMINATION` |
| Typed adjudication graph | Adopted in principle | Content-addressed artifact graph and typed references |
| Minority objection preservation | Strengthened | Blocking-objection closure checks |
| Compact wire syntax | Deferred | No compact delimiter-based wire format is standardized |
| Binary encoding | Deferred | No CBOR or MessagePack binding is standardized |
| Transport bindings | Out of core scope | Transport remains independent of protocol semantics |
| Hidden-state exclusion | Adopted | Private chain-of-thought and private model state are outside the interoperability boundary |

## 3. Privacy Lineage

The paper proposed four privacy classes:

- `P0`: public problem data;
- `P1`: shared deliberation state;
- `P2`: provider-private operational state; and
- `P3`: forbidden internal model state.

MSB Research Draft 0.1 adopts the underlying boundary but does not currently
standardize these four labels as wire-level protocol values.

MSB requires that interoperability must not depend on private chain-of-thought,
hidden activations, system prompts, private memory, model weights, or
provider-private reasoning payloads.

A future profile may define explicit privacy labels only if independent
implementation experience shows that shared labels improve interoperability
without creating false assurances about data classification.

## 4. Threat-Model Lineage

The paper identified prompt injection, evidence poisoning, false consensus,
privacy leakage, role hijacking, schema ambiguity, evidence laundering,
overclaiming, tool-result instruction attacks, and model conformity.

MSB carries these concerns forward through:

- fail-closed validation;
- explicit provenance;
- immutable history;
- unresolved-objection preservation;
- explicit failure and termination;
- separation of evidence from private model state;
- extension controls; and
- security and privacy considerations.

The current draft does not claim that these mechanisms constitute a complete
adversarial-security proof. Formal threat analysis and adversarial evaluation
remain open work.

## 5. Conformance Lineage

The paper proposed levels `L0` through `L4`, ranging from human-readable
structured messages to verified implementations.

MSB does not currently adopt that level structure. The present repository
instead distinguishes:

1. restricted canonical JSON profile conformance;
2. complete protocol-semantic conformance; and
3. independent cross-implementation interoperability.

The public canonical-profile suite contains four positive and eleven negative
vectors. Passing all fifteen vectors demonstrates tested behavior of one
implementation; it does not demonstrate independent interoperability.

## 6. Evaluation Lineage

The paper proposed baselines and metrics for token use, accuracy, expert
acceptance, evidence grounding, objection resolution, minority retention,
privacy leakage, traceability, and adversarial robustness.

Those metrics remain research proposals unless executed by a reproducible
harness. MSB therefore does not report them as observed results.

Future evaluation should preserve the paper's reporting requirements where
applicable, including model identity, tokenizer, dataset, protocol version,
orchestration policy, message count, token count, latency, invalid-message
rate, privacy violations, and decision-quality method.

## 7. Related Work Lineage

The paper positioned the proposal relative to:

- KQML and FIPA-ACL as historical agent-communication languages;
- natural-language multi-agent debate;
- CIPHER as embedding-mediated debate;
- G2CP as graph-grounded communication;
- MCP as a tool, resource, prompt, and context protocol;
- A2A as application-level agent interoperability; and
- ACP as an agent communication layer.

MSB occupies a narrower layer: the semantics and auditability of public
deliberation artifacts. It does not replace those protocols.

References selected for a future Internet-Draft must be independently checked
for bibliographic accuracy, current status, and normative relevance before
submission.

## 8. Material Not Yet Standardized

The following paper concepts are intentionally not represented as completed
MSB requirements:

- compact delimiter-based wire grammar;
- session dictionaries or binary encoding;
- `L0` through `L4` conformance labels;
- role-reliability scoring;
- adjudication thresholds;
- empirical superiority claims;
- token-reduction claims;
- accuracy claims;
- zero-leakage claims outside tested conditions; and
- a final protocol name.

These items require evidence, implementation experience, or explicit scope
decisions before specification freeze.

## 9. Publication Boundary

The Evdran paper and MSB repository are related but distinct publications.

The paper provides motivation, design lineage, related work, and proposed
evaluation methods. MSB Research Draft 0.1 defines the current experimental
public-artifact contract and records only evidence supported by the project
ledger.

A future Internet-Draft may draw from both sources, but every normative
requirement must be reconciled with the implemented profile, public test
vectors, security analysis, and available interoperability evidence.
