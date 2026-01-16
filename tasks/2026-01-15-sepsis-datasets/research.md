# Datasety epidemiologii sepsy - Research

Data: 2026-01-15

## Podsumowanie dostępności

| Kategoria | Ilość | Możliwość pobrania przez agenta |
|-----------|-------|--------------------------------|
| 🟢 W pełni otwarte | 8 | ✅ Tak |
| 🟡 Darmowe z rejestracją | 12 | ❌ Wymaga ludzkiej rejestracji |
| 🔴 Płatne / ograniczone | 5 | ❌ Nie |

---

## 🟢 W PEŁNI OTWARTE (bez rejestracji)

### 1. Kaggle - Prediction of Sepsis
- **URL:** https://www.kaggle.com/datasets/salikhussaini49/prediction-of-sepsis
- **Dostęp:** Publiczny (wymaga konta Kaggle, ale darmowe)
- **Zawartość:** Dane kliniczne do predykcji sepsy
- **Populacja:** Pacjenci ICU
- **Agent może pobrać:** ✅ Tak (przez Kaggle API)

**Zastosowanie w analizie:**
- Analiza czynników ryzyka sepsy
- Budowa modeli predykcyjnych
- Identyfikacja kluczowych biomarkerów klinicznych
- Baseline do porównania z innymi datasetami

---

### 2. Kaggle - Sepsis Survival Prediction
- **URL:** https://www.kaggle.com/datasets/joebeachcapital/sepsis-survival-minimal-clinical-records
- **Dostęp:** Publiczny
- **Zawartość:** Minimalne dane kliniczne + outcome (przeżycie)
- **Agent może pobrać:** ✅ Tak

**Zastosowanie w analizie:**
- Analiza śmiertelności sepsy
- Identyfikacja predyktorów przeżycia
- Prosty dataset do szybkich analiz eksploracyjnych

---

### 3. NCHS WONDER - Mortality Data
- **URL:** https://wonder.cdc.gov/
- **Dostęp:** Publiczny interfejs webowy
- **Zawartość:** Dane o zgonach USA 1999-2024, kody ICD-10
- **Granularność:** Rok, wiek, płeć, rasa, stan, przyczyna zgonu
- **Agent może pobrać:** ⚠️ Częściowo (przez web scraping lub manual export)

**Zastosowanie w analizie:**
- **Trendy czasowe** śmiertelności z sepsy w USA (25+ lat danych)
- **Dysproporcje demograficzne** - wiek, płeć, rasa
- **Geograficzne różnice** między stanami
- **Wpływ COVID-19** na śmiertelność z sepsy
- Porównanie kodowania ICD-9 vs ICD-10

---

### 4. GBD Results Tool (IHME)
- **URL:** https://vizhub.healthdata.org/gbd-results/
- **Dostęp:** Publiczny eksport CSV
- **Zawartość:** Incydencja, śmiertelność, DALY dla sepsy 1990-2021
- **Zakres:** 204 kraje, wszystkie grupy wiekowe
- **Agent może pobrać:** ✅ Tak (eksport CSV)

**Zastosowanie w analizie:**
- **Globalne porównania** - kraje, regiony WHO
- **Trendy 30-letnie** incydencji i śmiertelności
- **Obciążenie chorobowe** (DALY, YLL, YLD)
- **Stratyfikacja** wg wieku, płci, SDI (Socio-Demographic Index)
- Analiza nierówności globalnych (LMIC vs HIC)

---

### 5. Data.gov - Sepsis Datasets
- **URL:** https://catalog.data.gov/dataset/?tags=sepsis
- **Dostęp:** Publiczny
- **Zawartość:** Różne zbiory rządowe USA dot. sepsy
- **Agent może pobrać:** ✅ Tak

**Zastosowanie w analizie:**
- Dane z programów federalnych
- Metryki jakości szpitali
- Uzupełnienie innych źródeł

---

### 6. GEO NCBI - Dane genomiczne
- **URL:** https://www.ncbi.nlm.nih.gov/geo/
- **Dostęp:** Publiczny
- **Kluczowe datasety:**
  - GSE185263 - największy RNA-seq (348 sepsa, 44 kontrole)
  - GSE65682 - sepsa vs SIRS
  - GSE54514 - sepsa pediatryczna
  - GSE95233 - early vs late sepsis
- **Agent może pobrać:** ✅ Tak (przez GEOquery lub bezpośrednio)

**Zastosowanie w analizie:**
- **Biomarkery molekularne** sepsy
- **Sygnatury transkryptomiczne** - rozróżnienie sepsy od SIRS
- **Fenotypy sepsy** - subgrupy pacjentów
- Identyfikacja targetów terapeutycznych
- Walidacja biomarkerów klinicznych

---

### 7. WHO Mortality Database
- **URL:** https://www.who.int/data/data-collection-tools/who-mortality-database
- **Dostęp:** Publiczny
- **Zawartość:** Standaryzowane wskaźniki zgonów, 36 krajów, 1985-2019
- **Agent może pobrać:** ✅ Tak

**Zastosowanie w analizie:**
- **Porównania międzynarodowe** śmiertelności
- **Długoterminowe trendy** (35 lat)
- Standaryzacja wg wieku dla porównań
- Analiza zmian definicji/kodowania w czasie

---

### 8. SC2sepsis Database
- **URL:** https://academic.oup.com/database/article/doi/10.1093/database/baac061/6671201
- **Dostęp:** Publiczny interfejs webowy
- **Zawartość:** Single-cell RNA-seq sepsy, 20 populacji komórkowych z PBMC
- **Agent może pobrać:** ⚠️ Przez interfejs webowy

**Zastosowanie w analizie:**
- **Odpowiedź immunologiczna** na poziomie pojedynczych komórek
- Identyfikacja kluczowych populacji komórkowych
- Mechanizmy immunosupresji w sepsie

---

## 🟡 DARMOWE Z REJESTRACJĄ

### 9. MIMIC-IV (PhysioNet)
- **URL:** https://physionet.org/content/mimiciv/3.1/
- **Rejestracja:** Konto PhysioNet + CITI training + DUA
- **Czas uzyskania dostępu:** ~1-2 tygodnie
- **Zawartość:**
  - 364,627 pacjentów, 94,458 pobytów ICU
  - Dane 2008-2019, Beth Israel Deaconess (Boston)
  - Vital signs, lab, leki, procedury, notatki kliniczne
- **Agent może pobrać:** ❌ (wymaga ludzkiej rejestracji)

**Zastosowanie w analizie:**
- **Złoty standard** do badań ICU nad sepsą
- Szczegółowa charakterystyka kliniczna pacjentów septycznych
- Analiza trajektorii choroby (od przyjęcia do wypisu/zgonu)
- Skuteczność interwencji (antybiotyki, płyny, wazopresory)
- Predykcja outcomes (śmiertelność, czas pobytu, readmisje)
- Identyfikacja fenotypów sepsy (klastry pacjentów)
- Analiza compliance z wytycznymi (Surviving Sepsis Campaign)

---

### 10. MIMIC-III (PhysioNet)
- **URL:** https://physionet.org/content/mimiciii/1.4/
- **Rejestracja:** Jak MIMIC-IV
- **Zawartość:** 40,000+ pacjentów, 26 tabel relacyjnych
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- Replikacja publikowanych badań (większość literatury używa MIMIC-III)
- Porównanie z nowszymi danymi MIMIC-IV
- Dostęp do większej liczby gotowych skryptów/narzędzi

---

### 11. eICU Collaborative Research Database
- **URL:** https://physionet.org/content/eicu-crd/
- **Rejestracja:** PhysioNet credentialed access
- **Zawartość:** 139,000+ pacjentów z wielu szpitali USA
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Wieloośrodkowa walidacja** modeli z MIMIC
- Analiza zmienności między szpitalami
- Generalizowalność wyników
- Różnice regionalne w USA

---

### 12. HiRID (PhysioNet)
- **URL:** https://physionet.org/content/hirid/1.0/
- **Rejestracja:** PhysioNet credentialed access
- **Zawartość:** ICU Bern (Szwajcaria), dane co 2 minuty
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Wysoka rozdzielczość czasowa** - dynamika sepsy
- Wczesne wykrywanie pogorszenia
- Europejski kontekst (porównanie z USA)
- Analiza real-time alertów

---

### 13. SICdb - Salzburg ICU Database
- **URL:** https://physionet.org/content/sicdb/1.0.5/
- **Rejestracja:** PhysioNet credentialed access
- **Zawartość:** 27,386 przyjęć, 4 ICU, dane co minutę, 2013-2021
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Najwyższa granularność** (co minutę)
- Europejskie standardy opieki
- Analiza krótkoterminowej dynamiki (godziny)

---

### 14. AmsterdamUMCdb
- **URL:** https://amsterdammedicaldatascience.nl/amsterdamumcdb/
- **Rejestracja:** Osobna aplikacja
- **Zawartość:** 23,000 przyjęć, Holandia, 2003-2016
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- Europejski mixed surgical-medical ICU
- Długi okres obserwacji (13 lat)
- Porównanie praktyk europejskich vs amerykańskich

---

### 15. PhysioNet Challenge 2019
- **URL:** https://physionet.org/content/challenge-2019/1.0.0/
- **Rejestracja:** Konto PhysioNet (prostsze niż credentialed)
- **Zawartość:** 40,336 pacjentów ICU, 3 systemy szpitalne
- **Format:** Dane godzinowe, vital signs, lab, demographics
- **Agent może pobrać:** ⚠️ Możliwe po prostej rejestracji

**Zastosowanie w analizie:**
- **Benchmark** dla modeli ML wczesnej detekcji sepsy
- Standaryzowany format danych
- Porównanie algorytmów predykcyjnych
- Definicja sepsy wg Sepsis-3

---

### 16. N3C (National COVID Cohort Collaborative)
- **URL:** https://covid.cd2h.org/N3C
- **Rejestracja:** Instytucjonalny DUA
- **Zawartość:** 23 mln osób, 240 organizacji, dane COVID + sepsa
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Sepsa w kontekście COVID-19**
- Największy zbiór pandemiczny USA
- Interakcja viral sepsis z bacterial sepsis
- Zmiany w epidemiologii 2020-2023

---

### 17. ISARIC COVID-19
- **URL:** https://isaric.org/
- **Rejestracja:** Współpraca badawcza
- **Zawartość:** 705,000+ hospitalizowanych, 62 kraje
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Globalna perspektywa** COVID/sepsy
- Porównania międzynarodowe praktyk
- Outcomes w różnych systemach zdrowotnych

---

### 18. BioLINCC - PETAL Network Trials
- **URL:** https://biolincc.nhlbi.nih.gov/
- **Rejestracja:** Aplikacja badawcza
- **Dostępne trialle:**
  - CLOVERS (resuscytacja płynowa w sepsie)
  - ROSE (blokada nerwowo-mięśniowa)
  - ASTER (acetaminophen w sepsie)
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Dane z RCT** - najwyższa jakość
- Analiza skuteczności interwencji
- Szczegółowe dane o ARDS/sepsie
- Biospecimeny do badań translacyjnych

---

### 19. CHoRUS Dataset
- **URL:** Dostępne przez AIM-AHEAD
- **Rejestracja:** Wymagana
- **Zawartość:** 11,312 pacjentów, format OMOP CDM
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Standaryzowany format OMOP** - łatwa integracja
- AI/ML ready
- 19.85% z sepsą

---

### 20. HMS-Sepsis Registry Michigan
- **URL:** Kontakt z autorami
- **Zawartość:** 66 szpitali Michigan, 2020-2024
- **Agent może pobrać:** ❌

**Zastosowanie w analizy:**
- Community-onset sepsis
- Quality improvement metrics
- Najnowsze dane (do 2024)

---

## 🔴 PŁATNE / OGRANICZONE

### 21. HCUP NIS (National Inpatient Sample)
- **URL:** https://hcup-us.ahrq.gov/nisoverview.jsp
- **Koszt:** ~$200-500 za rok danych
- **Zawartość:** 7 mln wypisów/rok, 33 mln ważonych
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Reprezentatywność narodowa** USA
- Trendy hospitalizacji z sepsą
- Koszty leczenia
- Dysproporcje rasowe/ekonomiczne
- Comorbidities i outcomes

---

### 22. HCUP SID (State Inpatient Databases)
- **URL:** https://hcup-us.ahrq.gov/
- **Koszt:** Zależny od stanu
- **Zawartość:** Wszystkie hospitalizacje w danym stanie
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- Analizy stanowe
- Porównania między stanami
- Policy analysis

---

### 23. CMS Medicare/Medicaid Claims
- **URL:** https://www.cms.gov/Research-Statistics-Data-and-Systems
- **Koszt:** Płatny + DUA
- **Zawartość:** Claims data ubezpieczonych federalnie
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- Populacja 65+ (Medicare)
- Longitudinalne śledzenie pacjentów
- Readmisje, koszty długoterminowe

---

### 24. SPROUT Study Data
- **URL:** Kontakt z autorami
- **Zawartość:** 128 PICU, 26 krajów, 6,925 dzieci
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Sepsa pediatryczna** - globalna perspektywa
- Point prevalence
- Rozbieżności definicji vs praktyka kliniczna

---

### 25. BARNARDS Study Data
- **URL:** Kontakt z autorami
- **Zawartość:** Neonatal sepsis, 7 LMIC, 12 ośrodków
- **Agent może pobrać:** ❌

**Zastosowanie w analizie:**
- **Sepsa noworodkowa w LMIC**
- Patogeny specyficzne dla regionu
- Antybiotykooporność

---

## 🇵🇱 ŹRÓDŁA POLSKIE

### Polish Severe Sepsis Registry (Rejestr Ciężkiej Sepsy)
- **Prowadzący:** Polish Working Group for Sepsis (PTAiIT)
- **Koordynator:** Prof. Andrzej Kübler, Uniwersytet Medyczny we Wrocławiu
- **Kontakt:** kai@umed.wroc.pl
- **Okres:** 2003 - ongoing
- **Zakres:** >4,000 rekordów (do 2007), 140 ICU w Polsce
- **Dostęp:** 🔴 Zamknięty - wymaga kontaktu z autorami
- **Agent może pobrać:** ❌

**Zawartość:**
- Dane demograficzne (wiek średni 57 lat, 58% mężczyźni)
- Przyczyny sepsy (56% chirurgiczne, 49% infekcje wewnątrzbrzuszne)
- Dysfunkcja narządowa (89% ≥3 narządy)
- APACHE II score (średnio 26 pkt)
- Mikrobiologia (58% Gram-ujemne, 34% Gram-dodatnie, 16% grzyby)
- Posiewy krwi (41% dodatnie)
- Outcomes - śmiertelność spadła z 54-56% (2003-04) do 46% (2009)

**Zastosowanie w analizie:**
- **Jedyne szczegółowe dane kliniczne sepsy z Polski**
- Trendy śmiertelności w polskich ICU
- Charakterystyka mikrobiologiczna (polska specyfika patogenów)
- Porównanie z danymi europejskimi (MIMIC, AmsterdamUMCdb)
- Ocena compliance z wytycznymi SSC w Polsce

**Kluczowe publikacje:**
- Kübler A et al. "Results of the severe sepsis registry in ICUs in Poland from 2003-2009" (2015)
- Kübler A et al. "Severe sepsis in Poland - point prevalence study 2012-2013" (2015)
- Kübler A et al. "Severe sepsis in Poland - internet surveillance of 1043 cases" (2004)

---

### NFZ - API Statystyki Świadczeń ✅ POBRANE
- **URL:** https://api.nfz.gov.pl/app-stat-api-jgp/
- **Portal:** https://statystyki.nfz.gov.pl/
- **Dostęp:** 🟢 Publiczny (API)
- **Agent może pobrać:** ✅ Tak (przez API)
- **Plik:** `data/nfz_sepsis_hospitalizations.csv`

**Dostępne grupy JGP dla sepsy:**
- `S53 POSOCZNICA` - dane 2009-2012
- `S56 POSOCZNICA O CIĘŻKIM PRZEBIEGU` - dane 2014-2024
- `P51 POSOCZNICA O CIĘŻKIM PRZEBIEGU LECZONA ZACHOWAWCZO` - dane 2019-2024 (dzieci)

**Zawartość pobranych danych:**
- Liczba pacjentów i hospitalizacji
- Wskaźnik rehospitalizacji
- Mediana i moda czasu pobytu (dni)
- Średni koszt hospitalizacji (PLN i punkty)

**Kluczowe obserwacje:**
| Grupa | Rok | Hospitalizacje | Trend |
|-------|-----|----------------|-------|
| S53 | 2009 | 10,209 | - |
| S53 | 2012 | 16,072 | +57% |
| S56 | 2014 | 11,460 | - |
| S56 | 2024 | 31,721 | +177% |
| P51 (dzieci) | 2019 | 282 | - |
| P51 (dzieci) | 2024 | 678 | +140% |

**Ograniczenia:**
- Dane zagregowane (nie indywidualne)
- Brak danych S53 po 2012 (zmiana klasyfikacji?)
- Brak danych o śmiertelności w API
- Brak podziału wg województw w podstawowych danych

---

### GUS - Statystyka Przyczyn Zgonów
- **URL:** https://stat.gov.pl/obszary-tematyczne/ludnosc/statystyka-przyczyn-zgonow/
- **Dostęp:** 🟢 Publiczny
- **Agent może pobrać:** ✅ Tak (raporty PDF, dane tabelaryczne)

**Zawartość:**
- Zgony wg przyczyn (ICD-10)
- Podział wg wieku, płci, województwa
- Roczne raporty

**Zastosowanie w analizie:**
- **Oficjalna śmiertelność z sepsy w Polsce**
- Trendy wieloletnie
- Porównania regionalne
- Porównanie z danymi WHO/GBD

**⚠️ WAŻNE OGRANICZENIE:**
Sepsa jest **niedorejestrowana** w oficjalnych statystykach:
- Szacunki: ~25,000 zgonów/rok z sepsy w Polsce
- Oficjalne statystyki znacznie niższe
- Problem: sepsa często kodowana jako choroba podstawowa (np. zapalenie płuc)
- Prof. Kübler: "Przypadki sepsy nie są prawidłowo rejestrowane przez lekarzy"

---

### NIZP-PZH - Meldunki Epidemiologiczne
- **URL:** https://www.pzh.gov.pl/serwisy-tematyczne/meldunki-epidemiologiczne/
- **Biuletyny:** https://wwwold.pzh.gov.pl/oldpage/epimeld/
- **Dostęp:** 🟢 Publiczny
- **Agent może pobrać:** ✅ Tak

**Zawartość:**
- Choroby zakaźne i zatrucia w Polsce (roczniki)
- Meldunki dwutygodniowe, kwartalne, roczne
- Nadzór epidemiologiczny

**Zastosowanie w analizie:**
- **Infekcje prowadzące do sepsy** (nie sama sepsa)
- Trendy chorób zakaźnych
- Kontekst epidemiologiczny

**Ograniczenie:** Sepsa jako taka nie jest raportowana w meldunkach PZH (nie jest "chorobą zakaźną" w rozumieniu ustawy).

---

### Przegląd Epidemiologiczny (czasopismo)
- **URL:** https://www.przeglepidemiol.pzh.gov.pl/
- **Wydawca:** NIZP-PZH
- **Dostęp:** 🟢 Open access
- **Agent może pobrać:** ✅ Tak (artykuły PDF)

**Zastosowanie w analizie:**
- Publikacje o epidemiologii sepsy w Polsce
- Kronika Epidemiologiczna - raporty sytuacyjne
- Kontekst dla danych ilościowych

---

### Dane epidemiologiczne z publikacji polskich autorów

| Metryka | Wartość | Źródło |
|---------|---------|--------|
| Incydencja ciężkiej sepsy | 65/100,000/rok | NHC system via Kübler 2015 |
| Pacjenci z sepsą w ICU | ~24,905/rok | NHC system |
| Prevalence sepsy w ICU | 34% (wszystkie formy) | Point prevalence 2012-13 |
| Prevalence ciężkiej sepsy | 16% | Point prevalence 2012-13 |
| Prevalence wstrząsu septycznego | 6% | Point prevalence 2012-13 |
| Śmiertelność ICU | 46% (2009) | Rejestr 2003-2009 |
| Szacowane zgony rocznie | ~25,000 | Eksperci (Kübler) |

---

### Podsumowanie źródeł polskich

| Źródło | Dostęp | Dane o sepsie | Agent |
|--------|--------|---------------|-------|
| Polish Severe Sepsis Registry | 🔴 Kontakt | ✅ Bezpośrednie, szczegółowe | ❌ |
| NFZ API | 🟢 Publiczny | ⚠️ Pośrednie (kody ICD) | ✅ |
| GUS zgony | 🟢 Publiczny | ⚠️ Niedorejestrowane | ✅ |
| PZH meldunki | 🟢 Publiczny | ❌ Brak sepsy | ✅ |
| GBD (Polska) | 🟢 Publiczny | ✅ Modelowane | ✅ |

**Rekomendacja:** Dla polskich danych najlepsze źródło to **kontakt z Prof. Küblerem** (Rejestr) + **GBD** (modelowane dane dla Polski) + **NFZ API** (hospitalizacje).

---

## PRIORYTETYZACJA DLA ANALIZY

### Faza 1: Natychmiastowy dostęp (agent może pobrać)
1. **GBD Results Tool** → globalne trendy, porównania międzynarodowe
2. **NCHS WONDER** → trendy USA, demografia
3. **Kaggle datasets** → szybkie prototypowanie ML
4. **GEO (GSE185263)** → biomarkery molekularne

### Faza 2: Krótka rejestracja (~1-2 tyg)
5. **MIMIC-IV** → szczegółowa analiza kliniczna ICU
6. **eICU** → walidacja wieloośrodkowa
7. **PhysioNet Challenge 2019** → benchmark ML

### Faza 3: Dłuższa rejestracja / płatne
8. **HCUP NIS** → reprezentatywność narodowa, koszty
9. **N3C** → kontekst COVID
10. **BioLINCC** → dane z RCT

---

## MAPOWANIE NA WYMIARY ANALIZY

| Wymiar analizy | Priorytetowe datasety |
|----------------|----------------------|
| **Incydencja globalna** | GBD, WHO Mortality |
| **Śmiertelność** | GBD, NCHS WONDER, MIMIC-IV |
| **Trendy czasowe** | GBD (1990-2021), NCHS (1999-2024), WHO (1985-2019) |
| **Demografia (wiek, płeć)** | GBD, NCHS WONDER, HCUP NIS |
| **Geografia/regiony** | GBD, NCHS WONDER (stany), eICU |
| **Koszty** | HCUP NIS, CMS |
| **Charakterystyka kliniczna** | MIMIC-IV, eICU, HiRID |
| **Biomarkery** | GEO, MIMIC-IV (lab) |
| **Pediatria** | SPROUT, BARNARDS, CDC EOS |
| **LMIC** | GBD, BARNARDS, GLOSS |
| **COVID-19** | N3C, ISARIC |
| **Predykcja ML** | PhysioNet 2019, Kaggle, MIMIC |
| **🇵🇱 Polska** | GBD (Polska), NFZ API, Polish Severe Sepsis Registry |

---

## 📦 POBRANE DANE (2026-01-15)

Lokalizacja: `tasks/2026-01-15-sepsis-datasets/data/`

### Podsumowanie

| Dataset | Rozmiar | Rekordy | Status |
|---------|---------|---------|--------|
| GEO GSE185263 (RNA-seq) | 11 MB | 348 pacjentów | ✅ Pobrane |
| Kaggle Sepsis Prediction (PhysioNet 2019) | 462 MB | 1.55 mln wierszy + 20,336 plików pacjentów | ✅ Pobrane |
| Kaggle Sepsis Survival | 1.1 MB | 129,395 rekordów (3 kohorty) | ✅ Pobrane |
| California Severe Sepsis | 4 KB | 15 lat (2010-2024) | ✅ Pobrane |
| WHO Neonatal Mortality | 9.1 MB | 14,858 rekordów (LMIC) | ✅ Pobrane |
| **🇵🇱 NFZ Hospitalizacje Sepsa** | 1.3 KB | 21 rekordów (2009-2024) | ✅ Pobrane |

**Łączny rozmiar:** ~560 MB

---

### 1. GEO GSE185263 - Transkryptomika sepsy

**Pliki:**
- `GSE185263_raw_counts.csv.gz` (11 MB) - raw RNA-seq counts
- `GSE185263_series_matrix.txt` (748 KB) - metadata pacjentów

**Zawartość:**
- 348 pacjentów z sepsy + 44 kontrole
- Dane z 4 emergency rooms + 1 ICU
- Pełne profile transkryptomiczne (RNA-seq)
- Dane kliniczne: severity, organ dysfunction, mortality

**Publikacja:** "Predicting sepsis severity at first clinical presentation" (PMID: 35027333)

**Użycie:**
```python
import pandas as pd
import gzip
# Wczytanie counts
with gzip.open('GSE185263_raw_counts.csv.gz', 'rt') as f:
    counts = pd.read_csv(f)
```

---

### 2. Kaggle Sepsis Prediction (PhysioNet Challenge 2019)

**Pliki:**
- `kaggle_sepsis/Dataset.csv` - 1,552,211 wierszy (dane godzinowe)
- `kaggle_sepsis/training_setA/` - 20,336 plików pacjentów (.psv)

**Zawartość:**
- Vital signs: HR, O2Sat, Temp, SBP, MAP, DBP, Resp
- Lab values: Lactate, Creatinine, Bilirubin, WBC, Platelets, etc.
- Demographics: Age, Gender, Unit, HospAdmTime
- Target: SepsisLabel (0/1)

**Format .psv (pipe-separated):**
```
HR|O2Sat|Temp|SBP|MAP|DBP|Resp|EtCO2|BaseExcess|...|SepsisLabel
80|98|36.8|120|80|60|18|||...|0
```

**Użycie:**
```python
import pandas as pd
# Główny dataset
df = pd.read_csv('kaggle_sepsis/Dataset.csv')
# Pojedynczy pacjent
patient = pd.read_csv('kaggle_sepsis/training_setA/training/p000001.psv', sep='|')
```

---

### 3. Kaggle Sepsis Survival

**Pliki:**
- `kaggle_survival/.../s41598-020-73558-3_sepsis_survival_primary_cohort.csv` (110,205 rekordów)
- `kaggle_survival/.../s41598-020-73558-3_sepsis_survival_study_cohort.csv` (19,052 rekordów)
- `kaggle_survival/.../s41598-020-73558-3_sepsis_survival_validation_cohort.csv` (138 rekordów)

**Kolumny:**
- `age_years` - wiek
- `sex_0male_1female` - płeć
- `episode_number` - numer epizodu
- `hospital_outcome_1alive_0dead` - outcome (przeżycie)

**Publikacja:** Scientific Reports 2020

---

### 4. California Severe Sepsis

**Plik:** `california_severe_sepsis.csv` (15 wierszy, 2010-2024)

**Kolumny (wybrane):**
- `Year` - rok
- `NumberofSevereSepsis` - liczba przypadków
- `hospitaldeath` - zgony szpitalne
- `PctofInHspDth` - % śmiertelności
- `PctofHospAcquired` - % hospital-acquired
- `MeanLOS` - średni czas pobytu
- Breakdown wg ubezpieczenia, typu szpitala, rozmiaru

**Użycie:**
```python
df = pd.read_csv('california_severe_sepsis.csv')
# Trend śmiertelności
df[['Year', 'PctofInHspDth']].plot(x='Year')
```

---

### 5. WHO Neonatal Mortality Rate

**Plik:** `who_neonatal_mortality_rate.json` (9.1 MB)

**Zawartość:**
- 14,858 rekordów
- Głównie kraje LMIC (Low-Middle Income Countries)
- **Brak Polski** - dane tylko dla krajów rozwijających się

**Ograniczenie:** Nie zawiera danych dla Polski ani większości krajów europejskich.

---

### 6. 🇵🇱 NFZ Hospitalizacje Sepsa

**Plik:** `nfz_sepsis_hospitalizations.csv` (1.3 KB)

**Zawartość:**
- 21 rekordów (2009-2024)
- 3 grupy JGP: S53, S56, P51
- Liczba pacjentów i hospitalizacji
- Mediana czasu pobytu
- Średni koszt (częściowo)

**Kolumny:**
```
group,year,patients,hospitalizations,rehospitalization_ratio,median_los_days,mode_los_days,avg_cost_pln,avg_cost_points
```

**Kluczowe statystyki:**
| Rok | S53 (ogólna) | S56 (ciężka) | P51 (dzieci) |
|-----|-------------|--------------|--------------|
| 2009 | 10,209 | - | - |
| 2014 | - | 11,460 | - |
| 2019 | - | 20,724 | 282 |
| 2024 | - | 31,721 | 678 |

**Użycie:**
```python
import pandas as pd
df = pd.read_csv('nfz_sepsis_hospitalizations.csv')
# Trend hospitalizacji
df.groupby(['group', 'year'])['hospitalizations'].sum().unstack(0).plot()
```

---

### Datasets których NIE UDAŁO się pobrać automatycznie

| Dataset | Powód | Rozwiązanie |
|---------|-------|-------------|
| GBD Results | Wymaga interaktywnego interfejsu | Manual export z vizhub.healthdata.org |
| NCHS WONDER | Wymaga interaktywnego interfejsu | Manual export z wonder.cdc.gov |
| PhysioNet (MIMIC-IV) | Wymaga rejestracji CITI | Rejestracja na physionet.org |

---

## NASTĘPNE KROKI

### Wykonane ✅
1. [x] Pobrać Kaggle datasets (ML baseline)
2. [x] Pobrać GSE185263 z GEO (transkryptomika)
3. [x] Pobrać California Severe Sepsis z Data.gov
4. [x] Pobrać WHO Neonatal Mortality (ograniczone dane)
5. [x] **Pobrać dane NFZ o hospitalizacjach z sepsą (Polska)**

### Wymaga manualnej akcji
6. [ ] Wyeksportować dane z GBD Results Tool (globalne trendy + Polska)
7. [ ] Wyeksportować dane z NCHS WONDER (USA mortality)
8. [ ] Rozpocząć rejestrację PhysioNet (MIMIC-IV, eICU)
9. [ ] Kontakt z Prof. Küblerem (kai@umed.wroc.pl) - Polish Severe Sepsis Registry
10. [ ] Ocenić potrzebę zakupu HCUP NIS

---

## ŹRÓDŁA

### Wyszukiwania
- PubMed, Google Scholar
- PhysioNet documentation
- AHRQ/HCUP reports
- WHO/CDC/ECDC oficjalne strony

### Kluczowe publikacje
- Rudd KE et al. Lancet 2020 - Global Burden of Sepsis
- Johnson AEW et al. Scientific Data 2016 - MIMIC-III
- Pollard TJ et al. Scientific Data 2018 - eICU-CRD

### Publikacje polskie
- Kübler A et al. Anaesthesiol Intensive Ther 2015 - "Results of severe sepsis registry in Poland 2003-2009"
- Kübler A et al. Anaesthesiol Intensive Ther 2015 - "Point prevalence study 2012-2013"
- Kübler A et al. Med Sci Monit 2004 - "Severe sepsis in Poland - 1043 cases"
