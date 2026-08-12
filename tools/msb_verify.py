#!/usr/bin/env python3
"""Reference verifier for the MSB Restricted Canonical JSON Profile 0.1."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any, NoReturn

MIN_INTEGER = -9007199254740991
MAX_INTEGER = 9007199254740991
ARTIFACT_ID_PATTERN = re.compile(r"sha256:[0-9a-f]{64}\Z")


class ProfileError(ValueError):
    """Base class for fail-closed profile errors."""

    error_class = "malformed_input"


class MalformedInput(ProfileError):
    error_class = "malformed_input"


class UnsupportedValue(ProfileError):
    error_class = "unsupported_value"


class NormalizationCollision(ProfileError):
    error_class = "normalization_collision"


class InvalidArtifactIdentifierSyntax(ProfileError):
    error_class = "invalid_artifact_identifier_syntax"


class ArtifactIdentifierMismatch(ProfileError):
    error_class = "artifact_identifier_mismatch"


def _reject_float(value: str) -> NoReturn:
    raise UnsupportedValue(f"floating-point value is not admitted: {value}")


def _reject_constant(value: str) -> NoReturn:
    raise UnsupportedValue(f"non-finite value is not admitted: {value}")


def _parse_integer(value: str) -> int:
    parsed = int(value)
    if not MIN_INTEGER <= parsed <= MAX_INTEGER:
        raise UnsupportedValue("integer is outside the admitted range")
    return parsed


def _contains_surrogate(value: str) -> bool:
    return any(0xD800 <= ord(character) <= 0xDFFF for character in value)


def _object_from_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    raw_names: set[str] = set()
    normalized_names: set[str] = set()
    result: dict[str, Any] = {}

    for raw_name, value in pairs:
        if raw_name in raw_names:
            raise MalformedInput(f"duplicate object member name: {raw_name!r}")
        raw_names.add(raw_name)

        if _contains_surrogate(raw_name):
            raise UnsupportedValue("object member name contains an unpaired surrogate")

        normalized_name = unicodedata.normalize("NFC", raw_name)
        if normalized_name in normalized_names:
            raise NormalizationCollision(
                f"object member names collide after NFC normalization: {raw_name!r}"
            )
        normalized_names.add(normalized_name)
        result[normalized_name] = value

    return result


def parse_json_bytes(data: bytes) -> Any:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise MalformedInput("input is not valid UTF-8") from exc

    if data.startswith(b"\xef\xbb\xbf"):
        raise MalformedInput("UTF-8 byte-order mark is not admitted")

    try:
        return json.loads(
            text,
            object_pairs_hook=_object_from_pairs,
            parse_int=_parse_integer,
            parse_float=_reject_float,
            parse_constant=_reject_constant,
        )
    except ProfileError:
        raise
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise MalformedInput("malformed JSON input") from exc


def _normalize_and_validate(value: Any) -> Any:
    if value is None or isinstance(value, bool):
        return value

    if isinstance(value, int):
        if not MIN_INTEGER <= value <= MAX_INTEGER:
            raise UnsupportedValue("integer is outside the admitted range")
        return value

    if isinstance(value, float):
        raise UnsupportedValue("floating-point values are not admitted")

    if isinstance(value, str):
        if _contains_surrogate(value):
            raise UnsupportedValue("string contains an unpaired surrogate")
        return unicodedata.normalize("NFC", value)

    if isinstance(value, list):
        return [_normalize_and_validate(item) for item in value]

    if isinstance(value, dict):
        normalized: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise UnsupportedValue("object member names must be strings")
            if _contains_surrogate(key):
                raise UnsupportedValue("object member name contains an unpaired surrogate")

            normalized_key = unicodedata.normalize("NFC", key)
            if normalized_key in normalized:
                raise NormalizationCollision(
                    f"object member names collide after NFC normalization: {key!r}"
                )
            normalized[normalized_key] = _normalize_and_validate(item)
        return normalized

    raise UnsupportedValue(f"unsupported value type: {type(value).__name__}")


def _serialize_string(value: str) -> str:
    output = ['"']
    short_escapes = {
        '"': '\\"',
        "\\": "\\\\",
        "\b": "\\b",
        "\f": "\\f",
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
    }

    for character in value:
        escaped = short_escapes.get(character)
        if escaped is not None:
            output.append(escaped)
        elif ord(character) <= 0x1F:
            output.append(f"\\u{ord(character):04x}")
        else:
            output.append(character)

    output.append('"')
    return "".join(output)


def _serialize(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return _serialize_string(value)
    if isinstance(value, list):
        return "[" + ",".join(_serialize(item) for item in value) + "]"
    if isinstance(value, dict):
        ordered_keys = sorted(value, key=lambda key: key.encode("utf-8"))
        members = (
            _serialize_string(key) + ":" + _serialize(value[key])
            for key in ordered_keys
        )
        return "{" + ",".join(members) + "}"
    raise UnsupportedValue(f"unsupported value type: {type(value).__name__}")


def canonicalize(value: Any) -> bytes:
    normalized = _normalize_and_validate(value)
    return _serialize(normalized).encode("utf-8")


def calculate_identifier(value: Any) -> str:
    normalized = _normalize_and_validate(value)
    if not isinstance(normalized, dict):
        raise UnsupportedValue("top-level artifact value must be an object")

    artifact_body = dict(normalized)
    artifact_body.pop("artifact_id", None)
    digest = hashlib.sha256(canonicalize(artifact_body)).hexdigest()
    return f"sha256:{digest}"


def verify_identifier(value: Any) -> str:
    normalized = _normalize_and_validate(value)
    if not isinstance(normalized, dict):
        raise UnsupportedValue("top-level artifact value must be an object")

    submitted = normalized.get("artifact_id")
    if not isinstance(submitted, str) or ARTIFACT_ID_PATTERN.fullmatch(submitted) is None:
        raise InvalidArtifactIdentifierSyntax(
            "artifact_id must match sha256:[0-9a-f]{64}"
        )

    calculated = calculate_identifier(normalized)
    if submitted.encode("utf-8") != calculated.encode("utf-8"):
        raise ArtifactIdentifierMismatch("artifact identifier does not match content")

    return calculated


def _read_input(path: str) -> bytes:
    if path == "-":
        return sys.stdin.buffer.read()
    return Path(path).read_bytes()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Calculate or verify an MSB restricted canonical JSON identifier."
    )
    parser.add_argument("operation", choices=("calculate", "verify"))
    parser.add_argument("input", help="JSON file path, or - for standard input")
    arguments = parser.parse_args()

    try:
        artifact = parse_json_bytes(_read_input(arguments.input))
        identifier = (
            calculate_identifier(artifact)
            if arguments.operation == "calculate"
            else verify_identifier(artifact)
        )
    except ProfileError as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error_class": exc.error_class,
                    "message": str(exc),
                },
                separators=(",", ":"),
            ),
            file=sys.stderr,
        )
        return 1
    except OSError as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error_class": "malformed_input",
                    "message": str(exc),
                },
                separators=(",", ":"),
            ),
            file=sys.stderr,
        )
        return 1

    print(json.dumps({"ok": True, "artifact_id": identifier}, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
