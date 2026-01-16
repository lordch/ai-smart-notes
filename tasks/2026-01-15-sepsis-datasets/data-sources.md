# Źródła danych: Epidemiologia sepsy

Mapowanie pytań badawczych → źródła danych.

---

## 1. Wolumen pacjentów (TAM)

| Pytanie | Źródła danych |
|---------|---------------|
| Incydencja globalna | **Rudd et al. 2020 (Lancet)** — najczęściej cytowane globalne szacunki; WHO Global Health Estimates |
| Incydencja USA | **CDC WONDER**; **HCUP NIS** (Nationwide Inpatient Sample) — kody ICD dla sepsy |
| Incydencja EU | **ECDC** (European Centre for Disease Prevention and Control); Eurostat; narodowe rejestry (np. NHS Digital UK) |
| Hospitalizacje z podejrzeniem sepsy | HCUP NIS — szersze kody ICD (infekcje + SIRS); badania kohortowe ED |
| Liczba testów diagnostycznych | Raporty rynkowe (Kalorama, MarketsandMarkets); dane od producentów (bioMérieux, Roche) |
| Trendy i prognozy | **Fleischmann et al. 2016** (trend analysis); raporty market research |

**Kluczowe publikacje:**
- Rudd KE et al. "Global, regional, and national sepsis incidence and mortality, 1990–2017" Lancet 2020
- Fleischmann C et al. "Assessment of Global Incidence and Mortality of Hospital-treated Sepsis" AJRCCM 2016

---

## 2. Segmentacja po setting klinicznym

| Pytanie | Źródła danych |
|---------|---------------|
| Rozkład ED vs ICU vs ward | **HCUP NIS/NEDS** (Nationwide Emergency Department Sample); rejestry ICU |
| Rejestry ICU | **ICNARC** (UK), **ANZICS** (Australia/NZ), **eICU** (USA, Philips) |
| Gdzie POC ma przewagę | Badania kliniczne POC vs lab; publikacje o time-to-result |

**Kluczowe źródła:**
- eICU Collaborative Research Database (publicznie dostępna)
- MIMIC-IV (MIT, publicznie dostępna po rejestracji)

---

## 3. Ciężkość problemu (value justification)

| Pytanie | Źródła danych |
|---------|---------------|
| Śmiertelność overall | **Surviving Sepsis Campaign** data; metaanalizy; HCUP NIS |
| Śmiertelność per ciężkość | Publikacje używające Sepsis-3 definitions; rejestry ICU |
| Time-to-antibiotic impact | **Kumar et al. 2006** (klasyka); Seymour et al. 2017; Liu et al. 2017 |
| Koszt hospitalizacji | **AHRQ HCUPnet**; CMS Medicare data; Paoli et al. 2018 |
| LOS | HCUP NIS; publikacje cost-of-illness |
| Readmisje | CMS Hospital Readmissions Reduction Program data |

**Kluczowe publikacje:**
- Kumar A et al. "Duration of hypotension before initiation of effective antimicrobial therapy..." Crit Care Med 2006
- Seymour CW et al. "Time to Treatment and Mortality during Mandated Emergency Care for Sepsis" NEJM 2017

---

## 4. Diagnostyczny funnel

| Pytanie | Źródła danych |
|---------|---------------|
| % podejrzeń → potwierdzona sepsa | Badania kohortowe ED (np. Shapiro et al.); lokalne audyty |
| Culture-positive vs negative | **Phua et al. 2013**; metaanalizy; dane mikrobiologiczne szpitali |
| Czas oczekiwania na posiew | Publikacje o blood culture TAT; dane od producentów (BD BACTEC, bioMérieux) |
| Czas biomarkerów | Specyfikacje produktów (PCT: bioMérieux VIDAS, Roche Elecsys) |
| Czułość/swoistość metod | **Cochrane Reviews**; metaanalizy biomarkerów (Wacker et al. 2013 dla PCT) |

**Kluczowe publikacje:**
- Wacker C et al. "Procalcitonin as a diagnostic marker for sepsis: a systematic review and meta-analysis" Lancet Infect Dis 2013
- Phua J et al. "Characteristics and outcomes of culture-negative versus culture-positive severe sepsis" Crit Care 2013

---

## 5. Segmentacja po populacji

| Pytanie | Źródła danych |
|---------|---------------|
| Sepsa noworodkowa | **Vermont Oxford Network**; **NICHD Neonatal Research Network**; Stoll et al. publikacje |
| Sepsa pediatryczna | **SPROUT study** (Weiss et al. 2015); **PERSIST** registry |
| Geriatryczna | HCUP NIS z filtrem wiekowym; Martin et al. 2006 |
| Immunosupresja/onkologia | Rejestry onkologiczne; SEER-Medicare; publikacje o febrile neutropenia |
| Hospital-acquired vs community | HCUP NIS (admission source); Page et al. 2015 |

**Kluczowe publikacje:**
- Weiss SL et al. "Global epidemiology of pediatric severe sepsis: the sepsis prevalence, outcomes, and therapies study" AJRCCM 2015
- Stoll BJ et al. "Early Onset Neonatal Sepsis" (seria publikacji NICHD)

---

## 6. Etiologia

| Pytanie | Źródła danych |
|---------|---------------|
| Gram+ vs Gram- vs fungal | **EPIC II study** (Vincent et al. 2009); lokalne dane mikrobiologiczne |
| Top patogeny | EARS-Net (Europa); CDC NHSN (USA); publikacje surveillance |
| Antybiotykooporność | **EARS-Net annual reports**; **CDC AR Threats Report**; GLASS (WHO) |

**Kluczowe źródła:**
- EARS-Net: https://www.ecdc.europa.eu/en/surveillance-atlas-infectious-diseases
- CDC AR Threats Report: https://www.cdc.gov/drugresistance/biggest-threats.html

---

## Podsumowanie: Gdzie szukać najpierw

| Priorytet | Źródło | Co daje |
|-----------|--------|---------|
| 🔴 Must | Rudd et al. 2020 (Lancet) | Globalna incydencja, śmiertelność |
| 🔴 Must | Kumar et al. 2006 | Time-to-treatment impact |
| 🔴 Must | HCUP NIS / HCUPnet | USA: wolumen, koszty, LOS |
| 🟡 Should | MIMIC-IV / eICU | Granularne dane kliniczne |
| 🟡 Should | Wacker et al. 2013 | Biomarker performance |
| 🟢 Nice | EARS-Net | Etiologia, AMR |

---

*Utworzono: 2026-01-15*
