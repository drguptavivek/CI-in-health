# CII Case Studies: Digital Health Platforms

This chapter presents case studies for **digital health platforms** including national health information systems, personal health records, and hospital management information systems (HMIS).

---

## Case Study 1: National Digital Health Platform - "SwasthyaSetu"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | SwasthyaSetu (fictional national health ID platform) |
| **Type** | National digital health infrastructure |
| **Operator** | National Health Authority (government agency) |
| **Coverage** | 800 million registered beneficiaries |
| **Functions** | Health ID issuance, consent management, health record linking, facility registry |
| **Integrations** | Connected to 50,000+ health facilities; insurance platforms; pharmacies |
| **Employees** | 450 (central team) |
| **Infrastructure** | Multi-cloud; government data centers |

### CII Classification Assessment

#### Automatic Tier 1 Trigger Analysis

| "Regardless of Size" Criterion | Applies? |
|:-------------------------------|:--------:|
| Operates national-level health information system | ✓ |
| National health ID infrastructure | ✓ |
| Connected to national insurance platform | ✓ |
| Cross-sector dependencies (links to multiple sectors) | ✓ |

### Classification Result

| Assessment | Result | Rationale |
|:-----------|:-------|:----------|
| **Automatic Tier 1** | Yes | Meets multiple "regardless of size" triggers |
| **Comparable to** | National EHR/HIE systems globally | Similar to Singapore NEHR, UK NHS Spine |

### Applicable Obligations (Tier 1 - National System)

- **Governance**: Dedicated CISO + Security Operations Centre
- **Audit**: Continuous security monitoring; annual third-party audit; penetration testing
- **Incident reporting**: 12-hour early warning; 48-hour detailed notification
- **Business continuity**: Real-time disaster recovery; multi-region failover
- **Supply chain**: Rigorous vendor security assessment; cloud security requirements
- **Regulatory**: Direct reporting to national cyber authority
- **Exercises**: Mandatory participation in national/sectoral cyber drills

---

## Case Study 2: Personal Health Record Platform - "MyHealthVault"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | MyHealthVault |
| **Type** | Private consumer PHR/health data aggregation platform |
| **Users** | 25 million registered users |
| **Data aggregated** | Lab reports, prescriptions, hospital records, wearable data |
| **Integrations** | Connected to 5,000+ labs, 2,000+ hospitals, 15 insurance companies |
| **Employees** | 350 |
| **Revenue model** | Freemium + B2B data analytics (anonymized) |
| **Infrastructure** | Multi-cloud (public cloud providers) |
| **Special consideration** | Aggregates data from multiple sources; consent-based sharing |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Data volume** | 25M users × multiple records = billions of health data points |
| **Data sensitivity** | Complete longitudinal health records; genetic data for some users |
| **Aggregation risk** | Single breach exposes data from multiple source institutions |
| **Third-party dependencies** | Uses third-party APIs, cloud infrastructure, AI/ML partners |
| **Cross-border considerations** | Some data processing in foreign jurisdictions |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | 25M users (not case-based, but data scale) | 25 |
| **B. Data Aggregation Risk** | Centralized aggregation of distributed health data | 20 |
| **C. Health System Integration** | Connected to hospitals, labs, insurance | 15 |
| **D. Consumer Dependency** | Users rely on platform for health record access | 10 |
| **TOTAL** | | **70** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 70 | **Tier 1 (Essential)** | Scale of data aggregation; integration with health ecosystem |

> [!WARNING]
> PHR platforms present **unique aggregation risks** not captured by traditional facility-based metrics. A breach affects data originally held by thousands of source institutions. This case demonstrates why **data volume and aggregation** should be explicit scoring factors.

### Applicable Obligations

- Dedicated CISO and DPO (Data Protection Officer)
- Annual third-party security audit + penetration testing
- 24-hour incident reporting for data breaches
- Consent management system audit
- Cloud vendor security assessment
- Cross-border data transfer compliance
- User notification protocols for breaches

---

## Case Study 3: State HMIS Platform - "SwasthyaMitra"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | SwasthyaMitra State HMIS Platform |
| **Type** | Hospital Management Information System serving state government hospitals |
| **Operator** | State Health Department (via NIC/state IT agency) |
| **Coverage** | 500+ district hospitals, sub-district hospitals, and CHCs across the state |
| **Users** | 45,000 healthcare workers; 800 facility administrators |
| **Functions** | Patient registration, OPD/IPD management, lab, pharmacy, billing, HMIS reporting |
| **Data volume** | 15 million patient records; 50 million annual transactions |
| **Infrastructure** | State Data Center; hybrid cloud backup |
| **Integrations** | Connected to national ABDM, state insurance, disease surveillance, referral network |
| **Special consideration** | **Single platform for entire state public health system** |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Scale** | 500+ facilities; single point of failure for state healthcare |
| **Dependency** | All state government hospitals depend on this platform |
| **Data concentration** | 15M patient records in single system |
| **Operational impact** | Outage affects patient care statewide |
| **Integration hub** | Gateway to national systems (ABDM, insurance) |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | 500+ facilities; 15M patient records | 30 |
| **B. System Dependency** | Single platform for all state public hospitals | 25 |
| **C. Integration Role** | Hub connecting facilities to national systems | 15 |
| **D. User Base** | 45,000 healthcare workers depend on system | 10 |
| **TOTAL** | | **80** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 80 | **Tier 1 (Essential)** | State-wide system; single point of failure for 500+ facilities |

> [!IMPORTANT]
> Large-scale HMIS platforms serving hundreds of facilities are **system-level CII** regardless of whether individual facilities would independently qualify. The **concentration risk** of a shared platform elevates criticality significantly.

### Applicable Obligations

- Dedicated security team (not just focal point)
- Continuous security monitoring (24/7 SOC)
- 12-24 hour incident reporting
- Disaster recovery with state-level failover
- Annual third-party penetration testing
- Change management security controls
- User access audit (45,000 users)
- API security for national integrations
- Backup and recovery testing (quarterly)
- Vendor security assessment (NIC/SI partners)

---

## Case Study 4: Multi-Hospital HMIS - "CareSync Enterprise"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | CareSync Enterprise HMIS |
| **Type** | Hospital Management Information System for private hospital group |
| **Operator** | CareSync Hospitals Private Limited |
| **Coverage** | 5 large hospitals (average 400 beds each; 2,000 total beds) |
| **Users** | 4,000 healthcare workers; 150 administrators |
| **Functions** | EMR, OPD/IPD, lab, radiology, pharmacy, billing, HR, analytics |
| **Data volume** | 2 million patient records; 8 million annual transactions |
| **Infrastructure** | Private cloud; DR site |
| **Integrations** | Insurance TPA, ABDM, lab aggregators |
| **Special consideration** | **Centralized system for mid-size hospital chain** |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Scale** | 5 hospitals; 2,000 beds total |
| **Dependency** | All 5 hospitals share single platform |
| **Data concentration** | 2M patient records |
| **Operational impact** | Outage affects 5 facilities simultaneously |
| **Market position** | Regional player; not nationally critical |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | 5 facilities; 2M patient records | 20 |
| **B. System Dependency** | Centralized platform for hospital chain | 15 |
| **C. Geographic Criticality** | Regional presence; alternative providers exist | 5 |
| **D. National Integration** | ABDM connected but not sole gateway | 5 |
| **TOTAL** | | **45** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 45 | **Tier 2 (Important)** | Mid-scale platform; regional not national impact |

> [!NOTE]
> Smaller multi-hospital HMIS platforms like CareSync are **Tier 2** rather than Tier 1. The key differentiator from SwasthyaMitra is **scale and concentration**: 5 hospitals vs 500+, regional vs statewide impact, and presence of alternative providers.

### Applicable Obligations

- Security focal point (may be shared CISO for group)
- Biennial third-party audit
- 72-96 hour incident reporting
- Business continuity plan with tested failover
- User access management
- Vendor security requirements
- ABDM integration security

---

## Comparison: Large vs Small HMIS

| Factor | SwasthyaMitra (Large) | CareSync (Small) |
|:-------|:---------------------|:-----------------|
| **Facilities** | 500+ | 5 |
| **Patient records** | 15M | 2M |
| **Users** | 45,000 | 4,000 |
| **Geographic scope** | State-wide | Regional |
| **Alternative providers** | No (sole state system) | Yes |
| **Tier** | **Tier 1** | **Tier 2** |
| **Audit frequency** | Annual | Biennial |
| **Reporting timeline** | 12-24 hours | 72-96 hours |
| **SOC requirement** | 24/7 dedicated | Shared/outsourced |

---

## Summary: Digital Health Platform Classification

| Case Study | Platform Type | Score | Tier |
|:-----------|:--------------|:-----:|:----:|
| SwasthyaSetu | National digital health | Auto | **Tier 1** (auto) |
| MyHealthVault | PHR/health data aggregator | 70 | **Tier 1** |
| SwasthyaMitra | State HMIS (500+ hospitals) | 80 | **Tier 1** |
| CareSync Enterprise | Multi-hospital HMIS (5 hospitals) | 45 | **Tier 2** |

### Key Insights

1. **National platforms are automatic Tier 1**: Any national-level health information system triggers automatic classification
2. **Data aggregation creates concentrated risk**: PHR platforms aggregating from thousands of sources have unique criticality
3. **HMIS scale determines tier**: 500+ facilities is Tier 1; 5 facilities is Tier 2—a 100x difference justifies different classification
4. **System-level assessment matters**: A platform's criticality exceeds the sum of its connected facilities

