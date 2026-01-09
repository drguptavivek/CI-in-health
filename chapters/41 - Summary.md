# Part 2: Comparative Synthesis & Framework Design Recommendations

## **Comparative Framework Overview**

| Country/Region | Designation Model | Transparency | Explicit Thresholds | 2025-2026 Updates |
| :---- | :---- | :---- | :---- | :---- |
| **Singapore** | System-level (individual CII) | Criteria public, lists confidential | No (qualitative "debilitating") | No major updates |
| **Australia** | Asset-level (ICU hospitals) | Criteria fully public, SoNS confidential | **Yes (ICU presence)** | **Ransomware payment reporting (May 2025), strict enforcement (Jan 2026\)** |
| **UK** | Entity-level (OES) | Criteria public, lists confidential | **Yes (incident thresholds most explicit globally)** | **Cyber Security Bill (Nov 2025), expands to MSPs/suppliers, 24-hr reporting** |
| **EU (NIS2)** | Entity-level (Essential/Important) | Criteria fully public, lists vary by state | **Yes (≥50 employees, €10M)** | **CER Directive (July 2026 deadline), all-hazard resilience** |
| **USA** | Sector-level (no designation) | Frameworks public, priorities confidential | No (voluntary, qualitative) | **CIRCIA final rule expected (May 2026), 72-hr incident/24-hr ransom reporting** |
| **Canada** | Fragmented (federal \+ provincial) | Partially public | No (qualitative) | No major updates |
| **New Zealand** | Informal (NSO \+ CNI developing) | Partially public | No (qualitative, developing) | No major updates |
| **Germany** | System/entity (KRITIS \+ NIS2) | **High (30,000 cases public)** | **Yes (30,000 inpatient cases/year)** | NIS2 implementation ongoing |
| **Japan** | Entity-level (discretionary) | Medium (hospital categories public) | No (qualitative assessment) | No major updates |
| **China** | System/entity (CII) | Low (general criteria only) | No (party-state discretion) | No major updates |

# **Universal Health Information Systems Prioritized Globally**

**All ten jurisdictions prioritize:**

1. **Emergency call-taking and ambulance dispatch** (111/112/119/911/999 \+ Computer Aided Dispatch)  
2. **Major hospital core clinical systems** (EMR, EDIS, ICU monitoring)  
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

# **Emerging Global Trends (2025-2026)**

### **1\. Supply Chain Regulation Expansion**

* **UK**: New Bill explicitly targets **Managed Service Providers (MSPs)** and **critical suppliers**  
* **EU**: NIS2 includes manufacturers of medical devices and pharmaceuticals  
* **Implication**: Future frameworks must include criteria for assessing and mandating security standards for third and fourth-party vendors

### **2\. All-Hazard Resilience Integration**

* **EU CER Directive**: Mandates resilience plans for physical, environmental, natural disaster, and supply chain disruptions  
* **Shift**: Moving beyond pure cybersecurity to require planning for broader disruptions that could impact digital services  
* **Implication**: Critical infrastructure frameworks should integrate business continuity planning for multi-hazard scenarios

### **3\. Stricter & Harmonized Incident Reporting**

* **Convergence**: Towards **24-hour initial / 72-hour detailed** reporting (UK, US CIRCIA, EU NIS2)  
* **Special Focus**: **24-hour ransom payment reporting** (US, Australia)  
* **Implication**: Clear, tiered incident reporting windows aligned with global standards ensure rapid response and information sharing

### **4\. Enhanced Enforcement Postures**

* **Australia**: Shift to "stricter enforcement-oriented posture" from January 2026  
* **EU**: Significant penalties (up to €10M or 2% global turnover)  
* **Implication**: Compliance moving from voluntary guidance to mandatory requirement with serious consequences for non-compliance

# **Updated Recommendations for Framework Design (2025-2026)**

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

# **Implementation Roadmap for New Jurisdictions**

### **Phase 1: Foundation (Months 1-6)**

* Conduct sector risk assessment  
* Define hybrid criticality criteria  
* Establish competent authority and governance structure

### **Phase 2: Design & Consultation (Months 7-12)**

* Develop three-tier framework  
* Draft incident reporting thresholds  
* Consult with stakeholders (hospitals, vendors, cybersecurity experts)

### **Phase 3: Pilot Implementation (Months 13-18)**

* Pilot with largest hospitals and national systems  
* Refine criteria and processes  
* Develop guidance materials and training

### **Phase 4: Full Implementation (Months 19-24)**

* Roll out to all in-scope entities  
* Establish monitoring and enforcement mechanisms  
* Initiate cross-sector collaboration

### **Phase 5: Maturity & Evolution (Ongoing)**

* Regular review and update of criteria  
* Integration with international frameworks  
* Continuous capability development

---

## **Conclusion**

The global landscape for health information system critical infrastructure classification is undergoing significant transformation in 2025-2026. Four key trends dominate:

1. **Expanded Scope**: Regulations now explicitly encompass supply chains, with MSPs and critical suppliers facing direct obligations (UK, EU).  
2. **Holistic Resilience**: The shift from pure cybersecurity to all-hazard resilience planning (EU CER Directive) reflects recognition that health systems face multifaceted threats.  
3. **Stricter Reporting**: Convergence towards 24/72-hour incident reporting and specific ransomware payment reporting creates a new baseline for timely response.  
4. **Enhanced Enforcement**: Moving from voluntary guidance to mandatory requirements with significant penalties signals regulatory maturity.

Despite diverse legal traditions and cultural contexts, remarkable consensus exists on which health systems merit highest protection: emergency services, major hospital clinical systems, blood/organ services, and disease surveillance platforms.

The most effective frameworks emerging from this global analysis combine **transparent, objective criteria** (enabling self-assessment) with **proportionate, risk-based obligations** (ensuring appropriate resource allocation), while maintaining necessary **confidentiality over specific asset lists** (preserving security).

For jurisdictions developing or updating their health critical infrastructure frameworks, the 2025-2026 updates from the UK, EU, US, and Australia provide a clear roadmap emphasizing supply chain security, all-hazard resilience, and harmonized incident reporting. These developments, coupled with the foundational principles from established frameworks like Germany's precise thresholds and Singapore's system-level approach, create a comprehensive model for protecting the digital foundations of healthcare in an increasingly interconnected and threatened world.

---

## **References**

\[1\] Cyber Security Agency of Singapore. (2018). Cybersecurity Act. [https://www.csa.gov.sg/legislation/cybersecurity-act/](https://www.csa.gov.sg/legislation/cybersecurity-act/)

\[2\] Cyber Security Agency of Singapore. (2021). Code of Practice for Critical Information Infrastructure Protection (Second Edition). [https://www.csa.gov.sg/](https://www.csa.gov.sg/)

\[3\] Cyber Security Agency of Singapore. (2021). Healthcare Cybersecurity Masterplan 2021-2023.

\[4\] Australian Government. (2018). Security of Critical Infrastructure Act 2018\. [https://www.legislation.gov.au/](https://www.legislation.gov.au/)

\[5\] Australian Government, Department of Home Affairs. (2023). Security of Critical Infrastructure (Definitions) Rules 2021\.

\[6\] Australian Government, Department of Home Affairs. (2023). Security of Critical Infrastructure (Risk Management Program) Rules 2023\.

\[7\] Critical Infrastructure Centre. (2024). SOCI Act 2018 for healthcare and medical. [https://www.cisc.gov.au/](https://www.cisc.gov.au/)

\[8\] UK Parliament. (2018). The Network and Information Systems Regulations 2018 (SI 2018/506). [https://www.legislation.gov.uk/uksi/2018/506](https://www.legislation.gov.uk/uksi/2018/506)

\[9\] UK Department of Health and Social Care. (2023). The Network and Information Systems Regulations 2018: guide for the health sector in England. [https://www.gov.uk/government/publications/](https://www.gov.uk/government/publications/)

\[10\] UK National Cyber Security Centre. (2023). Cyber Assessment Framework (CAF). [https://www.ncsc.gov.uk/](https://www.ncsc.gov.uk/)

\[11\] European Parliament and Council. (2022). Directive (EU) 2022/2555 on measures for a high common level of cybersecurity across the Union (NIS2 Directive). Official Journal of the European Union, L 333/80.

\[12\] European Commission. (2023). FAQs on NIS2 Directive. [https://digital-strategy.ec.europa.eu/](https://digital-strategy.ec.europa.eu/)

\[13\] European Commission. (2025). Infringement proceedings for non-transposition of NIS2. [https://ec.europa.eu/](https://ec.europa.eu/)

\[14\] The White House. (2013). Presidential Policy Directive 21 (PPD-21): Critical Infrastructure Security and Resilience.

\[15\] Cybersecurity and Infrastructure Security Agency (CISA). (2023). National Critical Functions. [https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-critical-functions](https://www.cisa.gov/topics/critical-infrastructure-security-and-resilience/national-critical-functions)

\[16\] U.S. Department of Health and Human Services. (2023). Health Industry Cybersecurity Practices (HICP). [https://405d.hhs.gov/](https://405d.hhs.gov/)

\[17\] U.S. Department of Health and Human Services. (2023). HIPAA Security Rule. [https://www.hhs.gov/hipaa/](https://www.hhs.gov/hipaa/)

\[18\] National Conference of State Legislatures. (2024). State Critical Infrastructure Laws. [https://www.ncsl.org/](https://www.ncsl.org/)

\[19\] U.S. Government Accountability Office. (2023). Federal Health Cybersecurity. [https://www.gao.gov/](https://www.gao.gov/)

\[20\] Public Safety Canada. (2023). National Strategy for Critical Infrastructure. [https://www.publicsafety.gc.ca/](https://www.publicsafety.gc.ca/)

\[21\] Ontario Ministry of Health. (2023). Emergency Management Framework for Health. [https://www.health.gov.on.ca/](https://www.health.gov.on.ca/)

\[22\] Canadian Centre for Cyber Security. (2023). Cyber Incident Management for Canada's Health Sector. [https://cyber.gc.ca/](https://cyber.gc.ca/)

\[23\] New Zealand Government. (2016). Computer Emergency Response Team Act 2016\.

\[24\] Te Whatu Ora \- Health New Zealand. (2023). Cybersecurity and Critical Infrastructure Framework (Draft).

\[25\] Bundesamt für Sicherheit in der Informationstechnik (BSI). (2021). BSI-KritisV and IT-Sicherheitsgesetz 2.0. [https://www.bsi.bund.de/](https://www.bsi.bund.de/)

\[26\] Bundesministerium des Innern und für Heimat. (2024). NIS2-Umsetzungsgesetz (NIS2UmsuCG). [https://www.bmi.bund.de/](https://www.bmi.bund.de/)

\[27\] National center of Incident readiness and Strategy for Cybersecurity (NISC), Japan. (2023). Cybersecurity Basic Act and Policy Guidelines. [https://www.nisc.go.jp/](https://www.nisc.go.jp/)

\[28\] Ministry of Health, Labour and Welfare (MHLW), Japan. (2023). Healthcare Information System Security Guidelines. [https://www.mhlw.go.jp/](https://www.mhlw.go.jp/)

\[29\] Personal Information Protection Commission, Japan. (2023). Health Data Breach Reporting. [https://www.ppc.go.jp/](https://www.ppc.go.jp/)

\[30\] National People's Congress, China. (2017). Cybersecurity Law of the People's Republic of China.

\[31\] State Council, China. (2021). Critical Information Infrastructure Security Protection Regulations.

\[32\] Ministry of Public Security, China. (2019). Multi-Level Protection Scheme 2.0 Standards (GB/T 22239-2019, GB/T 25070-2019).

\[33\] National Health Commission, China. (2023). Health Critical Information Infrastructure Protection Guidelines.

\[34\] Cyberspace Administration of China. (2023). CII Security Incident Reporting Requirements. [https://www.cac.gov.cn/](https://www.cac.gov.cn/)  
