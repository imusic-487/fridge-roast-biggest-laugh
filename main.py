"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (<= 200 characters) to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "My smart fridge makes me watch a 30-second ad before it gives me water, "
    "so now I pay a monthly subscription to stay hydrated in my own kitchen."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
