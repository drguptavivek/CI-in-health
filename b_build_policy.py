import subprocess
import re
import sys
from pathlib import Path

# Base directory (script location)
BASE_DIR = Path(__file__).resolve().parent
CHAPTERS_DIR = BASE_DIR / "chapters"
OUTPUT_DIR = BASE_DIR / "_build"
OUTPUT_DIR.mkdir(exist_ok=True)
PDF_OUT = OUTPUT_DIR / "CI_health.pdf"
DOCX_OUT = OUTPUT_DIR / "CI_health.docx"

# Collect markdown files in order
md_files = sorted(
    CHAPTERS_DIR.rglob("*.md"),
    key=lambda p: p.as_posix()
)

# Exclude merged or helper files if needed
md_files = [
    p for p in md_files
    if "COMPLETE" not in p.name.upper()
]
md_paths = [str(p) for p in md_files]
print("Markdown files included:")
for p in md_paths:
    print(" -", p)

def get_indent(line: str) -> int:
    """Return the number of leading spaces in a line."""
    return len(line) - len(line.lstrip(' '))

def preprocess_markdown(content: str) -> str:
    """
    Preprocess markdown to remove blank lines between list items.
    This forces pandoc to create tight lists. Indentation alone defines
    nested structure, so blank lines between nested items are also removed.
    """
    lines = content.split('\n')
    result = []
    i = 0
    while i < len(lines):
        current = lines[i]
        # Check if current line is a list item
        is_list_item = bool(re.match(r'^\s*([*+-]|\d+\.)\s+', current))
        if is_list_item:
            result.append(current)
            i += 1
            # Consume all following blank lines and list items as a continuous block
            # Stop when we hit non-list, non-blank content
            while i < len(lines):
                next_line = lines[i]
                if next_line.strip() == '':
                    # Blank line - skip it (we're collapsing all blanks in lists)
                    i += 1
                    continue
                elif re.match(r'^\s*([*+-]|\d+\.)\s+', next_line):
                    # Another list item - add it and continue
                    result.append(next_line)
                    i += 1
                else:
                    # Non-blank, non-list content - stop here
                    # Preserve a blank before the non-list content for readability
                    if not result or result[-1].strip() != '':
                        result.append('')
                    break
        else:
            result.append(current)
            i += 1
    return '\n'.join(result)


# Create preprocessed merged markdown
merged_md = BASE_DIR / "_build_temp_merged.md"
with open(merged_md, 'w') as out:
    for md_file in md_files:
        content = md_file.read_text()
        preprocessed = preprocess_markdown(content)
        out.write(preprocessed)
        out.write('\n\n')

# --------------------

# Build DOCX

# --------------------
docx_cmd = [
    "pandoc",
    str(merged_md),
    "--from=markdown+raw_tex+raw_attribute",
    "--lua-filter", str(BASE_DIR / "pagebreak.lua"),
    "--standalone",
    "--metadata", "pagetitle=Global Classification of Health Information Systems as Critical Infrastructure",
    "-o", str(DOCX_OUT),
]
print("\nGenerating DOCX...")
subprocess.run(docx_cmd, check=True)

# --------------------

# Build PDF

# --------------------
pdf_cmd = [
    "pandoc",
    str(merged_md),
    "--from=markdown+raw_tex+raw_attribute",
    "--lua-filter", str(BASE_DIR / "pagebreak.lua"),
    "--pdf-engine=xelatex",
    "--include-in-header", str(BASE_DIR / "preamble.tex"),
    "-V", "geometry:margin=1in",
    "-V", "fontsize=11pt",
    "-V", "documentclass=article",
    "-V", "colorlinks=true",
    "-V", "linkcolor=blue",
    "-V", "urlcolor=blue",
    "-o", str(PDF_OUT),
]

print("\nGenerating PDF...")
subprocess.run(pdf_cmd, check=True)

# Clean up temp file
merged_md.unlink()
print("\nBuild successful")
print("PDF :", PDF_OUT)
print("DOCX:", DOCX_OUT)
