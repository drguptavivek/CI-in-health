# CII Case Studies: Public Health Programs and Surveillance

This chapter presents case studies for **national public health programs** including disease control programs, surveillance systems, and population health initiatives.

---

## Case Study 1: Population-Based Surveillance System - "SurveilHealth"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | SurveilHealth Integrated Disease Surveillance Platform |
| **Type** | National real-time disease surveillance and outbreak detection |
| **Operator** | National Centre for Disease Control (government) |
| **Coverage** | All 28 states; 750 districts; 150,000 reporting units |
| **Functions** | Real-time syndromic surveillance, outbreak detection, alert generation, response coordination |
| **Data volume** | 50 million surveillance reports/year |
| **Integrations** | Laboratory network, hospital reporting, mortality surveillance, veterinary surveillance (One Health) |
| **Response capability** | Automated alert escalation; rapid response team coordination |
| **Special consideration** | **National epidemic response backbone** |

### CII Classification Assessment

#### Automatic Tier 1 Trigger Analysis

| "Regardless of Size" Criterion | Applies? |
|:-------------------------------|:--------:|
| National infectious disease surveillance | ✓ |
| Epidemic/pandemic response capability | ✓ |
| Public health emergency coordination | ✓ |
| One Health / cross-sector integration | ✓ |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. National Coverage** | 100% district coverage; 150,000 reporting points | 30 |
| **B. Public Health Function** | Epidemic detection and response | 25 |
| **C. Real-time Criticality** | Outbreak detection delays cost lives | 20 |
| **D. Cross-sector Integration** | One Health (human + animal surveillance) | 10 |
| **TOTAL** | | **85** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 85 | **Tier 1 (Essential)** | National epidemic response backbone; automatic trigger |

> [!IMPORTANT]
> Population-based surveillance systems are **foundational pandemic preparedness infrastructure**. COVID-19 demonstrated that countries with robust surveillance detected outbreaks faster and responded more effectively. This is **non-negotiable Tier 1**.

### Applicable Obligations

- Dedicated CISO + 24/7 Security Operations Centre
- Continuous security monitoring (real-time system criticality)
- 12-hour incident reporting (given outbreak detection dependency)
- Highly available infrastructure (multi-site redundancy)
- Data integrity controls (false data injection is attack vector)
- Integration security (APIs to laboratories, hospitals, veterinary)
- Annual penetration testing
- Participation in national cyber exercises

---

## Case Study 2: National TB Elimination Program - "TB-Mukt Bharat"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | TB-Mukt Bharat (National Tuberculosis Elimination Program) |
| **Type** | National disease control program |
| **Operator** | Central TB Division, Ministry of Health (government) |
| **Coverage** | All 28 states; 750 districts; 1.2 million+ DOTS providers |
| **Annual notifications** | 2.5 million TB cases notified/year |
| **Functions** | Case notification, treatment tracking, drug resistance surveillance, contact tracing, preventive therapy |
| **Key systems** | Ni-kshay (national TB notification portal), drug logistics (DVS), lab network (RNTCP-NET) |
| **Integrations** | Linked to death registry, private sector portal, pharmacy dispensation, insurance |
| **International obligations** | WHO End TB Strategy reporting; Global Fund accountability |
| **Special consideration** | **India has highest TB burden globally; elimination target 2025** |

### CII Classification Assessment

#### Automatic Tier 1 Trigger Analysis

| "Regardless of Size" Criterion | Applies? |
|:-------------------------------|:--------:|
| National disease surveillance function | ✓ |
| Epidemic control program | ✓ |
| International reporting obligations | ✓ |
| Drug supply chain management | ✓ |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. National Coverage** | 100% district coverage; 2.5M cases/year | 30 |
| **B. Public Health Function** | TB elimination national priority | 25 |
| **C. Drug Supply Chain** | National TB drug procurement and distribution | 15 |
| **D. International Accountability** | WHO reporting; Global Fund grants | 10 |
| **TOTAL** | | **80** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 80 | **Tier 1 (Essential)** | National TB elimination program; automatic trigger for disease surveillance |

> [!IMPORTANT]
> National disease control programs like TB-Mukt Bharat are **disease-specific critical infrastructure**. Disruption affects case detection, treatment continuity, drug supply, and international reporting. **Drug-resistant TB emergence** is a direct consequence of treatment disruption.

### Applicable Obligations

- Dedicated program security officer
- Annual audit of Ni-kshay and connected systems
- 24-hour incident reporting (especially for supply chain disruption)
- Drug logistics system integrity monitoring
- Laboratory network data security
- Private sector portal integration security
- State-level IT node security coordination
- Data quality and integrity controls (false notifications are attack vector)

---

## Case Study 3: National NCD Program - "Sankalp"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Sankalp (National Programme for Prevention and Control of NCDs) |
| **Type** | National non-communicable disease control program |
| **Operator** | NCD Division, Ministry of Health (government) |
| **Coverage** | 700+ NCD clinics; 150,000+ HWCs for screening |
| **Focus areas** | Diabetes, hypertension, cancer, cardiovascular disease, stroke |
| **Functions** | Population screening, risk stratification, treatment protocols, follow-up tracking |
| **Key systems** | NCD App (screening/tracking), Cancer Registry integration, CPHC portal |
| **Screenings** | 80 million population screened annually |
| **Special consideration** | **NCDs cause 62% of mortality in India** |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Population coverage** | 80M annual screenings; lifetime chronic disease tracking |
| **Continuity of care** | Chronic disease management requires uninterrupted longitudinal tracking |
| **Screening data** | Early cancer/CVD detection depends on data integrity |
| **Treatment continuity** | Hypertension/diabetes patients require continuous medication access |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Population Coverage** | 80M screenings/year across 700+ clinics | 30 |
| **B. Public Health Function** | NCDs are #1 mortality cause | 20 |
| **C. Chronic Care Coordination** | Longitudinal patient tracking essential | 15 |
| **D. HWC Integration** | 150,000+ frontline facilities connected | 10 |
| **TOTAL** | | **75** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 75 | **Tier 1 (Essential)** | Major national burden; population-scale screening and tracking |

> [!NOTE]
> NCD programs differ from acute disease programs in requiring **longitudinal data integrity over decades**. A patient's 10-year hypertension history affects current treatment decisions. Data corruption has delayed, but serious, consequences.

### Applicable Obligations

- Program security focal point
- Annual audit of NCD App and connected systems
- 48-hour incident reporting
- Data integrity controls for longitudinal records
- HWC integration security (high-volume low-resource endpoints)
- Screening data backup and recovery
- Cancer registry linkage security

---

## Case Study 4: National Blindness Control Program - "DrishtiRaksha"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | DrishtiRaksha (National Programme for Control of Blindness & Visual Impairment) |
| **Type** | National eye care and blindness prevention program |
| **Operator** | Ophthalmology Division, Ministry of Health (government) |
| **Coverage** | District hospitals + 700 vision centres + school screening |
| **Annual surgeries** | 7 million cataract surgeries/year (largest in world) |
| **Functions** | Cataract surgery tracking, school screening, IOL distribution, outcome monitoring |
| **Key systems** | NPCB-VI MIS, surgery outcome database, IOL inventory system |
| **Integrations** | District hospital systems, private eye hospital network |
| **Special consideration** | **World's largest cataract surgery program** |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Surgery volume** | 7M surgeries/year; logistics coordination essential |
| **Supply chain** | IOL (intraocular lens) procurement and distribution |
| **Outcome tracking** | Post-surgical complication monitoring affects quality improvement |
| **School screening** | Detection of childhood visual impairment |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | 7M surgeries/year; largest global program | 25 |
| **B. Supply Chain** | IOL procurement and distribution | 15 |
| **C. Outcome Monitoring** | Quality assurance for surgical outcomes | 10 |
| **D. School Health** | Childhood screening program | 10 |
| **TOTAL** | | **60** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 60 | **Tier 1 (Essential)** | Largest national surgical program; supply chain criticality |

### Applicable Obligations

- Program security focal point
- Annual audit of MIS and inventory systems
- 48-hour incident reporting
- IOL supply chain system monitoring
- Outcome database integrity controls
- School screening data protection
- Private hospital integration security

---

## Case Study 5: National Nutrition Program - "Poshan Rakshak"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Poshan Rakshak (Integrated Child Development Services + POSHAN Abhiyaan) |
| **Type** | National nutrition supplementation and growth monitoring program |
| **Operator** | Ministry of Women and Child Development + Ministry of Health (joint) |
| **Coverage** | 1.4 million Anganwadi centres; 14 crore children; 3.5 crore pregnant/lactating women |
| **Functions** | Growth monitoring, supplementary nutrition, immunization coordination, severe acute malnutrition (SAM) management |
| **Key systems** | ICDS-CAS (Common Application Software), Poshan Tracker, growth monitoring app, SAM referral system |
| **Frontline workers** | 2.7 million Anganwadi workers with mobile devices |
| **Integrations** | Linked to immunization registry, MCTS (Mother and Child Tracking), hospital systems for SAM referrals |
| **Special consideration** | **Largest nutrition program globally; child survival dependency** |

### CII Classification Assessment

#### Automatic Tier 1 Trigger Analysis

| "Regardless of Size" Criterion | Applies? |
|:-------------------------------|:--------:|
| National child health program | ✓ |
| Life-critical for vulnerable populations (children, pregnant women) | ✓ |
| Supply chain for nutrition supplements | ✓ |
| Frontline health worker coordination | ✓ |

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Population** | 14 crore children + 3.5 crore PLW = 175M beneficiaries |
| **Life-critical** | SAM management prevents child deaths |
| **Supply chain** | Supplementary nutrition distribution |
| **Data scale** | 2.7M frontline workers generating daily data |
| **Integration complexity** | Multi-ministry, multi-system integration |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Beneficiary Scale** | 175M beneficiaries (children + PLW) | 30 |
| **B. Life-Critical Function** | SAM management; child survival | 25 |
| **C. Supply Chain** | Nutrition supplement distribution | 15 |
| **D. Frontline Worker Coordination** | 2.7M Anganwadi workers | 10 |
| **TOTAL** | | **80** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 80 | **Tier 1 (Essential)** | Largest nutrition program; child survival dependency; automatic trigger |

> [!CAUTION]
> Nutrition programs have **immediate life-safety implications for vulnerable populations**. Growth faltering detection delays directly increase child mortality. SAM referral system disruption is equivalent to emergency care disruption. This is **non-negotiable Tier 1**.

### Applicable Obligations

- Dedicated program security officer
- Annual audit of Poshan Tracker and ICDS-CAS
- 24-hour incident reporting (given life-safety for children)
- SAM referral system high-availability requirements
- Supply chain system integrity monitoring
- Frontline worker device security (2.7M mobile endpoints)
- Multi-ministry coordination security protocols
- Growth data integrity controls (false data affects intervention targeting)
- Immunization linkage security

---

## Summary: Public Health Program Classification

| Case Study | Program Type | Score | Tier |
|:-----------|:-------------|:-----:|:----:|
| SurveilHealth | Disease surveillance | 85 | **Tier 1** (auto) |
| TB-Mukt Bharat | TB elimination | 80 | **Tier 1** (auto) |
| Sankalp | NCD control | 75 | **Tier 1** |
| DrishtiRaksha | Blindness control | 60 | **Tier 1** |
| Poshan Rakshak | Nutrition/growth monitoring | 80 | **Tier 1** (auto) |

### Key Insights

1. **National surveillance is foundational CII**: Pandemic preparedness depends on surveillance system integrity
2. **Disease control programs have supply chain dependencies**: TB drugs, IOL distribution, nutrition supplements are attack vectors
3. **NCD programs need longitudinal integrity**: Chronic disease tracking requires decade-long data protection
4. **Child health programs are life-critical**: Nutrition monitoring and SAM referrals directly affect child mortality
5. **Frontline worker systems scale massively**: 2.7M devices create enormous endpoint security challenge

