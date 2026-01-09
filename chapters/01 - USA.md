```{=openxml}
<w:p><w:pPr><w:sectPr><w:pgNumType w:fmt="decimal" w:start="1"/></w:sectPr></w:pPr></w:p>
```

# UNITED STATES OF AMERICA (USA)

## Final category

**Healthcare and Public Health (HPH) Sector** — one of the U.S. **Critical Infrastructure Sectors**.

In the U.S. model, this is primarily a **sector-level classification** (not a single public “designated list” of health information systems).


## What is “classified” or “designated” in practice?

### 1) Sector classification (public)

CISA describes U.S. Critical Infrastructure as organized into multiple sectors; **Healthcare and Public Health** is one of them.

### 2) Entity/asset scoping for incident reporting (developing, rule-based)

Under **CIRCIA**, reporting obligations apply to **“covered entities”** in critical infrastructure (as further defined by rulemaking). The law sets **reporting timelines** (e.g., covered cyber incidents and ransomware payments) but the exact boundary of “covered entity” is operationalized through regulation.


## Exact criteria used (as expressed in the cited U.S. materials)

### A) Sector boundary (HPH scope)

The HPH sector includes both **public health** and **healthcare** functions/services (sector overview framing).

### B) Criticality logic that drives “what systems matter most” (functional dependence)

The HPH Sector-Specific Plan notes that the sector **depends on vast, complex information technology systems** and the **rapid, secure transmission and storage of large amounts of data**—a direct rationale for treating key health information systems as high-impact from a resilience/security perspective.

### C) CIRCIA reporting thresholds (obligation trigger)

CIRCIA sets statutory reporting clocks: **covered cyber incidents** must be reported **within 72 hours**, and **ransomware payments** **within 24 hours** (as summarized in the fact sheet).


## Is there grading / tiering of “criticality” for health information systems?

The U.S. approach is expressed more as:

* a **sector construct** (HPH as a CI sector), and
* **reporting/obligation scoping** via CIRCIA’s “covered entity / covered incident” framework,

rather than an explicit **public tiering scheme** that assigns every health information system to a graded level.

However, CISA operational publications do show **risk-impact thinking** (e.g., protection goals like availability/integrity for “critical HPH systems, functions, and data”).


## What is public vs confidential?
**Public**
* The fact that HPH is a **Critical Infrastructure Sector** is public.
* High-level reporting obligations and timelines under CIRCIA are public (as summarized by CISA).
**Potentially non-public / organization-specific**
* Exact lists of which specific hospitals/entities/systems are most critical in a given locality or network are typically handled through **risk management and coordination**, rather than a single universal public register in the materials provided.
* RVA-type findings are published in anonymized form; the advisory describes the engagement and outcomes without naming the organization.


## Which *health information systems* are most likely to be treated as “highest criticality” in the U.S. framing?
CISA sector documents and advisories emphasize **mission-essential functions**, **data dependence**, and **operational disruption patterns**. Consequently, the “highest criticality” systems in the health sector typically cluster into these categories:

### 1) Care-delivery operational systems (availability-critical)
Systems whose loss disrupts direct patient care delivery and continuity:
* Core clinical workflow platforms and associated identity/access dependencies (because HPH depends on large, complex IT and rapid/secure data flows).
CISA’s mitigation guide is explicit that threats can affect **critical HPH systems, functions, and data** and highlights patient-focused service impacts as a central concern.

### 2) Public-health coordination and information flows (societal-impact critical)

Systems enabling public health operations and situational awareness—because the sector’s planning and operations depend on **information sharing and data**. The SSP explicitly frames dependency on secure transmission/storage at scale.

### 3) Enterprise IAM / domain services and internal network controls (blast-radius critical)
CISA’s RVA advisory shows that once an attacker is “inside,” **misconfigurations/weak passwords** can enable **domain compromise**, and it highlights actions like **phishing-resistant MFA for administrative access**, removing default credentials, and **network segregation**—all pointing to IAM/domain control planes as high criticality in health enterprises.

### 4) Vulnerability/patch posture for legacy and exposed systems (exploitability critical)
The same RVA advisory documents issues such as weak password policy and stresses the importance of stronger credential hygiene (e.g., longer passwords), patching, and segregation when patching is not possible—patterns highly relevant to clinical environments with legacy platforms and constrained devices.

### 5) Ransomware resilience dependencies (operational continuity critical)
The ransomware advisory for HPH explicitly frames ransomware as an operational disruption problem for the sector—driving prioritization of systems needed for continuity of care and contingency operations.


## Practical “tests” (derived from the U.S. documents)

A health information system in the U.S. context is most plausibly “high criticality / highest security priority” if it satisfies one or more of these document-grounded tests:

1. **IT-dependence test:** It is part of the “vast, complex” IT environment required for healthcare delivery and for rapid, secure data movement/storage at scale.
2. **Service disruption test:** Its compromise materially affects “critical HPH systems, functions, and data,” especially patient-focused service continuity.
3. **Enterprise blast-radius test:** Its compromise enables broad takeover (e.g., domain compromise) or bypass of administrative control—highlighted by CISA’s RVA outcomes and recommended mitigations (phishing-resistant admin MFA, default credential removal, segregation).
4. **Regulatory reporting relevance test (CIRCIA):** Incidents affecting it are more likely to be “covered cyber incidents” (depending on final covered-entity definitions) and therefore time-bound reporting obligations (72h/24h) become operationally relevant for the owning organization.


## References (USA)
1. **CISA — Critical Infrastructure Sectors** (includes Healthcare and Public Health as a sector). ([CISA][1])

2. **CISA — Healthcare and Public Health Sector** (sector overview framing). ([CISA][2])

3. **NIPP Sector-Specific Plan: Healthcare and Public Health (2015)** — dependency on complex IT and rapid/secure data flows. ([CISA][3])

4. **CISA — CIRCIA Fact Sheet (2022)** — 72-hour covered incident reporting and 24-hour ransomware payment reporting timelines. ([CISA][4])

5. **CISA — AA23-349A: HPH Sector Risk & Vulnerability Assessment** — internal weaknesses leading to domain compromise; recommended mitigations. ([CISA][5])

6. **CISA — AA20-302A: Ransomware Activity Targeting the HPH Sector** — operational disruption framing for HPH ransomware. ([CISA][6])


[1]: https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors "Critical Infrastructure Sectors | CISA"

[2]: https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/critical-infrastructure-sectors/healthcare-and-public-health-sector "Healthcare and Public Health Sector | CISA"

[3]: https://www.cisa.gov/sites/default/files/2023-01/nipp-ssp-healthcare-public-health-2015-508.pdf "NIPP Healthcare and Public Health Sector-Specific Plan 2015"

[4]: https://www.cisa.gov/resources-tools/resources/circia-fact-sheet "CIRCIA Fact Sheet | CISA"

[5]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-349a "AA23-349A: Enhancing Cyber Resilience in the HPH Sector"

[6]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-302a "AA20-302A: Ransomware Activity Targeting the HPH Sector"

