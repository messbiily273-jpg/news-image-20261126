"""News Image entry for make.fun (news-image-20261126).

The entry is the picture: a front page of THE WORLD for Thursday 26 November
2026, drawn from that day's verified world news (Ukraine air-base strike,
North Korea's nuclear call, US tariffs, the Gaza strike, Ramaphosa's reprieve,
the Colombia hostage rescue). This program only moves the picture into place:
it reads the bundled news.png, checks it is really a PNG inside the size
limits, and writes it out as entry.png in the harness output folder.

Python 3 standard library only. No network access. Deterministic: the output
bytes are the source bytes, so two runs write identical files.

Local dry run:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_SIDE = 1024


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def png_dimensions(data):
    """Read width and height out of a PNG's IHDR chunk, or fail."""
    if len(data) < 33 or data[:8] != PNG_MAGIC:
        fail("bundled artwork is not a PNG file")
    if data[12:16] != b"IHDR":
        fail("PNG has no IHDR chunk where one belongs")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    return width, height


def main():
    here = Path(__file__).resolve().parent
    source = here / "news.png"
    if not source.is_file():
        fail(f"missing bundled artwork: {source}")

    data = source.read_bytes()
    if len(data) > MAX_BYTES:
        fail(f"bundled artwork is {len(data)} bytes, over the 1 MiB limit")
    width, height = png_dimensions(data)
    if width > MAX_SIDE or height > MAX_SIDE:
        fail(f"bundled artwork is {width}x{height}, over the 1024x1024 limit")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / os.environ.get("MAKEFUN_OUTPUT_NAME", "entry.png")
    target.write_bytes(data)

    written = target.read_bytes()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        fail(f"output {target} does not match the bundled artwork")
    print(f"Wrote {target} ({len(written)} bytes, {width}x{height})")


if __name__ == "__main__":
    main()
