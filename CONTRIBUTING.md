# Contributing

MSB is a protocol research project.

Contributions are evaluated primarily on whether they improve interoperability, auditability, security, privacy, or specification precision.

## What Makes a High-Value Contribution

Useful contributions include:

- identifying an ambiguous normative requirement;
- constructing an interoperability counterexample;
- demonstrating a closure or history failure;
- proposing a smaller protocol primitive;
- supplying an independent implementation;
- adding deterministic test vectors;
- identifying a security or privacy weakness;
- challenging an unsupported research claim; or
- improving the distinction between protocol semantics and implementation policy.

## Protocol Changes

A protocol change should explain:

1. the concrete interoperability problem;
2. the proposed semantic change;
3. compatibility impact;
4. security impact;
5. privacy impact;
6. failure behavior;
7. conformance impact; and
8. evidence or test vectors supporting the change.

Normative requirements should not be added merely because a model, framework, or provider currently behaves in a particular way.

## Evidence Requirements

When a contribution makes an empirical claim, identify the source.

The project distinguishes:

- observed execution evidence;
- trace-verified evidence;
- external evidence;
- model-generated analysis; and
- hypotheses.

A model-generated benchmark, estimate, or simulation must not be presented as measured project evidence unless it has been independently executed or verified.

## Privacy Rule

Do not submit private chain-of-thought, hidden model state, system prompts, private memory, credentials, or provider-private reasoning payloads as protocol evidence.

Public rationale and public artifacts are sufficient for protocol review.

## Specification Style

Specification changes should:

- define terms before using them normatively;
- distinguish normative requirements from informative explanation;
- use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` deliberately;
- specify failure behavior where applicable;
- avoid provider-specific assumptions in core semantics; and
- identify unresolved design questions rather than hiding them.

## Pull Requests

A protocol pull request should remain narrowly scoped.

Where applicable, include:

- rationale;
- compatibility notes;
- security considerations;
- privacy considerations;
- test vectors; and
- evidence references.

A change to the evidence ledger must preserve the distinction between source evidence and interpretation.

## Research Integrity

Failed experiments, negative results, and non-convergence are valid evidence.

Do not rewrite historical experiment records to make a later design appear cleaner.

Corrections should be prospective and explicitly documented.
