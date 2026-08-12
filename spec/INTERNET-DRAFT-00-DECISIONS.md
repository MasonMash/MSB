# Internet-Draft -00 Decisions

## 1. Purpose

This document freezes the technical and publication boundaries used to author
the first MSB-derived individual Internet-Draft.

It governs preparation of revision `-00`. It is not a claim of IETF adoption,
IETF consensus, implementation maturity, or final protocol naming.

## 2. Publication Posture

| Item | Decision |
|---|---|
| Submission type | Individual Internet-Draft |
| Intended status | Experimental |
| Working title | Auditable Public Artifacts for Model-Independent Deliberation |
| Working document name | `draft-mashayekhi-auditable-model-deliberation-00` |
| Author | Mohsen Mashayekhi |
| Organization | Independent Researcher |
| Stream or working group | None claimed |
| IANA actions | None |
| Standards claim | None |
| Protocol-name freeze | Deferred |

The working document name is an IETF filename, not a final protocol brand.

## 3. Document Packaging

Revision `-00` will be one self-contained document.

The restricted canonical JSON profile will be included as normative content in
the Internet-Draft rather than being required only through a GitHub-relative
reference.

The repository may continue to maintain the canonical profile as a separate
research document and test surface.

## 4. Core Semantic Scope

Revision `-00` will define these seven public artifact types:

- `CLAIM`;
- `EVIDENCE`;
- `OBJECTION`;
- `REVISION`;
- `DECISION`;
- `FAILURE`; and
- `TERMINATION`.

The common abstract artifact members are:

- `protocol_version`;
- `artifact_id`;
- `artifact_type`;
- `payload`;
- `references`; and
- optional `extensions`.

Transport addresses, provider names, model names, prompts, tool calls, private
memory, hidden chain-of-thought, logits, activations, and model weights are not
core artifact members.

## 5. Canonical Identity

For the active `-00` profile:

- the top-level artifact value is a JSON object;
- the restricted canonical JSON profile is mandatory;
- the identifier algorithm is SHA-256;
- the identifier form is `sha256:` followed by 64 lowercase hexadecimal
  digits;
- exactly the top-level `artifact_id` member is removed for identifier
  calculation;
- nested members named `artifact_id` are retained; and
- malformed or unsupported input fails closed.

The public four-positive and eleven-negative vector suite is the initial
profile conformance suite.

Passing the suite does not establish independent interoperability.

## 6. Reference and Graph Decisions

The `-00` profile uses a directed acyclic public artifact graph.

A closure verifier MUST reject a reference cycle.

Core reference relations are:

- `supports`;
- `objects-to`;
- `revises`;
- `supersedes`;
- `considers`; and
- `decides`.

A required unavailable reference causes closure verification to fail.

Multiple concurrent graph tips are permitted.

A `REVISION` may reference multiple prior artifacts. No separate merge artifact
type is introduced in revision `-00`.

A decision declares its audited closure through references. It MUST NOT claim
closure while omitting an unresolved blocking objection reachable from that
closure.

## 7. Failure Under Partial Availability

Transport partitions and provider failures are outside the core transport
scope.

If a required artifact is unavailable, an implementation MUST NOT silently
construct a partial successful closure.

The implementation must instead produce or expose an explicit failure outcome.

Retries must not erase a canonical failure that belongs to the auditable
record.

## 8. Versioning and Extensions

The initial protocol version is `0.1`.

An implementation:

- MUST reject an unsupported major version;
- MUST NOT infer minor-version compatibility;
- MAY accept a different minor version only under an explicit compatibility
  rule;
- MUST keep extension data separate from core fields; and
- MUST NOT interpret unknown extensions as changing core semantics.

Revision `-00` defines no critical-extension mechanism and requests no
extension registry.

An extension requiring changes to core interpretation requires a later profile
revision.

## 9. Authentication and Signatures

Content addressing detects artifact-content changes. It does not authenticate
an author, authorize an action, prove model identity, or establish evidence
trustworthiness.

Artifact author authentication, signatures, key discovery, authorization, and
non-repudiation are outside the normative scope of revision `-00`.

The draft will identify these as security requirements for future profiles
rather than implying that SHA-256 provides authenticity.

## 10. Privacy Boundary

Revision `-00` standardizes the public/private boundary, not the paper's `P0`
through `P3` labels.

A conforming implementation MUST NOT require disclosure of private
chain-of-thought or private model state for interoperability.

Public artifacts may still contain sensitive information. Implementations must
apply their disclosure, minimization, authorization, and retention policies
before publication.

## 11. Conformance Claims

A conformance claim must identify its target:

1. canonical JSON and identifier conformance;
2. artifact-semantic validation conformance; or
3. closure-verification conformance.

A claim covering only the canonical profile MUST NOT be presented as complete
protocol conformance.

Independent cross-implementation interoperability remains an evidence goal,
not a prerequisite for publishing revision `-00`.

## 12. Evidence and Evaluation Claims

Revision `-00` may describe EXP-001-R2, EXP-002, and EXP-003 as experimental
background.

It must preserve these limitations:

- EXP-001-R2 used single-hop direct context;
- EXP-002 stopped fail-closed at Round 2;
- EXP-003 was deterministic prototype conformance testing;
- the public fifteen-vector suite tests one reference implementation; and
- no completed benchmark proves efficiency, accuracy, scale, privacy safety,
  or universal interoperability.

Proposed evaluation metrics from the Evdran paper remain future-work methods
unless independently executed.

## 13. Adjacent Internet-Drafts

The following active documents require informative comparison during
revision `-00` preparation:

- `draft-farley-acta-knowledge-units-00`, which defines Knowledge Units
  produced by a particular structured multi-model deliberation process;
- `draft-farley-acta-signed-receipts`, which defines signed receipts;
- `draft-ovidi-lip-4d-00`, which addresses intent context and authorization
  dialogue; and
- `draft-c4tz-marc`, which addresses control and uncertainty disclosure.

MSB differs by defining model-independent public artifact semantics,
append-only revision, explicit objections, failure and termination, and
decision closure without prescribing a fixed round sequence or knowledge-base
output format.

No claim of priority, replacement, compatibility, or endorsement is made.

## 14. Normative Reference Plan

The `-00` source will include or resolve normative references for:

- BCP 14 requirement language;
- JSON;
- UTF-8;
- Unicode NFC normalization; and
- SHA-256.

RFC 8785 will remain informative because the restricted canonical profile does
not claim JCS conformance.

Adjacent agent, deliberation, and model protocols will be informative
references.

## 15. Deferred Work

The following are explicitly deferred beyond revision `-00`:

- author-authentication and signature profiles;
- transport bindings;
- media-type registration;
- extension registry creation;
- bounded-history checkpoints;
- binary encodings;
- compact delimiter-based wire grammar;
- role-reliability scoring;
- adjudication thresholds;
- privacy-class wire labels;
- independent implementation results; and
- final protocol naming.

Deferral does not prevent these issues from being discussed in Security
Considerations, Operational Considerations, or Future Work.

## 16. Authoring Exit Criteria

Stage 4 may generate the RFCXML source only when it preserves every decision in
this document and does not silently promote deferred work into a normative
requirement.
