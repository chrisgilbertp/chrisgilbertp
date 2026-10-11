"""Verify frozen input hashes against the declared manifest."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / "manifest.json").read_text())
    missing = []
    mismatched = []
    for rel, expected in manifest.get("files", {}).items():
        path = ROOT / rel
        if not path.is_file():
            missing.append(rel)
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != expected:
            mismatched.append((rel, expected, digest))
    if missing or mismatched:
        raise SystemExit(f"input verification failed: missing={missing} mismatched={mismatched}")
    print("input hashes verified")


if __name__ == "__main__":
    main()
