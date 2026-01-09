# CII Case Studies: Diagnostics, Pharma, and Biotech

This chapter presents case studies for **diagnostic services, pharmaceutical manufacturing, and biotechnology research** entities.

---

## Case Study 1: Private Laboratory Chain - "DiagnoFirst"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | DiagnoFirst Laboratory Network |
| **Type** | Private diagnostic laboratory chain |
| **Coverage** | 500 collection centres; 25 processing labs |
| **Tests performed** | 15 million per year |
| **Employees** | 4,000 |
| **Key services** | Pathology, radiology, molecular diagnostics |
| **Digital systems** | Centralized LIMS; patient portal; doctor portal |
| **Integrations** | Connected to 200+ hospitals; insurance platforms |

### CII Classification Assessment

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Scale** | 15M tests/year (major national diagnostic player) | 25 |
| **B. Capability** | Reference laboratory for complex diagnostics | 15 |
| **C. Geographic Criticality** | Alternative labs available in most areas | 5 |
| **D. National Program Integration** | Disease surveillance contributor; insurance linked | 15 |
| **TOTAL** | | **60** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 60 | **Tier 1 (Essential)** | Major diagnostic infrastructure; disease surveillance role |

### Applicable Obligations

- Group CISO for network
- Annual audit of centralized LIMS
- 24-48 hour incident reporting
- Supply chain security for IT vendors
- Data protection compliance (patient reports)

---

## Case Study 2: Genomic Sequencing Laboratory - "GenomeIndia Labs"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | GenomeIndia Labs |
| **Type** | Genomic sequencing and analysis laboratory |
| **Operator** | Public-private partnership (government + research institute) |
| **Capacity** | 500,000 whole genome sequences/year |
| **Data holdings** | 2 million genomic sequences (national population diversity project) |
| **Services** | Clinical genomics, research sequencing, population genomics |
| **Key infrastructure** | High-performance computing cluster; petabyte-scale storage |
| **Integrations** | Connected to national biobank, cancer registry, rare disease network |
| **Special consideration** | **National population genomic data asset** |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **Data uniqueness** | Population-representative genomic data is irreplaceable national asset |
| **Sensitivity** | Genomic data is uniquely identifying and immutable |
| **Research value** | Supports drug development, disease research, personalized medicine |
| **Sovereignty concern** | Foreign access to population genomics is national security issue |
| **Re-identification risk** | Genomic data cannot be truly anonymized |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Data Uniqueness** | 2M population genomic sequences (irreplaceable) | 30 |
| **B. Data Sensitivity** | Genomic data (highest sensitivity health data) | 25 |
| **C. National Strategic Value** | Population genomics as national asset | 20 |
| **D. Research Infrastructure** | Supports national health research ecosystem | 10 |
| **TOTAL** | | **85** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 85 | **Tier 1 (Essential)** | National genomic data asset; highest sensitivity data type |

> [!CAUTION]
> Genomic data presents **unique risks** not fully captured by traditional health data frameworks. It is permanently identifying, affects biological relatives, and has sovereignty implications. Jurisdictions should consider **genomic-specific CII criteria**.

### Applicable Obligations

- Dedicated CISO with research data security expertise
- Annual third-party audit including HPC infrastructure
- 24-hour incident reporting for any data exfiltration
- Access control: Tiered researcher access with approval workflow
- Data sovereignty: No unauthorized cross-border transfer
- Encryption: At-rest and in-transit for all genomic data
- Consent management audit
- International collaboration review (data sharing agreements)

---

## Case Study 3: Vaccine Manufacturer - "BioShield Pharma"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | BioShield Pharma Ltd. |
| **Type** | Vaccine and biologics manufacturer |
| **Products** | 12 vaccines in portfolio (including childhood immunization, COVID-19) |
| **Production capacity** | 500 million doses/year |
| **Market share** | 35% of national vaccine supply; exports to 40 countries |
| **Employees** | 8,000 |
| **Key systems** | Manufacturing Execution System (MES), Quality Management System (QMS), Cold chain monitoring, Batch release systems |
| **Regulatory status** | WHO prequalified; national regulatory authority licensed |
| **Special consideration** | **Critical to national immunization program** |

### CII Classification Assessment

#### Automatic Tier 1 Trigger Analysis

| "Regardless of Size" Criterion | Applies? |
|:-------------------------------|:--------:|
| Critical to national immunization infrastructure | ✓ |
| Significant share (>20%) of essential medicine supply | ✓ |
| Export dependency by other countries | ✓ |
| Pandemic preparedness role | ✓ |

#### Scoring (Using EU NIS2 Annex II-inspired criteria)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. Supply Criticality** | 35% of national vaccine supply | 30 |
| **B. Manufacturing Scale** | 500M doses/year | 25 |
| **C. Essential Medicine** | Childhood immunization vaccines | 20 |
| **D. Export/International** | WHO prequalified; 40 countries depend | 15 |
| **TOTAL** | | **90** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 90 | **Tier 1 (Essential)** | Critical national supply; automatic trigger for essential medicine manufacturing |

> [!NOTE]
> EU NIS2 Annex II explicitly includes **pharmaceutical manufacturers** and **medicinal products**. This case demonstrates applying supply-chain criticality metrics beyond traditional healthcare delivery.

### Applicable Obligations

- Dedicated CISO with OT/ICS security expertise
- Annual audit of manufacturing systems (MES, QMS)
- 24-hour incident reporting for production disruptions
- Supply chain security for raw materials and packaging
- Business continuity: Redundant manufacturing capability
- Cold chain system monitoring and backup
- Coordination with national immunization program authority

---

## Case Study 4: Biotech Research Company - "GeneSys BioTech"

### Entity Profile

| Attribute | Details |
|:----------|:--------|
| **Name** | GeneSys BioTech Private Limited |
| **Type** | Biotech research company developing biosimilars |
| **Products in pipeline** | 8 biosimilars (oncology, autoimmune); 3 in Phase III trials |
| **Key IP** | Proprietary cell lines, manufacturing processes, clinical trial data |
| **Employees** | 1,200 |
| **R&D investment** | $150M cumulative in current pipeline |
| **Key systems** | Electronic Lab Notebook (ELN), Clinical Trial Management System (CTMS), IP database, Bioinformatics cluster |
| **Partnerships** | Licensing agreements with 3 multinational pharma companies |
| **Special consideration** | **High-value IP target; national biotech capability** |

### CII Classification Assessment

#### Key Risk Factors

| Factor | Assessment |
|:-------|:-----------|
| **IP value** | $150M+ R&D investment; biosimilar formulations are high-value targets |
| **State-actor threat** | Biosimilar development is target for economic espionage |
| **National capability** | One of few domestic companies with advanced biosimilar capability |
| **Clinical data** | Phase III trial data for thousands of patients |
| **Supply chain** | Potential future essential medicine supplier |

#### Scoring (Developing Country Framework)

| Domain | Criterion | Points Scored |
|:-------|:----------|:-------------:|
| **A. IP/Data Sensitivity** | Proprietary biosimilar formulations; cell lines | 25 |
| **B. National Strategic Value** | Domestic biotech capability; import substitution potential | 20 |
| **C. Clinical Trial Data** | Multi-thousand patient trial data | 15 |
| **D. Future Supply Chain Role** | Pipeline products for oncology/autoimmune | 10 |
| **TOTAL** | | **70** |

### Classification Result

| Framework | Score | Tier | Rationale |
|:----------|:------|:-----|:----------|
| **Developing Country** | 70 | **Tier 1 (Essential)** | Strategic IP value; national biotech capability |

> [!IMPORTANT]
> This case illustrates **IP-based criticality** distinct from service delivery. Compromise of biosimilar development IP could set back national pharmaceutical capability by years and benefit foreign competitors. **Economic security** is a valid CII consideration.

### Applicable Obligations

- Dedicated CISO with R&D security focus
- IP protection controls (access management, DLP, insider threat)
- Annual security audit including research systems
- 48-hour incident reporting (IP theft/exfiltration focus)
- Third-party research partner security assessment
- Bioinformatics infrastructure protection
- Secure collaboration protocols for international partners

---

## Summary: Diagnostics, Pharma, and Biotech Classification

| Case Study | Entity Type | Score | Tier |
|:-----------|:------------|:-----:|:----:|
| DiagnoFirst Labs | Private lab chain | 60 | **Tier 1** |
| GenomeIndia Labs | Genomic sequencing lab | 85 | **Tier 1** |
| BioShield Pharma | Vaccine manufacturer | 90 | **Tier 1** (auto) |
| GeneSys BioTech | Biotech (biosimilars IP) | 70 | **Tier 1** |

### Key Insights

1. **Major diagnostic chains are CII**: Laboratories with significant market share and disease surveillance roles qualify for Tier 1
2. **Genomic data has unique sovereignty implications**: Population genomics is a national asset requiring special protection
3. **Supply chain entities are CII**: Vaccine/pharma manufacturers with significant market share are Critical Infrastructure
4. **IP-based criticality is valid**: High-value biotech research IP warrants CII consideration for economic security

