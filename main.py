"""The Word You'd Delete From the Dictionary — entry writer.

Draft pick: "maybe" — deleting it would force everyone to finally
commit to a yes or a no: no more "maybe later", no more maybes on
RSVPs, dates or deadlines. The joke is the social gap it leaves.

Writes the single word, exactly, to /output/entry.txt (override with
ENTRY_OUTPUT for local runs). Deterministic, stdlib only.
"""

import os
import tempfile

ENTRY_TEXT = "maybe"


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
