# MSB

**A research project for interoperable, auditable deliberation between heterogeneous AI models.**

MSB studies the minimum public record that heterogeneous AI systems may need in order to inspect, challenge, revise, and audit one another's contributions without exposing private reasoning.

The project is a research and experimental environment. It is not an adopted standard, an IETF publication, or a claim that the current artifact model is final.

## What MSB Is

MSB investigates how independently implemented AI systems could share an auditable deliberation state across differences in provider, architecture, model family, orchestration framework, and private reasoning format.

The project currently has three distinct layers:

| Layer | Meaning | Current status |
|---|---|---|
| MSB | The research project and public repository | Active research |
| Current research profile | Candidate artifact semantics and technical contracts used to test the research thesis | Experimental |
| Future standards proposal | A possible independently named interoperability specification derived from sufficient evidence | Not yet authored or submitted |

Keeping these layers separate prevents experimental design choices from being mistaken for settled standards requirements.

## Research Question

Can heterogeneous AI systems participate in a shared deliberation whose public record allows an independent reviewer to determine:

- what was claimed;
- what evidence supported the claim;
- what was challenged;
- what changed after the challenge;
- which objections remain unresolved;
- what failures occurred;
- whether termination was legitimate; and
- why a decision does or does not follow from the public record?

The reviewer should not require access to private chain-of-thought, hidden state, system prompts, model weights, private memory, or provider-specific reasoning payloads.

## Why Message Transport Is Not Enough

A multi-model system can exchange text or invoke tools without sharing stable semantics for deliberation.

A conventional transcript does not inherently define:

- immutable artifact identity;
- evidence provenance;
- explicit challenge relationships;
- revision without historical mutation;
- machine-verifiable failure states;
- terminal-state semantics;
- unresolved-objection handling; or
- verifiable closure over the public record.

Transport interoperability therefore does not automatically produce deliberation interoperability. MSB studies whether a narrow public-artifact contract can bridge that gap.

## Public Study Model

The intended boundary is deliberately narrow:

~~~text
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
~~~

Models may differ internally at every step above the public-artifact boundary. The design under study concerns public artifacts, not private reasoning traces.

A participating implementation may use arbitrary private computation to produce an artifact. Interoperability should depend only on the public contract and should never require disclosure of private chain-of-thought.

## Candidate Artifact Lifecycle

The current research profile studies seven candidate public-artifact semantics:

| Candidate semantic | Research role | Current status |
|---|---|---|
| `CLAIM` | Introduces a proposition that can be supported, challenged, revised, or decided | Specified in Research Draft 0.1 |
| `EVIDENCE` | Provides public support with explicit provenance | Specified in Research Draft 0.1 |
| `OBJECTION` | Challenges an artifact or protocol assumption and may be blocking | Specified in Research Draft 0.1 |
| `REVISION` | Creates a new public position without mutating history | Specified in Research Draft 0.1 |
| `DECISION` | Records an outcome, its public basis, and objection dispositions | Specified in Research Draft 0.1 |
| `FAILURE` | Records why normal progression could not continue | Specified in Research Draft 0.1 |
| `TERMINATION` | Records an explicit terminal outcome | Specified in Research Draft 0.1 |

A representative lifecycle is:

~~~text
CLAIM
  +-- EVIDENCE
  +-- OBJECTION
        +-- REVISION
              +-- EVIDENCE
                    +-- DECISION
                          +-- TERMINATION
~~~

`FAILURE` may terminate or interrupt the lifecycle when validation, execution, authorization, resource, or protocol conditions prevent normal continuation.

These semantics are candidates in the current profile. They are not asserted to be the final vocabulary of a future standards proposal.

## Current Research Profile

Research Draft 0.1 studies a public artifact graph with:

- candidate claim, evidence, objection, revision, decision, failure, and termination semantics;
- explicit evidence provenance;
- content-addressed artifact identity;
- append-only history;
- versioned extensions;
- fail-closed validation;
- explicit terminal states; and
- decision-closure checks for unresolved blocking objections.

The research profile separates two different provenance concerns:

| Provenance level | Purpose |
|---|---|
| Artifact-level provenance | Classifies support carried by a public deliberation artifact |
| Research/publication evidence class | Classifies what the project may responsibly claim from experiments, traces, model analysis, failures, and deterministic tests |

These taxonomies operate at different levels and should not be treated as a single vocabulary.

The artifact-level classes currently defined by the research draft are:

- `TRACE_VERIFIED_OBSERVATION`
- `MODEL_GENERATED_ANALYSIS`
- `EXTERNAL_EVIDENCE`
- `HYPOTHESIS`

The publication-facing distinctions are documented in the [Evidence Ledger](research/EVIDENCE_LEDGER.md) and [Methodology](research/METHODOLOGY.md).

## What Is Implemented Today

The repository's current public implementation surface is intentionally narrower than the complete research draft.

| Capability | Repository status | Evidence boundary |
|---|---|---|
| Restricted canonical JSON profile | Implemented | Defined in the canonical profile |
| Deterministic canonical serialization | Implemented in `tools/msb_verify.py` | Profile-level behavior |
| SHA-256-based `artifact_id` calculation | Implemented in `tools/msb_verify.py` | Profile-level behavior |
| `artifact_id` verification | Implemented in `tools/msb_verify.py` | Profile-level behavior |
| Positive canonical JSON vectors | Four public input/canonical/identifier triplets | All four pass the public profile runner |
| Negative canonical JSON vectors | Eleven rejection vectors | All eleven pass with the expected error classes |
| Full seven-semantic protocol verifier | Not currently provided as a public repository tool | Must not be inferred from `msb_verify.py` |
| Independent implementation | Not yet available | Interoperability remains unproven |
| Cross-implementation testing | Not yet performed | Required before stronger interoperability claims |

The current verifier calculates or checks canonical identifiers. Its existence does not mean that every semantic rule in Research Draft 0.1 is enforced by a single public tool.

## Evidence and Limitations

Three study stages inform the current research profile.

| Study | Observed result | Responsible interpretation |
|---|---|---|
| `EXP-001-R2` | A heterogeneous twelve-round panel completed 12 of 12 planned calls | Structured public artifacts carried proposals, objections, revisions, and judgment; the direct context was single-hop |
| `EXP-002` | The canonical run stopped fail-closed at Round 2 after schema rejection | A harness-stress result that exposed validation, accounting, and forensic-persistence defects; not a complete quality comparison |
| `EXP-003` | Seven targeted deterministic conformance groups passed with no paid model calls | Verification of tested behavior in the implemented research profile; not proof of universal interoperability, security, scale, or performance |

The evidence base currently supports continued research and publication of an experimental research draft. It does not establish:

- independent cross-implementation interoperability;
- adversarial security;
- privacy safety across deployments;
- scalability;
- statistical performance;
- token efficiency;
- universal model compatibility; or
- readiness as a completed standard.

Historical experimental evidence and the repository's current public implementation are also distinct:

| Evidence surface | Meaning |
|---|---|
| Historical `EXP-003` result | Tested behavior of the prototype used in that experiment |
| Current `msb_verify.py` | Restricted canonical JSON and identifier implementation |
| Current public vectors | Four positive and eleven negative canonical-profile vectors |
| Independent interoperability evidence | Not yet available |

Model-generated quantitative language is not treated as empirical evidence unless the harness actually executed and recorded the claimed measurement.

Raw canonical traces are not included in the initial public snapshot. The repository publishes cryptographic lineage for canonical local evidence sets. Publishing raw or sanitized traces requires a separate disclosure and privacy review.

## What MSB Is Not

MSB is not intended to be:

- an agent framework;
- a workflow engine;
- an MCP replacement;
- a tool-calling protocol;
- a model-control API;
- a transport protocol;
- a hidden language between models;
- a mechanism for extracting private chain-of-thought;
- a guarantee of factual correctness or agreement; or
- a completed consensus or security system.

Existing systems may transport or process candidate MSB artifacts, but those systems remain outside the core research scope.

## From Research to a Future Standards Proposal

The project's next controlled objective is to complete and internally reconcile the public GitHub repository across:

- research narrative;
- specification language;
- evidence classification;
- canonical representation;
- verifier behavior;
- test vectors;
- security and privacy analysis; and
- contribution and review guidance.

After that repository phase is complete, the project intends to author and publish its own independently named Internet-Draft `-00`.

Publication of an Internet-Draft would begin public standards discussion. It would not imply IETF endorsement, adoption, consensus, or standards status.

Progress toward that draft is evidence-gated:

| Gate | Required outcome |
|---|---|
| Repository consistency | Narrative, specification, evidence, implementation, and tests do not contradict one another |
| Canonical profile completeness | Positive and negative vectors cover the stated representation contract |
| Independent implementation readiness | Another implementation can be built without private assumptions |
| Interoperability evidence | Independent implementations exchange and verify compatible artifacts |
| Security and privacy review | Threats, leakage boundaries, abuse cases, and mitigations are documented |
| Naming review | Repository naming history and current protocol-name conflicts are reviewed before draft naming |
| Draft preparation | Scope and normative requirements are supported by available evidence |
| Submission | An independently named Internet-Draft `-00` is authored and published by the project |

The future proposal's name, final vocabulary, conformance structure, and standards path remain open until the relevant evidence and review gates are satisfied.

## Open Research Questions

Current open questions include:

- Is the seven-semantic artifact model minimal, excessive, or incomplete?
- Which references are required for independently verifiable closure?
- How should authority, adjudication, and conflicting decisions be represented?
- Which objections must block closure?
- What privacy classifications are required at the public boundary?
- How should malicious, misleading, or low-quality artifacts be handled?
- Which extension rules preserve interoperability across versions?
- What conformance roles and levels are justified by implementation evidence?
- How should transports carry artifacts without redefining their semantics?
- What test corpus is sufficient for independent implementation?
- What measurements are needed before making efficiency or scalability claims?

## Repository Map

| Path | Purpose |
|---|---|
| [`spec/PROTOCOL-DRAFT-0.1.md`](spec/PROTOCOL-DRAFT-0.1.md) | Experimental protocol research draft |
| [`spec/CANONICAL-JSON-PROFILE-0.1.md`](spec/CANONICAL-JSON-PROFILE-0.1.md) | Restricted canonical JSON and identifier profile |
| [`tools/msb_verify.py`](tools/msb_verify.py) | Reference canonicalization and `artifact_id` tool |
| [`test-vectors/`](test-vectors/) | Public canonical-profile test inputs |
| [`research/EVIDENCE_LEDGER.md`](research/EVIDENCE_LEDGER.md) | Deduplicated publication-facing evidence |
| [`research/METHODOLOGY.md`](research/METHODOLOGY.md) | Experimental design and evidence policy |
| [`research/EVDRAN-TO-MSB-TRACEABILITY.md`](research/EVDRAN-TO-MSB-TRACEABILITY.md) | Research lineage and disposition of the Evdran paper concepts |
| [`evidence/manifest.json`](evidence/manifest.json) | Cryptographic evidence lineage |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution and review requirements |
| [`CITATION.cff`](CITATION.cff) | Citation metadata |

## Contributing

Technical criticism is encouraged.

The highest-value contributions are those that expose ambiguity, interoperability failure, security risk, privacy leakage, unsupported claims, or missing conformance conditions.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

This repository is licensed under the Apache License 2.0.

See [`LICENSE`](LICENSE).
