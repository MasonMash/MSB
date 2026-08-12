# Protocol Examples

## Status

Every example in this document is illustrative and non-normative.

The examples are not records of real model executions; do not demonstrate
accuracy, efficiency, optimality, or interoperability; use arbitrary advisory
values; do not define another wire format; and do not alter revision `-00`.

## Separation of Layers

Orchestration metadata may be maintained outside a canonical artifact:

```json
{
  "session_id": "s91",
  "round": 2,
  "participant": "model-b",
  "role": "objector",
  "token_budget_remaining": 2780,
  "round_budget_remaining": 4
}
```

This is not a core MSB artifact. A future binding must define authentication,
retention, and identifier treatment for such metadata.

## Documentation Form

```json
{
  "protocol_version": "0.1",
  "artifact_id": "sha256:<64-lowercase-hex>",
  "artifact_type": "OBJECTION",
  "payload": {
    "statement": "The claim lacks an independently verifiable source.",
    "blocking": true
  },
  "references": [
    {
      "artifact_id": "sha256:<claim-identifier>",
      "relation": "objects-to"
    }
  ],
  "extensions": {}
}
```

The placeholder identifiers are not valid identifiers.

## Conceptual Primitives

| Primitive | Purpose |
|---|---|
| problem | Problem or objective under deliberation |
| constraint | Mandatory condition or preference |
| claim | Proposition that can be examined |
| candidate | Proposed answer or course of action |
| evidence vector | References, provenance, polarity, and advisory confidence |
| objection | Structured challenge |
| rebuttal | Response to an objection |
| resolution | Disposition or escalation of disagreement |
| delta | Change from a prior public position |
| adjudication | Evaluation of competing paths |
| decision | Keep, drop, hold, revise, escalate, or finalize |
| uncertainty | Remaining unknown or ambiguity |
| risk | Possible failure mode |

Only a subset is realized as core artifact types in revision `-00`.

## Illustrative Compact Projection

This compact line is a research sketch, not a wire specification:

```text
msb/0.1|s=s91|r=2|actor=model-b|role=obj|claim=c05|obj=evidence_gap:.69|request=source_check|delta=-.22|decision=hold|privacy=p1
```

A real specification would require escaping, Unicode normalization, canonical
ordering, repeated and nested fields, unknown-field behavior, version
negotiation, identifier boundaries, and error recovery.

## Typed Deliberation Graph Example

Research node types include Task, Constraint, Claim, Candidate, Evidence,
Objection, Rebuttal, Resolution, Risk, Decision, Uncertainty, Failure, and
Termination.

| Relation | Illustrative source and target |
|---|---|
| supports | Evidence to Claim |
| contradicts | Evidence or Objection to Claim |
| revises | Revision or delta to Claim or Candidate |
| supersedes | New artifact to replaced public position |
| resolves | Rebuttal or Resolution to Objection |
| depends-on | Claim to Constraint |
| escalates | Objection or Risk to Decision |
| selects | Decision to Candidate |
| invalidates | Evidence or Objection to Candidate |
| considers | Decision to examined artifact |
| decides | Decision to selected or rejected subject |

Only relations explicitly defined by revision `-00` are core relations.

## Illustrative Adjudication Procedure

1. Parse a candidate artifact.
2. Validate the envelope and type-specific payload contract.
3. Apply disclosure, recipient, and authorization policy.
4. Quarantine evidence attempting to mutate role, system, privacy, or policy.
5. Verify the artifact identifier and required references.
6. Append the immutable artifact; do not mutate prior artifacts.
7. Recompute implementation-local advisory assessments.
8. Preserve every unresolved blocking objection.
9. Request additional evidence when policy and budget permit.
10. Create a decision only when closure requirements pass.
11. Create an explicit termination artifact.

Local scores and thresholds are outside revision `-00`.

## Decision Without Raw Majority Rule

MSB does not prohibit voting, but majority agreement is not sufficient evidence
of closure. A final decision must not hide a reachable unresolved blocking
objection.

Research implementations may consider evidence strength, constraint severity,
provenance quality, uncertainty persistence, contradiction density, risk,
resource budget, and minority-objection status. Role reliability and numerical
thresholds are unspecified.

```text
msb/0.1|s=s91|r=3|actor=model-b|role=obj|claim=c05|obj=minority:source_conflict:.74|preserve=true|decision=hold|privacy=p1
```

## Illustrative Two-Model Trace

This trace demonstrates representation, not measured performance.

```text
session=s91|goal=review_claim|budget.tokens=4000|budget.rounds=6|privacy=p1
```

Model A proposes:

```text
actor=model-a|role=proposer|claim=c05|risk=.24|decision=keep
```

Model B objects:

```text
actor=model-b|role=objector|claim=c05|obj=evidence_gap:.69,scope_drift:.41|request=source_check|decision=hold
```

Model A supplies evidence and revises:

```text
actor=model-a|role=verifier|claim=c05|evidence=external:e12:.82|obj=evidence_gap:.18|decision=revise
```

Model B records residual risk:

```text
actor=model-b|role=risk-reviewer|claim=c05|risk=scope_drift:.19,overclaim:.22|uncertainty=low|decision=hold
```

Decision and termination:

```text
actor=orchestrator|status=final|outcome=accept_revised_claim|unresolved=none
```

A final DECISION is permitted only after visible disposition of the blocking
objection. A completed TERMINATION then references that decision.

## Illustrative Lifecycle

```text
INITIALIZE -> FRAME -> PROPOSE -> OBJECT -> VERIFY -> REVISE -> DECIDE -> TERMINATE
```

Revision `-00` does not require this sequence, these roles, or a fixed number
of rounds.
