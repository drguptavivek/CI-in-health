# Global Classification of Health Information Systems as Critical Infrastructure

**A policy-grade comparative study (updated through January 2026)**
*Version 2.1 — January 2026*

## Overview

This repository contains a comprehensive comparative analysis of how different jurisdictions worldwide classify health-related information systems as **Critical Information Infrastructure (CII)** or equivalent constructs (e.g., Essential Services, Critical Entities).

The study highlights the convergent prioritization of "life-and-safety" digital functions in healthcare and examines the varying regulatory frameworks, designation models, and incident reporting obligations that apply to these systems.

**New in Version 2.1:** A complete CII Metrics and Grading Framework with 22 illustrative case studies covering healthcare delivery, digital platforms, diagnostics, pharma/biotech, public health programs, and registries/biobanks.

---

## Repository Structure

The content is organized into logical sections within the `chapters/` directory:

### Front Matter
- [Frontmatter](chapters/00%20-%201%20-%20frontmatter.md)
- [Executive Summary](chapters/00%20-%202%20-%20Executive%20Summary.md)
- [Table of Contents](chapters/00%20-%203%20-%20TOC.md)
- [Methodology](chapters/00%20-%204%20-%20Methods.md)

### Part 1: Jurisdiction Chapters (17 Countries)
| Region | Jurisdictions |
|:-------|:--------------|
| **North America** | [USA](chapters/01%20-%20USA.md), [Canada](chapters/03%20-%20Canada.md) |
| **Europe** | [EU (NIS2)](chapters/02%20-%20EU.md), [UK](chapters/04%20-%20UK.md), [Germany](chapters/05%20-%20Germany.md), [France](chapters/11%20-%20France.md), [Norway](chapters/12%20-%20Norway.md), [Switzerland](chapters/13%20-%20Switzerland.md) |
| **Asia-Pacific** | [Australia](chapters/02%20-%20Australia.md), [Singapore](chapters/06%20-%20Singapore.md), [New Zealand](chapters/07%20-%20NZ.MD), [Japan](chapters/08%20-%20JAPAN.md), [China](chapters/09%20-%20China.md), [South Korea](chapters/10%20-%20South%20Korea.md), [Taiwan](chapters/14%20-%20Taiwan.md), [Thailand](chapters/15%20-%20Thailand.md), [Hong Kong](chapters/16%20-%20Hong%20Kong.md) |
| **Middle East** | [Israel](chapters/17%20-%20Israel.md) |

### Part 2: Synthesis & Summary
- [Comparative Synthesis & Framework Design Recommendations](chapters/41%20-%20Summary.md)
- [Health as CII Sector - Multi-Region Evidence Table](chapters/50%20-%20Country%20summary.md)

### Part 3: CII Metrics and Grading Framework
- [CII Metrics and Grading Framework](chapters/60%20-%20CII%20Metrics%20and%20Grading%20Framework.md)
  - Designation Metrics (Quantitative & Qualitative)
  - Multi-Tier Classification Framework
  - Scoring Methodology
  - System-Level Metrics
  - Incident Impact Thresholds
  - Implementation Guidance
  - Developing Country Adaptations (India focus)

### Part 4: Case Studies (22 Illustrative Examples)

| Chapter | Domain | Case Studies |
|:--------|:-------|:-------------|
| [Overview & Index](chapters/61%20-%20Case%20Studies%20-%20Overview%20and%20Summary.md) | Summary | Complete index with key insights |
| [Healthcare Delivery](chapters/61%20-%20Case%20Studies%20-%20Healthcare%20Delivery.md) | Hospitals, CHCs, Telemedicine | 6 case studies |
| [Digital Health Platforms](chapters/62%20-%20Case%20Studies%20-%20Digital%20Health%20Platforms.md) | National HIE, PHR, HMIS | 4 case studies |
| [Diagnostics, Pharma & Biotech](chapters/63%20-%20Case%20Studies%20-%20Diagnostics%20Pharma%20Biotech.md) | Labs, Genomics, Manufacturing | 4 case studies |
| [Public Health Programs](chapters/64%20-%20Case%20Studies%20-%20Public%20Health%20Programs.md) | Surveillance, TB, NCD, Nutrition | 5 case studies |
| [Registries, Biobanks & Blood](chapters/65%20-%20Case%20Studies%20-%20Registries%20Biobanks%20Blood.md) | Cancer Registry, Biobank, Blood Services | 3 case studies |

### Build Outputs
- [PDF Version](_build/CI_health.pdf)
- [Word Version (DOCX)](_build/CI_health.docx)

---

## Key Findings

### Global Trends (2025-2026)
- **Convergence on all-hazard resilience** with expanded scope to supply chains
- **Stricter incident reporting**: 12-24h early warning, 48-72h detailed notification
- **Enhanced enforcement** with significant administrative penalties
- **Integration of new technologies**: AI, cloud, and OT/IoT security requirements

### Universal Prioritization
All jurisdictions consistently prioritize these health information systems:
1. Emergency dispatch/ambulance coordination
2. ICU/critical care patient monitoring
3. Blood bank/transfusion systems
4. Organ allocation systems
5. Disease surveillance platforms
6. National EHR/HIE infrastructure

### Framework Design Principles
1. **Hybrid designation models** (quantitative thresholds + qualitative triggers)
2. **"Regardless of size" exceptions** for sole providers and life-critical functions
3. **Tiered obligations** proportionate to criticality level
4. **Developing country adaptations** for different contexts

---

## Methodology

This analysis synthesizes official legislation, competent-authority guidance, and policy literature updated through January 2026. Key methodological principles:

- **Evidence hierarchy**: Primary legal texts → Official guidance → Explanatory materials
- **Strict verification**: Claims supported only by accessible primary sources
- **Consistent categorization**: Entity-based vs. asset-based vs. sector-based regimes
- **Transparency**: Access limitations explicitly documented

See [Methodology](chapters/00%20-%204%20-%20Methods.md) for full details.

---

## Build Instructions

The project uses a Python script to merge the chapters and convert them into PDF and Word formats using **Pandoc**.

### Prerequisites
- **Python 3.13+** (managed by **uv**)
- **Pandoc**: Required for document conversion
- **XeLaTeX**: Required for PDF generation (TeX Live or MiKTeX)

### Environment Setup
```bash
uv sync
```

### Running the Build
```bash
uv run python b_build_policy.py
```

Output files are generated in the `_build/` directory.

---

## Formatting Standards

Each jurisdiction chapter follows a standardized structure:
1. Final categories (legal labels)
2. Exact legal/regulatory criteria
3. Grading/tiering scheme
4. Incident reporting tests and thresholds
5. Health information systems "most likely" designated
6. Public vs. Confidential designation
7. Latest updates (2025–2026)
8. References

Each case study follows a standardized structure:
1. Entity profile
2. CII classification assessment (scoring)
3. Classification result with rationale
4. Applicable obligations by tier

---

## License

*For more detailed findings, please see the [Executive Summary](chapters/00%20-%202%20-%20Executive%20Summary.md).*

