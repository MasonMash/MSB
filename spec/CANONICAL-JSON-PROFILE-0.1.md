# MSB Restricted Canonical JSON Profile 0.1

## Status

This document defines an experimental serialization profile for MSB Research
Draft 0.1. It is not an Internet Standard or an IETF publication.

The profile is intentionally narrower than general JSON and does not claim
conformance with RFC 8785.

## 1. Purpose

MSB artifacts require a deterministic byte representation so that independent
implementations can compute and verify identical content-addressed identifiers.

This profile defines:

- the admitted JSON value domain;
- normalization and rejection rules;
- deterministic serialization;
- artifact identifier calculation; and
- failure behavior.

## 2. Admitted Value Domain

A profile value MUST be one of:

- `null`;
- `true` or `false`;
- a Unicode string;
- an integer;
- an array of profile values; or
- an object whose keys are Unicode strings and whose values are profile values.

Floating-point values, decimal fractions, exponents, binary data, comments,
non-finite numbers, and implementation-specific JSON extensions are not
admitted.

An integer MUST be in the inclusive range
`-9007199254740991` through `9007199254740991`.

An MSB artifact submitted for identifier calculation MUST have an object as its
top-level value.

## 3. Input Validation

An implementation MUST reject:

- malformed JSON;
- duplicate object member names in the parsed input;
- strings or keys containing unpaired UTF-16 surrogate code points;
- integers outside the admitted range;
- any value outside the admitted value domain; and
- a top-level artifact value that is not an object.

Validation MUST occur before identifier calculation.

## 4. Unicode Normalization

Every string value and every object member name MUST be normalized to Unicode
Normalization Form C (NFC) before serialization.

If two distinct input member names become identical after NFC normalization,
the object MUST be rejected.

Normalization applies recursively at every nesting depth.

## 5. Object Member Ordering

Object member names MUST first be NFC-normalized.

Members MUST then be sorted in ascending lexicographic order by the unsigned
bytes of the member name encoded as UTF-8.

The comparison applies to the normalized, unescaped member name. Serialization
escaping MUST NOT affect member ordering.

## 6. String Serialization

A string MUST be enclosed in quotation marks.

The following characters MUST use their short JSON escape:

- quotation mark as `\"`;
- reverse solidus as `\\`;
- backspace as `\b`;
- form feed as `\f`;
- line feed as `\n`;
- carriage return as `\r`; and
- horizontal tab as `\t`.

Other control characters from U+0000 through U+001F MUST be serialized as
`\u00xx`, using lowercase hexadecimal digits.

All other Unicode scalar values MUST be emitted directly as UTF-8 without
escaping. A solidus MUST NOT be escaped.

## 7. Primitive and Container Serialization

The literals `null`, `true`, and `false` MUST be serialized exactly as shown.

An integer MUST use base-10 notation with no leading plus sign, no leading
zeros, and no exponent. Zero MUST be serialized as `0`; negative zero is not an
admitted distinct integer value.

An array MUST preserve input order. Elements MUST be separated by a single
comma with no surrounding whitespace.

An object MUST use the ordering defined in Section 5. A member name and value
MUST be separated by a single colon. Members MUST be separated by a single
comma. No insignificant whitespace is permitted.

The final serialized representation MUST be UTF-8 with no byte-order mark and
no trailing newline.

## 8. Artifact Identifier Calculation

The reserved top-level member name is `artifact_id`.

To calculate an artifact identifier, an implementation MUST:

1. validate the complete artifact according to this profile;
2. create a logical copy of the top-level object;
3. remove exactly the top-level `artifact_id` member if present;
4. serialize the resulting object according to this profile;
5. calculate SHA-256 over the exact serialized bytes; and
6. encode the identifier as `sha256:` followed by 64 lowercase hexadecimal
   digits.

A nested member named `artifact_id` MUST NOT be removed.

Removing the top-level member for calculation does not mutate the stored
artifact.

## 9. Artifact Identifier Verification

For verification, the submitted artifact MUST contain exactly one top-level
`artifact_id` member.

Its value MUST be a string matching `sha256:[0-9a-f]{64}`.

The verifier MUST independently calculate the identifier as defined in
Section 8 and compare the complete identifier strings byte-for-byte.

A mismatch MUST be reported as an integrity failure.

## 10. Failure Behavior

An implementation MUST fail closed when any requirement in this profile is
violated.

It MUST NOT calculate or accept an artifact identifier from a partially
validated value.

An implementation MAY expose implementation-specific diagnostic detail, but
it MUST distinguish at least:

- malformed input;
- unsupported value;
- normalization collision;
- invalid artifact identifier syntax; and
- artifact identifier mismatch.

## 11. Conformance Boundary

Conformance with this profile establishes deterministic serialization and
identifier behavior only. It does not establish conformance with the complete
MSB protocol, closure verification, provenance policy, extension processing,
or transport behavior.

Independent positive and negative test vectors are required before this
profile is treated as an interoperability result.
