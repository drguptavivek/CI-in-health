# Global Classification of Health Information Systems as Critical Infrastructure
**A policy-grade comparative study (updated through January 2026)**
*Version 2.0 — January 2026*

## Overview
This repository contains a comprehensive comparative analysis of how different jurisdictions worldwide classify health-related information systems as **Critical Information Infrastructure (CII)** or equivalent constructs (e.g., Essential Services, Critical Entities). 
The study highlights the convergent prioritization of "life-and-safety" digital functions in healthcare and examines the varying regulatory frameworks, designation models, and incident reporting obligations that apply to these systems.

## Repository Structure
The content is organized into logical sections within the `chapters/` directory:
- **Introduction & Frontmatter**
  - [Frontmatter](chapters/00%20-%201%20-%20frontmatter.md)
  - [Executive Summary](chapters/00%20-%202%20-%20Executive%20Summary.md)
  - [Table of Contents](chapters/00%20-%203%20-%20TOC.md)
- **Jurisdiction Chapters**
  - [USA](chapters/01%20-%20USA.md)
  - [Australia](chapters/02%20-%20Australia.md)
  - [European Union (NIS2)](chapters/02%20-%20EU.md)
  - [Canada](chapters/03%20-%20Canada.md)
  - [United Kingdom (UK)](chapters/04%20-%20UK.md)
  - [Germany](chapters/05%20-%20Germany.md)
  - [Singapore](chapters/06%20-%20Singapore.md)
  - [New Zealand](chapters/07%20-%20NZ.MD)
  - [Japan](chapters/08%20-%20JAPAN.md)
  - [China](chapters/09%20-%20China.md)
  - [South Korea](chapters/10%20-%20South%20Korea.md)
  - [France](chapters/11%20-%20France.md)
  - [Norway](chapters/12%20-%20Norway.md)
  - [Switzerland](chapters/13%20-%20Switzerland.md)
  - [Taiwan](chapters/14%20-%20Taiwan.md)
  - [Thailand](chapters/15%20-%20Thailand.md)
  - [Hong Kong (HKSAR)](chapters/16%20-%20Hong%20Kong.md)
  - [Israel](chapters/17%20-%20Israel.md)
- **Synthesis & Summary**
  - [Comparative Summary](chapters/41%20-%20Summary.md)
  - [Multi-Region Evidence Table](chapters/50%20-%20Country%20summary.md)
- **Build Outputs**
  - [PDF Version](_build/CI_health.pdf)
  - [Word Version (DOCX)](_build/CI_health.docx)


## Methodology
This analysis synthesizes official legislation, competent-authority guidance, and policy literature updated through January 2026. Substantive claims are supported by primary evidence, with a clear distinction between explicit legal requirements and expert inferences.

## Build Instructions
The project uses a Python script to merge the chapters and convert them into PDF and Word formats using **Pandoc**.

### Prerequisites
- **Python 3.13+** (managed by **uv**)
- **Pandoc**: Required for document conversion.
- **XeLaTeX**: Required for PDF generation (ensure a TeX distribution like TeX Live or MiKTeX is installed).
- **Environment Setup**:
  ```bash
  uv sync
  ```

### Running the Build
To generate the distribution files in the `_build/` directory, run:
```bash
uv run b_build_policy.py
```

## Formatting Standards
Each jurisdiction chapter follows a standardized structure to ensure comparability:
1. Final categories
2. Exact legal/regulatory criteria
3. Grading/tiering scheme
4. Incident reporting tests and thresholds
5. Health information systems “most likely” designated
6. Public vs. Confidential
7. Latest updates (2025–2026)
8. References
*For more detailed findings, please see the [Executive Summary](chapters/00%20-%202%20-%20Executive%20Summary.md).*
