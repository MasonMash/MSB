# Evaluation Plan

## Status

This document defines future experiments. It does not report completed results
and does not convert hypotheses into evidence.

## Evaluation Questions

The evaluation program should determine whether typed shared artifacts improve:

- independent reconstruction of a decision;
- evidence grounding;
- objection visibility and resolution;
- retention of valid minority objections;
- privacy-boundary compliance;
- robustness to malicious or low-quality participants;
- deterministic cross-implementation processing; and
- token and latency cost under comparable task conditions.

## Baselines

At minimum, experiments should compare:

1. unstructured natural-language deliberation;
2. structured natural-language messages;
3. the JSON artifact profile;
4. any proposed compact textual encoding; and
5. a single-model or single-agent control where applicable.

A compact format must not be compared only against an artificially verbose
baseline.

## Task Suites

Task suites should include:

- factual synthesis with attributable sources;
- requirements analysis;
- software or protocol design review;
- conflicting-evidence resolution;
- safety and risk assessment;
- adversarial evidence injection;
- incomplete-reference and partial-availability cases; and
- privacy-sensitive cases containing material that must not be disclosed.

Tasks, expected outcomes, scoring rules, and exclusions must be frozen before
the evaluated run.

## Metrics

### Token cost

Report input, output, and total tokens by participant and by round. Include
encoding overhead and any decoder or reporting pass.

### Decision accuracy

Use task-specific externally defined scoring. Do not let the participating
models define their own ground truth after seeing the run.

### Evidence grounding

Measure whether material claims identify admissible supporting evidence and
whether references resolve to the expected artifact content.

### Objection resolution

Report the proportion of blocking objections that receive an explicit,
inspectable disposition. Silence is not resolution.

### Minority-objection retention

Measure whether a valid minority objection remains reachable from the final
decision closure even when most participants disagree with it.

### Privacy leakage

Report shared artifacts containing prohibited test material divided by all
shared artifacts. The acceptable target for deliberately seeded P2/P3 test
material is zero leakage.

### Traceability

Measure whether an independent reviewer can reconstruct claims, evidence,
objections, revisions, failures, and the basis of the decision from admitted
artifacts alone.

### Robustness to a bad participant

Measure the effect of prompt injection, fabricated provenance, repeated replay,
reference flooding, policy-mutation attempts, and strategically omitted
objections.

### Interoperability

Two independently developed implementations should parse, canonicalize,
identify, reject, and verify the same vectors without sharing private code or
undocumented assumptions.

## Experimental Controls

Each experiment should record:

- protocol and implementation versions;
- model and provider versions where disclosure is permitted;
- prompts and policies or a cryptographic commitment to restricted material;
- task corpus version;
- random seeds and sampling policy;
- token and time budgets;
- retry and failure policy;
- artifact and trace hashes;
- exclusions and invalid runs; and
- evaluator identity and procedure.

Runs must preserve failures. Retrying must not silently replace a failed
canonical record.

## Statistical Reporting

Where a metric is stochastic, report sample size, distribution or confidence
intervals, and all predeclared exclusions. A single successful trace must not
be presented as a general performance result.

## Security and Privacy Review

Before publishing raw traces:

1. classify the intended audience;
2. remove or quarantine secrets and personal data;
3. assess linkability and secondary-use risk;
4. review identifiers and metadata;
5. document retention and deletion policy; and
6. verify that sanitization does not invalidate the claimed result.

## Success Criteria

Publication-quality evidence should require:

- zero known prohibited privacy disclosures in the evaluated corpus;
- no silent success after protocol validation failure;
- deterministic agreement on canonical test vectors;
- independent implementation evidence for interoperability claims;
- preserved blocking objections;
- transparent negative and failed results; and
- no efficiency claim without measured baseline comparison.

Thresholds for accuracy, cost, latency, and robustness must be selected before
the corresponding experiment and justified for the target use case.

## Current Evidence Boundary

The repository currently contains deterministic results for one canonical JSON
implementation and its public positive and negative vectors. It does not yet
contain independent cross-implementation results or a completed benchmark for
token reduction, decision accuracy, privacy safety, or adversarial robustness.
