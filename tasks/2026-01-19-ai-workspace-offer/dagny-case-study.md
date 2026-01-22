# Case Study: Dagny Krankowska — AI Workspace dla lekarza-badacza

Konkretny przykład jak wyglądałoby wdrożenie AI Workspace Build dla dr Dagny Krankowskiej.

---

## Profil klienta

**Kim jest Dagny:**
- Lekarz, asystent w Klinice Chorób Zakaźnych WUM
- Doktor nauk medycznych (2024)
- Specjalizacja: HIV/AIDS, choroby zakaźne
- Robi badania retrospektywne oparte na danych szpitalnych

**Jej główny workflow:**
```
Hipoteza kliniczna 
    → Literature review (celowany, 20-50 paperów)
    → Protokół + etyka
    → Zbieranie danych (Excel ze szpitalnego systemu)
    → Analiza statystyczna (outsourcowana!)
    → Pisanie paperu
```

**Główne bóle:**
1. Literature review zajmuje ~20h, notatki rozproszone
2. Analiza statystyczna zależna od zewnętrznego statystyka (dni/tygodnie oczekiwania)
3. Brak iteracji — każda zmiana = kolejne dni
4. Wiedza domenowa w głowie, nie w plikach

---

## Co Dagny dostałaby po wdrożeniu

### 1. Struktura workspace'u

```
dagny-research/
├── CLAUDE.md
├── context/
│   ├── domain/
│   │   ├── glossary.md              # HIV, CD4, ART, choroby oportunistyczne...
│   │   ├── statistical-methods.md   # Testy, kiedy używać
│   │   └── journal-guidelines.md    # Wymogi czasopism
│   ├── workflows/
│   │   ├── retrospective-study.md   # Jak robimy badanie retrospektywne
│   │   └── literature-review.md     # Jak robimy lit review
│   └── examples/
│       ├── good-table1.md           # Wzorcowa Table 1
│       ├── good-introduction.md     # Wzorcowy wstęp
│       └── paper-extraction.md      # Jak wyciągać info z paperów
├── templates/
│   ├── paper-extraction-form.md     # Formularz do ekstrakcji z literatury
│   ├── table1-template.md           # Szablon Table 1
│   ├── statistical-report.md        # Raport z analizy
│   └── paper-draft.md               # Szablon paperu (IMRAD)
├── skills/
│   ├── literature-search.md         # Skill: budowanie search strategy
│   ├── extract-paper.md             # Skill: ekstrakcja z PDF
│   ├── generate-table1.md           # Skill: Table 1 z Excela
│   ├── statistical-analysis.md      # Skill: analiza danych
│   └── draft-section.md             # Skill: draft sekcji paperu
├── projects/
│   └── [nazwa-badania]/
│       ├── brief.md
│       ├── literature/
│       │   ├── search-strategy.md
│       │   ├── papers/              # PDFy
│       │   └── extraction-table.md  # Tabela z wyciągniętymi info
│       ├── data/
│       │   ├── raw-data.xlsx
│       │   └── analysis/
│       └── paper/
│           ├── draft-v1.md
│           └── figures/
└── archive/
```

### 2. CLAUDE.md dla Dagny

```markdown
# Context: Dr Dagny Krankowska

## Kim jestem
Lekarz i badacz w Klinice Chorób Zakaźnych, Tropikalnych i Hepatologii 
Warszawskiego Uniwersytetu Medycznego. Specjalizuję się w HIV/AIDS 
i chorobach oportunistycznych. Robię badania retrospektywne 
na danych z systemów szpitalnych.

## Terminologia
Agent zna i nie pyta o:
- **ART** (Antiretroviral Therapy) — terapia antyretrowirusowa
- **CD4** — limfocyty T pomocnicze, marker stanu immunologicznego w HIV
- **Viral load** — wiemia, liczba kopii wirusa we krwi
- **Choroby oportunistyczne** — infekcje u osób z obniżoną odpornością
- **PML** — postępująca wieloogniskowa leukoencefalopatia
- **Kryptokokoza** — grzybicze zapalenie opon mózgowych
- Pełny glosariusz: context/domain/glossary.md

## Jak pracujemy

### Język
- Komunikacja: polski
- Dokumenty naukowe: angielski
- Kod i komentarze: angielski

### Formatowanie
- Tabele medyczne: mediana (IQR) dla zmiennych ciągłych, n (%) dla kategorycznych
- P-values: trzy miejsca po przecinku, <0.001 jeśli mniejsze
- Cytowania: Vancouver style

### Czego agent NIE robi
- Nie zmyśla danych
- Nie interpretuje wyników klinicznie bez mojej weryfikacji
- Nie podejmuje decyzji o metodologii bez konsultacji

## Główne workflow'y
1. **Literature review** → skills/literature-search.md, skills/extract-paper.md
2. **Analiza danych** → skills/generate-table1.md, skills/statistical-analysis.md
3. **Pisanie paperu** → skills/draft-section.md

## Artefakty
- Paper extraction form → templates/paper-extraction-form.md
- Table 1 → templates/table1-template.md
- Statistical report → templates/statistical-report.md
- Paper draft → templates/paper-draft.md
```

### 3. Glosariusz (fragment)

| Termin | Definicja | Kontekst |
|--------|-----------|----------|
| CD4 | Limfocyty T pomocnicze; marker immunologiczny | CD4 < 200 = ciężki niedobór odporności |
| ART | Antiretroviral Therapy | Standard of care w HIV |
| Viral load | Liczba kopii HIV RNA/ml | Undetectable = <50 kopii |
| Opportunistic infection | Infekcja u immunoniekompetentnych | PML, kryptokokoza, PCP, CMV... |
| Kaplan-Meier | Metoda estymacji przeżycia | Do analiz time-to-event |
| Log-rank test | Test porównujący krzywe przeżycia | p-value dla różnic między grupami |
| Table 1 | Tabela charakterystyki demograficznej | Standard w publikacjach |
| IMRAD | Introduction, Methods, Results, Discussion | Struktura paperu naukowego |

### 4. Template: Paper Extraction Form

```markdown
# Paper Extraction: [Autor et al., Rok]

## Metadata
- **PMID:** 
- **DOI:**
- **Journal:**

## Populacja
- **n:** 
- **Kryteria włączenia:**
- **Setting:** (single-center / multi-center, country)

## Design
- [ ] Retrospective cohort
- [ ] Prospective cohort
- [ ] Cross-sectional
- [ ] Case-control
- [ ] RCT
- [ ] Systematic review

## Key findings
| Outcome | Result | 95% CI | p-value |
|---------|--------|--------|---------|
|         |        |        |         |

## Limitations
- 

## Relevance to my question
- [ ] Directly relevant
- [ ] Somewhat relevant
- [ ] Background only

**How it relates:**

## Quotes to potentially cite
> "..."
```

### 5. Skill: Generate Table 1

```markdown
# Skill: Generate Table 1

## Trigger
"Zrób Table 1" / "Wygeneruj charakterystykę grupy" / "Table 1 z tego Excela"

## Input potrzebny
1. Plik Excel z danymi (wskazany path)
2. Zmienna grupująca (np. "grupa", "outcome")
3. Lista zmiennych do uwzględnienia (lub "wszystkie")

## Kroki

### 1. Wczytaj dane
```python
import pandas as pd
df = pd.read_excel("[path]")
```

### 2. Zidentyfikuj typy zmiennych
- Ciągłe (wiek, CD4, viral load...)
- Kategoryczne (płeć, stadium choroby...)

### 3. Dla każdej zmiennej oblicz
**Ciągłe:** 
- mediana (IQR) lub mean ± SD
- Test: Mann-Whitney (non-parametric) lub t-test (parametric)

**Kategoryczne:**
- n (%)
- Test: chi-kwadrat lub Fisher exact (jeśli expected <5)

### 4. Sformatuj tabelę
| Variable | Group A (n=X) | Group B (n=Y) | p-value |
|----------|---------------|---------------|---------|
| Age, median (IQR) | | | |
| Male sex, n (%) | | | |

### 5. Eksportuj
- Markdown (do przeglądu)
- Word (.docx) dla współautorów
- LaTeX (jeśli potrzebne)

## Output
- Tabela w formacie zgodnym z journal guidelines
- Plik z kodem (reproducibility)

## Przykład
Zobacz: context/examples/good-table1.md
```

### 6. Slash Commands

```
/search [temat]         → Zbuduj search strategy do PubMed
/extract [pdf]          → Wyciągnij info z paperu do extraction form
/table1 [excel] [grupa] → Wygeneruj Table 1
/analyze [excel]        → EDA + podstawowa statystyka
/km [excel] [time] [event] [group] → Kaplan-Meier
/draft [sekcja]         → Napisz draft sekcji (intro/methods/results/discussion)
```

---

## Wartość dla Dagny

### Przed wdrożeniem vs Po

| Aspekt | Przed | Po |
|--------|-------|-----|
| **Literature review** | ~20h, notatki wszędzie | ~6h, strukturyzowana tabela |
| **Analiza statystyczna** | Dni/tygodnie (outsource) | Godziny (sama z agentem) |
| **Iteracja** | Kolejne dni oczekiwania | "Dodaj tę zmienną" → 30 sek |
| **Table 1** | Ktoś robi ręcznie | `/table1` → gotowe |
| **Kontekst dla AI** | Od zera każdą sesję | Agent zna jej domenę |
| **Terminologia** | Tłumaczy agentowi | Agent rozumie CD4, ART... |

### ROI (przykładowy)

Jeśli Dagny robi 3-4 publikacje/rok:
- Oszczędność na literature review: 3 × 14h = **42h/rok**
- Oszczędność na statystyce: 3 × 20h = **60h/rok** (plus eliminacja oczekiwania)
- Oszczędność na iteracjach: trudne do policzenia, ale znaczące

**~100+ godzin/rok** + jakościowa zmiana (autonomia, iteracja, zrozumienie).

---

## Co wymagałoby wdrożenie

### Od Dagny
- 15-18h rozłożone na 4-6 tygodni
- Przykładowe papery które napisała
- Przykładowy Excel z danymi (można zanonimizować)
- Lista terminów z jej domeny (draft)
- Otwartość na nowy sposób pracy

### Ode mnie
- 35-43h pracy
- Zrozumienie jej workflow'u (medycyna to nie moja domena — uczę się od niej)
- Budowa całego systemu

---

## Ograniczenia

### Co workspace NIE rozwiąże
- **Zbieranie danych** — dane zostają w szpitalu, RODO, nie można eksportować
- **Dostęp do PDF-ów** — paywall to paywall
- **Ostateczna interpretacja kliniczna** — to robi Dagny, nie AI

### Co wymaga jej uwagi
- Weryfikacja wyników statystycznych (AI może się mylić)
- Decyzje metodologiczne (AI sugeruje, ona decyduje)
- Aktualizacja glosariusza gdy domena się rozwija

---

## Potencjał rozszerzenia

Po podstawowym wdrożeniu można dodać:
- **Więcej typów badań** (prospektywne, case studies)
- **Skille dla systematic review** (PRISMA, PICO)
- **Integracje** (Zotero connector, PubMed API)
- **Szkolenie dla zespołu** (jeśli ma studentów/rezydentów)
