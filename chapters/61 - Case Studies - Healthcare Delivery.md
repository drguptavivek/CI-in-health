# CII Case Studies: Healthcare Delivery Facilities

This chapter presents case studies for **healthcare delivery facilities** including hospitals, medical colleges, community health centres, and telemedicine services.

---

## Case Study 1: Metro General Hospital

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Metro General Hospital |
| **Type** | Government tertiary teaching hospital |
| **Location** | State capital city (population 5 million) |
| **Beds** | 1,200 |
| **Annual inpatient cases** | 45,000 |
| **Employees** | 3,500 |
| **Key departments** | ICU (50 beds), Emergency, Trauma Centre, Cardiac Surgery, Organ Transplant |
| **Digital systems** | Integrated HIS, EMR, PACS, LIS, Blood Bank Management |
| **Connectivity** | 24/7 broadband; connected to national health exchange |

### CII Classification Assessment

#### Scoring (Developed Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | ≥30,000 cases/year | 30 |
| **B. Capability** | General ICU present | 25 |
| **C. Functions** | Blood bank/transfusion + Organ allocation | 20 |
| **D. Uniqueness** | Alternative providers available (metro area) | 0 |
| **E. Dependencies** | Other regional facilities depend on transplant services | 8 |
| **TOTAL** | | **83** |

#### Scoring (Developing Country Framework - Adapted)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | ≥10,000 cases/year | 30 |
| **B. Public System Role** | Major Government Medical College | 25 |
| **C. Geographic Criticality** | Metro (not sole provider) | 0 |
| **D. National Program Integration** | Connected to national HIE | 15 |
| **TOTAL** | | **70** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developed Country** | 83 | **Tier 1 (Essential)** | Exceeds 60-point threshold; ICU + transplant capability |
| **Developing Country** | 70 | **Tier 1 (Essential)** | Major teaching hospital; national program integration |

### Applicable Obligations

- Annual security audit (third-party)
- 24-48 hour incident reporting
- Dedicated CISO required
- Mandatory business continuity plan
- Participation in cyber drills
- 24/7 security monitoring

---

## Case Study 2: Rural District Hospital - Greenfield DH

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Greenfield District Hospital |
| **Type** | Government district hospital |
| **Location** | Rural district headquarters (district population 1.2 million) |
| **Beds** | 150 |
| **Annual inpatient cases** | 8,000 |
| **Employees** | 280 |
| **Key departments** | General surgery, Obstetrics, Emergency, No ICU |
| **Digital systems** | Basic HIS, connected to state disease surveillance |
| **Connectivity** | Intermittent broadband; mobile backup |
| **Special status** | **Only hospital with surgical capability in the district** |

### CII Classification Assessment

#### Scoring (Developed Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | 5,000–14,999 cases/year | 10 |
| **B. Capability** | Emergency department only (no ICU) | 10 |
| **C. Functions** | None of the critical functions listed | 0 |
| **D. Uniqueness** | Sole provider in region | 10 |
| **E. Dependencies** | Limited external dependencies | 3 |
| **TOTAL** | | **33** |

#### Scoring (Developing Country Framework - Adapted)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | 5,000–9,999 cases/year | 20 |
| **B. Public System Role** | District Hospital (sole in district) | 25 |
| **C. Geographic Criticality** | Sole provider >50km radius | 20 |
| **D. National Program Integration** | State disease surveillance node | 10 |
| **TOTAL** | | **75** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developed Country** | 33 | **Tier 2 (Important)** | Above 30 threshold; sole provider adds weight |
| **Developing Country** | 75 | **Tier 1 (Essential)** | **Automatic Tier 1 trigger**: Sole district hospital |

> [!IMPORTANT]
> This case illustrates why developing country adaptations are critical. Under developed-country thresholds, this hospital would be Tier 2. However, as the **sole surgical/obstetric facility for 1.2 million people**, it merits Tier 1 designation in the developing country context.

### Applicable Obligations (Developing Country Tier 1)

- Annual security audit (may be state-supported)
- 24-48 hour incident reporting
- Security focal point required (may share with district administration)
- Business continuity plan with manual fallback procedures
- State SOC integration (shared services model)

---

## Case Study 3: Private Hospital Chain - HealthFirst Network

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | HealthFirst Hospital Network |
| **Type** | Private corporate hospital chain |
| **Coverage** | 15 hospitals across 8 states |
| **Total beds** | 4,500 (average 300 per hospital) |
| **Annual inpatient cases** | 180,000 (network-wide) |
| **Employees** | 12,000 |
| **Key features** | ICU in all facilities; 3 hospitals with cardiac surgery |
| **Digital systems** | Centralized cloud EHR; unified patient portal |
| **Market position** | Second-largest private chain in the country |

### CII Classification Assessment

#### Entity-Level vs System-Level Analysis

| Analysis Level | Scope | Approach |
|:---------------|:------|:---------|
| **Entity-level (network)** | Entire chain as single entity | Aggregate scoring |
| **System-level** | Centralized EHR platform | System criticality assessment |
| **Facility-level** | Each hospital individually | Facility-by-facility scoring |

#### Network-Level Scoring (Developing Country)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | ≥10,000 cases/year (network: 180,000) | 30 |
| **B. Capability** | ICU present in all facilities | 25 |
| **C. Geographic Criticality** | Multi-state presence; alternative providers in most locations | 5 |
| **D. National Program Integration** | PM-JAY empaneled; national HIE connected | 20 |
| **TOTAL** | | **80** |

#### System-Level Assessment: Centralized EHR Platform

| Factor | Assessment | Score |
|:-------|:-----------|:-----:|
| **Availability Impact** | Outage affects 180,000 patients/year across 15 hospitals | 10 |
| **Integrity Impact** | Data corruption could affect treatment decisions | 9 |
| **Confidentiality Impact** | Millions of patient records at risk | 9 |
| **Substitutability** | Paper fallback possible but severely impacts operations | 7 |
| **Recovery Time** | RTO estimated 48+ hours for full restoration | 9 |
| **TOTAL** | | **44** |

### Classification Result

| Level | Score | Tier | Rationale |
|:------|:------|:-----|:----------|
| **Network (entity)** | 80 | **Tier 1** | Scale + capability + national program integration |
| **Centralized EHR (system)** | 44 | **Tier 1 System** | High criticality across all factors |
| **Individual hospitals** | Varies | **Tier 1 or 2** | Based on local sole-provider status |

### Applicable Obligations

**Network-level:**
- Dedicated Group CISO required
- Annual third-party audit of centralized systems
- 24-hour incident reporting for centralized platform incidents
- Participation in national cyber drills
- Supply chain security assessment for cloud vendors

**Facility-level:**
- Site-level security focal points
- Local business continuity plans
- Integration with network SOC

---

## Case Study 4: Community Health Centre - Riverside CHC

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Riverside Community Health Centre |
| **Type** | Government block-level CHC |
| **Location** | Rural block (block population 120,000) |
| **Beds** | 30 |
| **Annual inpatient cases** | 1,200 |
| **Employees** | 45 |
| **Key departments** | General OPD, Labor room, No surgery, No ICU |
| **Digital systems** | RCH portal access; immunization tracking |
| **Connectivity** | Mobile data; intermittent connectivity |
| **Special status** | Not designated as First Referral Unit (FRU) |

### CII Classification Assessment

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | <2,000 cases/year | 5 |
| **B. Public System Role** | CHC (not FRU, not sole in block) | 5 |
| **C. Geographic Criticality** | District hospital 35km away | 5 |
| **D. National Program Integration** | RCH portal access | 5 |
| **TOTAL** | | **20** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 20 | **Tier 3 (Baseline)** | Small scale; not sole provider; limited digital footprint |

### Applicable Obligations (Tier 3)

- Self-assessment recommended
- Voluntary incident reporting
- Basic cyber hygiene guidance
- May benefit from state-level shared services (SOC, backup)
- Not subject to mandatory audits or reporting timelines

---

## Case Study 5: Telemedicine Hub - "Sehat Setu"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Sehat Setu Regional Telemedicine Hub |
| **Type** | Government telemedicine hub serving remote/tribal areas |
| **Coverage** | 3 remote districts; 200 spoke locations |
| **Functions** | Video consultations; specialist referrals; prescription support |
| **Consultations** | 150,000 per year |
| **Employees** | 35 |
| **Population served** | 2.5 million (primarily tribal, remote) |
| **Special status** | Only specialist access for tribal blocks |

### CII Classification Assessment

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | Not a hospital (consultations-based) | 10 |
| **B. Public System Role** | Government telemedicine hub | 15 |
| **C. Geographic Criticality** | Sole specialist access for remote population | 20 |
| **D. Functions** | Telemedicine hub for tribal/remote areas | 15 |
| **TOTAL** | | **60** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 60 | **Tier 1 (Essential)** | Threshold met; sole specialist access for underserved population |

> [!NOTE]
> This case demonstrates how **telemedicine hubs serving remote populations** can qualify as Tier 1 despite modest scale, because they represent the **only access point** for specialist care.

### Applicable Obligations

- Security focal point
- 24-48 hour incident reporting
- Business continuity: Backup connectivity; manual referral protocols
- Annual audit (may be combined with state ICT audit)
- Data protection: Patient consultation confidentiality

---

## Case Study 6: Medical College Research Institution - "Lakshmi Devi Medical College"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Lakshmi Devi Medical College & Research Institute |
| **Type** | Government medical college with attached teaching hospital |
| **Location** | State capital city |
| **Beds** | 1,500 (attached hospital) |
| **Annual admissions** | MBBS: 250; PG: 150; Super-specialty: 50 |
| **Research programs** | 45 active research projects; 12 clinical trials |
| **Research funding** | ₹50 crore active grants (national and international) |
| **Key systems** | Hospital Information System (HIS), Clinical Trial Management System (CTMS), Electronic Lab Notebook (ELN), Research Data Repository, Student Information System |
| **Data holdings** | 25 years of patient records; 200,000+ research subjects data |
| **Integrations** | Connected to national clinical trial registry; multiple international research collaborations |
| **Special consideration** | **Dual role: clinical care + research training pipeline** |

### CII Classification Assessment

#### Dual Assessment: Clinical vs Research Functions

| Function | Criticality Basis |
|:---------|:------------------|
| **Clinical care** | Major tertiary hospital with ICU, trauma, specialty services |
| **Medical education** | Trains future healthcare workforce; pipeline criticality |
| **Research** | Clinical trials, longitudinal studies, collaborative research data |
| **Research IP** | Proprietary research findings, unpublished data |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Clinical Scale** | 1,500 beds; major tertiary hospital | 30 |
| **B. Capability** | ICU, emergency, tertiary specialty services | 25 |
| **C. Research Function** | 45 active projects; clinical trial data | 15 |
| **D. Training Pipeline** | 450 trainees/year; workforce development | 10 |
| **TOTAL** | | **80** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 80 | **Tier 1 (Essential)** | Major tertiary hospital + research institution + training function |

> [!NOTE]
> Medical colleges have **triple criticality**: clinical care, research data, and workforce training. A cyber incident affecting a medical college simultaneously impacts patient care, ongoing research, and future healthcare capacity.

### Applicable Obligations

**Clinical side:**
- All Tier 1 hospital obligations (CISO, audit, incident reporting, BCP)

**Research side:**
- Research data protection controls (ELN, CTMS, repositories)
- Clinical trial data integrity monitoring
- International collaboration data transfer controls
- Research ethics committee security awareness

**Education side:**
- Student data protection
- Examination system security
- Training continuity planning

---

## Summary: Healthcare Delivery Classification

| Case Study | Entity Type | Score | Tier |
|:-----------|:------------|:-----:|:----:|
| Metro General Hospital | Tertiary teaching | 70 | **Tier 1** |
| Greenfield District Hospital | District hospital (sole) | 75 | **Tier 1** (auto) |
| HealthFirst Network | Private chain | 80 | **Tier 1** |
| Riverside CHC | Community health centre | 20 | **Tier 3** |
| Sehat Setu Telemedicine | Remote telemedicine hub | 60 | **Tier 1** |
| Lakshmi Devi Medical College | Medical college + research | 80 | **Tier 1** |

### Key Insights

1. **Geographic factors outweigh scale**: Sole district hospitals are Tier 1 regardless of size
2. **Private chains can be CII**: Large networks with centralized systems warrant high classification
3. **Telemedicine criticality**: Access-based criticality applies to underserved population hubs
4. **Medical colleges have compound criticality**: Clinical + research + training functions multiply risk
5. **Tier 3 facilities benefit from shared services**: Even unclassified facilities need security resources

