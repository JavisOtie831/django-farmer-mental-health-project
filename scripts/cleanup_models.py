"""
Post-process Django inspectdb output. Handles any common encoding.

Usage:
    python scripts/cleanup_models.py _raw_afya.py     afya
    python scripts/cleanup_models.py _raw_audit.py    audit
    python scripts/cleanup_models.py _raw_research.py research
"""
import re
import sys
from pathlib import Path


def read_text_any_encoding(path: Path) -> str:
    """Read a file regardless of whether it was saved as UTF-8,
    UTF-8 with BOM, UTF-16 LE, or UTF-16 BE (PowerShell 5.1 writes UTF-16)."""
    data = path.read_bytes()
    if data[:2] in (b"\xff\xfe", b"\xfe\xff"):
        return data.decode("utf-16")               # UTF-16 LE/BE with BOM
    if data[:3] == b"\xef\xbb\xbf":
        return data.decode("utf-8-sig")            # UTF-8 with BOM
    if data[:4] in (b"\xff\xfe\x00\x00", b"\x00\x00\xfe\xff"):
        return data.decode("utf-32")
    return data.decode("utf-8", errors="replace")


def prefix_schema(text: str, schema: str) -> str:
    """db_table = 'users'  -->  db_table = 'afya"."users'"""
    def replace(match):
        table = match.group(1)
        if '"' in table:
            return match.group(0)
        return f'db_table = \'{schema}"."{table}\''
    return re.sub(r"db_table = '([^']+)'", replace, text)


def force_managed_false(text: str) -> str:
    # Every Meta block that doesn't already have managed=False gets it
    def add_managed(match):
        block = match.group(0)
        if "managed = False" in block:
            return block
        return block.replace(
            "class Meta:\n",
            "class Meta:\n        managed = False\n",
            1,
        )
    return re.sub(r"class Meta:\n(?:        .*\n)+", add_managed, text)


def fix_research_views(text: str) -> str:
    # inspectdb injects a fake AutoField PK on views; drop it
    text = re.sub(
        r"\n    id = models\.AutoField\(primary_key=True\)\n",
        "\n    # no real PK — first field is designated primary_key below\n",
        text,
    )
    return text


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/cleanup_models.py <file> <schema>")
        sys.exit(1)

    path = Path(sys.argv[1])
    schema = sys.argv[2]

    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    text = read_text_any_encoding(path)
    original_len = len(text)

    text = prefix_schema(text, schema)
    text = force_managed_false(text)
    if schema == "research":
        text = fix_research_views(text)

    # Always write as UTF-8, Unix line endings — no BOM
    path.write_text(text, encoding="utf-8", newline="\n")
    print(f"Cleaned {path.name} (schema={schema}) — {original_len} -> {len(text)} bytes")


if __name__ == "__main__":
    main()