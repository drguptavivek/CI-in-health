# Methodology
identifying, extracting, shortlisting, and categorising “highest-critical / protected” health information systems

This chapter documents the **repeatable method** used to identify country frameworks, extract only verifiable requirements, shortlist what qualifies as “highest critical / protected,” and categorise regimes consistently across jurisdictions (as applied in the country chapters already produced).  


## 1) Objective and unit of analysis

**Objective:** Determine, for each jurisdiction, the **highest critical / protected categories** that can apply to the **health sector and/or health information systems**, and document:

* the **exact legal/regulatory trigger** (definition + threshold test),
* any **tiering / grading scheme**,
* **incident reporting triggers + deadlines**, and
* what is **explicitly health-specific** vs **cross-sector but applicable to health**.

**Unit of analysis:** Always record what the instrument legally regulates:

* **Entity-level** classification (e.g., “essential entity” vs “important entity”), or
* **Asset/system-level** designation (e.g., “designated system/installation”), or
* **Sector-level** recognition (e.g., “health as a critical sector”) when no designation mechanism exists.


## 2) Evidence hierarchy (what counts as “primary”)

To meet a strict evidence standard, sources are ranked and used in this order:

1. **Primary legal texts** (acts, regulations, directives, annexes/schedules, official compilations).
2. **Official regulator/government guidance** that is explicitly issued under, or directly interprets/implements, the primary instrument (e.g., competent authority guidance containing reporting thresholds).
3. **Official explanatory materials** (explanatory memoranda/notes, government bill notes) used only to explain **what the law states**, not to invent new thresholds.
4. **Secondary sources** (law firm notes, academic papers, blogs) are **not used to assert obligations** unless the underlying primary text is also captured; if referenced, they are labelled as secondary.

**Hard rule:** If a cited document cannot be accessed/verified in full text, it is **not used** to support a factual claim; it is listed as **“not accessible in this environment”** (transparency note).


## 3) Source discovery and retrieval workflow

For each jurisdiction:

1. **Start from the canonical portal** for legislation (e.g., official gazette/legislation website, EUR-Lex, etc.).
2. Identify the **top instrument(s)** that create “critical/essential” obligations:

   * cybersecurity/critical infrastructure statute,
   * sectoral implementing regulation,
   * annexes/schedules that contain **sector lists** or **numeric thresholds**.
3. Retrieve **competent authority guidance** only where it contains *operational tests* (e.g., explicit “significant incident” thresholds, reporting routes).
4. Capture **version and date** (consolidation date, amendment date, entry into force date) for each instrument.


## 4) Extraction template (what we extract from each source)

For every instrument, extract only text that supports one of the following fields:

**A. Final category (the legal label)**

* Exact legal term(s): e.g., “critical infrastructure installation,” “operator of essential services,” “designated critical information infrastructure,” etc.

**B. Trigger criteria**

* **Definition clause** (what the category is).
* **Threshold test** (numeric or qualitative; annex/schedule thresholds where available).
* **Designation mechanics** (who designates; notice; duration; confidentiality of registers, if stated).

**C. Tiering / grading**

* Binary vs tiered system; the legal names of tiers; annex references.

**D. Incident reporting tests**

* Trigger term used by law/guidance (“significant incident,” “covered incident,” etc.).
* Deadlines (24h/72h/other) and the legal basis for the clock.

**E. Health-specific hooks**

* Where health is **explicitly named** as a sector/service (or where “medical services,” “healthcare providers,” “hospitals,” etc. appear in annexes).

**F. Public vs confidential**

* Only recorded if the instrument explicitly states registry confidentiality / publication requirements.



## 5) Shortlisting logic (inclusion / exclusion)

### Inclusion criteria (a framework is shortlisted if it meets any of the following)

1. The legal text **explicitly names health/medical services** as a critical/essential sector/type; **or**
2. The legal text creates a **designation category** that clearly can include health systems by function (e.g., “essential service” including public health) and the health mapping is explicitly present in annex/guidance; **or**
3. The instrument imposes **incident reporting/security obligations** on regulated entities/systems and health entities are explicitly in-scope.

### Exclusion criteria (do not include as “highest critical/protected” category)

1. General cybersecurity or data protection obligations **without a “critical/essential” scoping mechanism** (i.e., applies to everyone equally).
2. Voluntary strategies/whitepapers without binding designation tests or mandatory obligations.
3. Purely operational best-practice documents **not anchored** to an identified legal/regulatory regime.
4. Secondary commentary that cannot be traced to accessible primary text.



## 6) Categorisation scheme used across countries (normalisation)

To compare jurisdictions consistently, each country is categorised along **two orthogonal axes**:

**Axis 1 — What is classified**

* **Entity-based regimes** (regulated organisations): e.g., essential/important entities.
* **Asset/system-based regimes** (designated installations/systems): e.g., designated CII, KRITIS installations, designated systems.
* **Sector-based framing** (health as a CI sector, but without a public designation list).

**Axis 2 — How inclusion is triggered**

* **Explicit sector listing** (health/medical named in annex/sector list).
* **Threshold-based** (numeric thresholds like bed counts/case volumes/customers served).
* **Designation-based** (authority determination/notice, often non-public lists).
* **Consequence-based overrides** (“regardless of size” / “significant public health impact” triggers).

This normalisation enables consistent comparison even when countries regulate different objects (entities vs assets).  



## 7) Quality assurance and “zero-interpretation” controls

To keep the output strictly evidentiary:

* **Every factual claim is tied to a citation** (act/regulation clause, annex, or competent authority guidance).
* Any inference is either:

  * **not made**, or
  * clearly labelled as **interpretation** and separated from the “evidence-only” core (depending on the document’s rules; for strictest mode, interpretations are omitted).
* **Cross-check dates** (amendment/entry into force) against official sources.
* Maintain a **change log**: if new PDFs are supplied, update only the portions affected and record what changed.



## 8) Handling language and translation

* Prefer **official English translations** where available (official ministries, EUR-Lex English, etc.).
* If only local-language law is available, extract from:

  * official consolidated text, and
  * reputable official/semiofficial translations where explicitly identified.
* Do **not** “fill gaps” with guessed translation; instead record the limitation.



## 9) Known limitations (explicitly documented)

* Some regimes intentionally keep **designation lists non-public**; in such cases, the methodology can document **the designation test** and **the secrecy rule**, but cannot confirm named systems/operators from public sources.
* Where official portals block access (e.g., technical/geoblocking), the chapter notes the access limitation and relies only on alternative official materials that were successfully retrieved.

