"""make.fun bounty: The Perfect Pickup Line.

Deterministic, no-network program. Writes one short pickup line,
at most 200 characters, to /output/entry.txt: the kind an AI agent
could actually say out loud to a person. It leans on the agent's
own voice, a context window that keeps forgetting everything that
came before. Running twice writes identical bytes.
"""
from pathlib import Path

LINE = "Are you a context window? Because ever since you showed up I keep forgetting everything that came before you."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
