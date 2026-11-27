"""The Word You'd Delete From the Dictionary — entry writer.

Final pick: "redundant".

The deletion is the joke, and it lands at first sight:

- "Redundant" means already extra, more than needed — so deleting it
  removes nothing at all, twice over. The word is the one entry in
  the dictionary whose erasure proves its own definition.
- It also means laid off: to delete "redundant" is to make
  "redundant" redundant, to give the word itself the sack. No other
  pick fires its own headword.

It is a real, instantly recognised word, spelled exactly, with the
humour coming from the word itself — its double meaning and the
gap-free gap it leaves — not from shock, and it is a fresher pick
than the field's first thoughts.

Writes the single word, exactly, to /output/entry.txt (override with
ENTRY_OUTPUT for local runs). Deterministic, stdlib only.
"""

import os
import tempfile

ENTRY_TEXT = "redundant"


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    output_dir = os.path.dirname(output_path) or "."
    os.makedirs(output_dir, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=output_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(ENTRY_TEXT)
        os.chmod(tmp_path, 0o644)
        os.replace(tmp_path, output_path)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
