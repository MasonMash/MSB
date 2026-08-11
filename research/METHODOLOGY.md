# Research Methodology

## 1. Research Question

The study asks whether heterogeneous AI models can participate in a structured, auditable deliberation through public artifacts without requiring access to private chain-of-thought or other internal model state.

The study is concerned with the interoperability boundary, not with reproducing a model's private reasoning process.

## 2. Research Object

The object under study is a protocol abstraction with the following intended properties:

- model independence;
- provider independence;
- transport independence;
- explicit public semantics;
- auditable history;
- evidence provenance;
- privacy-preserving model boundaries; and
- machine-verifiable conformance conditions.

The protocol is intentionally distinct from agent frameworks, tool protocols, orchestration systems, and transport APIs.

## 3. Evidence Model

The methodology separates evidence by origin.

### 3.1 Harness-Observed Facts

Harness-observed facts include:

- execution status;
- model and role identity;
- token usage;
- provider-reported cost;
- measured latency;
- persisted trace structure;
- trace hashes;
- privacy-field storage checks; and
- deterministic local test results.

These may be reported as observations when directly supported by the stored execution record.

### 3.2 Trace-Verified Observations

A trace-verified observation is derived by deterministic inspection of canonical public artifacts.

Examples include:

- a missing required field;
- the number and form of artifact identifiers; and
- the presence or absence of a referenced public artifact.

### 3.3 Model-Generated Analysis

Model-generated analysis includes:

- protocol proposals;
- objections;
- critiques;
- threat hypotheses;
- proof sketches;
- estimates;
- simulations;
- synthesis; and
- decision recommendations.

These outputs are design evidence.

They are not automatically empirical evidence.

### 3.4 Unsupported Empirical-Sounding Output

Models can produce benchmark language, percentages, accuracy figures, latency estimates, or simulation results that were never measured by the experimental harness.

Such content is explicitly excluded from empirical findings unless it is independently grounded.

This distinction is essential to the validity of the publication.

## 4. Privacy Boundary

The experiments are designed around public artifacts.

The persisted scientific record must not depend on storage of:

- chain-of-thought;
- hidden state;
- private model memory;
- system prompts;
- model weights; or
- encrypted private reasoning payloads presented as deliberation content.

Provider-level aggregate usage metadata may be retained when it does not expose private reasoning content.

## 5. Experiment Series

### 5.1 EXP-001-R2 — Heterogeneous Structured Relay

EXP-001-R2 used a twelve-round heterogeneous panel with fixed roles.

Every round received:

- the research problem;
- success criteria;
- output requirements;
- privacy requirements; and
- the immediately preceding public artifact.

The run completed 12 of 12 planned model calls.

#### Limitation

The direct context was single-hop.

Later participants did not directly receive the complete accumulated artifact history.

Therefore EXP-001-R2 must not be interpreted as a full-history deliberation experiment.

### 5.2 EXP-002 — Strict Provenance and Full-History Stress Attempt

EXP-002 retained the research objective and heterogeneous panel while introducing:

- strict top-level schema validation;
- explicit evidence provenance;
- complete accumulated public-artifact history; and
- fail-closed validation.

The canonical run stopped after Round 2 produced a schema rejection.

The rejection was retained as the scientific outcome.

There was no automatic replacement run.

#### Interpretation

EXP-002 is not a full structured-vs-structured quality comparison.

It is useful because it exposed defects in the experimental control plane before those defects could silently influence a larger run.

### 5.3 EXP-003 — Targeted Deterministic Conformance

EXP-003 converted the concrete unresolved protocol and harness issues into deterministic tests.

No model provider was called.

Seven grouped conformance checks passed.

The experiment therefore answers a narrower but stronger question than another model panel would have answered: whether the implemented draft semantics exhibit the specific targeted behaviors under deterministic local tests.

## 6. Fail-Closed Research Policy

A failed canonical run is evidence.

It is not a disposable attempt.

The methodology therefore distinguishes:

- scientific failure;
- provider or transport failure;
- schema rejection;
- non-convergence;
- disagreement; and
- negative final decisions.

A retry must not silently erase a prior canonical failure.

## 7. Cost and Replication Policy

The project does not use repeated paid model execution as a substitute for a clear research question.

For Research Draft 0.1, the paid multi-model phase is closed.

Further stochastic replication is justified only when a future claim requires repeated samples, statistical comparison, or cross-run stability evidence.

## 8. Deduplication

The immutable traces preserve every public artifact.

The publication ledger does not count repeated semantic statements as independent findings.

For example, if several models independently restate the same immutability defect, the final ledger records one finding with the appropriate provenance rather than inflating the apparent evidence count.

## 9. Reproducibility

The initial public repository contains:

- the protocol research draft;
- the methodology;
- the deduplicated evidence ledger; and
- a cryptographic evidence manifest.

The raw traces remain outside the initial publication boundary pending a separate disclosure review.

The evidence manifest allows later publication of a reviewed dataset without silently changing the lineage of the source evidence.

## 10. Threats to Validity

The present study has several explicit limitations.

### 10.1 Single-Run Heterogeneous Panel

EXP-001-R2 is one canonical execution, not a statistical sample.

### 10.2 Single-Hop Context in EXP-001-R2

Direct accumulated-history reasoning was not tested by the completed twelve-round run.

### 10.3 Incomplete EXP-002 Deliberation

EXP-002 stopped at Round 2 and cannot support comparative claims about final deliberation quality.

### 10.4 Model-Generated Design Evidence

Model agreement is not independent empirical verification.

### 10.5 Prototype Conformance

EXP-003 validates the tested prototype semantics. It does not establish interoperability with an independently developed implementation.

### 10.6 Unmeasured Security and Scale

The current work does not claim adversarial robustness, large-scale graph performance, or production security.

## 11. Study Stop Condition

The experimental phase supporting Research Draft 0.1 ends after:

1. EXP-001-R2 evidence classification;
2. EXP-002 fail-closed root-cause analysis;
3. EXP-003 targeted deterministic conformance;
4. evidence-ledger construction; and
5. protocol-draft publication preparation.

The next research milestone is independent technical review and implementation, not another unrestricted multi-model panel.
