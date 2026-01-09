#!/usr/bin/env python3
"""
Post-processing script to add footer references and page numbering to sections.

Sections without footers (no page numbers):
- Section 1: Cover + Version_Control
- Section 2: Blank_Page + foreword + TOC

Sections with footers and Roman numeral page numbers (i, ii, iii...):
- Section 3-7: Executive_Summary through Relationship_to_Standards_and_SOPs

Sections with footers and Arabic numeral page numbers (1, 2, 3...):
- Section 8 onwards: SECTION_1 through end of document
"""

import sys
import tempfile
import shutil
from pathlib import Path

# Add docx skill to path
DOCX_SKILL = Path.home() / '.claude/plugins/cache/anthropic-agent-skills/document-skills/69c0b1a06741/skills/docx'
sys.path.insert(0, str(DOCX_SKILL))

from scripts.document import DocxXMLEditor

def add_footers_to_all_sections(docx_path: str):
    """Add footer references and page numbering to all sections in a DOCX file."""
    # Unpack the DOCX
    unpack_script = DOCX_SKILL / 'ooxml/scripts/unpack.py'
    pack_script = DOCX_SKILL / 'ooxml/scripts/pack.py'

    temp_dir = Path(tempfile.mkdtemp())
    try:
        # Unpack
        import subprocess
        subprocess.run([sys.executable, str(unpack_script), str(docx_path), str(temp_dir)],
                      check=True, capture_output=True)

        # Process document.xml
        doc_xml = temp_dir / 'word/document.xml'
        editor = DocxXMLEditor(doc_xml, rsid="00AB1234")

        # Get all sectPr elements
        sectprs = editor.dom.getElementsByTagName('w:sectPr')

        # Footer reference IDs - check what's in relationships
        rels_file = temp_dir / 'word/_rels/document.xml.rels'
        footer_rids = {}

        if rels_file.exists():
            rels_editor = DocxXMLEditor(rels_file, rsid="00AB1234")
            for rel in rels_editor.dom.getElementsByTagName('Relationship'):
                if 'footer' in rel.getAttribute('Type'):
                    rid = rel.getAttribute('Id')
                    target = rel.getAttribute('Target')
                    # Map based on footer file name
                    if 'footer1.xml' in target:
                        footer_rids['even'] = rid
                    elif 'footer2.xml' in target:
                        footer_rids['default'] = rid
                    elif 'footer3.xml' in target:
                        footer_rids['first'] = rid

        # Fallback to default IDs if not found
        if not footer_rids:
            footer_rids = {'even': 'rId10', 'default': 'rId11', 'first': 'rId13'}

        # Process sections
        count = 0
        found_decimal_reset = False
        for idx, sectpr in enumerate(sectprs):
            # Skip first 2 sections (no page numbers for Cover through TOC)
            if idx < 2:
                continue

            # Check if this section has decimal page numbering (from SECTION_1.md)
            has_decimal = False
            for child in list(sectpr.childNodes):
                if child.nodeType == child.ELEMENT_NODE and child.tagName == 'w:pgNumType':
                    fmt = child.getAttribute('w:fmt')
                    if fmt == 'decimal':
                        has_decimal = True
                        found_decimal_reset = True

            # Add footer references to sections that don't have them
            has_footer = any(child.nodeType == child.ELEMENT_NODE and
                           child.tagName == 'w:footerReference'
                           for child in sectpr.childNodes)

            if not has_footer:
                even_ref = f'<w:footerReference w:type="even" r:id="{footer_rids.get("even", "rId10")}"/>'
                default_ref = f'<w:footerReference w:type="default" r:id="{footer_rids.get("default", "rId11")}"/>'
                first_ref = f'<w:footerReference w:type="first" r:id="{footer_rids.get("first", "rId13")}"/>'

                # Find first element child
                first_child = None
                for child in sectpr.childNodes:
                    if child.nodeType == child.ELEMENT_NODE:
                        first_child = child
                        break

                if first_child:
                    editor.insert_before(first_child, first_ref)
                    editor.insert_before(first_child, default_ref)
                    editor.insert_before(first_child, even_ref)
                else:
                    editor.append_to(sectpr, even_ref)
                    editor.append_to(sectpr, default_ref)
                    editor.append_to(sectpr, first_ref)
                count += 1

            # Now handle page numbering
            # For sections before decimal reset (sections 3-7): add lowerRoman if no pgNumType
            # For sections after decimal reset: remove any lowerRoman (they should continue with decimal)
            has_pgnumtype = any(child.nodeType == child.ELEMENT_NODE and
                               child.tagName == 'w:pgNumType'
                               for child in sectpr.childNodes)

            if not has_decimal and not has_pgnumtype and not found_decimal_reset:
                # Section 3-7: add explicit lowerRoman numbering
                pgnum_type = '<w:pgNumType w:fmt="lowerRoman"/>'
                editor.append_to(sectpr, pgnum_type)
            elif found_decimal_reset and not has_decimal:
                # After decimal reset: remove any lowerRoman to continue decimal
                for child in list(sectpr.childNodes):
                    if child.nodeType == child.ELEMENT_NODE and child.tagName == 'w:pgNumType':
                        fmt = child.getAttribute('w:fmt')
                        if fmt == 'lowerRoman':
                            sectpr.removeChild(child)

        editor.save()
        print(f"Added footer references to {count} sections")

        # Pack back
        subprocess.run([sys.executable, str(pack_script), str(temp_dir), str(docx_path)],
                      check=True, capture_output=True)

    finally:
        # Cleanup
        shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <docx_file>")
        sys.exit(1)

    add_footers_to_all_sections(sys.argv[1])
    print(f"Page numbers added to {sys.argv[1]}")
