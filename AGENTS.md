# Repository Guidelines

## Project Purpose & Structure
- This repo holds a **global comparative study**: "Global Classification of Health Information Systems as Critical, Protected, or High-Security Infrastructure" (Version 2.0, January 2026).
- Content is Markdown-first, built into DOCX/PDF via pandoc.
- **Country chapters** live under `chapters/` with numbered prefixes (01 - USA, 02 - Australia, etc.).
- Scripts at root: `a_cleanup_emojis.py` (sanitizes Markdown), `b_build_policy.py` (runs pandoc), `c_add_footers.py` (post-processing). Outputs land in `_build/`.
- LaTeX templates and Lua filters at root (`template.tex`, `center-images.lua`, `tight_lists.lua`).

## Build & Development Commands
- Build artifacts: `uv run b_build_policy.py` (needs pandoc + xelatex) -> `_build/CI_health.docx/.pdf`.
- Pre-build cleanup: `uv run a_cleanup_emojis.py` after editing content.
- Footer processing: `uv run c_add_footers.py` for PDF post-processing.

## Document Structure

### Chapter Organization
- `00 - frontmatter.md`: Executive summary, methodology, global snapshot table, evidence labels
- `01 - USA.md` through `09 - China.md`: Individual country/jurisdiction analyses

### Country Chapter Structure
Each country chapter follows a consistent structure:
1. **Final category** - What legal category the country uses (e.g., Critical Infrastructure Sector, Essential Entity)
2. **What is classified/designated** - Public vs confidential designation status
3. **Exact criteria** - Legal/regulatory criteria for designation
4. **Grading/tiering schemes** - Whether there are tiers of criticality
5. **Incident reporting** - Timelines and thresholds
6. **Health information systems** - Which systems are most likely treated as critical
7. **References** - Numbered citations to official sources

## Content Editing Principles
- **Evidence-based**: All claims must be sourced. Use evidence labels: (A) Explicit, (B) Guidance, (C) Criteria inference, (D) Expert judgement.
- **Distinguish interpretation from evidence**: Clearly mark interpretive statements vs direct legal citations.
- **Neutral comparative tone**: Describe what each jurisdiction does without advocating for one approach.
- **Jurisdiction-accurate terminology**: Use each country's actual legal terms (e.g., "OES" for UK, "Essential Entity" for EU, "Critical Infrastructure Sector" for USA).
- **Current as of date**: Note the "updated through" date in frontmatter; update when adding new regulatory developments.

## Naming, Style & Assets
- Markdown files: `NN - Title.md` (two-digit prefix, space-dash-space, title).
- Python scripts: 4-space indents; prefer `pathlib`. Keep scripts short and procedural.
- Assets: lowercase with underscores; reference relatively from chapter files.

## Testing & Validation
- No automated tests. Validation = clean pandoc run plus manual review of DOCX/PDF.
- Check that tables render correctly (especially the Global Snapshot table in frontmatter).
- Verify all reference links are formatted consistently.

## Git, Commits & PRs
- Branch: `main`. Use clear, present-tense commit messages (e.g., "Add Japan incident reporting thresholds").
- PRs should note which jurisdictions were updated and whether new regulatory developments are included.

## Security & Dependencies
- Do not embed secrets or internal URLs.
- Dependencies: pandoc, xelatex, uv (Python). Note any new Lua filters or LaTeX packages in README.

## Key Terminology

### Designation Models (used throughout)
- **System-based designation**: Specific systems are designated
- **Entity-based designation**: Operators/providers are designated (systems they run become in-scope)
- **Asset-based designation**: Specific assets/facilities are designated
- **Sector-based regulation**: Obligations apply to classes of organizations, often with thresholds

### Common Regulatory Terms
- **NIS2 (EU)**: Network and Information Systems Directive 2
- **CER (EU)**: Critical Entities Resilience Directive
- **CIRCIA (USA)**: Cyber Incident Reporting for Critical Infrastructure Act
- **OES (UK)**: Operator of Essential Services
- **RDSP (UK)**: Relevant Digital Service Provider
- **HPH (USA)**: Healthcare and Public Health Sector
- **SOCI (Australia)**: Security of Critical Infrastructure Act

### Evidence Labels
- **(A) Explicit**: Directly stated in law/regulation
- **(B) Guidance**: Stated in regulator guidance or policy documents
- **(C) Criteria inference**: Inferred from published designation criteria
- **(D) Expert judgement**: Reasoned judgement where sources are incomplete

## Jurisdictions Covered
1. USA - Healthcare and Public Health Sector / CIRCIA
2. Australia - SOCI Act / Critical Infrastructure
3. EU - NIS2 / CER Directives
4. Canada
5. UK - NIS Regulations / OES framework
6. Germany
7. Singapore
8. New Zealand
9. Japan
10. China

## Important Notes
- This is a **comparative policy research document**, not an institutional policy.
- Focus on accurate representation of each jurisdiction's legal framework.
- Keep regulatory updates current - note effective dates and upcoming deadlines.
- The document serves policymakers, security professionals, and researchers comparing approaches globally.
