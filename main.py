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
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    print("wrote %s" % target)


if __name__ == "__main__":
    main()
