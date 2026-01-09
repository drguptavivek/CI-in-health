# Health Sector Critical Information Infrastructure: Metrics and Grading Framework

## Introduction

This chapter synthesizes the comprehensive analysis of 17 jurisdictions to define a **metrics-based framework** for identifying and classifying health sector entities as **Critical Information Infrastructure (CII)**. The framework combines quantitative thresholds with qualitative criteria, drawing on global best practices to create a practical, adaptable approach.

---

## Part 1: Designation Metrics

### 1.1 Quantitative Thresholds (Direct Evidence from Global Frameworks)

| Metric Category | Threshold | Jurisdiction Source | Evidence Level |
|:----------------|:----------|:--------------------|:---------------|
| **Inpatient case volume** | ≥30,000 full inpatient cases/year | Germany (BSI-KritisV Anhang 5) | Explicit |
| **ICU presence** | Hospital has a general ICU (capable of mechanical ventilation for several days + invasive cardiovascular monitoring) | Australia (SOCI Act 2018) | Explicit |
| **Organization size** | ≥50 employees OR €10M+ annual turnover | EU NIS2 Directive | Explicit |
| **Laboratory throughput** | ≥1,500,000 diagnostic tests/year | Germany (BSI-KritisV) | Explicit |
| **Blood/plasma production** | ≥34,000 products manufactured or marketed/year | Germany (BSI-KritisV) | Explicit |
| **Customer impact (national)** | Service loss affecting >100,000 customers | New Zealand (NVA 2023) | Explicit |
| **Customer impact (regional)** | Service loss affecting 20,000–100,000 customers | New Zealand (NVA 2023) | Explicit |

### 1.2 Qualitative Designation Criteria

#### Functional Criticality Criteria (from 17 jurisdictions)

| Criterion | Description | Jurisdiction Examples |
|:----------|:------------|:----------------------|
| **Sole provider** | Entity is the only provider of an essential service in a geographic area | EU NIS2, UK, Singapore |
| **Debilitating effect** | System compromise would have a debilitating effect on service availability | Singapore (Cybersecurity Act) |
| **Public health impact** | Disruption could seriously affect public health or safety | EU NIS2, Norway, Thailand, France |
| **Cross-border impact** | Significant systemic risk with potential cross-border effects | EU NIS2 |
| **Life-safety dependency** | Direct dependency for life-critical patient care | All 17 jurisdictions |
| **National/regional importance** | Critical due to specific importance at national or regional level | EU NIS2, South Korea |
| **Core function essentiality** | System is essential to the core function of the infrastructure | Hong Kong |
| **Substitutability** | Difficult to substitute or replace | France, Hong Kong |

---

## Part 2: Multi-Tier Classification Framework

### 2.1 Recommended Three-Tier Model

Based on global synthesis, a **three-tier classification** balances precision with administrative feasibility:

```
┌─────────────────────────────────────────────────────────────────┐
│                     TIER 1: ESSENTIAL                           │
│     (Highest obligations, ex-ante supervision, 24/7 monitoring) │
├─────────────────────────────────────────────────────────────────┤
│                     TIER 2: IMPORTANT                           │
│     (Moderate obligations, ex-post supervision, regular audits) │
├─────────────────────────────────────────────────────────────────┤
│                     TIER 3: BASELINE                            │
│     (Basic cyber hygiene, voluntary reporting, self-assessment) │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Tier Definitions and Criteria

#### TIER 1: Essential (Critical)

| Criterion | Threshold/Test | Weight |
|:----------|:---------------|:-------|
| **Quantitative Size** | Meets ANY explicit threshold (e.g., ≥30,000 cases/year OR ≥50 employees) | High |
| **ICU/Emergency Capability** | Hospital with ICU and/or major trauma/emergency department | High |
| **National System** | Operates a national-level health information system | High |
| **Sole Provider** | Only provider of essential health service in region | High |
| **Blood/Organ Services** | Operates blood bank, organ allocation, or transfusion services at national/regional level | High |
| **Disease Surveillance** | Operates infectious disease surveillance at national/regional level | High |

**Examples of Tier 1 Entities:**
- Major hospitals with ICU and emergency departments
- National/regional health information exchanges (EHR platforms)
- National blood and organ allocation services
- Disease surveillance and epidemic response systems
- Emergency ambulance dispatch systems (CAD)
- Class III Grade A hospitals (China terminology)

---

#### TIER 2: Important

| Criterion | Threshold/Test | Weight |
|:----------|:---------------|:-------|
| **Moderate Size** | Employs 10-49 OR €2M-€10M turnover | Medium |
| **Regional Service** | Provides essential services at regional/metropolitan level | Medium |
| **Supply Chain Criticality** | Key supplier to Tier 1 entities | Medium |
| **Specialty Care** | Specialty hospital or referral center | Medium |
| **Diagnostic Services** | Medical laboratories (reference/diagnostic) | Medium |
| **Pharmaceutical** | Pharmaceutical manufacturers/distributors | Medium |


**Examples of Tier 2 Entities:**
- Community hospitals without ICU but with significant ED
- Reference and diagnostic laboratories
- Pharmaceutical manufacturers and distributors
- Medical device manufacturers (especially IVD and implantables)
- Regional immunization registries
- Managed service providers (MSPs) serving health sector

---

#### TIER 3: Baseline

| Criterion | Threshold/Test | Weight |
|:----------|:---------------|:-------|
| **Small Enterprise** | <10 employees AND <€2M turnover | Low |
| **Local Service** | Provides primarily local/community services | Low |
| **Redundancy Available** | Alternative providers exist in the service area | Low |
| **Non-acute Care** | Outpatient specialty, primary care, wellness | Low |

**Examples of Tier 3 Entities:**
- Primary care/GP clinics (unless sole provider)
- Outpatient specialty clinics
- Dental practices
- Allied health providers
- Health research institutions (non-pandemic)

---

## Part 3: Scoring Methodology

### 3.1 Weighted Scoring Matrix

A **point-based scoring system** translates criteria into tier classification:

| Domain | Criterion | Points | Max Points |
|:-------|:----------|:------:|:----------:|
| **A. Scale** | | | **30** |
| | ≥30,000 inpatient cases/year | 30 | |
| | 15,000–29,999 cases/year | 20 | |
| | 5,000–14,999 cases/year | 10 | |
| | <5,000 cases/year | 5 | |
| **B. Capability** | | | **25** |
| | General ICU present | 25 | |
| | High-dependency unit (no ICU) | 15 | |
| | Emergency department only | 10 | |
| | No acute care capability | 0 | |
| **C. Functions** | | | **25** |
| | Emergency dispatch (111/999/911) | 25 | |
| | Blood bank/transfusion services | 20 | |
| | Disease surveillance (national/regional) | 20 | |
| | Organ allocation services | 20 | |
| | National EHR/HIE platform | 25 | |
| | Regional EHR/HIE platform | 15 | |
| **D. Uniqueness** | | | **10** |
| | Sole provider in region | 10 | |
| | Unique specialty capability | 8 | |
| | Alternative providers available | 0 | |
| **E. Dependencies** | | | **10** |
| | Cross-sector dependencies (telecom, power) | 10 | |
| | Other health systems depend on this entity | 8 | |
| | Limited external dependencies | 3 | |

### 3.2 Tier Classification Thresholds

| Tier | Score Range | Classification |
|:-----|:------------|:---------------|
| **Tier 1** | ≥60 points | Essential |
| **Tier 2** | 30–59 points | Important |
| **Tier 3** | <30 points | Baseline |

### 3.3 Automatic Tier 1 Triggers ("Regardless of Size" Criteria)

Regardless of score, an entity is automatically classified as **Tier 1** if:

1. **Sole provider** of an essential health service in a geographic area
2. Operates a **national-level** health information system
3. Operates **emergency ambulance dispatch** or **air ambulance** services
4. Operates **blood or organ allocation** services at national/regional level
5. Operates national/regional **infectious disease surveillance**
6. Explicitly designated by competent authority as **CII**

---

## Part 4: System-Level Metrics

### 4.1 Critical Health Information Systems (Global Consensus)

The following systems are prioritized across **80%+ of jurisdictions**:

| System Category | Criticality Rationale | Tier |
|:----------------|:----------------------|:-----|
| **Emergency Dispatch (CAD)** | Immediate life-safety impact | 1 |
| **Hospital EMR/EHR** (ICU/ED settings) | Direct patient care continuity | 1 |
| **ICU Monitoring Systems** | Real-time life support | 1 |
| **Blood Bank/Transfusion** | Immediate clinical dependency | 1 |
| **Disease Surveillance** | Epidemic response capability | 1 |
| **National EHR/HIE** | Systemic healthcare function | 1 |
| **Operating Theatre Management** | Surgical care continuity | 1-2 |
| **Pharmacy Management** | Medication safety | 1-2 |
| **LIMS (Laboratory)** | Diagnostic capability | 2 |
| **RIS/PACS (Radiology)** | Diagnostic capability | 2 |
| **Hospital ADT/PAS** | Administrative continuity | 2 |
| **ePrescribing** | Medication management | 2 |
| **Immunization Registries** | Public health function | 2 |
| **Organ Transplant Allocation** | Life-critical matching | 1 |

### 4.2 System Criticality Scoring

| Factor | Assessment Question | Score |
|:-------|:--------------------|:-----:|
| **Availability Impact** | Service unavailable: life-threatening within 4 hours? | 0-10 |
| **Integrity Impact** | Data corruption: direct patient harm possible? | 0-10 |
| **Confidentiality Impact** | Breach: significant personal health data exposure? | 0-10 |
| **Substitutability** | Manual workaround available? | 0-10 |
| **Recovery Time** | RTO > 24 hours = critical | 0-10 |

**Total: 50 points maximum**

| Score | System Tier |
|:------|:------------|
| ≥35 | Tier 1 System |
| 20–34 | Tier 2 System |
| <20 | Tier 3 System |

---

## Part 5: Incident Impact Thresholds

### 5.1 UK-Style Quantitative Thresholds (Most Explicit Globally)

| Impact Category | Threshold | Tier Applicability |
|:----------------|:----------|:-------------------|
| **Excess fatalities** | >0 | All tiers |
| **Potential clinical harm** | >50 patients at risk | Tier 1, 2 |
| **ED closure/diversion** | >3 hours (major trauma center) | Tier 1 |
| **ED closure/diversion** | >24 hours (other hospitals) | Tier 2 |
| **Outpatient appointments cancelled** | >1,500 | Tier 1, 2 |
| **Inpatient episodes cancelled** | >250 | Tier 1, 2 |
| **Emergency call-taking unavailable** | >3 hours | Tier 1 |
| **Data breach** | >30,000 records | All tiers |

### 5.2 Reporting Timelines (Global Convergence)

| Reporting Stage | Standard | Tier 1 | Tier 2 | Tier 3 |
|:----------------|:---------|:------:|:------:|:------:|
| **Early Warning** | 12–24 hours | 12h | 24h | N/A |
| **Detailed Notification** | 48–72 hours | 48h | 72h | 72h |
| **Final Report** | 14–30 days | 14d | 30d | 30d |
| **Ransom Payment** | 24 hours | 24h | 24h | 24h |

---

## Part 6: Composite Grading Framework

### 6.1 Final Classification Matrix

```
ENTITY CLASSIFICATION = f(Entity Score, System Criticality, Function Type)

                     ┌───────────────────────────────────────────┐
                     │           FUNCTION TYPE                   │
                     ├─────────────┬─────────────┬───────────────┤
                     │ Life-Safety │ Diagnostic  │ Administrative│
         ┌───────────┼─────────────┼─────────────┼───────────────┤
         │ Score ≥60 │   TIER 1    │   TIER 1    │    TIER 2     │
ENTITY   ├───────────┼─────────────┼─────────────┼───────────────┤
SCORE    │ Score 30-59│   TIER 1   │   TIER 2    │    TIER 2     │
         ├───────────┼─────────────┼─────────────┼───────────────┤
         │ Score <30 │   TIER 2    │   TIER 2    │    TIER 3     │
         └───────────┴─────────────┴─────────────┴───────────────┘
```

### 6.2 Obligations by Tier

| Obligation | Tier 1 | Tier 2 | Tier 3 |
|:-----------|:------:|:------:|:------:|
| **Risk Management Plan** | Required | Required | Recommended |
| **Security Officer (CISO)** | Required | Required | Optional |
| **Annual Risk Assessment** | Required | Required | Recommended |
| **Security Audit** | Annual | Biennial | Self-assessment |
| **Incident Reporting** | 12h/48h mandatory | 24h/72h mandatory | Voluntary |
| **Cyber Exercise Participation** | Mandatory | Encouraged | Voluntary |
| **Supply Chain Security** | Required | Required | Recommended |
| **24/7 Monitoring** | Required | Recommended | Optional |
| **Business Continuity Plan** | Required | Required | Recommended |
| **Regulatory Supervision** | Ex-ante | Ex-post | Self-regulated |

### 6.3 Penalty Framework (Proportionate)

| Tier | Maximum Administrative Fine | Basis |
|:-----|:----------------------------|:------|
| **Tier 1** | €10M or 2% global turnover | EU NIS2 model |
| **Tier 2** | €7M or 1.4% global turnover | EU NIS2 model |
| **Tier 3** | Warning → Compliance order | Graduated |

---

## Part 7: Implementation Guidance

### 7.1 Self-Assessment Questionnaire

Entities should complete the following to determine preliminary tier classification:

| Question | Yes Score | No Score |
|:---------|:---------:|:--------:|
| Do you operate an ICU? | +25 | 0 |
| Do you provide emergency ambulance dispatch? | +25 | 0 |
| Do you operate blood/organ allocation services? | +20 | 0 |
| Do you have ≥30,000 inpatient cases/year? | +30 | 0 |
| Are you the sole provider of essential services in your area? | +10 | 0 |
| Do you operate a national/regional disease surveillance system? | +20 | 0 |
| Do you have ≥50 employees? | +10 | 0 |
| Do other health systems depend on your systems? | +8 | 0 |

**Preliminary Classification:**
- Score ≥60 → Likely Tier 1
- Score 30–59 → Likely Tier 2
- Score <30 → Likely Tier 3

### 7.2 Regulatory Review Process

1. **Self-Assessment** → Entity completes questionnaire and submits to regulator
2. **Validation** → Regulator reviews against national health data
3. **Designation** → Entity receives written notification of tier classification
4. **Appeals** → 30-day window to contest classification
5. **Periodic Review** → Classification reviewed every 2 years (EU NIS2 model)

### 7.3 Transition Timeline

| Phase | Timeline | Activity |
|:------|:---------|:---------|
| **Phase 1** | Months 1-3 | Self-assessment by entities |
| **Phase 2** | Months 4-6 | Regulatory validation and designation |
| **Phase 3** | Months 7-12 | Compliance planning and gap analysis |
| **Phase 4** | Months 13-18 | Full compliance (Tier 1 first) |
| **Phase 5** | Months 19-24 | Full compliance (all tiers) |

---

## Part 8: Reference Jurisdictions for Each Component

| Framework Component | Primary Reference | Secondary Reference |
|:--------------------|:------------------|:--------------------|
| Quantitative thresholds | Germany (BSI-KritisV) | Australia (SOCI Act) |
| Three-tier structure | EU NIS2, Israel | Hong Kong |
| Incident reporting timelines | Hong Kong, Norway | EU NIS2 |
| Impact thresholds | UK (DHSC CAF) | — |
| "Regardless of size" triggers | EU NIS2 | Singapore |
| System-level designation | Singapore (CII) | Hong Kong |
| Public criteria/confidential lists | Most jurisdictions | South Korea (exception: public) |
| Proportionate penalties | EU NIS2 | Hong Kong |
| Registration obligation | Germany (NIS2) | Taiwan |
| Periodic review | EU NIS2 (2-year) | UK |

---

## Part 9: Developing Country Adaptations

> [!IMPORTANT]
> The thresholds derived from European, North American, and Australian frameworks (Parts 1-8) are calibrated for **developed healthcare systems** with high IT maturity, abundant regulatory capacity, and relatively uniform digital infrastructure. **Direct application to developing countries may be problematic** and requires significant adaptation.

### 9.1 Why Developed-Country Thresholds Are Inappropriate

| Factor | Developed Country Context | Developing Country Reality |
|:-------|:--------------------------|:---------------------------|
| **Case volume** | 30,000 inpatient cases = mid-size hospital | 30,000 cases may be a **major tertiary center** |
| **ICU availability** | Most hospitals have ICUs | ICU availability concentrated in metros; many districts have **zero ICU beds** |
| **Employee count** | 50 employees = small clinic | 50 employees may be a **district hospital** |
| **Digital maturity** | EHR penetration >80% | EHR penetration may be <20% in public sector |
| **Regulatory capacity** | Dedicated cyber agencies with health expertise | Nascent regulatory capacity; limited health-cyber specialists |
| **Connectivity** | Ubiquitous broadband | Intermittent connectivity in rural areas; offline-first systems critical |
| **Health system structure** | Insurance-based or tax-funded universal | Mixed public-private; large informal sector |

### 9.2 Adapted Threshold Framework for Developing Countries

#### A. Inpatient Case Volume (Adjusted)

| Tier | Developed Country Threshold | Developing Country Threshold | Rationale |
|:-----|:----------------------------|:-----------------------------|:----------|
| **Tier 1** | ≥30,000 cases/year | ≥10,000 cases/year | Lower threshold captures district/tertiary hospitals |
| **Tier 2** | 5,000–29,999 | 2,000–9,999 | Community and sub-district hospitals |
| **Tier 3** | <5,000 | <2,000 | PHCs and small facilities |

#### B. Bed Count Alternative (Where Case Data Unavailable)

| Tier | Developed Country | Developing Country (e.g., India) |
|:-----|:------------------|:---------------------------------|
| **Tier 1** | ≥500 beds | ≥200 beds OR District Hospital status |
| **Tier 2** | 100–499 beds | 50–199 beds OR Sub-District Hospital |
| **Tier 3** | <100 beds | <50 beds OR PHC/CHC |

#### C. Employee Count (Adjusted)

| Tier | EU NIS2 Threshold | Developing Country Threshold |
|:-----|:------------------|:-----------------------------|
| **Tier 1** | ≥250 employees | ≥100 employees |
| **Tier 2** | 50–249 employees | 25–99 employees |
| **Tier 3** | <50 employees | <25 employees |

### 9.3 India-Specific Critical Information Systems

Beyond the globally-recognized systems, **India has unique national digital health systems** that warrant CII consideration:

| System | Description | Criticality | Suggested Tier |
|:-------|:------------|:------------|:---------------|
| **Ayushman Bharat Digital Mission (ABDM)** | National digital health ID and ecosystem | National HIE equivalent | Tier 1 |
| **PM-JAY (Pradhan Mantri Jan Arogya Yojana)** | National health insurance platform for 500M+ beneficiaries | Financial access to healthcare | Tier 1 |
| **CoWIN** | COVID vaccination platform; adaptable for routine immunization | National immunization system | Tier 1 |
| **eVIN (Electronic Vaccine Intelligence Network)** | Cold chain and vaccine inventory management | Supply chain criticality | Tier 1-2 |
| **IHIP (Integrated Health Information Platform)** | Disease surveillance and outbreak response | Epidemic response | Tier 1 |
| **NIKSHAY** | TB surveillance and treatment tracking | Public health surveillance | Tier 1-2 |
| **RCH Portal (Reproductive & Child Health)** | Maternal and child health tracking | Population health | Tier 2 |
| **HMIS/eHospital** | Hospital management for central/state government hospitals | Hospital operations | Tier 2 |
| **NIC infrastructure for emergency services** | 112 ERSS (Emergency Response Support System) | Emergency dispatch | Tier 1 |
| **National Blood Transfusion Council systems** | Blood bank management | Blood supply chain | Tier 1-2 |

### 9.4 Geographic and Accessibility Criteria

In developing countries, **geographic accessibility** is a more relevant criticality factor than pure scale:

| Criterion | Application | Weight |
|:----------|:------------|:-------|
| **Sole provider in district** | Only hospital with surgical/obstetric capability in district | Automatic Tier 1 |
| **Distance to next facility** | Nearest equivalent facility >50km away | +15 points |
| **Population served without alternative** | Serves >100,000 population as primary referral | +15 points |
| **Border/remote area** | Located in border districts, islands, or hill regions with limited connectivity | +10 points |
| **Aspirational district** | Located in government-designated "aspirational district" | +10 points |

#### India-Specific Geographic Triggers

An entity should be automatically classified as **Tier 1** if:

1. **District Hospital** — Only referral hospital in the district
2. **FRU (First Referral Unit)** — Only facility with C-section/blood transfusion capability in the block/sub-district
3. **State reference laboratory** — Only accredited reference lab in the state
4. **Blood bank (standalone)** — Only licensed blood bank in the district
5. **Major Government Medical College Hospital** — Apex referral and training institution

### 9.5 Tiered Public Health System Considerations

India's **tiered public health infrastructure** requires adapted tier mapping:

| Health Facility Type | Typical Characteristics | Suggested CII Tier |
|:---------------------|:------------------------|:-------------------|
| **AIIMS / National Institutes** | Apex tertiary + research; 1,000+ beds | Tier 1 |
| **State/Central Government Medical College Hospitals** | Major tertiary; 500-1,500 beds | Tier 1 |
| **District Hospital (DH)** | District headquarters; 100-500 beds; surgery/obstetrics | Tier 1 (if sole in district) |
| **Sub-District Hospital (SDH)** | Taluk/sub-district; 30-100 beds | Tier 2 |
| **Community Health Centre (CHC)** | Block level; 30 beds; FRU function | Tier 2 (if sole FRU in block) |
| **Primary Health Centre (PHC)** | Primary care; 6 beds; limited digital systems | Tier 3 |
| **Health & Wellness Centre (HWC)** | Sub-centre upgrade; ASHA coordination | Tier 3 |
| **Major Private Corporate Hospitals** | 200+ beds; multi-specialty; extensive IT | Tier 1-2 (based on scale/function) |

### 9.6 Digital Maturity Considerations

| Factor | Developed Country Assumption | Developing Country Reality | Adaptation |
|:-------|:-----------------------------|:---------------------------|:-----------|
| **EHR adoption** | Universal or near-universal | Variable; paper-based common | Prioritize facilities with digital systems for CII scope |
| **Internet connectivity** | Always-on broadband | Intermittent; mobile-dependent | **Offline-capable systems** as critical; data sync mechanisms |
| **IT staffing** | Dedicated IT/security teams | Often shared/outsourced; limited capacity | **Shared services** (state-level SOC) as Tier 1 system |
| **Cloud vs on-premise** | Cloud-first / hybrid | On-premise or central data centers | **State Data Centers (SDCs)** hosting health systems as Tier 1 |
| **Supply chain visibility** | Integrated vendor management | Fragmented; informal procurement | Lower emphasis on third-party risk scoring initially |

### 9.7 Regulatory and Compliance Capacity

| Challenge | Developed-Country Approach | Developing-Country Adaptation |
|:----------|:---------------------------|:------------------------------|
| **Limited regulators** | Sector-specific competent authorities | **Single nodal agency** with health ministry support |
| **Audit capacity** | Annual third-party audits | **Phased approach**: Tier 1 first; self-assessment for Tier 3 |
| **Incident reporting** | Real-time portals; dedicated CERT | **Simplified reporting**: SMS/email fallback; longer initial timelines |
| **Penalties** | €10M+ fines | **Proportionate**: Compliance orders first; modest fines scaled to public sector budgets |
| **Technical guidance** | Sector-specific security standards | **Adopt/adapt** existing standards (ISO 27799, NIST Healthcare) with local context |

### 9.8 Adapted Incident Reporting Timelines

| Reporting Stage | Developed Country | Developing Country (Initial Phase) | Rationale |
|:----------------|:------------------|:-----------------------------------|:----------|
| **Early Warning** | 12–24 hours | 24–48 hours | Account for connectivity and capacity limitations |
| **Detailed Notification** | 48–72 hours | 72–96 hours | More time for investigation in resource-limited settings |
| **Final Report** | 14–30 days | 30–45 days | Extended analysis period |
| **Ransom Payment** | 24 hours | 24 hours | Keep consistent for law enforcement coordination |

### 9.9 India-Specific "Regardless of Size" Triggers

Regardless of scale, an entity should be **automatically Tier 1** in India if it:

1. Operates **ABDM (Ayushman Bharat Digital Mission)** infrastructure at national/state level
2. Operates **PM-JAY** transaction processing or beneficiary management systems
3. Is the **sole government hospital** in a district
4. Operates **112 ERSS** (National Emergency Number) dispatch for any state
5. Operates **state-level integrated disease surveillance** (IHIP)
6. Is a **national or regional reference laboratory** (NCDC, NIV, ICMR labs)
7. Operates **state blood bank council** or regional blood transfusion center
8. Is a **State Data Center** hosting health applications
9. Provides **telemedicine hub services** for remote/tribal areas (e.g., eSanjeevani hubs)
10. Operates **cold chain management systems** (eVIN) at state level

### 9.10 Developing Country Scoring Adjustments

#### Adjusted Scoring Matrix for Developing Countries

| Domain | Criterion | Points (Developed) | Points (Developing) |
|:-------|:----------|:------------------:|:-------------------:|
| **A. Scale** | | | |
| | ≥10,000 inpatient cases/year | — | 30 |
| | 5,000–9,999 cases/year | — | 20 |
| | 2,000–4,999 cases/year | — | 10 |
| **B. Public System Role** | | | |
| | District Hospital (sole in district) | — | 25 |
| | FRU (sole in block) | — | 20 |
| | CHC/PHC digitized | — | 5 |
| **C. Geographic Criticality** | | | |
| | Sole provider >50km radius | — | 20 |
| | Aspirational/border district | — | 10 |
| | Remote/tribal area | — | 10 |
| **D. National Program Integration** | | | |
| | Hosts ABDM/PM-JAY systems | — | 25 |
| | State disease surveillance node | — | 20 |
| | eVIN/immunization registry | — | 15 |

### 9.11 Phased Implementation Approach

Given capacity constraints, developing countries should adopt a **phased rollout**:

| Phase | Timeline | Scope | Focus |
|:------|:---------|:------|:------|
| **Phase 1** | Year 1 | National systems only | ABDM, PM-JAY, 112 ERSS, national surveillance, State Data Centers |
| **Phase 2** | Year 2 | Tier 1 entities (national + major tertiary) | AIIMS, GMCHs, major private chains, state blood banks |
| **Phase 3** | Year 3-4 | Tier 2 entities (district level) | District hospitals, state reference labs, regional facilities |
| **Phase 4** | Year 5+ | Tier 3 entities (voluntary) | PHCs, CHCs, small private hospitals |

### 9.12 Capacity Building Requirements

| Requirement | Developed Country | Developing Country Approach |
|:------------|:------------------|:----------------------------|
| **Sector-specific guidance** | Published standards (B3S, CAF) | **Develop simplified health CII security baseline** |
| **Training** | Commercial certifications | **Subsidized/free government training programs** |
| **Shared services** | Commercial MSPs | **State-level Security Operations Centers (SOCs)** for public health facilities |
| **Incident response** | Sector CERTs | **National Health-CERT** with state nodes |
| **Technical assistance** | Market-driven consulting | **Government technical support units** for compliance assistance |

### 9.13 Developing Country Case Studies

The following jurisdictions provide relevant models for adapting CII frameworks to developing country contexts:

---

#### A. China: Multi-Level Protection Scheme (MLPS) for Healthcare

**Key Features:**
- **Five-tier grading system** (Levels 1-5) applied to all network information systems
- **Explicit health-sector guidance** (2011 NHC directive) specifying which systems are "≥ Level 3"
- **Party-state designation authority** rather than purely market-based self-assessment

**Systems Explicitly Designated Level 3+ (Health Sector):**

| System Type | Level | Scope |
|:------------|:------|:------|
| Cross-province national networked systems (infectious disease reporting, health statistics) | ≥3 | National |
| National/provincial/municipal health information platforms | ≥3 | National/Provincial |
| Core business information systems of **Class III Grade A hospitals** (三级甲等医院) | ≥3 | Major tertiary hospitals |
| New Rural Cooperative Medical Scheme (NRCMS) systems | ≥3 | National |
| Health supervision and maternal & child health registries | ≥3 | National |

**Relevance for India:**
- China's "Class III Grade A" hospital threshold is conceptually similar to India's **AIIMS/major government medical college** tier
- The MLPS **annual evaluation requirement** for Level 3+ systems could inform India's audit approach
- Focus on **public health surveillance systems** as automatic high-tier matches India's IHIP context

---

#### B. Thailand: Public Health as CII Sector

**Key Features:**
- **Cybersecurity Act B.E. 2562 (2019)** explicitly includes **"Public Health"** as a CII sector (Section 49)
- **Committee-based designation** (case-by-case review by NCSC Committee)
- **Three cyber threat levels** (non-critical / critical / crisis) with "public health" explicitly referenced in "critical level" definition
- **September 2025 CII List Revision** updated health sector designations

**Designation Mechanism:**

| Element | Thailand Approach | Applicability |
|:--------|:------------------|:--------------|
| **Sector trigger** | "Public health" listed in Section 49 aspects | Qualitative, broad |
| **Designation process** | Committee notification → case-by-case review → Government Gazette publication | Administrative discretion |
| **No numeric thresholds** | Qualitative ("maintaining national security, public security, national economic security") | Flexible for diverse health system |
| **Annual assessment** | Risk assessment + examination at least once per year | Realistic for developing context |
| **Penalty** | ฿200,000 fine for non-reporting (modest by global standards) | Proportionate |

**Relevance for India:**
- Thailand's **qualitative designation** with committee discretion suits contexts where quantitative data is unreliable
- **Annual assessment** (not biennial) is achievable for high-tier facilities
- **Modest penalties** more appropriate than EU-style €10M fines for public-sector hospitals

---

#### C. Malaysia: National Critical Information Infrastructure (NCII)

**Key Features:**
- **NACSA (National Cyber Security Agency)** lists **"Healthcare Services"** as an NCII sector
- **Sector-based approach** with sector leads responsible for designation
- Part of broader **11-sector NCII framework**

**Model Elements:**

| Element | Malaysia Approach |
|:--------|:------------------|
| **Governing body** | NACSA (centralized coordination) |
| **Sector implementation** | Ministry of Health as sector lead |
| **Scope** | Hospitals, clinics, public health agencies |
| **Reporting** | Incident reporting to sector regulator → NACSA |

**Relevance for India:**
- Malaysia's **sector lead model** (health ministry coordination with central cyber agency) aligns with India's potential MoHFW + CERT-In + NCIIPC structure
- NACSA's role as **coordinating body** (not sole designator) mirrors India's federated model with state health departments

---

#### D. Indonesia: Vital Information Infrastructure (Perpres 82/2022)

**Key Features:**
- **Presidential Regulation 82/2022** establishes Vital Information Infrastructure protection
- **"Sektor Kesehatan" (Health Sector)** explicitly listed as strategic sector
- **BSSN (National Cyber and Crypto Agency)** as coordinating regulator

**Framework Structure:**

| Element | Indonesia Approach |
|:--------|:------------------|
| **Legal basis** | Presidential Regulation (Perpres) — fast executive action |
| **Sector classification** | Health listed among strategic sectors |
| **Designation authority** | Sector ministry with BSSN coordination |
| **Implementation** | Still developing detailed health-sector guidelines |

**Relevance for India:**
- Indonesia's use of **executive regulation** (Perpres) rather than primary legislation enables faster implementation
- Could inform India's approach via **IT Act rules** or **DPDP Act rules** rather than new legislation
- Both countries share **archipelago/large-geography** challenges requiring offline-first system considerations

---

#### E. Ghana: African Model for Health CII

**Key Features:**
- **Cyber Security Authority (CSA) directive** explicitly lists **"Health"** as a CII sector
- Part of **national CII protection framework** under Cybersecurity Act 2020
- Relatively early adopter in Sub-Saharan Africa

**Relevance for India:**
- Demonstrates that **even resource-limited contexts** can establish explicit health CII frameworks
- Ghana's approach emphasizes **sector listing first, detailed thresholds later** — incremental model

---

#### F. Kazakhstan / Kyrgyz Republic: Central Asian Models

**Key Features:**
- Both jurisdictions **explicitly include "healthcare"** in their CII/CIIC definitions
- **Legal text definitions** rather than detailed implementation guidance
- Reflects **post-Soviet legal tradition** of broad framework laws

| Country | Definition | Source |
|:--------|:-----------|:-------|
| **Kazakhstan** | "Critical information and communication infrastructure" explicitly includes **healthcare** | Adilet LIS CIIC Rules |
| **Kyrgyz Republic** | "Critical information infrastructure" includes the field of **healthcare** | Regulation for Information Protection in SIS |

**Relevance for India:**
- Shows that **explicit sector listing in law** is foundational — India could do this via IT Act amendment or DPDP rules
- Central Asian models are also adapting **Russian-style graduated protection** (similar to China's MLPS)

---

### 9.14 Comparative Summary: Developing Country Models

| Feature | China | Thailand | Malaysia | Indonesia | India (Proposed) |
|:--------|:------|:---------|:---------|:----------|:-----------------|
| **Sector explicitly listed** | ✓ (MLPS, CII Reg) | ✓ (Section 49) | ✓ (NCII) | ✓ (Perpres 82/2022) | ✓ (Recommend) |
| **Tiering system** | 5 levels | 3 threat levels | Binary | Binary | 3 tiers |
| **Quantitative thresholds** | No (Class III-A qualitative) | No | No | No | Yes (adapted) |
| **Hospital tier explicit** | Class III-A | No | No | No | Yes (AIIMS/DH/PHC) |
| **National systems separate** | Yes (Level 3+) | Implicit | Implicit | Implicit | Yes (ABDM, PM-JAY) |
| **Geographic factors** | No | No | No | No | Yes (sole provider) |
| **Audit frequency** | Annual (Level 3+) | Annual | Not specified | Not specified | Annual (T1) / Biennial (T2) |
| **Penalties** | Administrative sanctions | ฿200K fine | Not specified | Not specified | Proportionate |
| **Legal instrument** | Law + State Council Reg | Cybersecurity Act | Agency directive | Presidential Reg | IT Act rules / new law |

### 9.15 Recommended Approach for India

Based on global developing country models, the recommended approach for India:

1. **Explicit sector listing**: Amend IT Act rules or issue executive notification explicitly designating "Healthcare" as CII sector under existing NCIIPC framework

2. **Tiered designation with geographic factors**: Adopt 3-tier model with:
   - **Tier 1**: National digital systems + AIIMS/GMCHs + sole district providers
   - **Tier 2**: District hospitals + reference labs + major private chains
   - **Tier 3**: PHCs/CHCs (voluntary/self-regulated)

3. **Qualitative + quantitative hybrid**: Use adapted quantitative thresholds (10,000 cases/year, 200 beds) with qualitative triggers (sole provider, geographic remoteness)

4. **Committee-based designation** (Thailand model): Health-CII Designation Committee with MoHFW, MeitY, NCIIPC, and CERT-In representation

5. **Phased implementation** (China model): 
   - Year 1: National systems (ABDM, PM-JAY, 112 ERSS)
   - Year 2: Tier 1 facilities
   - Year 3-4: Tier 2 facilities

6. **Proportionate obligations**: 
   - Tier 1: Annual audits, 24-48h reporting, mandatory BCP
   - Tier 2: Biennial audits, 72-96h reporting
   - Tier 3: Self-assessment, voluntary reporting

7. **Shared services model**: State-level SOCs for public health facilities (leveraging NIC/state IT infrastructure)

8. **Health-CERT**: Establish sectoral CERT under MoHFW with CERT-In coordination (similar to sectoral CERTs in banking/power)

---



## Conclusion

This metrics and grading framework provides a **structured, evidence-based approach** for classifying health sector entities as Critical Information Infrastructure. Key design principles include:

1. **Hybrid criteria**: Combines quantitative thresholds with qualitative safety-net triggers
2. **Proportionality**: Three-tier structure aligns obligations with criticality
3. **Transparency**: Clear criteria enable self-assessment
4. **Adaptability**: Framework accommodates diverse health system contexts
5. **Global alignment**: Harmonized with emerging international standards

The framework should be adapted to national context, with particular attention to:
- Local health system structure and governance
- Existing regulatory frameworks
- Data availability for quantitative metrics
- Administrative capacity for enforcement

---

## References

This framework synthesizes criteria from the 17 jurisdictions analyzed in this study:

1. USA (CISA/HPH Sector)
2. Australia (SOCI Act 2018)
3. European Union (NIS2 Directive)
4. Canada (National CI Strategy)
5. United Kingdom (NIS Regulations / CAF)
6. Germany (BSI-KritisV / NIS2UmsuCG)
7. Singapore (Cybersecurity Act)
8. New Zealand (HISO 10029 / NVA)
9. Japan (CIP Policy)
10. China (Cybersecurity Law / MLPS)
11. South Korea (CIIC Act)
12. France (OIV/SAIV/SIIV)
13. Norway (Digital Security Act)
14. Switzerland (ISG/CSV)
15. Taiwan (CSMA)
16. Thailand (Cybersecurity Act)
17. Hong Kong (PCICSO)

