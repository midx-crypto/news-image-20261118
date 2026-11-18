#!/usr/bin/env python3
"""news-image-20261118 round 3: entry point.

The entry is one pre-rendered newspaper front page, entry.png
(JPEG bytes, 1024x1024), drawn by build.py in the sibling build
directory from generated photos and a generated world map, with all
text rendered on top. This program does nothing but copy that file
into the output directory, byte for byte.

It uses only the standard library, touches no network, and holds no
state, so two runs always write the same bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
LIMIT = 1024 * 1024


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if os.path.getsize(SOURCE) > LIMIT:
        print("entry.png exceeds the 1 MiB limit", file=sys.stderr)
        return 1
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    want = _sha256(SOURCE)
    shutil.copyfile(SOURCE, target)
    if _sha256(target) != want:
        print("copied file failed its integrity check", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (target, os.path.getsize(target), want))
    return 0


if __name__ == "__main__":
    sys.exit(main())
