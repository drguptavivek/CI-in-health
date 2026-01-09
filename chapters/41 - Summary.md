# Part 2: Comparative Synthesis & Framework Design Recommendations

## Comparative Framework Overview
This study provides deep-dive analysis of **17 jurisdictions** with detailed chapter coverage, plus an additional **20+ countries** surveyed in the multi-region overview table.

### Deep-Dive Jurisdictions (17 Countries)
| Country/Region | Designation Model | Transparency | Explicit Thresholds | 2025-2026 Updates |
| :---- | :---- | :---- | :---- | :---- |
| **USA** | Sector-level (HPH sector) | Frameworks public, priorities confidential | No (voluntary, qualitative) | **CIRCIA final rule expected (May 2026), 72-hr incident/24-hr ransom reporting** |
| **Australia** | Asset-level (ICU hospitals) | Criteria fully public, SoNS confidential | **Yes (ICU presence)** | **Ransomware payment reporting (May 2025), strict enforcement (Jan 2026)** |
| **EU (NIS2)** | Entity-level (Essential/Important) | Criteria fully public, lists vary by state | **Yes (≥50 employees, €10M)** | **CER Directive (July 2026 deadline), all-hazard resilience** |
| **Canada** | Sector-based (10 CI sectors) | CI definition public | No (qualitative) | **Bill C-8/CCSPA proposed (72-hr reporting)** |
| **UK** | Entity-level (OES) | Criteria public, lists confidential | **Yes (incident thresholds most explicit globally)** | **Cyber Security Bill (Nov 2025), expands to MSPs/suppliers, 24-hr reporting** |
| **Germany** | System/entity (KRITIS + NIS2) | **High (thresholds public)** | **Yes (30,000 inpatient cases/year)** | **NIS2 implementation law in force (6 Dec 2025)** |
| **Singapore** | System-level (individual CII) | Criteria public, lists confidential | No (qualitative "debilitating") | No major updates |
| **New Zealand** | Risk-based (HISO segmentation) | Partially public | No (qualitative, developing) | **PSR GOV framework (1 Oct 2025)** |
| **Japan** | Entity-level (discretionary) | Medium (hospital categories public) | No (qualitative "excluding small scale") | No major updates |
| **China** | System/entity (CII + MLPS) | Low (general criteria only) | No (party-state discretion) | No major updates |
| **South Korea** | Designation-based (CIIC) | **High (Official Gazette publication)** | No (5-factor qualitative test) | No major updates |
| **France** | Entity-level (OIV/SAIV) | Criteria public, lists confidential | No (qualitative) | No major updates |
| **Norway** | Entity-level (socially important services) | Criteria public | No (qualitative "significantly disruptive") | **Digital Security Act in force (1 Oct 2025), 24h/72h reporting** |
| **Switzerland** | Entity-level (CI operators) | Criteria public, entities via permits | No (qualitative, category-based) | **Cybersecurity Ordinance (CSV) in force (1 Apr 2025), 24h reporting** |
| **Taiwan** | Designation-based (CI providers) | Criteria public | No (administrative designation) | **CSMA revised (24 Sept 2025), MoDA as authority** |
| **Thailand** | Designation-based (CII orgs) | Criteria public (Gazette) | No (Committee notification) | No major updates cited |
| **Hong Kong** | Designation-based (CI operators) | **High (criteria + obligations public)** | No (qualitative "essential to core function") | **CI Ordinance in force (1 Jan 2026), 12h/48h/14d reporting** |
| **Israel** | Database security levels | Criteria public | **Yes (3-tier: Basic/Medium/High)** | **Privacy Law Amendment 13 effective (14 Aug 2025)** |

# Universal Health Information Systems Prioritized Globally

**Across all 17 deep-dive jurisdictions, consistent prioritization emerges for:**

1. **Emergency call-taking and ambulance dispatch** (111/112/119/911/999 + Computer Aided Dispatch)  
2. **Major hospital core clinical systems** (EMR/EHR, EDIS, ICU monitoring)  
3. **Intensive care unit systems** (explicitly: Australia, UK, Germany; implicitly: all others)  
4. **Blood bank and transfusion services** (national/regional level)  
5. **National/regional infectious disease surveillance**  
6. **National health information infrastructure** (where exists: electronic prescription, national EHR)
**High but variable priority:**

7. Ambulance electronic patient care records (ePCR/ePRF)  
8. Operating theatre management and anesthesia systems  
9. Hospital laboratory information systems (LIMS)  
10. Pharmacy management and ePrescribing (hospital-based)  
11. Medical imaging systems (PACS/RIS in acute settings)  
12. National immunization registries  
13. Organ and tissue transplant allocation systems

**Lower priority (but still important):**

* Community hospital systems (if alternatives exist)  
* Primary care / GP systems (unless sole provider)  
* Outpatient specialty clinics  
* Health research systems (non-pandemic)  
* Administrative/billing systems

# Emerging Global Trends (2025-2026)

### Key Regulatory Milestones (2025-2026)
| Date | Jurisdiction | Milestone |
|:-----|:-------------|:----------|
| **1 Apr 2025** | Switzerland | Cybersecurity Ordinance (CSV) enters into force; 24-hour reporting |
| **30 May 2025** | Australia | Mandatory ransomware payment reporting in effect |
| **14 Aug 2025** | Israel | Privacy Protection Law Amendment 13 enters into force |
| **24 Sept 2025** | Taiwan | Revised Cyber Security Management Act promulgated |
| **1 Oct 2025** | Norway | Digital Security Act and Regulations enter into force |
| **1 Oct 2025** | New Zealand | PSR GOV Policy Framework implemented |
| **Nov 2025** | UK | Cyber Security and Resilience Bill introduced |
| **6 Dec 2025** | Germany | NIS2 implementation law (NIS2UmsuCG) enters into force |
| **1 Jan 2026** | Australia | Strict enforcement posture begins |
| **1 Jan 2026** | Hong Kong | Protection of Critical Infrastructures Ordinance enters into force |
| **May 2026** | USA | CIRCIA final rule expected |
| **17 July 2026** | EU | CER Directive deadline for identifying critical entities |

### 1. Supply Chain Regulation Expansion

* **UK**: New Bill explicitly targets **Managed Service Providers (MSPs)** and **critical suppliers**  
* **EU**: NIS2 includes manufacturers of medical devices and pharmaceuticals  
* **Implication**: Future frameworks must include criteria for assessing and mandating security standards for third and fourth-party vendors

### 2. All-Hazard Resilience Integration

* **EU CER Directive**: Mandates resilience plans for physical, environmental, natural disaster, and supply chain disruptions  
* **Shift**: Moving beyond pure cybersecurity to require planning for broader disruptions that could impact digital services  
* **Implication**: Critical infrastructure frameworks should integrate business continuity planning for multi-hazard scenarios

### 3. Stricter & Harmonized Incident Reporting
Global convergence towards standardized reporting timelines:
| Reporting Stage | Common Standard | Examples |
|:----------------|:----------------|:---------|
| **Early warning** | 12-24 hours | Hong Kong (12h), Norway (24h), Switzerland (24h), EU NIS2 (24h) |
| **Detailed notification** | 48-72 hours | Hong Kong (48h), Norway (72h), EU NIS2 (72h), USA CIRCIA (72h) |
| **Final report** | 14-30 days | Hong Kong (14d), Norway (1 month), EU NIS2 (1 month) |
| **Ransom payment** | 24 hours | USA CIRCIA, Australia |

### 4. Enhanced Enforcement Postures

* **Australia**: Shift to "stricter enforcement-oriented posture" from January 2026  
* **EU**: Significant penalties (up to €10M or 2% global turnover)  
* **Hong Kong**: Fines up to HK$5M for non-compliance with CI operator obligations
* **Implication**: Compliance moving from voluntary guidance to mandatory requirement with serious consequences for non-compliance

# Key Policy Design Insights for New Jurisdictions
This section synthesizes lessons learned from the 17 jurisdictions analyzed, organized as actionable decision points for policymakers.

## Designation Model Trade-offs
| Model | Advantages | Disadvantages | Best For | Examples |
|:------|:-----------|:--------------|:---------|:---------|
| **Sector-based** (no designation) | Low administrative burden; covers all entities in sector | Lacks precision; may burden small providers unnecessarily | Countries with limited regulatory capacity | USA, Canada |
| **Entity-based designation** | Clear accountability; scales with organization | May miss critical small providers | Developed regulatory systems | UK (OES), EU (NIS2), France (OIV) |
| **System-based designation** | Precise; focuses on actual critical systems | Complex to administer; requires technical assessment | High IT maturity jurisdictions | Singapore (CII) |
| **Asset-based designation** | Clear thresholds; easy to verify | May be too rigid; misses critical functions at smaller sites | Jurisdictions wanting explicit rules | Australia (ICU hospitals), Germany (30k cases) |
| **Hybrid** | Flexible; covers edge cases | More complex to implement | Most jurisdictions moving this direction | Germany (KRITIS + NIS2), Hong Kong |
> **Recommendation for new countries:** Start with **sector + entity-based** for broad coverage, then add **system/asset thresholds** as regulatory capacity matures.


## Which Health Entities to Include (Global Consensus)
Based on analysis across all 17 jurisdictions, the following entities appear most frequently in CI/CII frameworks:

### Tier 1: Near-Universal Inclusion (explicitly included in 80%+ of frameworks)
| Entity Type | Notes | Example Jurisdictions |
|:------------|:------|:----------------------|
| **Hospitals with ICU/emergency capability** | Often defined by bed count or case volume | Australia, Germany, UK, EU, Hong Kong |
| **National/regional health information exchanges** | EHR platforms, health data networks | Singapore, Japan, Taiwan |
| **Blood and organ allocation services** | Often at national level | Germany, France, UK |
| **Disease surveillance systems** | Epidemic response capability | All jurisdictions (explicitly or implicitly) |
| **Emergency ambulance dispatch (CAD)** | Often in "emergency services" sector | UK, EU, Australia |

### Tier 2: Frequently Included (50-80% of frameworks)
| Entity Type | Notes | Example Jurisdictions |
|:------------|:------|:----------------------|
| **Medical laboratories (reference/diagnostic)** | Often linked to epidemic response | Switzerland, EU, Germany |
| **Pharmaceutical manufacturers/distributors** | Supply chain criticality | EU (NIS2), Germany |
| **Medical device manufacturers** | Especially IVD and implantables | EU (NIS2 Annex II), Germany |
| **National immunization registries** | Pandemic preparedness | Japan, Taiwan |

### Tier 3: Variable Inclusion (depends on national context)
| Entity Type | Notes | Jurisdictions with Explicit Inclusion |
|:------------|:------|:--------------------------------------|
| **Private hospital chains** | Based on market share or regional importance | Singapore, Hong Kong |
| **Telehealth platforms** | Emerging; few explicit designations yet | None explicitly (emerging area) |
| **Health insurance claims systems** | Administrative criticality | USA (implicit), Germany |


## Governance Structure Options
| Structure | Description | Pros | Cons | Examples |
|:----------|:------------|:-----|:-----|:---------|
| **Centralized cyber agency** | Single agency designates and supervises all CI | Consistency; clear accountability | May lack health sector expertise | Singapore (CSA), Israel (INCD) |
| **Sector-specific regulator** | Health ministry/agency handles health CI | Domain expertise; existing relationships | May lack cyber expertise; fragmentation | Japan (MHLW), France (health ministry) |
| **Hybrid with sector leads** | Central cyber coordination; sector authorities designate | Balances expertise; coordination | Complexity; inter-agency friction | UK, Germany, Hong Kong |
| **Federated (federal countries)** | Shared federal/state responsibility | Respects local context | Coordination challenges; gaps | Canada, Australia, Germany |
> **Recommendation for new countries:** **Hybrid model** with a central cybersecurity coordination body and sector-specific designation authority in the health ministry tends to balance expertise best.


## Threshold Design: Quantitative vs Qualitative
| Approach | Description | When to Use | Examples |
|:---------|:------------|:------------|:---------|
| **Explicit quantitative** | Numeric thresholds (beds, cases, employees) | High data availability; desire for predictability | Germany (30,000 cases/yr), EU (≥50 employees), Australia (ICU presence) |
| **Qualitative + factors** | Multi-factor assessment; committee review | Lower data availability; diverse health system | South Korea (5-factor test), Singapore ("debilitating effect") |
| **Functional designation** | Based on services provided, not size | Small but critical providers (e.g., sole provider in region) | EU ("regardless of size" exceptions), UK, NZ |
| **Registration-based** | Entities self-assess and register; spot-check enforcement | Resource-constrained regulators | Germany (NIS2 registration), Hong Kong |
> **Key insight from global analysis:** **Pure quantitative thresholds miss edge cases.** Best practice combines a quantitative baseline with qualitative "safety net" criteria (e.g., "sole provider," "unique capability," "cross-border impact").


## Common Implementation Pitfalls (Lessons from Established Frameworks)
| Pitfall | Lesson Learned | Countries with This Issue |
|:--------|:---------------|:--------------------------|
| **Confidential lists become stale** | Build in mandatory periodic review (e.g., every 2 years) | EU (mandates 2-year review), UK |
| **Small critical providers overlooked** | Include "regardless of size" exceptions for unique/sole providers | EU NIS2, UK |
| **Supply chain not covered** | Explicitly include MSPs, cloud providers, medical device vendors | UK (new Bill), EU |
| **No escalation path for evolving threats** | Build in mechanism for emergency temporary designation | Taiwan, South Korea |
| **Reporting burden on small providers** | Tiered reporting obligations proportionate to size/criticality | EU (Essential vs Important), Israel (3-tier) |
| **Siloed from other CI sectors** | Map and address interdependencies (power, telecom, water) | Most mature frameworks address this |


## What to Make Public vs Confidential
| Element | Global Consensus | Rationale |
|:--------|:-----------------|:----------|
| **Designation criteria** | **PUBLIC** | Enables self-assessment; transparency; predictability |
| **Reporting thresholds** | **PUBLIC** | Clear compliance expectations |
| **List of designated entities** | **CONFIDENTIAL** | Avoid creating target list for attackers |
| **Aggregate statistics** | **PUBLIC (anonymized)** | Sector learning; accountability |
| **Incident reports** | **CONFIDENTIAL** (individual); **PUBLIC** (aggregated/anonymized) | Balance learning vs security |
> **South Korea exception:** Official Gazette publication of designated CII is required by law, demonstrating that transparency models can work with appropriate security measures.


# Updated Recommendations for Framework Design (2025-2026)
Based on comprehensive analysis and latest global developments:


### **1\. Adopt Hybrid Criticality Criteria**
* **Combine Approaches**: Use explicit thresholds (like Germany's 30,000 cases, Australia's ICU presence) for objectivity, supplemented by qualitative assessment for unique critical providers.  
* **Include Supply Chain**: Explicitly incorporate MSPs and critical suppliers in scope (following UK model).  
* **Functional \+ Size-Based**: Combine functional designations (emergency services, blood/organ systems) with size-based thresholds (EU's ≥50 employees).

### **2\. Implement Proportional Three-Tier System**
* **Tier 1 (Essential/Critical)**: Highest obligations, ex-ante supervision, 24/7 monitoring requirements  
* **Tier 2 (Important)**: Moderate obligations, ex-post supervision, regular assessments  
* **Tier 3 (Baseline)**: Basic cyber hygiene, voluntary reporting  
* **Align Penalties**: Proportionate penalties based on tier and organizational size

### **3\. Establish Clear Incident Reporting Thresholds**
* **Adopt UK-Style Metrics**: Implement explicit, quantitative incident thresholds (patient counts, service disruption durations)  
* **Harmonize Timelines**: Align with emerging global standards (24-hour initial, 72-hour detailed)  
* **Special Ransomware Reporting**: Consider mandatory ransom payment reporting within 24 hours

### **4\. Ensure Strategic Transparency**
* **Public Criteria**: Publish clear designation criteria enabling self-assessment  
* **Confidential Lists**: Maintain confidential entity lists to avoid creating target lists  
* **Aggregate Reporting**: Publish anonymized sector statistics and case studies for learning

### **5\. Integrate All-Hazard Resilience**
* **Beyond Cybersecurity**: Require business continuity and disaster recovery planning for physical, environmental, and supply chain disruptions  
* **Regular Testing**: Mandate annual or biennial testing of resilience plans  
* **Cross-Sector Dependencies**: Map and address interdependencies with other critical infrastructure sectors

### **6\. Future-Proof for Emerging Technologies**
* **Telehealth Platforms**: Explicitly include national/regional telehealth systems  
* **AI/ML Systems**: Consider criticality of AI-driven diagnostic and treatment systems  
* **IoT Medical Devices**: Address security of connected medical device ecosystems

# Implementation Roadmap for New Jurisdictions

## Quick-Start Decision Tree
```
START: Is health explicitly listed as a CI sector in existing national law?
  │
  ├─ YES → Proceed to Step 2 (Define health-specific criteria)
  │
  └─ NO → Step 1: Establish legal foundation
           ├─ Option A: Add health to existing CI framework
           ├─ Option B: Create sector-specific cybersecurity law
           └─ Option C: Issue ministerial regulation under existing powers
```

## Model Legislation Elements (Based on Global Best Practices)
| Element | Recommended Approach | Reference Models |
|:--------|:--------------------|:-----------------|
| **Definition of "health CI"** | Entity-based + functional criteria | EU NIS2 (healthcare providers), Australia (ICU hospitals) |
| **Designation authority** | Health ministry with cybersecurity agency coordination | Hong Kong, Germany, UK |
| **Scope criteria** | Quantitative baseline + qualitative exceptions | Germany + EU hybrid |
| **Obligations structure** | Tiered (Essential/Important or Tier 1/2/3) | EU NIS2, Israel |
| **Incident reporting** | 24h early warning / 72h detailed / 30d final | EU NIS2, Norway, Hong Kong |
| **Penalties** | Proportionate to size; administrative fines + compliance orders | EU, Hong Kong |
| **Review cycle** | Mandatory 2-year review of designated list | EU NIS2 |


## Phase 1: Foundation (Months 1-6)

### 1.1 Legal Authority Assessment
- [ ] Review existing cybersecurity/CI laws for health sector applicability
- [ ] Identify gaps requiring new legislation vs ministerial regulation
- [ ] Map existing health sector regulatory bodies and their powers

### 1.2 Sector Risk Assessment

- [ ] Inventory major health information systems in the country
- [ ] Identify single points of failure (sole providers, national systems)
- [ ] Assess current incident reporting and cyber hygiene baseline

### 1.3 Stakeholder Mapping

- [ ] Identify designated authority (cybersecurity agency, health ministry, or hybrid)
- [ ] Map hospitals, labs, insurers, technology vendors in health sector
- [ ] Establish working group with sector representatives


## Phase 2: Design & Consultation (Months 7-12)

### 2.1 Develop Designation Criteria

- [ ] Define quantitative thresholds (e.g., bed count, case volume, employee count)
- [ ] Add qualitative safety-net criteria (sole provider, unique capability)
- [ ] Draft "regardless of size" exception triggers

### 2.2 Draft Obligations Framework

- [ ] Tier 1 (Essential): Risk management plan, security officer, 24h reporting, annual audit
- [ ] Tier 2 (Important): Risk management, 72h reporting, biennial assessment
- [ ] Tier 3 (Baseline): Basic cyber hygiene, voluntary reporting

### 2.3 Stakeholder Consultation

- [ ] Publish draft framework for public comment
- [ ] Conduct workshops with hospital associations, health IT vendors
- [ ] Align with telecom, energy, finance CI frameworks on cross-sector issues


## Phase 3: Pilot Implementation (Months 13-18)

### 3.1 Pilot Designation

- [ ] Designate 5-10 largest/most critical entities for pilot
- [ ] Test designation process and notification procedures
- [ ] Refine criteria based on pilot feedback

### 3.2 Develop Operational Guidance

- [ ] Create sector-specific security controls guidance (reference: Germany B3S, UK CAF)
- [ ] Develop incident reporting forms and submission system
- [ ] Establish information-sharing mechanisms (CERT, sectoral ISAC)

### 3.3 Capacity Building

- [ ] Train designated entities on compliance requirements
- [ ] Train regulatory staff on supervision and enforcement
- [ ] Establish help desk for compliance questions


## Phase 4: Full Implementation (Months 19-24)

### 4.1 Full Rollout

- [ ] Designate all in-scope entities based on final criteria
- [ ] Activate mandatory incident reporting
- [ ] Begin compliance monitoring

### 4.2 Enforcement Framework

- [ ] Establish graduated enforcement (warning → compliance order → fine)
- [ ] Publish anonymized enforcement statistics for sector learning
- [ ] Create appeals/review mechanism

### 4.3 Cross-Sector Integration

- [ ] Map interdependencies with power, telecom, water CI
- [ ] Establish joint incident response protocols
- [ ] Participate in national/regional CI coordination mechanisms


## Phase 5: Maturity & Evolution (Ongoing)

### 5.1 Continuous Improvement

- [ ] Conduct annual review of designation criteria effectiveness
- [ ] Update thresholds based on sector evolution (e.g., telehealth growth)
- [ ] Incorporate lessons from incident response

### 5.2 International Alignment

- [ ] Monitor and align with regional frameworks (EU NIS2, ASEAN, etc.)
- [ ] Participate in international information-sharing networks
- [ ] Consider mutual recognition agreements for cross-border operators

### 5.3 Emerging Technology Integration

- [ ] Add AI/ML diagnostic systems to scope consideration
- [ ] Address IoT medical device security
- [ ] Update for cloud and SaaS health platforms


## Conclusion
This comprehensive analysis of **17 jurisdictions** with detailed chapter coverage, plus an additional **20+ countries** surveyed across Latin America, ASEAN, Africa, Middle East, and Central Asia, reveals a global landscape undergoing significant transformation in 2025-2026.
**Five key trends dominate:**

1. **Expanded Scope**: Regulations now explicitly encompass supply chains, with MSPs and critical suppliers facing direct obligations (UK, EU).  
2. **Holistic Resilience**: The shift from pure cybersecurity to all-hazard resilience planning (EU CER Directive) reflects recognition that health systems face multifaceted threats.  
3. **Stricter Reporting**: Convergence towards 12-24 hour early warning and 48-72 hour detailed notification, with specific ransomware payment reporting (24 hours in USA, Australia).  
4. **Enhanced Enforcement**: Moving from voluntary guidance to mandatory requirements with significant penalties (EU up to €10M, Hong Kong up to HK$5M).
5. **New Jurisdictions Entering the Framework**: 2025-2026 sees major new entrants including Hong Kong (CI Ordinance), Switzerland (CSV), Norway (Digital Security Act), and Taiwan (revised CSMA).
Despite diverse legal traditions and cultural contexts, remarkable consensus exists on which health systems merit highest protection: emergency services, major hospital clinical systems, blood/organ services, and disease surveillance platforms.
The most effective frameworks emerging from this global analysis combine **transparent, objective criteria** (enabling self-assessment) with **proportionate, risk-based obligations** (ensuring appropriate resource allocation), while maintaining necessary **confidentiality over specific asset lists** (preserving security).
For jurisdictions developing or updating their health critical infrastructure frameworks, the 2025-2026 updates from the UK, EU, US, Australia, Hong Kong, Switzerland, and Norway provide a clear roadmap emphasizing supply chain security, all-hazard resilience, and harmonized incident reporting. These developments, coupled with the foundational principles from established frameworks like Germany's precise thresholds, Singapore's system-level approach, and South Korea's transparent designation process, create a comprehensive model for protecting the digital foundations of healthcare in an increasingly interconnected and threatened world.


## References (Global Synthesis)
1. **Cyber Security Agency of Singapore (CSA).** **Cybersecurity Act**. ([CSA][1])

2. **Cyber Security Agency of Singapore (CSA).** **Code of Practice for Critical Information Infrastructure Protection (Second Edition)**. ([CSA][2])

3. **Cyber Security Agency of Singapore (CSA).** **Healthcare Cybersecurity Masterplan 2021-2023**.

4. **Australian Government.** **Security of Critical Infrastructure Act 2018**. ([Legislation.gov.au][4])

5. **Australian Government, Department of Home Affairs.** **Security of Critical Infrastructure (Definitions) Rules 2021**.

6. **Australian Government, Department of Home Affairs.** **Security of Critical Infrastructure (Risk Management Program) Rules 2023**.
7. **Critical Infrastructure Centre.** **SOCI Act 2018 for healthcare and medical**. ([CISC][7])

8. **UK Parliament.** **The Network and Information Systems Regulations 2018 (SI 2018/506)**. ([Legislation.gov.uk][8])

9. **UK Department of Health and Social Care.** **The Network and Information Systems Regulations 2018: guide for the health sector in England**. ([GOV.UK][9])

10. **UK National Cyber Security Centre.** **Cyber Assessment Framework (CAF)**. ([NCSC][10])

11. **European Parliament and Council.** **Directive (EU) 2022/2555 (NIS2 Directive)**.

12. **European Commission.** **FAQs on NIS2 Directive**. ([European Commission][12])

13. **European Commission.** **Infringement proceedings for non-transposition of NIS2**. ([European Commission][13])
14. **The White House.** **Presidential Policy Directive 21 (PPD-21): Critical Infrastructure Security and Resilience**.

15. **Cybersecurity and Infrastructure Security Agency (CISA).** **National Critical Functions**. ([CISA][15])

16. **U.S. Department of Health and Human Services.** **Health Industry Cybersecurity Practices (HICP)**. ([405d.hhs.gov][16])

17. **U.S. Department of Health and Human Services.** **HIPAA Security Rule**. ([HHS.gov][17])

18. **National Conference of State Legislatures.** **State Critical Infrastructure Laws**. ([NCSL][18])

19. **U.S. Government Accountability Office.** **Federal Health Cybersecurity**. ([GAO][19])

20. **Public Safety Canada.** **National Strategy for Critical Infrastructure**. ([Public Safety Canada][20])
21. **Ontario Ministry of Health.** **Emergency Management Framework for Health**. ([Ontario.ca][21])

22. **Canadian Centre for Cyber Security.** **Cyber Incident Management for Canada's Health Sector**. ([Cyber.gc.ca][22])

23. **New Zealand Government.** **Computer Emergency Response Team Act 2016**.

24. **Te Whatu Ora - Health New Zealand.** **Cybersecurity and Critical Infrastructure Framework (Draft)**.

25. **Bundesamt für Sicherheit in der Informationstechnik (BSI).** **BSI-KritisV and IT-Sicherheitsgesetz 2.0**. ([BSI][25])

26. **Bundesministerium des Innern und für Heimat.** **NIS2-Umsetzungsgesetz (NIS2UmsuCG)**. ([BMI][26])

27. **National center of Incident readiness and Strategy for Cybersecurity (NISC), Japan.** **Cybersecurity Basic Act and Policy Guidelines**. ([NISC][27])
28. **Ministry of Health, Labour and Welfare (MHLW), Japan.** **Healthcare Information System Security Guidelines**. ([MHLW][28])

29. **Personal Information Protection Commission, Japan.** **Health Data Breach Reporting**. ([PPC][29])

30. **National People's Congress, China.** **Cybersecurity Law of the People's Republic of China**.

31. **State Council, China.** **Critical Information Infrastructure Security Protection Regulations**.

32. **Ministry of Public Security, China.** **Multi-Level Protection Scheme 2.0 Standards**.

33. **National Health Commission, China.** **Health Critical Information Infrastructure Protection Guidelines**.

34. **Cyberspace Administration of China.** **CII Security Incident Reporting Requirements**. ([CAC][34])

