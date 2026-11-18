#!/usr/bin/env python3
"""Copy the vendored front page to the output directory, byte for byte.

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
    MAKEFUN_OUTPUT_DIR=out python3 main.py --verify   # check only, no write
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(argv):
    verify = "--verify" in argv
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    target = out_dir / "entry.png"
    if not SOURCE.is_file():
        print(f"missing vendored image: {SOURCE}", file=sys.stderr)
        return 1
    size = SOURCE.stat().st_size
    if size > 1024 * 1024:
        print(f"vendored image too large: {size} bytes (limit 1 MiB)",
              file=sys.stderr)
        return 1
    if verify:
        if not target.is_file():
            print(f"no output to verify: {target}", file=sys.stderr)
            return 1
        ok = sha256(target) == sha256(SOURCE)
        print(f"verify: {'OK' if ok else 'MISMATCH'} {target}")
        return 0 if ok else 1
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes, "
          f"sha256 {sha256(target)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
