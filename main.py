# SPDX-License-Identifier: MIT
"""Rename the Planet — one-line entry.

Writes the planet's new name and the why to the grader's output file.
The line is one sentence (200 characters at most) with the twist in its
final words.
"""

import os

# Candidate 3 (sharp-observational, Saturn), 142 characters, no em dash:
# Saturn renamed "The Hula Hoop", because it has spun the same ring
# around its waist for four billion years and still will not admit it
# is stuck.
LINE = "Saturn is now 'The Hula Hoop', because it has spun the same ring around its waist for four billion years and still will not admit it is stuck."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
