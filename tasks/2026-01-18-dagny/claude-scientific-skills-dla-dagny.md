# Claude Scientific Skills — analiza dla Dagny

## Źródło

**Repository:** [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)

Kolekcja 140 gotowych "skilli" dla Claude, które umożliwiają pracę z bibliotekami naukowymi, bazami danych i narzędziami badawczymi. Można zainstalować jako plugin do Claude Code lub użyć przez MCP server w Cursor.

---

## Kontekst: Workflow Dagny

Dagny robi **retrospektywne badania kliniczne** w obszarze HIV/AIDS:

```
Hipoteza kliniczna → Literature review → Dane z Excela → Statystyka → Paper
```

Kluczowy pain point: **statystyka jest outsourcowana** — agent mógłby to przejąć.

---

## Przydatne skille

### Statystyka i analiza danych (PRIORYTET)

| Skill | Opis | Zastosowanie u Dagny |
|-------|------|---------------------|
| **scikit-learn** | ML klasyczny: regresja, klasyfikacja | Regresja logistyczna, predykcja outcomes |
| **statsmodels** | Testy statystyczne, regresja | Chi-kwadrat, t-test, regresja wielokrotna, p-values |
| **scikit-survival** | Analiza przeżycia | **Kaplan-Meier**, hazard ratios — core w badaniach HIV |
| **Statistical Analysis** | Gotowe workflow statystyczne | Table 1, porównania grup, testy |
| **EDA** | Exploratory Data Analysis | Wstępna analiza Exceli z danymi pacjentów |
| **SHAP** | Interpretacja modeli ML | Wyjaśnialność predykcji (ważne w medycynie) |
| **PyMC** | Metody bayesowskie | Zaawansowana analiza (opcjonalnie) |

### Wizualizacja (publication-ready)

| Skill | Opis | Zastosowanie u Dagny |
|-------|------|---------------------|
| **Matplotlib** | Podstawowe wykresy | Histogramy, scatter plots |
| **Seaborn** | Statystyczne wykresy | Box plots, violin plots, heatmapy |
| **Scientific Visualization** | Publikacyjne figury | Forest plots, Kaplan-Meier curves |
| **ReportLab** | Generowanie PDF | Raporty z tabelami i wykresami |

### Literatura i pisanie

| Skill | Opis | Zastosowanie u Dagny |
|-------|------|---------------------|
| **PubMed** | Wyszukiwanie w PubMed | Literature review (główne narzędzie) |
| **OpenAlex** | Alternatywna baza literatury | Szersze przeszukiwanie |
| **Literature Review** | Workflow przeglądu | Synteza findings, draft Introduction |
| **Scientific Writing** | Pisanie naukowe | Drafty Methods/Results/Discussion |
| **Citation Management** | Zarządzanie cytowaniami | Bibliografia w paperach |

### Pomocnicze

| Skill | Opis | Zastosowanie u Dagny |
|-------|------|---------------------|
| **ClinicalTrials.gov** | Baza badań klinicznych | Kontekst badań HIV |
| **XLSX** | Praca z Excelem | Wczytywanie jej danych |
| **MarkItDown** | Przetwarzanie dokumentów | Konwersja formatów |

---

## Nieprzydatne dla Dagny

Te kategorie skilli **nie pasują** do jej pracy:

- **Cheminformatyka** (RDKit, ChEMBL, DiffDock) — drug discovery
- **Single-cell analysis** (Scanpy, scvi-tools) — genomika
- **Proteomika** (pyOpenMS, matchms) — spektrometria mas
- **Bioinformatyka** (BioPython, pysam) — sekwencje DNA/RNA
- **Obrazowanie medyczne** (pydicom, PathML) — DICOM, patologia
- **Lab automation** (PyLabRobot, Opentrons) — roboty laboratoryjne
- **Materials science** (Pymatgen) — materiałoznawstwo
- **Quantum computing** (Qiskit, PennyLane) — obliczenia kwantowe

---

## Rekomendacja: Minimalny zestaw na start

Dla warsztatu z Dagny wystarczy **5 skilli**:

| Priorytet | Skill | Pokrywa |
|-----------|-------|---------|
| 1 | **statsmodels** | Testy statystyczne, regresja |
| 2 | **scikit-survival** | Kaplan-Meier, analiza przeżycia |
| 3 | **Seaborn** | Wykresy do paperu |
| 4 | **PubMed** | Literature review |
| 5 | **Scientific Writing** | Drafty sekcji paperu |

### Killer demo scenario

> "Dagny, daj mi swój Excel z danymi pacjentów. Agent zrobi Ci Table 1, porówna grupy, narysuje Kaplan-Meier i wygeneruje draft sekcji Results."

To pokazuje wartość **bez** konieczności nauki programowania.

---

## Instalacja

### Claude Code (rekomendowane)

```bash
# Dodaj marketplace
/plugin marketplace add K-Dense-AI/claude-scientific-skills

# Zainstaluj plugin
/plugin install scientific-skills@claude-scientific-skills
```

### Cursor (MCP server)

Użyj hosted MCP server:
```
https://mcp.k-dense.ai/claude-scientific-skills/mcp
```

---

## Linki

- **GitHub:** https://github.com/K-Dense-AI/claude-scientific-skills
- **Dokumentacja skilli:** https://github.com/K-Dense-AI/claude-scientific-skills/tree/main/docs
- **K-Dense Web (pełna wersja):** https://k-dense.ai

---

## Notatki

- Repository ma licencję MIT, ale poszczególne skille mogą mieć inne licencje
- K-Dense Web oferuje 200+ skilli (vs 140 w open source) + cloud compute
- Warto sprawdzić czy Dagny potrzebuje czegoś z clinical research tools (ClinVar, COSMIC) — raczej nie, bo jej fokus to epidemiologia, nie genetyka



## Anthropic Life Sciences Tutorials

**Source:** https://claude.com/resources/tutorials-category/life-sciences

Oficjalne tutoriale Anthropic dla branży life sciences. Pokazują jak używać Claude (connectors, skills) w pracy naukowej/medycznej.

### Przydatne dla Dagny (badania kliniczne HIV)

| Tutorial | Opis | Relevance |
|----------|------|-----------|
| **PubMed Connector** | Wyszukiwanie w PubMed z poziomu Claude | ⭐⭐⭐ Core tool dla literature review |
| **bioRxiv/medRxiv Connector** | Dostęp do preprintów | ⭐⭐⭐ Najnowsze badania przed publikacją |
| **ClinicalTrials.gov Connector** | Przeszukiwanie bazy badań klinicznych | ⭐⭐ Kontekst badań HIV |
| **Clinical Trial Protocol Draft Generation** | Skill do pisania protokołów | ⭐⭐ Jeśli pisze protokoły badawcze |
| **Getting Started with Claude for Life Sciences** | Intro do użycia Claude w nauce | ⭐⭐ Punkt startowy |
| **Scientific Problem Selection Skill** | Wybór problemów badawczych | ⭐ Planowanie badań |

### Przydatne dla innych klientów (nie Dagny)

| Tutorial | Opis | Dla kogo |
|----------|------|----------|
| **ChEMBL Connector** | Baza bioaktywności związków | Drug discovery, farmacja |
| **Open Targets Connector** | Baza celów terapeutycznych | Pharma, target identification |
| **Benchling Connector** | Integracja z LIMS | Laboratoria, biotech |
| **single-cell-rna-qc Skill** | QC danych single-cell | Genomika, bioinformatyka |
| **scVI-Tools Skill Bundle** | Analiza single-cell | Bioinformatycy |
| **Owkin Connector** | AI dla patologii | Digital pathology |
| **Medidata Connector** | Clinical trial data management | CRO, pharma |
| **Synapse.org Connector** | Data sharing platform | Collaborative research |
| **ToolUniverse Extension** | Meta-narzędzie do znajdowania tools | Power users |

### Obserwacje

1. **Anthropic buduje ekosystem dla life sciences** — connectors do głównych baz (PubMed, ClinicalTrials, ChEMBL)
2. **Skills to "ready-made" workflows** — można je użyć jako inspirację lub bezpośrednio
3. **Connector ≠ Skill**: Connector = dostęp do danych, Skill = workflow/procedura
4. **Dobry materiał demo** — pokazuje non-coding use cases Claude w nauce

---

## Deep Dive: Skill "Literature Review"

**Source:** https://github.com/K-Dense-AI/claude-scientific-skills/blob/main/scientific-skills/literature-review/SKILL.md

### Struktura skilla

```yaml
name: literature-review
description: Conduct comprehensive, systematic literature reviews using multiple 
             academic databases (PubMed, arXiv, bioRxiv, Semantic Scholar, etc.)
allowed-tools: [Read, Write, Edit, Bash]
license: MIT license
```

### 7-fazowy workflow

| Faza | Opis | Artefakty |
|------|------|-----------|
| **1. Planning & Scoping** | PICO framework, research question, inclusion/exclusion criteria | Search strategy document |
| **2. Systematic Search** | Multi-database (PubMed, bioRxiv, arXiv, Semantic Scholar) | JSON results, aggregated_results.md |
| **3. Screening & Selection** | Title → Abstract → Full-text, deduplikacja | PRISMA flow diagram |
| **4. Data Extraction** | Jakość badań (Cochrane, Newcastle-Ottawa), tematyczna organizacja | Extraction tables |
| **5. Synthesis & Analysis** | Tematyczna synteza (NIE study-by-study), critical analysis | Review sections |
| **6. Citation Verification** | verify_citations.py sprawdza DOI przez CrossRef | Verification report |
| **7. Document Generation** | PDF z pandoc/xelatex, multiple citation styles | Final PDF |

### Kluczowe elementy

**Mandatory figures:**
> "Every literature review MUST include at least 1-2 AI-generated figures"
- PRISMA flow diagram
- Search strategy flowchart
- Thematic synthesis diagram

**Citation verification script:**
```bash
python scripts/verify_citations.py my_literature_review.md
```
- Sprawdza DOI przez CrossRef API
- Weryfikuje metadane
- Formatuje do wybranego stylu (APA, Nature, Vancouver)

**High-impact paper prioritization:**

| Wiek paperu | Próg cytowań | Klasyfikacja |
|-------------|--------------|--------------|
| 0-3 lata | 100+ | Highly Influential |
| 3-7 lat | 500+ | Landmark Paper |
| 7+ lat | 1000+ | Foundational |

**Journal tiers:**
- Tier 1: Nature, Science, Cell, NEJM, Lancet
- Tier 2: IF>10, top conferences
- Tier 3: IF 5-10 specialized journals

### Ocena dla Dagny

**Co jest przydatne:**

| Element | Użyteczność | Komentarz |
|---------|-------------|-----------|
| 7-fazowy workflow | ⭐⭐⭐ | Systematyczny, zgodny z PRISMA — standardem w medycynie |
| PICO framework | ⭐⭐⭐ | Dagny prawdopodobnie już to zna |
| Citation verification | ⭐⭐⭐ | Automatyczne sprawdzanie DOI — oszczędza czas |
| Multi-database search | ⭐⭐ | PubMed primary, bioRxiv dla preprintów |
| PDF generation | ⭐⭐ | Gotowe formatowanie do publikacji |
| High-impact prioritization | ⭐⭐ | Pomaga filtrować setki wyników |

**Co może być zbyt skomplikowane:**

- **Wiele baz naraz** — Dagny głównie używa PubMed, nie potrzebuje arXiv
- **Scripty Pythonowe** — wymaga środowiska z zależnościami
- **AI-generated figures** — wymaga dodatkowego skilla (scientific-schematics)

### Wniosek

Ten skill to **profesjonalny workflow do systematic review** — bardzo dobry jako **inspiracja i struktura**, ale dla Dagny:

1. **Workflow tak** — 7 faz to dobra struktura do naśladowania
2. **Scripty opcjonalnie** — może po prostu rozmawiać z Claude o weryfikacji
3. **PICO + PRISMA** — Dagny to zna, ale agent może przypominać

**Praktyczne podejście**: Zamiast instalować cały skill, Dagny może powiedzieć agentowi:

> *"Zrób mi literature review na temat X zgodnie z PRISMA guidelines"*

Agent powinien sam zastosować podobny workflow bez konieczności instalacji pluginu.
