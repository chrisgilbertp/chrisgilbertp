"""Refresh SHA256 manifest for frozen inputs."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    files = {}
    for path in sorted((ROOT / "data").rglob("*")):
        if path.is_file():
            rel = str(path.relative_to(ROOT)).replace("\\\\", "/")
            files[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest = {"files": files}
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"manifest refreshed with {len(files)} files")


if __name__ == "__main__":
    main()
