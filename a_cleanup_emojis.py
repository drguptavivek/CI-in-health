from pathlib import Path

# Replace symbols/emojis that cause Pandoc/LaTeX font issues with ASCII-safe text
REPLACEMENTS = {
    "\uFE0F": "",  # variation selector
    "\u2714": "Aligned",
    "\u26A0": "Partially aligned",
    "\u2718": "Not required",
    "\u2502": "|",
    "\u251C": "|-",
    "\u2500": "-",
    "\u2514": "\\-",
    "\U0001F6E1": "[SECURE]",
    "\U0001F512": "[ENCRYPTED]",
    "\U0001F511": "[KEY]",
    "\U0001F4DD": "[NOTE]",
    "\U0001F4C4": "[DOCUMENT]",
    "\U0001F4C1": "[FOLDER]",
    "\U0001F6AB": "[PROHIBITED]",
    "\u26D4": "[NOT PERMITTED]",
}

def clean_file(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    original = text
    for needle, replacement in REPLACEMENTS.items():
        text = text.replace(needle, replacement)
    if text != original:
        md_path.write_text(text, encoding="utf-8")
        print(f"Cleaned: {md_path}")

def main():
    base_dir = Path(__file__).resolve().parent
    for md_file in base_dir.rglob("*.md"):
        clean_file(md_file)
    print("\nEmoji cleanup completed.")

if __name__ == "__main__":
    main()
