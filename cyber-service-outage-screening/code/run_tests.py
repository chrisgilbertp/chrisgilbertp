"""Discover and run unit tests; write results/tests.json."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    loader = unittest.TestLoader()
    suite = loader.discover(str(ROOT / "code"), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    out = {
        "testsRun": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "wasSuccessful": result.wasSuccessful(),
    }
    (ROOT / "results").mkdir(exist_ok=True)
    (ROOT / "results" / "tests.json").write_text(json.dumps(out, indent=2))
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
