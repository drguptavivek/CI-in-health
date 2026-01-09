# GERMANY

## Final categories

Germany applies **two distinct, formal classification layers** that can bring health-sector entities/systems into heightened cybersecurity obligations:

1. **KRITIS (Critical Infrastructure) — “Kritische Anlagen” / critical installations (anlagenbezogen)**
   * Instrument: **BSI-Kritisverordnung (BSI-KritisV)** (Verordnung zur Bestimmung kritischer Anlagen nach dem BSI-Gesetz). ([Gesetze im Internet][1])
   * Health sector thresholds are in **Anhang 5 (Sektor Gesundheit)**. ([Gesetze im Internet][2])

2. **NIS2 implementation (entity-based) — “Besonders wichtige Einrichtungen” and “Wichtige Einrichtungen”**
   * Instrument: **BSI-Gesetz (BSIG)** (2025 consolidated version on Gesetze-im-Internet), including sector lists in **Anlage 1** and **Anlage 2**. ([Gesetze im Internet][3])
   * Official statements indicate the **NIS-2 implementation law entered into force on 6 Dec 2025**. ([Bundesregierung][4])


## Exact legal / regulatory criteria (how classification is determined)

### A) KRITIS (Health sector) — threshold test in BSI-KritisV Anhang 5

A health installation is KRITIS-relevant when it matches an Anlagenkategorie in **Anhang 5** and meets the defined **Schwellenwert**. 

Examples explicitly shown in the annex include:

* **Hospitals (Krankenhaus)**: **Vollstationäre Fallzahl/Jahr = 30,000**. ([Gesetze im Internet][2])
* **Labor / lab IT service constellation** (diagnostics/therapy-control IT services for at least one lab): **1,500,000** (threshold shown in the Anhang 5 text snippet). ([Gesetze im Internet][2])
* **Blood/plasma donation control system** (*Blut- oder Plasmaspendensteuerungssystem*): **Hergestellte oder in Verkehr gebrachte Produkte/Jahr = 34,000**. ([Gesetze im Internet][5])

**Timing rule (when KRITIS status applies):** the BSI-KritisV provides that an installation is treated as KRITIS **from 1 April of the calendar year following** the year in which the threshold is first reached/ exceeded (and ceases similarly after dropping below). ([bmi.bund.de][6])


### B) NIS2 (BSIG 2025) — entity/sector test via Anlage 1 & Anlage 2

Under the BSIG consolidated 2025 version, the sector lists in **Anlage 1** and **Anlage 2** are used to classify organisations as:

* **“Besonders wichtige Einrichtungen”** (especially important) and/or
* **“Wichtige Einrichtungen”** (important),
depending on the applicable sector listing and legal framing. ([Gesetze im Internet][7])

**Health-relevant entries evidenced in the annexes include:**

* **Anlage 1** contains health-related entries such as **pharmaceutical R&D** (in relation to medicines), and references to **medical devices for public-health emergency situations** (linked to EU emergency mechanisms). ([Gesetze im Internet][7])
* **Anlage 2** includes **manufacture of in-vitro diagnostics** and related medical device manufacturing language (as shown in the Anlage 2 snippet). ([Gesetze im Internet][8])

*(The evidence above is limited to the retrieved official passages.)*


## Registration / notification (explicit requirement)

The BSIG includes a **registration obligation**: covered entities must register **no later than three months** and provide required information to the competent system/authority. ([Gesetze im Internet][9])


## Grading / tiering scheme (as evidenced)

* **KRITIS (BSI-KritisV):** effectively **binary** at installation level (threshold met vs not met), using **numeric thresholds** in Anhang 5. ([Gesetze im Internet][2])
* **NIS2 (BSIG 2025):** **two-tier entity categorisation** via **Anlage 1 vs Anlage 2** structure (especially important vs important sectors/entities). ([Gesetze im Internet][7])


## Public vs confidential

* **Public:** KRITIS thresholds for health are published in **Anhang 5** (Gesetze-im-Internet), and BSIG sector annexes are also published on Gesetze-im-Internet. ([Gesetze im Internet][2])
* **KRITIS statistics:** BSI publishes KRITIS “in figures” (aggregated reporting). ([BSI][10])


## Operational note

Germany’s hospital sector uses **B3S (branch-specific security standard) materials** in practice. The DKG’s submitted B3S document explicitly references applicability beyond only KRITIS hospitals (e.g., those exceeding **30,000** inpatient cases) and frames B3S usage as an implementation approach in context. ([dkgev.de][11])

## References (Germany)

1. **BSI-KritisV** (Gesetze-im-Internet) — regulation index. ([Gesetze im Internet][1])

2. **BSI-KritisV — Anhang 5 (Sektor Gesundheit)** (Gesetze-im-Internet) — hospital threshold 30,000 cases/year (and health sector annex basis). ([Gesetze im Internet][2])

3. **BSI-KritisV — health/lab IT threshold evidence** (Gesetze-im-Internet snippet from Anhang 5 showing 1,500,000). ([Gesetze im Internet][2])

4. **BSI-KritisV — Blut-/Plasmaspendensteuerungssystem threshold 34,000** (Gesetze-im-Internet + PDF snippet). ([Gesetze im Internet][5])

5. **BSI-KritisV timing rule (“ab dem 1. April …”)** (BMI PDF + Gesetze snippet). ([bmi.bund.de][6])

6. **BSIG (2025 consolidated)** (Gesetze-im-Internet) + **Anlage 1** + **Anlage 2**. ([Gesetze im Internet][3])

7. **Anlage 1 health-related entries (pharma R&D; emergency medical device linkage)** (Gesetze-im-Internet snippet). ([Gesetze im Internet][7])

8. **Anlage 2 health supply-chain entry (in-vitro diagnostics / medical devices manufacturing snippet)** (Gesetze-im-Internet snippet). ([Gesetze im Internet][8])

9. **BSIG §33 registration obligation (“spätestens drei Monate …”)** (Gesetze-im-Internet snippet). ([Gesetze im Internet][9])

10. **Entry into force date (6 Dec 2025) — Federal Government + BSI press release**. ([Bundesregierung][4])

11. **EU Regulation (EU) 2022/123 — Article 22 (“Liste kritischer Medizinprodukte …”)** (EUR-Lex PDF). ([EUR-Lex][12])

12. **DKG B3S hospital security standard submission document (2025-07-25)** (PDF). ([dkgev.de][11])


[1]: https://www.gesetze-im-internet.de/bsi-kritisv/ "BSI-KritisV Index"

[2]: https://www.gesetze-im-internet.de/bsi-kritisv/anhang_5.html "Anhang 5 BSI-KritisV: Health Sector"

[3]: https://www.gesetze-im-internet.de/bsig_2025/BJNR12D0B0025.html "BSI Act (BSIG) 2025"

[4]: https://www.bundesregierung.de/breg-de/aktuelles/nis-2-richtlinie-deutschland-2373174 "NIS2 Implementation in Germany | Bundesregierung"

[5]: https://www.gesetze-im-internet.de/bsi-kritisv/BJNR095800016.html "BSI-KritisV: Critical Infrastructure Determination"

[6]: https://www.bmi.bund.de/SharedDocs/downloads/DE/veroeffentlichungen/2016/kritis-vo.pdf?__blob=publicationFile&v=2 "KRITIS Regulation (BSI-KritisV) PDF"

[7]: https://www.gesetze-im-internet.de/bsig_2025/anlage_1.html "Anlage 1 BSIG: Especially Important Entities"

[8]: https://www.gesetze-im-internet.de/bsig_2025/anlage_2.html "Anlage 2 BSIG: Important Entities"

[9]: https://www.gesetze-im-internet.de/bsig_2025/__33.html "§ 33 BSIG: Registration Obligation"

[10]: https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/Kritische-Infrastrukturen/KRITIS-in-Zahlen/kritis-in-zahlen.html "KRITIS in Zahlen | BSI"

[11]: https://www.dkgev.de/fileadmin/default/Mediapool/2_Themen/2.1_Digitalisierung_Daten/2.1.4._IT-Sicherheit_und_technischer_Datenschutz/2.1.4.1._IT-Sicherheit_im_Krankenhaus/B3S_KH_v1.3_-_Gesamtdokument_Stand_Einreichung_BSI_2025-07-25.pdf "DKG B3S Hospital Security Standard v1.3"

[12]: https://eur-lex.europa.eu/legal-content/DE/TXT/PDF/?uri=CELEX%3A32022R0123 "Regulation (EU) 2022/123"

