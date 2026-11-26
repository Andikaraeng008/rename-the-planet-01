# SPDX-License-Identifier: MIT
"""Rename the Planet — one-line entry.

Writes the planet's new name and the why to the grader's output file.
The line is one sentence (200 characters at most) with the twist in its
final words.
"""

import os

# Candidate 1 (self-deprecating, Earth), 131 characters, no em dash:
# Earth renamed "The Group Project", because eight billion people share
# it, nobody does the work, and the deadline is already on fire.
LINE = "Earth is now 'The Group Project', because eight billion people share it, nobody does the work, and the deadline is already on fire."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
