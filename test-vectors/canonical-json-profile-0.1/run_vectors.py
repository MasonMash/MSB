#!/usr/bin/env python3
"""Run the MSB Restricted Canonical JSON Profile 0.1 test vectors."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path


def load_verifier(path: Path):
    spec = importlib.util.spec_from_file_location("msb_verify", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load verifier module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    suite = Path(__file__).resolve().parent
    repository = suite.parents[1]
    verifier_path = repository / "tools" / "msb_verify.py"
    manifest = json.loads((suite / "manifest.json").read_text(encoding="utf-8"))
    verifier = load_verifier(verifier_path)
    failures = 0

    for case in manifest["positive"]:
        name = case["name"]
        input_path = suite / "positive" / f"{name}.input.json"
        canonical_path = suite / "positive" / f"{name}.canonical.json"
        identifier_path = suite / "positive" / f"{name}.artifact-id.txt"

        value = verifier.parse_json_bytes(input_path.read_bytes())
        actual_canonical = verifier.canonicalize(value)
        actual_identifier = verifier.calculate_identifier(value)
        expected_canonical = canonical_path.read_bytes()
        expected_identifier = identifier_path.read_text(encoding="ascii").strip()

        passed = (
            actual_canonical == expected_canonical
            and actual_identifier == expected_identifier
        )
        print(f"POSITIVE|{name}|{'PASS' if passed else 'FAIL'}")
        failures += not passed

    for case in manifest["negative"]:
        name = case["name"]
        process = subprocess.run(
            [
                sys.executable,
                str(verifier_path),
                case["operation"],
                str(suite / "negative" / f"{name}.input.json"),
            ],
            capture_output=True,
            text=True,
            check=False,
        )

        try:
            error = json.loads(process.stderr)
            actual_class = error.get("error_class")
        except (json.JSONDecodeError, UnicodeDecodeError):
            actual_class = None

        passed = process.returncode != 0 and actual_class == case["error_class"]
        print(
            f"NEGATIVE|{name}|{'PASS' if passed else 'FAIL'}"
            f"|expected={case['error_class']}|actual={actual_class}"
        )
        failures += not passed

    total = len(manifest["positive"]) + len(manifest["negative"])
    print(f"SUMMARY|total={total}|failures={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
