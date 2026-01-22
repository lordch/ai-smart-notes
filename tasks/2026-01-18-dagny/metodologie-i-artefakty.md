# Metodologie badawcze - workflow i artefakty pośrednie

Analiza pięciu typów badań stosowanych przez dr Krankowską przez pryzmat **danych wejściowych**, **kroków pracy** i **artefaktów pośrednich** powstających po drodze.

---

## Etap 0: Przegląd literatury (wspólny dla wszystkich metodologii)

**Każde badanie naukowe** — niezależnie od metodologii — zaczyna się od przeglądu literatury. To nie jest "systematic review" jako formalna metodologia, ale pragmatyczne szukanie 20-50 kluczowych paperów.

### Cel
- Zrozumieć co już wiadomo na dany temat
- Zidentyfikować **lukę w wiedzy** (gap)
- Uzasadnić dlaczego nasze badanie jest potrzebne
- Napisać sekcję Introduction/Background

### Workflow (szczegółowo opisany w `literature-review-workflow.md`)

```
1. ORIENTACJA (~1h)
   - Wstępne query w PubMed
   - Szukanie review articles
   
   Artefakt: Notatki orientacyjne, lista głównych wątków

2. BUDOWANIE QUERY (~1h)
   - Iteracyjne zawężanie/rozszerzanie
   - MeSH terms, filtry
   
   Artefakt: Search strategy document

3. SCREENING ABSTRAKTÓW (~3h)
   - Przegląd tytułów i abstraktów
   - Decyzje: relevant / maybe / skip
   
   Artefakt: Lista kandydatów do pełnego czytania

4. POZYSKIWANIE PDF (~1.5h)
   - Open Access, biblioteka, Sci-Hub
   
   Artefakt: Folder z PDF-ami

5. CZYTANIE I NOTOWANIE (~6h)
   - Ekstrakcja kluczowych informacji
   - Notatki: metody, wyniki, ograniczenia
   
   Artefakt: PAPER EXTRACTION TABLE
   ┌────────┬──────┬─────────┬───────────┬─────────────────────┐
   │ Autor  │ Rok  │ n       │ Metoda    │ Główne wyniki       │
   ├────────┼──────┼─────────┼───────────┼─────────────────────┤
   │ Smith  │ 2019 │ 234     │ Retro     │ CD4<100 → 3x risk   │
   │ Jones  │ 2020 │ 89      │ Cohort    │ ART adherence 78%   │
   └────────┴──────┴─────────┴───────────┴─────────────────────┘

6. SNOWBALLING (~1.5h)
   - References (backward)
   - Cited by (forward)
   
   Artefakt: Dodatkowe papery

7. SYNTEZA I PISANIE (~6h)
   - Grupowanie tematyczne
   - Pisanie Background/Introduction
   
   Artefakt: Draft Introduction z cytowaniami
```

### Artefakty pośrednie
| Artefakt | Format | Cel |
|----------|--------|-----|
| Search strategy | Word | Dokumentacja procesu |
| Reference library | Zotero/Mendeley | Organizacja źródeł |
| Paper extraction table | Excel | Ustrukturyzowane notatki |
| Draft Introduction | Word | Wejście do manuskryptu |

### Czas: ~20h (rozłożone na 2-4 tygodnie)

### Gdzie agent może pomóc
- **Budowanie search query** z pytania badawczego
- **Wstępny screening** abstraktów (sugestie, nie decyzje)
- **Ekstrakcja danych z PDF** do tabeli
- **Pisanie draftu Introduction** z notatek

---

> **Uwaga**: Poniższe metodologie opisują etapy **po** przegladzie literatury. Każda z nich zakłada, że etap 0 został już wykonany i mamy draft Introduction.

---

## 1. Badania retrospektywne

**Przykład**: Porównanie pacjentów przerywających ART z pacjentami z późną diagnozą HIV (doktorat)

### Dane wejściowe
- Dokumentacja medyczna pacjentów (elektroniczna lub papierowa)
- Wyniki laboratoryjne (CD4, viral load, morfologia)
- Karty zleceń leków
- Historie hospitalizacji

### Workflow krok po kroku

```
1. PYTANIE BADAWCZE
   "Czy pacjenci przerywający ART mają podobne choroby oportunistyczne 
    jak pacjenci z późną diagnozą?"
   
   Artefakt: Protokół badania (cel, hipotezy, kryteria włączenia/wykluczenia)

2. DEFINIOWANIE KOHORT
   - Kryteria: pacjenci z HIV, leczeni w ośrodku X, lata 2018-2023
   - Podział: grupa 1 (przerwanie ART) vs grupa 2 (late diagnosis)
   
   Artefakt: Definicje operacyjne zmiennych
   
3. EKSTRAKCJA DANYCH Z DOKUMENTACJI
   Dla każdego pacjenta wyciąganie:
   - Demografia (wiek, płeć)
   - Data diagnozy HIV
   - Historia ART (start, przerwy, schematy)
   - Wyniki CD4 w czasie
   - Rozpoznania (ICD-10)
   - Uzależnienia
   
   Artefakt: TABELA EKSTRAKCJI (Excel/database)
   ┌────────┬─────┬────────┬───────┬─────────┬──────────────┐
   │ ID_pac │ Wiek│ Płeć   │ CD4_1 │ CD4_ost │ Candidiasis? │
   ├────────┼─────┼────────┼───────┼─────────┼──────────────┤
   │ 001    │ 34  │ M      │ 45    │ 320     │ Tak          │
   │ 002    │ 28  │ K      │ 180   │ 450     │ Nie          │
   └────────┴─────┴────────┴───────┴─────────┴──────────────┘

4. CZYSZCZENIE DANYCH
   - Brakujące wartości
   - Niespójności (np. data CD4 przed datą diagnozy)
   - Outliers
   
   Artefakt: Log czyszczenia danych, finalna tabela analityczna

5. ANALIZA STATYSTYCZNA
   - Porównanie grup (chi-kwadrat, t-test)
   - Regresja logistyczna (OR, 95% CI)
   
   Artefakt: Tabele wyników, wykresy, output z R/SPSS
   
6. INTERPRETACJA
   "Grzybica przełyku istotnie częstsza w grupie late diagnosis (p=0.009)"
   
   Artefakt: Draft sekcji Results
```

### Kluczowe artefakty pośrednie
| Artefakt | Format | Gdzie powstaje |
|----------|--------|----------------|
| Protokół badania | Word/PDF | Planowanie |
| Case Report Form (CRF) | Formularz | Definicja zmiennych |
| Tabela ekstrakcji | Excel | Zbieranie danych |
| Codebook | Excel/Word | Definicje kodów |
| Dataset analityczny | .csv/.xlsx | Po czyszczeniu |
| Skrypty R/SPSS | .R/.sps | Analiza |
| Tabele wyników | Word/Excel | Po analizie |

### Gdzie agent może pomóc
- **Tworzenie CRF** na podstawie pytania badawczego
- **Weryfikacja spójności** danych
- **Generowanie kodu R** do analiz
- **Pisanie sekcji Methods** z opisu procesu

---

## 2. Przeglądy systematyczne (Systematic Review jako METODOLOGIA)

> **Kluczowe rozróżnienie**: Tutaj przegląd literatury **sam w sobie jest badaniem**, nie tylko etapem wstępnym. Ma formalny protokół, rejestrację PROSPERO, raportowanie PRISMA. Etap 0 (przegląd do Introduction) nadal występuje — ale jest krótszy, bo służy tylko uzasadnieniu dlaczego potrzebny jest ten systematic review.

**Przykład**: Late HIV diagnosis among migrant women (IJID Regions 2023)

### Dane wejściowe
- Bazy bibliograficzne (PubMed, EMBASE, PsychINFO)
- Pełne teksty artykułów (PDF)
- Grey literature (raporty ECDC, WHO)

### Workflow krok po kroku

```
1. PYTANIE BADAWCZE (format PICO)
   P: Migrant women in Europe
   I: -
   C: -
   O: Barriers to HIV testing, late diagnosis factors
   
   Artefakt: Protokół PROSPERO (rejestracja przeglądu)

2. STRATEGIA WYSZUKIWANIA
   Budowanie query z operatorami Boolean:
   ("HIV" OR "human immunodeficiency virus") 
   AND ("migrant*" OR "immigrant*" OR "refugee*")
   AND ("women" OR "female")
   AND ("Europe" OR [lista krajów])
   AND ("barrier*" OR "late diagnosis" OR "testing")
   
   Artefakt: Search strategy document (query + bazy + daty)

3. WYSZUKIWANIE I DEDUPLIKACJA
   - PubMed: 342 wyniki
   - EMBASE: 289 wyniki
   - PsychINFO: 87 wyniki
   - Po deduplikacji: 518 unikalnych
   
   Artefakt: Baza referencji w Zotero/EndNote

4. SCREENING TYTUŁÓW I ABSTRAKTÓW
   Dwóch reviewerów niezależnie ocenia każdy abstrakt:
   - Include / Exclude / Maybe
   - Konflikt → trzeci reviewer
   
   Artefakt: SCREENING LOG
   ┌────────┬─────────────────────┬────────────┬────────────┬─────────┐
   │ ID     │ Tytuł (skrót)       │ Reviewer 1 │ Reviewer 2 │ Decyzja │
   ├────────┼─────────────────────┼────────────┼────────────┼─────────┤
   │ 001    │ HIV testing in...   │ Include    │ Include    │ Include │
   │ 002    │ Malaria prevalence  │ Exclude    │ Exclude    │ Exclude │
   │ 003    │ Migrant health...   │ Include    │ Maybe      │ Include │
   └────────┴─────────────────────┴────────────┴────────────┴─────────┘
   
   Po screeningu: 78 do full-text review

5. FULL-TEXT REVIEW
   Czytanie pełnych tekstów z kryteriami:
   - Czy populacja to migrantki w Europie?
   - Czy raportuje bariery/czynniki późnej diagnozy?
   - Jakość metodologiczna
   
   Artefakt: Exclusion reasons log
   "Excluded (n=66): Wrong population (23), No relevant outcome (31)..."

6. EKSTRAKCJA DANYCH Z WŁĄCZONYCH PRAC
   Dla każdego z 12 włączonych paperów:
   
   Artefakt: DATA EXTRACTION TABLE
   ┌────────┬──────┬─────────┬────────────┬───────────────────────┐
   │ Autor  │ Rok  │ Kraj    │ Populacja  │ Główne bariery        │
   ├────────┼──────┼─────────┼────────────┼───────────────────────┤
   │ Smith  │ 2019 │ UK      │ n=234, SSA │ Language, stigma      │
   │ Müller │ 2020 │ Germany │ n=89, mixed│ Legal status, fear    │
   └────────┴──────┴─────────┴────────────┴───────────────────────┘

7. QUALITY ASSESSMENT
   Ocena jakości każdego badania (CASP, Newcastle-Ottawa)
   
   Artefakt: Quality scores table

8. SYNTEZA
   - Grupowanie barier: strukturalne, socjokulturowe, indywidualne
   - Narrative synthesis (lub meta-analiza jeśli dane pozwalają)
   
   Artefakt: PRISMA flowchart, tabele syntezy, draft Discussion

9. RAPORTOWANIE
   Zgodnie z PRISMA checklist
   
   Artefakt: Wypełniony PRISMA checklist, manuskrypt
```

### Kluczowe artefakty pośrednie
| Artefakt | Format | Cel |
|----------|--------|-----|
| Protokół PROSPERO | Rejestracja online | Transparentność |
| Search strategy | Word | Powtarzalność |
| Reference library | Zotero/EndNote | Organizacja |
| Screening log | Excel/Rayyan | Śledzenie decyzji |
| Data extraction form | Excel | Standaryzacja |
| Quality assessment | Excel | Ocena wiarygodności |
| PRISMA flowchart | Diagram | Wizualizacja procesu |
| Evidence table | Word | Synteza |

### Gdzie agent może pomóc
- **Budowanie search query** z pytania PICO
- **Screening abstraktów** (sugestie, nie decyzje)
- **Ekstrakcja danych** z PDF-ów do tabeli
- **Generowanie PRISMA flowchart**
- **Pisanie narrative synthesis**

---

## 3. Badania kohortowe

**Przykład**: Obserwacja pacjentów z HIV przez 5 lat pod kątem rozwoju frailty

### Dane wejściowe
- Pacjenci rekrutowani prospektywnie
- Wizyty follow-up co 6-12 miesięcy
- Pomiary w wielu punktach czasowych

### Workflow krok po kroku

```
1. PROTOKÓŁ I ETYKA
   - Definicja ekspozycji (np. CD4 <200 vs >200)
   - Definicja outcome (np. frailty wg Fried criteria)
   - Punkty czasowe pomiaru
   
   Artefakt: Protokół, zgoda Komisji Bioetycznej, informed consent

2. REKRUTACJA
   - Kryteria włączenia (HIV+, >18 lat, na ART)
   - Baseline assessment
   
   Artefakt: BASELINE DATABASE
   ┌────────┬─────┬────────┬───────┬─────────────┬────────────┐
   │ ID     │ Wiek│ Płeć   │ CD4_0 │ Frailty_0   │ Data_rekr  │
   ├────────┼─────┼────────┼───────┼─────────────┼────────────┤
   │ C001   │ 52  │ K      │ 180   │ Pre-frail   │ 2020-03-15 │
   │ C002   │ 48  │ M      │ 420   │ Robust      │ 2020-04-02 │
   └────────┴─────┴────────┴───────┴─────────────┴────────────┘

3. FOLLOW-UP VISITS
   Każda wizyta = nowy wiersz danych
   
   Artefakt: LONGITUDINAL DATABASE
   ┌────────┬───────────┬───────┬─────────────┬─────────────┐
   │ ID     │ Wizyta    │ CD4   │ Frailty     │ Lost_to_FU? │
   ├────────┼───────────┼───────┼─────────────┼─────────────┤
   │ C001   │ Baseline  │ 180   │ Pre-frail   │ No          │
   │ C001   │ 12m       │ 310   │ Pre-frail   │ No          │
   │ C001   │ 24m       │ 280   │ Frail       │ No          │
   │ C002   │ Baseline  │ 420   │ Robust      │ No          │
   │ C002   │ 12m       │ -     │ -           │ Yes (died)  │
   └────────┴───────────┴───────┴─────────────┴─────────────┘

4. ŚLEDZENIE RETENTION
   - Kto wrócił na wizytę?
   - Kto lost to follow-up? Dlaczego?
   
   Artefakt: Retention log, flow diagram

5. ANALIZA SURVIVAL / TIME-TO-EVENT
   - Kaplan-Meier curves
   - Cox regression (hazard ratios)
   
   Artefakt: Survival curves, HR tables

6. ANALIZA ZMIAN W CZASIE
   - Mixed-effects models
   - Trajectories
   
   Artefakt: Trajectory plots, model outputs
```

### Kluczowe artefakty pośrednie
| Artefakt | Format | Specyfika |
|----------|--------|-----------|
| Protokół + informed consent | Word/PDF | Wymagane przez etykę |
| CRF dla każdej wizyty | Formularz | Standaryzacja |
| Longitudinal database | Long format | ID × wizyta |
| Retention tracking | Excel | Lost to follow-up |
| Survival curves | Wykres | Kaplan-Meier |
| Mixed model output | R output | Zmiany w czasie |

### Gdzie agent może pomóc
- **Projektowanie CRF** dla wizyt follow-up
- **Śledzenie brakujących wizyt** (alerty)
- **Generowanie survival curves**
- **Interpretacja hazard ratios**

---

## 4. Badania przekrojowe (cross-sectional)

**Przykład**: Risk factors for recurrent erysipelas (2020)

### Dane wejściowe
- Pacjenci hospitalizowani w określonym czasie
- Jednokrotny pomiar (snapshot)
- Porównanie grup (nawrót vs pierwszy epizod)

### Workflow krok po kroku

```
1. DEFINICJA POPULACJI I CZASU
   "Wszyscy pacjenci hospitalizowani z powodu róży/cellulitis 
    w Klinice X, lipiec 2016 - czerwiec 2019"
   
   Artefakt: Kryteria włączenia, definicje przypadków

2. IDENTYFIKACJA PRZYPADKÓW
   - Przegląd ksiąg przyjęć / systemu szpitalnego
   - Kody ICD-10: A46 (erysipelas), L03 (cellulitis)
   
   Artefakt: Lista potencjalnych przypadków

3. WERYFIKACJA I KLASYFIKACJA
   - Przegląd dokumentacji: czy spełnia kryteria?
   - Podział: pierwszy epizod vs nawrót
   
   Artefakt: FINAL SAMPLE
   Włączeni: 163 pacjentów
   - Pierwszy epizod: 98
   - Nawrót: 65

4. EKSTRAKCJA DANYCH (JEDNOPUNKTOWA)
   Dla każdego pacjenta, dane z momentu hospitalizacji:
   
   Artefakt: CROSS-SECTIONAL DATABASE
   ┌────────┬─────┬──────┬───────────┬────────────┬──────────┐
   │ ID     │ BMI │ DM?  │ Lymphedema│ Czas objaw │ Nawrót?  │
   ├────────┼─────┼──────┼───────────┼────────────┼──────────┤
   │ 001    │ 32.4│ Tak  │ Nie       │ 5 dni      │ Nie      │
   │ 002    │ 38.1│ Nie  │ Tak       │ 3 dni      │ Tak      │
   └────────┴─────┴──────┴───────────┴────────────┴──────────┘

5. ANALIZA PORÓWNAWCZA
   - Univariate: porównanie grup (nawrót vs nie)
   - Multivariate: regresja logistyczna
   
   Artefakt: Tabela 1 (baseline characteristics), Tabela 2 (OR)

6. INTERPRETACJA ASOCJACJI
   "Lymphedema: OR 6.9 (95% CI 1.4-33.8), p=0.015"
   
   Uwaga: cross-sectional → asocjacja, nie kauzacja
```

### Kluczowe artefakty pośrednie
| Artefakt | Format | Uwagi |
|----------|--------|-------|
| Case definition | Word | Operacyjna definicja |
| Screening log | Excel | Kto włączony/wykluczony |
| Single-timepoint database | Excel | Jeden wiersz = jeden pacjent |
| Table 1 (baseline) | Word | Charakterystyka grup |
| Table 2 (associations) | Word | OR, 95% CI, p-values |

### Gdzie agent może pomóc
- **Generowanie Table 1** z danych
- **Obliczanie OR** i interpretacja
- **Pisanie sekcji Results** z tabel

---

## 5. Badania interwencyjne (RCT)

**Przykład**: Well-being intervention in PLWHA (Applied Psychology 2022)

### Dane wejściowe
- Uczestnicy randomizowani do grup
- Interwencja (self-affirming implementation intentions)
- Pomiary przed i po

### Workflow krok po kroku

```
1. PROTOKÓŁ I REJESTRACJA
   - Preregistration (OSF, ClinicalTrials.gov)
   - Definicja primary/secondary outcomes
   - Power analysis (ile osób potrzeba)
   
   Artefakt: Preregistration document, CONSORT checklist

2. REKRUTACJA I RANDOMIZACJA
   - Screening: kto spełnia kryteria?
   - Randomizacja: przydział do grup
   
   Artefakt: RANDOMIZATION LOG
   ┌────────┬───────────┬─────────────┬────────────┐
   │ ID     │ Eligible? │ Randomized  │ Group      │
   ├────────┼───────────┼─────────────┼────────────┤
   │ R001   │ Yes       │ Yes         │ S-AII      │
   │ R002   │ Yes       │ Yes         │ Control    │
   │ R003   │ No (age)  │ -           │ -          │
   └────────┴───────────┴─────────────┴────────────┘
   
   Artefakt: CONSORT flow diagram (screening → randomization → analysis)

3. BASELINE ASSESSMENT (T0)
   Kwestionariusze przed interwencją:
   - Depresja (PHQ-9 lub podobne)
   - Well-being (MHC-SF)
   
   Artefakt: BASELINE SCORES
   ┌────────┬───────┬─────────────┬──────────────┐
   │ ID     │ Group │ Depression_T0│ Wellbeing_T0 │
   ├────────┼───────┼─────────────┼──────────────┤
   │ R001   │ S-AII │ 12          │ 45           │
   │ R002   │ Ctrl  │ 8           │ 52           │
   └────────┴───────┴─────────────┴──────────────┘

4. INTERWENCJA
   - Grupa S-AII: formułowanie planów "jeśli-to" z afirmacją
   - Grupa kontrolna: inna aktywność lub nic
   
   Artefakt: Protokół interwencji, materiały dla uczestników

5. FOLLOW-UP ASSESSMENT (T1, T2...)
   Te same kwestionariusze po interwencji (np. 2 tygodnie)
   
   Artefakt: LONGITUDINAL OUTCOMES
   ┌────────┬───────┬─────────────┬──────────────┬─────────────┬──────────────┐
   │ ID     │ Group │ Depr_T0     │ Depr_T1      │ WB_T0       │ WB_T1        │
   ├────────┼───────┼─────────────┼──────────────┼─────────────┼──────────────┤
   │ R001   │ S-AII │ 12          │ 10           │ 45          │ 51           │
   │ R002   │ Ctrl  │ 8           │ 9            │ 52          │ 50           │
   └────────┴───────┴─────────────┴──────────────┴─────────────┴──────────────┘

6. ANALIZA INTENTION-TO-TREAT
   - Wszyscy randomizowani, niezależnie od adherencji
   - Linear mixed models (grupa × czas)
   - Effect sizes (Cohen's d)
   
   Artefakt: ITT analysis output, effect size calculations

7. RAPORTOWANIE
   - CONSORT statement
   - Minimally clinically important difference (MCID)
   
   Artefakt: CONSORT checklist, manuskrypt
```

### Kluczowe artefakty pośrednie
| Artefakt | Format | Wymaganie |
|----------|--------|-----------|
| Preregistration | OSF/registry | Transparentność |
| CONSORT flow | Diagram | Standard raportowania |
| Randomization log | Excel | Audyt |
| Intervention protocol | Word | Replikowalność |
| Baseline + follow-up data | Long format | Analiza |
| ITT analysis | R output | Primary analysis |
| Effect sizes | Tabela | Interpretacja |

### Gdzie agent może pomóc
- **Power analysis** dla planowanego badania
- **Generowanie CONSORT diagram**
- **Obliczanie effect sizes**
- **Interpretacja mixed models**

---

## Podsumowanie: artefakty wspólne i specyficzne

### Wspólne dla wszystkich metodologii (Etap 0 + końcowe)

**Początek (Etap 0 - przegląd literatury):**
- Search strategy document
- Reference library (Zotero/Mendeley)
- Paper extraction table
- Draft Introduction

**Środek (specyficzne dla metodologii):**
- Patrz tabela poniżej

**Koniec:**
- Pytanie badawcze / hipotezy
- Definicje zmiennych (codebook)
- Dataset do analizy
- Tabele wyników
- Draft manuskryptu

### Specyficzne dla głównej części badania

| Metodologia | Artefakt charakterystyczny |
|-------------|----------------------------|
| Retrospektywne | Tabela ekstrakcji z dokumentacji |
| Systematic review | PRISMA flowchart, screening log |
| Kohortowe | Longitudinal database (ID × czas) |
| Cross-sectional | Table 1 baseline characteristics |
| RCT | CONSORT diagram, randomization log |

### Implikacje dla agenta

Agent może być najbardziej pomocny w:
1. **Tworzeniu struktur** (CRF, tabele ekstrakcji, codebook)
2. **Przetwarzaniu tekstu → dane** (ekstrakcja z PDF-ów)
3. **Generowaniu kodu analitycznego** (R scripts)
4. **Wizualizacji** (flowcharts, plots)
5. **Pisaniu** (Methods, Results z danych)

Agent wymaga ludzkiej weryfikacji w:
1. Decyzjach o włączeniu/wykluczeniu (screening)
2. Interpretacji klinicznej wyników
3. Ocenie jakości danych źródłowych
4. Formułowaniu wniosków praktycznych
