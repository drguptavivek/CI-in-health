# CII Case Studies: Registries, Biobanks, and Blood Services

This chapter presents case studies for **health data registries, biological sample repositories, and blood transfusion services**.

---

## Case Study 1: National Cancer Registry - "OncoWatch"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | OncoWatch National Cancer Registry |
| **Type** | National population-based cancer registry |
| **Operator** | National Institute of Cancer Research (government) |
| **Coverage** | 95% population coverage across 28 states |
| **Records** | 12 million cumulative cancer registrations since inception |
| **Annual new cases** | 1.4 million new registrations/year |
| **Data elements** | Demographics, diagnosis, staging, treatment, outcomes, mortality |
| **Integrations** | Linked to death registry, hospital cancer departments, pathology labs |
| **Uses** | National cancer control planning; research; epidemiology |

### CII Classification Assessment

#### Automatic Tier 1 Trigger Analysis

| "Regardless of Size" Criterion | Applies? |
|:-------------------------------|:--------:|
| National-level health information system | ✓ |
| Disease surveillance function | ✓ |
| Public health planning dependency | ✓ |
| Research infrastructure | ✓ |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Population Coverage** | 95% national coverage | 30 |
| **B. Data Sensitivity** | 12M cancer patient records with outcomes | 25 |
| **C. Public Health Function** | National cancer control planning | 20 |
| **D. Research Infrastructure** | Supports national/international cancer research | 10 |
| **TOTAL** | | **85** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 85 | **Tier 1 (Essential)** | National disease registry; public health planning dependency |

### Applicable Obligations

- Dedicated security officer
- Annual audit with focus on data integrity (registry accuracy is critical)
- 24-hour incident reporting
- Access control audit (researcher access management)
- Backup and recovery testing (longitudinal data irreplaceable)
- Data sharing agreement security review
- International collaboration security protocols

---

## Case Study 2: National Biobank - "JeevanKosh"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | JeevanKosh National Biobank |
| **Type** | National biological sample and data repository |
| **Operator** | National Institute of Biomedical Research (government) |
| **Sample holdings** | 5 million biological samples (blood, tissue, DNA) |
| **Linked data** | Clinical phenotypes, genomic data, longitudinal health outcomes |
| **Sources** | Population cohorts, disease-specific studies, hospital contributions |
| **Access** | Enables national and international research collaborations |
| **Infrastructure** | Automated sample storage (-80°C, liquid nitrogen); LIMS; linked databases |
| **Special consideration** | **Irreplaceable national research resource** |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Sample irreplaceability** | Samples from deceased donors or rare disease patients cannot be recreated |
| **Linked data sensitivity** | Samples linked to genomic, clinical, and outcome data |
| **Physical + cyber risks** | Both physical sample security and data security required |
| **Research dependency** | National health research ecosystem depends on biobank access |
| **Consent complexity** | Samples collected under specific consent; breach affects consent validity |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Sample Volume** | 5M biological samples | 25 |
| **B. Data Sensitivity** | Linked genomic + clinical data | 25 |
| **C. Irreplaceability** | Samples from discontinued cohorts, deceased donors | 20 |
| **D. Research Infrastructure** | National research ecosystem dependency | 15 |
| **TOTAL** | | **85** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 85 | **Tier 1 (Essential)** | Irreplaceable national research resource; linked sensitive data |

> [!NOTE]
> Biobanks present **hybrid physical-cyber security requirements**. Loss of sample integrity (physical) or linked data (cyber) both constitute major incidents. CII frameworks should explicitly address **biobank-specific criteria**.

### Applicable Obligations

- Dedicated security officer (physical + cyber)
- Annual audit covering both physical and IT security
- 24-hour incident reporting (including physical security events)
- Sample tracking integrity controls
- Access management for researchers (physical + data)
- Backup and disaster recovery for LIMS
- Consent management system security
- Third-party researcher security assessment
- International collaboration data transfer controls

---

## Case Study 3: State Blood Transfusion Council - "Jeevan Raksha"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | Jeevan Raksha State Blood Transfusion Council |
| **Type** | State-level blood transfusion coordination agency |
| **Coverage** | 28 districts; coordinates 45 blood banks |
| **Functions** | Blood inventory management, donor registry, cross-matching coordination |
| **Population served** | 50 million |
| **Employees** | 85 |
| **Digital systems** | State blood bank management system; real-time inventory |
| **Connectivity** | Connected to all district blood banks |

### CII Classification Assessment

#### Automatic Tier 1 Trigger Analysis

| "Regardless of Size" Criterion | Applies? |
|:-------------------------------|:--------:|
| Operates blood allocation services at regional level | ✓ |
| Single point of coordination for state blood supply | ✓ |
| Life-critical dependency (emergency transfusions) | ✓ |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | Not applicable (coordination agency) | 0 |
| **B. Public System Role** | State-level life-critical service | 25 |
| **C. Geographic Criticality** | Single coordination point for state | 20 |
| **D. Functions** | Blood bank coordination (life-critical) | 25 |
| **TOTAL** | | **70** |

### Classification Result

| Assessment | Result | Rationale |
|:-----------|:-------|:----------|
| **Score-based** | 70 → Tier 1 | High score on function and uniqueness |
| **Automatic Tier 1** | Yes | Blood supply coordination is automatic trigger |

### Applicable Obligations

- Dedicated security officer
- Real-time monitoring of blood inventory system
- 24-hour incident reporting (supply chain disruption)
- Business continuity: Manual fallback for blood matching/allocation
- Annual audit with focus on data integrity

---

## Summary: Registries, Biobanks, and Blood Services Classification

| Case Study | Entity Type | Score | Tier |
|:-----------|:------------|:-----:|:----:|
| OncoWatch | National cancer registry | 85 | **Tier 1** (auto) |
| JeevanKosh | National biobank | 85 | **Tier 1** |
| Jeevan Raksha | State blood coordination | 70 | **Tier 1** (auto) |

### Key Insights

1. **Disease registries support public health planning**: National registry data is irreplaceable and supports policy decisions
2. **Biobanks need hybrid security**: Physical sample integrity + cyber data protection are equally critical
3. **Blood services are life-critical**: Real-time coordination for emergency transfusions has immediate mortality implications
4. **Longitudinal data is irreplaceable**: Decades of registry/biobank data cannot be reconstructed after loss

