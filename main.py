#!/usr/bin/env python3
"""Round 2 entry for make.fun news-image-20261118.

Copies the front-page image vendored in this repository to the output
directory, byte for byte. Standard library only, no network, deterministic.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    if os.path.getsize(SRC) > 1024 * 1024:
        print("vendored image exceeds the 1 MiB limit", file=sys.stderr)
        return 1
    shutil.copyfile(SRC, dest)
    print("wrote", dest, os.path.getsize(dest), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
