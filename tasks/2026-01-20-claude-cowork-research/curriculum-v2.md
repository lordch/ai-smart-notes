# Knowledge Work with AI Agents

## Curriculum Overview

**Tagline:** Od konwersacji z AI do delegowania pracy agentom

**Dla kogo:** Knowledge workers, którzy chcą przejść od "chatowania z AI" do systemowego wykorzystania agentów w codziennej pracy. Nie wymaga umiejętności technicznych.

**Obietnica transformacji:**
> "Po tym kursie będziesz delegować zadania agentom AI tak, jak delegujesz pracę zespołowi - z jasnymi instrukcjami, oczekiwaniami i systemem weryfikacji."

**Format:** 6 modułów, ~12 godzin materiału, 3-4 tygodnie realizacji

---

## Filozofia kursu

### Trzy filary

1. **Tool-agnostic principles** - Uczymy zasad, nie klikania w interfejsy
2. **Artifact-centric** - Praca żyje w plikach, nie w chatach
3. **Progressive complexity** - Od prostego zadania do złożonych systemów

### Core Beliefs

> "Chatbot był formą przejściową. Istniał, bo LLM-y potrafiły generować tekst zanim nauczyły się niezawodnie wykonywać plany. To już nieprawda."

> "Agent nie jest źródłem wiedzy - jest procesorem wiedzy którą mu dajesz. Halucynacje biorą się z traktowania AI jako wyroczni."

---

## Struktura kursu

```
MODULE 0: Orientation (30 min)
    └── Mindset shift preview

MODULE 1: The Paradigm Shift (2.5h)
    └── Od chatu do delegacji

MODULE 2: Task Definition Mastery (2.5h)
    └── Formułowanie zadań, nie promptów

MODULE 3: Building Your Agent Workspace (2.5h)
    └── Środowisko pracy z agentami

MODULE 4: Skills & Procedural Knowledge (2h)
    └── Uczenie agenta twoich workflow'ów

MODULE 5: System Architecture (2h)
    └── Building blocks niezawodnych systemów

MODULE 6: Integration & Scaling (1.5h)
    └── Łączenie wszystkiego w całość
```

---

# MODULE 0: Orientation

**Czas:** 30 minut
**Cel:** Zbudować napięcie i pokazać destination

## 0.1 Welcome: The Before & After

**Format:** Video (5 min)

**Treść:**
- Pokazanie dwóch światów:
  - BEFORE: "Porozmawiaj z ChatGPT o strategii" → kopiuj/wklej → formatuj → poprawiaj
  - AFTER: "Przeanalizuj te 50 plików i stwórz executive summary w PowerPoint" → review → done
- Zapowiedź transformacji

## 0.2 The 10-Day Story

**Format:** Video (8 min)

**Treść:**
Historia Anthropic i Claude Cowork:
- Obserwacja: Deweloperzy używają narzędzia do kodowania... do organizacji rachunków
- 10 dni później: Pełny produkt dla wszystkich
- Lekcja: AI-native organizations operate differently

**Pytanie do refleksji:**
> "Gdybyś mógł delegować AI dowolne 3 zadania z tego tygodnia, które by to były?"

## 0.3 Course Map & Commitment

**Format:** Interactive (10 min)

**Treść:**
- Mapa 6 modułów
- Self-assessment: Gdzie jesteś teraz?
- Commitment exercise: Co chcesz osiągnąć?

---

# MODULE 1: The Paradigm Shift

**Czas:** 2.5 godziny
**Cel:** Przebudować mental model pracy z AI

## 1.1 The Fundamental Reframe

**Format:** Lecture (15 min)

### Treść konceptualna:

**Dlaczego ludzie nie ufają AI:**
- Traktują ChatGPT jako encyklopedię
- Pytają "co wiesz o X"
- AI halucynuje → utrata zaufania

**Zmiana paradygmatu:**
> "Agent nie jest źródłem wiedzy - jest procesorem wiedzy którą mu dajesz."

Kiedy agent pracuje na źródłach które mu dasz, halucynacje dramatycznie maleją. To nie jest wada AI - to zły tryb użycia.

**Co agent robi dobrze:**
- Ekstrakcja informacji ze źródeł
- Interpretacja i porównanie
- Framing i synteza
- Stosowanie metodologii/frameworków
- Techniczne zadania

**Co zostaje przy tobie:**
- Zapewnienie kontekstu (źródła, wiedza domenowa)
- Zapewnienie intencji (co chcesz osiągnąć)
- Dekompozycja na kroki
- Weryfikacja jakości i źródeł
- Decyzje kierunkowe

## 1.2 The Spectrum: Chat to Agent

**Format:** Lecture + Diagram (15 min)

### Treść konceptualna:

**To nie jest binarne.** Jest spectrum:

```
Pure chat → Chat z checkpointami → Agent ze sterowaniem → Pełna delegacja
```

| Tryb | Kiedy używać |
|------|--------------|
| Pure chat | Brainstorming, eksploracja, nie wiesz czego chcesz |
| Chat + checkpoint | Krystalizacja intencji, iteracja na wymaganiach |
| Agent + steering | Jasne zadanie, potrzebujesz artefaktu |
| Pełna delegacja | Powtarzalne zadanie, masz skill |

**Czat nie jest wrogiem** - służy do odkrywania intencji. Problem pojawia się gdy zostajemy w czacie zamiast przejść do artefaktów.

**Ewolucja interfejsów AI:**
```
2023: Prompt → Response (chat)
2024: Prompt → Chain of Thought → Response (reasoning)
2025: Task → Plan → Execution → Artifact (agentic)
2026: Task Queue → Parallel Execution → Review (delegation)
```

## 1.3 From Editing Loop to Steering Loop

**Format:** Lecture + Exercise (25 min)

### Treść konceptualna:

**Dwie pętle:**

| Editing Loop | Steering Loop |
|--------------|---------------|
| Prompt → Read response → Fix → Prompt again | Define task → Review plan → Redirect if needed → Accept artifact |
| Ty poprawiasz output | Ty kierujesz procesem |
| Cognitive load: HIGH | Cognitive load: LOW |
| Value: in editing | Value: in defining |

**Nowa umiejętność:**
> "The cognitive work is on you, but it happens at the top. It's the steering work - articulating what you want. Not downstream cleaning up what you got."

**Rola czatu w steering loop:**

```
Intencja niejasna → [CZAT: dialog, iteracja] → Intencja skrystalizowana
                                                        ↓
                                              [CHECKPOINT: zapisz artefakt]
                                                        ↓
                                              [Agent pracuje na artefakcie]
```

Nie zawsze masz instrukcje upfront:
- Intencje ewoluują w trakcie
- Oceniasz gdy widzisz output
- Uczysz się czego chcesz

Dlatego czat jest częścią systemu - służy krystalizacji. Optymalnie: guidance z czatu kondensuje się do instrukcji na przyszłość.

### Exercise: Loop Audit
1. Wybierz ostatnie 3 interakcje z AI
2. Ile razy wróciłeś do edycji?
3. Co musiałbyś zdefiniować lepiej na początku?

## 1.4 The Management Framing

**Format:** Lecture + Discussion (20 min)

### Treść konceptualna:

**Zmiana relacji:**
> "People manage workers differently than they converse with their advisers."

**Co się zmienia:**
- Jakie zadania wydają się "odpowiednie" do delegacji
- Ile kontekstu dajesz z góry
- Jak oceniasz output

**Verification as Scarce Skill:**
> "The tool amplifies people who already know what they're doing while potentially misleading people who don't."

### Discussion prompts:
- Jak zarządzasz ludzkim asystentem?
- Czym to się różni od "chatowania"?
- Co by się zmieniło w twoim podejściu, gdybyś traktował AI jak pracownika?

## 1.5 Context Drift

**Format:** Lecture (15 min)

### Treść konceptualna:

**Co to jest context drift:**
- Im dłuższy czat, tym bardziej agent "zapomina" początek
- Instrukcje z początku mają mniejszą wagę
- Jakość spada mimo dobrych intencji

**Objawy:**
- Agent ignoruje wcześniejsze ustalenia
- Styl się zmienia w trakcie
- Powtarzasz te same korekty

**Rozwiązanie: Checkpointing**
```
Praca w czacie → Checkpoint (zapisz artefakt) → Nowa sesja na artefakcie
```

Checkpoint rozwiązuje jednocześnie:
- **Drift** - świeży kontekst w nowej sesji
- **Slop** - mniejszy output do weryfikacji
- **Utratę pracy** - artefakt persystuje między sesjami

## 1.6 Anti-Slop Architecture

**Format:** Lecture + Case Study (25 min)

### Treść konceptualna:

**Problem "work slop":**
- AI generuje "passable-looking output"
- Cognitive burden przesuwa się na odbiorcę
- Badanie BetterUp: ~2h per piece of work slop received

**Dlaczego TY wypuszczasz slop:**
- Sprawdzenie wielkiego raportu jest żmudne
- Lenistwo + presja czasu
- "Wygląda profesjonalnie"

**Inverse supervision:**
- Agent produkuje szybko i dużo
- Bottleneck to TWOJA zdolność weryfikacji
- Więc projektujesz system pod łatwość weryfikacji, nie wykonania

**5 mechanizmów anti-slop:**

1. **Artifact-first output**
   - Output = gotowy deliverable
   - Nie blob tekstu do copy-paste

2. **Visible planning**
   - Widzisz plan przed wykonaniem
   - Możesz redirect w trakcie

3. **Specificity through files**
   - Wskazujesz realne pliki, nie opisujesz abstrakcyjnie
   - Input jest konkretny → output jest konkretny

4. **Checkpointing**
   - Mniejsza płaszczyzna do sprawdzenia
   - Nie marnujesz pracy gdy coś jest źle
   - Weryfikacja staje się tractable

5. **Quality from origin**
   - Architektury budowane dla kodu (gdzie slop = fatal)
   - Ten sam standard dla knowledge work

### Case Study:
Expense reports - pokaz różnicy między:
- Chat: "Pomóż mi zorganizować rachunki" → lista sugestii
- Agent: Folder z 47 plikami → gotowy Excel z VLOOKUP i formatowaniem

## 1.7 Module 1 Integration

**Format:** Exercise (25 min)

### Ćwiczenie: Paradigm Shift Map

**Instrukcje:**
1. Wybierz 5 zadań, które regularnie robisz z AI
2. Dla każdego określ:
   - Gdzie na spectrum chat→agent jest teraz?
   - Jaki byłby idealny artifact output?
   - Co musiałbyś zdefiniować inaczej?
3. Stwórz "Before/After" dla jednego zadania

**Deliverable:**
Tabela 5 zadań z mappingiem chat → agent

---

# MODULE 2: Task Definition Mastery

**Czas:** 2.5 godziny
**Cel:** Nauczyć formułowania zadań (nie promptów) dla agentów

## 2.1 Tasks vs Prompts

**Format:** Lecture + Examples (20 min)

### Treść konceptualna:

**Fundamentalna różnica:**

| Prompt | Task |
|--------|------|
| "Pomóż mi z prezentacją" | "Stwórz 10-slajdową prezentację o X z moich notatek w folderze Y" |
| Oczekujesz tekstu | Oczekujesz artefaktu |
| Open-ended | Bounded |
| Conversation starter | Work order |

**Anatomia dobrego taska:**

```
TASK = Input + Transformation + Output + Constraints
```

- **Input:** Co agent ma do dyspozycji (pliki, dane, kontekst)
- **Transformation:** Co ma z tym zrobić
- **Output:** Jaki artefakt ma powstać, gdzie ma trafić
- **Constraints:** Ograniczenia, format, styl, deadline

### Examples:

❌ Słaby prompt:
> "Przeanalizuj dane sprzedażowe"

✅ Dobry task:
> "Przeanalizuj pliki CSV w folderze /sales-q4. Znajdź top 10 produktów po revenue. Stwórz PowerPoint z wykresami trend'ów. Zapisz w /reports jako Q4-analysis.pptx"

## 2.2 The Intent Articulation Framework

**Format:** Lecture + Exercise (30 min)

### Treść konceptualna:

**Framework WIRE:**

**W - What** (Co ma powstać)
- Konkretny artefakt
- Format, długość, struktura
- Gdzie ma trafić

**I - Input** (Z czego)
- Jakie pliki/dane
- Jaki kontekst
- Jakie źródła

**R - Rules** (Jakie zasady)
- Styl, ton
- Ograniczenia
- Must-have / nice-to-have

**E - Examples** (Jak ma wyglądać)
- Reference outputs
- Anti-examples (czego unikać)
- Quality bar

### Exercise: WIRE Breakdown

Weź jedno zadanie z Module 1 i rozpisz przez WIRE:
- W: ___
- I: ___
- R: ___
- E: ___

## 2.3 Input Specificity

**Format:** Lecture + Demo (25 min)

### Treść konceptualna:

**Zasada:** Im bardziej konkretny input, tym bardziej użyteczny output.

**Hierarchy of Input Quality:**

```
WORST:  "Moje notatki ze spotkań"
BAD:    "Notatki z ostatniego miesiąca"
OKAY:   "Pliki w folderze /meetings/january"
GOOD:   "Te 5 plików: meeting-1.md, meeting-2.md..."
BEST:   Folder + context file opisujący co jest w środku
```

**File System as Context:**
> "The file system sandbox forces specificity. You cannot vaguely ask to help with expenses. You must point at real folders with real files."

### Demo:
Pokazanie tego samego zadania z różnymi poziomami input specificity

## 2.4 Output Definition

**Format:** Lecture + Templates (25 min)

### Treść konceptualna:

**Typy outputów:**

| Typ | Przykłady | Klucz do definicji |
|-----|-----------|-------------------|
| Document | PDF, DOCX, MD | Struktura, długość, styl |
| Spreadsheet | XLSX, CSV | Kolumny, formuły, format |
| Presentation | PPTX, Google Slides | Liczba slajdów, branding |
| Data | JSON, structured | Schema, walidacja |
| Code | Script, automation | Język, dependencies |

**Output Definition Checklist:**
- [ ] Format pliku
- [ ] Gdzie zapisać
- [ ] Jak nazwać
- [ ] Struktura wewnętrzna
- [ ] Przykład/template

### Templates:
Gotowe szablony definicji dla 5 najczęstszych typów outputów

## 2.5 Constraint Setting

**Format:** Lecture + Exercise (20 min)

### Treść konceptualna:

**Typy constraints:**

1. **Format constraints**
   - "Maksymalnie 10 slajdów"
   - "Każda sekcja < 200 słów"

2. **Style constraints**
   - "Ton profesjonalny ale przystępny"
   - "Użyj brand colors z pliku X"

3. **Content constraints**
   - "Skup się tylko na Q4 data"
   - "Nie uwzględniaj produktów < $1000 revenue"

4. **Process constraints**
   - "Najpierw pokaż plan"
   - "Zatrzymaj się po researchu do review"

### Exercise: Constraint Audit
Weź swój task z 2.2 i dodaj:
- 2 format constraints
- 1 style constraint
- 1 content constraint

## 2.6 The Redirect Skill

**Format:** Lecture + Practice (20 min)

### Treść konceptualna:

**Mid-execution communication:**
> "You can send a message to the agent in the middle of executing. The agent will pick up your context and add it into the long-running work without interrupting itself."

**Kiedy redirect:**
- Plan nie odpowiada oczekiwaniom
- Nowy kontekst się pojawił
- Chcesz zmienić kierunek

**Jak redirect:**
- Krótko
- Konkretnie
- Bez przepraszania

### Practice:
Symulacja: Agent wykonuje zadanie, musisz zredirectować w 3 różnych scenariuszach

## 2.7 Module 2 Integration

**Format:** Project (30 min)

### Projekt: Task Library v1

**Instrukcje:**
1. Zidentyfikuj 10 recurring tasks z twojej pracy
2. Przepisz każdy przez framework WIRE
3. Dodaj constraints
4. Stwórz "Task Library" dokument

**Deliverable:**
Dokument z 10 dobrze zdefiniowanymi taskami gotowymi do delegacji

---

# MODULE 3: Building Your Agent Workspace

**Czas:** 2.5 godziny
**Cel:** Stworzyć środowisko pracy optymalne dla agentów

## 3.1 The Workspace Philosophy

**Format:** Lecture (20 min)

### Treść konceptualna:

**Core principle:**
> "Context that is externalized can be used by agents. Context in your head cannot."

**Agentic Workspace = środowisko gdzie:**
- Wiedza żyje w plikach, nie w głowie
- Struktura jest przewidywalna
- Agent może nawigować samodzielnie
- Praca się kumuluje między sesjami

**Trzy warstwy workspace:**

```
LAYER 1: File System Structure
    └── Folders, naming conventions, organization

LAYER 2: Context Files
    └── README, INSTRUCTIONS, context for agents

LAYER 3: Procedural Knowledge
    └── Skills, templates, workflows
```

## 3.2 File System as Agent Interface

**Format:** Lecture + Demo (25 min)

### Treść konceptualna:

**Insight:**
> "File system agents operate in territory that is entirely yours. Your files don't have bot detection. Your folders don't require authentication."

**Designing for agents:**

| Human-friendly | Agent-friendly |
|----------------|----------------|
| Nested deep hierarchies | Flat when possible |
| Creative folder names | Predictable naming |
| Files everywhere | Clear inbox/archive |
| Implicit organization | Explicit README |

**Naming conventions:**
```
GOOD:  2026-01-22-client-meeting-notes.md
BAD:   notes.md

GOOD:  /projects/active/project-name/
BAD:   /stuff/2026/january/misc/

GOOD:  invoice-001-acme-corp-2026-01.pdf
BAD:   scan0042.pdf
```

### Demo:
Before/after reorganizacja folderu dla agent-friendliness

## 3.3 The Context File Pattern

**Format:** Lecture + Templates (25 min)

### Treść konceptualna:

**README.md dla folderów:**
```markdown
# /projects/client-x/

## What's here
Wszystkie materiały dla projektu Client X.

## Structure
- /briefs - briefy i wymagania
- /deliverables - gotowe materiały
- /research - zebrane źródła
- /drafts - work in progress

## Current status
Active project, phase 2 (design).

## Key files
- brief-v2.md - aktualny brief
- timeline.md - harmonogram

## Instructions for AI
Gdy pracujesz nad tym projektem:
1. Zawsze sprawdź brief-v2.md najpierw
2. Nowe deliverables zapisuj w /deliverables
3. Używaj naming convention: [type]-[version]-[date]
```

**Typy context files:**
- README.md - overview folderu
- INSTRUCTIONS.md - jak tu pracować
- CONTEXT.md - background knowledge
- GLOSSARY.md - definicje terminów

### Templates:
4 gotowe templates do pobrania

## 3.4 The Inbox Pattern

**Format:** Lecture + Exercise (20 min)

### Treść konceptualna:

**Jeden punkt wejścia:**
> "The Dropbox is the one place you're allowed to throw things without thinking. If capturing takes more than a couple of seconds, you won't do it consistently."

**Structure:**
```
/inbox/
├── to-process/     # Nowe rzeczy do przejrzenia
├── to-file/        # Przetworzone, do zorganizowania
└── archive/        # Historyczne

/workspace/
├── active/         # Bieżące projekty
└── reference/      # Materiały referencyjne
```

**Workflow:**
1. Wrzuć do inbox bez myślenia
2. Agent przetwarza (klasyfikuje, nazywa)
3. Ty weryfikujesz
4. Agent rozkłada do właściwych miejsc

### Exercise:
Stwórz strukturę inbox dla swojego workspace

## 3.5 Workspace Templates

**Format:** Walkthrough + Setup (30 min)

### Treść konceptualna:

**3 archetypy workspace:**

**A) Solo Professional**
```
/work/
├── inbox/
├── clients/
│   └── [client-name]/
├── projects/
│   └── [project-name]/
├── reference/
├── templates/
└── WORKSPACE.md
```

**B) Content Creator**
```
/content/
├── inbox/
├── ideas/
├── drafts/
├── published/
├── assets/
├── research/
└── WORKSPACE.md
```

**C) Researcher/Analyst**
```
/research/
├── inbox/
├── sources/
├── literature/
├── analysis/
├── outputs/
└── WORKSPACE.md
```

### Setup Session:
Wybierz archetyp lub stwórz własny, zbuduj strukturę

## 3.6 The Agent Instructions File

**Format:** Lecture + Template (25 min)

### Treść konceptualna:

**CLAUDE.md / AGENT.md pattern:**
```markdown
# Agent Instructions

## Who I am
[Kontekst o tobie i twojej pracy]

## How I work
[Twoje preferencje, styl, zasady]

## Key concepts
[Ważne pojęcia, definicje]

## Project structure
[Jak zorganizowany jest workspace]

## Common tasks
[Najczęstsze zadania i jak je robić]

## Rules
[Hard rules - czego nie robić]
```

**Dlaczego to działa:**
- Agent czyta przy starcie sesji
- Konsystentne zachowanie między sesjami
- Skaluje twoją wiedzę

### Template:
Pełny template AGENT.md z komentarzami

## 3.7 Module 3 Integration

**Format:** Project (30 min)

### Projekt: Workspace Setup

**Instrukcje:**
1. Wybierz lub stwórz archetype
2. Zbuduj strukturę folderów
3. Stwórz minimum 3 README.md dla key folders
4. Napisz swój AGENT.md
5. Zrób screenshot "before" i "after"

**Deliverable:**
- Functional workspace structure
- AGENT.md file
- 3+ context files

---

# MODULE 4: Skills & Procedural Knowledge

**Czas:** 2 godziny
**Cel:** Nauczyć budowania reusable wiedzy proceduralnej dla agentów

## 4.1 What Are Skills?

**Format:** Lecture (20 min)

### Treść konceptualna:

**Definicja (Anthropic):**
> "Skills are organized collections of files that package composable procedural knowledge for agents. In other words, they're folders."

**Dlaczego foldery:**
- Każdy umie tworzyć foldery
- Version control (Git)
- Shareable (zip, cloud)
- Agent i human mogą czytać

**Skill vs Prompt:**

| One-time Prompt | Reusable Skill |
|-----------------|----------------|
| W kontekście chatu | W file system |
| Znika po sesji | Persystuje |
| Single use | Composable |
| Implicit knowledge | Explicit knowledge |

## 4.2 Anatomy of a Skill

**Format:** Lecture + Examples (25 min)

### Treść konceptualna:

**Minimal skill:**
```
skill-name/
├── skill.md        # Main instructions
└── README.md       # Human documentation
```

**Complete skill:**
```
skill-name/
├── skill.md        # Main instructions
├── README.md       # Human docs
├── examples/       # Sample inputs/outputs
│   ├── input-1.md
│   └── output-1.md
├── templates/      # Templates to use
│   └── template.md
├── scripts/        # Automation (optional)
│   └── process.py
└── assets/         # Images, files
```

**skill.md structure:**
```markdown
# Skill: [Name]

## Description
[Co ten skill robi - 1-2 zdania]

## When to use
[Kiedy agent powinien użyć tego skilla]

## Instructions
[Krok po kroku jak wykonać]

## Inputs
[Czego skill potrzebuje]

## Outputs
[Co skill produkuje]

## Examples
[Linki do przykładów lub inline examples]
```

### Examples:
3 real-world skills z różnych domen

## 4.3 Progressive Disclosure

**Format:** Lecture + Demo (15 min)

### Treść konceptualna:

**Problem:** Nie chcesz ładować 50 skills do context window

**Rozwiązanie:** Progressive disclosure

```
AT REST:
[Agent widzi tylko listę skills z 1-line descriptions]

WHEN TRIGGERED:
[Agent ładuje pełny skill.md]

AS NEEDED:
[Agent czyta examples, templates, scripts]
```

**Praktyka:**
- skill.md ma sekcję "Description" na górze
- Reszta ładowana on-demand
- Agent decyduje kiedy potrzebuje więcej

### Demo:
Pokazanie jak agent wybiera i ładuje skill

## 4.4 Creating Your First Skill

**Format:** Workshop (30 min)

### Treść konceptualna:

**Workflow: od powtarzalnego zadania do skilla**

**Step 1: Identify**
- Jakie zadanie robisz regularnie?
- Czy ma przewidywalną strukturę?
- Czy output jest podobny za każdym razem?

**Step 2: Document**
- Napisz instrukcje jakbyś uczył nowego pracownika
- Bądź explicit - nie zakładaj nic
- Dodaj examples

**Step 3: Test**
- Daj skillowi zadanie
- Obserwuj gdzie agent się gubi
- Iteruj na instrukcjach

**Step 4: Refine**
- Dodaj edge cases
- Ulepszaj examples
- Upraszczaj gdzie możliwe

### Workshop:
Każdy uczestnik tworzy swój pierwszy skill (30 min hands-on)

## 4.5 The Teach Pattern

**Format:** Demo + Practice (20 min)

### Treść konceptualna:

**"Teach Claude" workflow:**
1. Wykonaj zadanie raz, nagrywając kroki
2. Powiedz agentowi: "Zapamiętaj to jako skill"
3. Agent tworzy skill.md z twoich działań
4. Review i refine

**Kiedy używać Teach vs Write:**

| Teach (Record) | Write (Manual) |
|----------------|----------------|
| Browser workflows | Complex logic |
| Repetitive clicks | Conditional rules |
| "Watch me do this" | "Here's how to think" |

### Practice:
Nagraj prosty workflow i przekształć w skill

## 4.6 Skill Composition

**Format:** Lecture + Examples (20 min)

### Treść konceptualna:

**Insight:**
> "A library of hundreds of skills that agent can decide to pull into context only at runtime when deciding to work on a particular task."

**Composition patterns:**

**A) Sequential:**
```
Task: Prepare client report
→ Use skill: data-analysis
→ Then use skill: report-writing
→ Then use skill: powerpoint-creation
```

**B) Conditional:**
```
Task: Process document
→ If PDF: use skill: pdf-extraction
→ If image: use skill: ocr-processing
→ Then: use skill: document-summary
```

**C) Parallel:**
```
Task: Research topic
→ skill: web-research (async)
→ skill: file-search (async)
→ skill: synthesis (after both complete)
```

### Examples:
3 composed skill workflows

## 4.7 Module 4 Integration

**Format:** Project (30 min)

### Projekt: Skill Library v1

**Instrukcje:**
1. Zidentyfikuj 5 powtarzalnych zadań
2. Stwórz skill dla 3 z nich
3. Dla każdego:
   - skill.md
   - Minimum 1 example
   - README.md
4. Zorganizuj w /skills folder

**Deliverable:**
/skills folder z 3 functional skills

---

# MODULE 5: System Architecture

**Czas:** 2 godziny
**Cel:** Nauczyć budowania niezawodnych systemów agentowych

## 5.1 Building Blocks Overview

**Format:** Lecture (25 min)

### Treść konceptualna:

**8 building blocks niezawodnych systemów:**

| Block | Funkcja | Przykład |
|-------|---------|----------|
| **Dropbox** | Capture point | Slack channel, email inbox |
| **Sorter** | Classification | AI decides: project/idea/task |
| **Form** | Schema | Fixed fields for each type |
| **Filing Cabinet** | Storage | Notion database, folder structure |
| **Receipt** | Audit trail | Log of what happened |
| **Bouncer** | Quality filter | Confidence threshold |
| **Tap on Shoulder** | Proactive nudge | Daily digest, weekly review |
| **Fix Button** | Easy correction | "Reply FIX to correct" |

**Zasada:**
> "You don't abandon systems because they're imperfect. You abandon them because you stop trusting them."

## 5.2 Trust Mechanisms

**Format:** Lecture + Examples (20 min)

### Treść konceptualna:

**Trust ≠ Capability**
- Capability: "System files notes"
- Trust: "I believe filing enough to keep using it"

**4 mechanizmy budowania trust:**

1. **Visibility (Receipt)**
   - Log wszystkiego co się dzieje
   - Możliwość trace'owania decyzji
   - "Co weszło, co wyszło, z jaką pewnością"

2. **Confidence scores**
   - Agent mówi jak pewny jest decyzji
   - Low confidence = ask, don't act
   - Human review dla edge cases

3. **Easy corrections (Fix Button)**
   - Poprawka musi być trywialna
   - "Reply FIX: this is project, not idea"
   - Jeśli poprawka = praca, nikt nie poprawia

4. **Graceful degradation**
   - System wie co robić gdy niepewny
   - Default to safe behavior
   - Ask rather than guess

### Examples:
Przypadki gdzie trust mechanism uratował system

## 5.3 The Separation Principle

**Format:** Lecture + Diagram (20 min)

### Treść konceptualna:

**Zasada:**
> "Separate memory from compute from interface."

**Trzy warstwy:**

```
┌─────────────────────────────────────────────┐
│                 INTERFACE                    │
│     (Where human interacts: Slack, email)   │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│                  COMPUTE                     │
│     (Where logic runs: AI, automation)      │
└─────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────┐
│                  MEMORY                      │
│     (Where truth lives: database, files)    │
└─────────────────────────────────────────────┘
```

**Dlaczego separacja:**
- Możesz zmienić interface (Slack → Teams) bez rebuildu
- Możesz zmienić AI (Claude → GPT) bez utraty danych
- Możesz zmienić storage (Notion → Airtable) bez zmiany logic

## 5.4 Engineering Principles for Non-Engineers

**Format:** Lecture + Exercise (25 min)

### Treść konceptualna:

**12 zasad:**

1. **One reliable human behavior**
   > "If your system requires three behaviors, you don't have a system."

2. **Separate memory, compute, interface**
   > Każda warstwa ma jedno zadanie

3. **Treat prompts like APIs**
   > Fixed input, fixed output, no surprises

4. **Build trust mechanisms, not just capability**
   > Logs, confidence, fix buttons

5. **Default to safe behavior when uncertain**
   > Low confidence = ask, don't file

6. **Small, frequent, actionable outputs**
   > <150 words daily, <250 weekly

7. **Next action as execution unit**
   > Nie "work on website", ale "email Sarah"

8. **Prefer routing over organizing**
   > AI routes, human doesn't decide taxonomy

9. **Keep categories painfully small**
   > 4 buckets usually enough

10. **Design for restart, not perfection**
    > Miss a week? Just restart, no guilt

11. **Build core loop, then modules**
    > Capture → File → Digest first, bells later

12. **Maintainability over cleverness**
    > Fewer tools, fewer steps, clear logs

### Exercise:
Audit istniejącego systemu (osobistego lub zawodowego) przez te zasady

## 5.5 Designing Your Core Loop

**Format:** Workshop (25 min)

### Treść konceptualna:

**Minimal Viable Loop:**
```
CAPTURE → PROCESS → STORE → SURFACE
```

**Rozwinięcie:**
```
1. CAPTURE
   - Single input point
   - Zero friction
   - No decisions

2. PROCESS
   - AI classification
   - Extract key info
   - Confidence scoring

3. STORE
   - Route to right place
   - Fill standard fields
   - Log transaction

4. SURFACE
   - Daily digest
   - Weekly review
   - On-demand queries
```

### Workshop:
Zaprojektuj swój core loop (paper prototype)

## 5.6 Module 5 Integration

**Format:** Project (25 min)

### Projekt: System Blueprint

**Instrukcje:**
1. Wybierz jeden workflow do systematyzacji
2. Zmapuj przez 8 building blocks
3. Określ trust mechanisms
4. Narysuj separation layers
5. Zdefiniuj core loop

**Deliverable:**
System Blueprint dokument z diagramami

---

# MODULE 6: Integration & Scaling

**Czas:** 1.5 godziny
**Cel:** Połączyć wszystko i pokazać ścieżkę wzrostu

## 6.1 Connecting the Pieces

**Format:** Lecture + Demo (20 min)

### Treść konceptualna:

**Integration stack (tool-agnostic):**

```
YOUR WORKSPACE (Files & Folders)
        │
        ▼
AGENT INTERFACE (Claude/GPT/etc)
        │
        ├── Skills (procedural knowledge)
        │
        ├── Context Files (README, AGENT.md)
        │
        └── Connectors (APIs, MCP, Zapier)
                │
                ▼
        EXTERNAL SYSTEMS
        (Calendar, Email, CRM, etc)
```

**Pattern: MCP + Skills**
> "MCP provides the connection to the outside world while skills provide the expertise."

### Demo:
Pokazanie full workflow: capture → process → output → external system

## 6.2 The Day 30 Vision

**Format:** Lecture + Exercise (20 min)

### Treść konceptualna:

**Cel:**
> "Claude on day 30 should be better than Claude on day 1 of working with you."

**Jak to osiągnąć:**

**Week 1:** Setup
- Workspace structure
- Basic AGENT.md
- 2-3 initial skills

**Week 2:** Capture
- Consistent capture habit
- Refine classification
- Add trust mechanisms

**Week 3:** Patterns
- Identify recurring tasks
- Create more skills
- Build core loop

**Week 4:** Compound
- Skills compose
- Context accumulates
- System learns from corrections

### Exercise:
Stwórz 30-day plan dla swojego systemu

## 6.3 Parallel Execution Model

**Format:** Demo + Practice (20 min)

### Treść konceptualna:

**New mental model:**
> "Instead of one long running chat, 6 different threads working in parallel."

**Workflow:**
1. Define 3-5 independent tasks
2. Launch all at once
3. Switch between to review progress
4. Collect artifacts when done

**Best practices:**
- Independent tasks (no dependencies)
- Clear outputs for each
- Don't micromanage in-progress
- Batch your review

### Practice:
Define and launch 3 parallel tasks

## 6.4 Scaling Patterns

**Format:** Lecture (15 min)

### Treść konceptualna:

**A) Personal → Team**
- Shared skill library
- Common workspace conventions
- Team-wide context files

**B) Simple → Complex**
- Start: single loop
- Add: multiple domains
- Scale: interconnected systems

**C) Manual → Automated**
- Start: manual trigger
- Add: scheduled runs
- Scale: event-driven

**Warning signs you're overcomplicating:**
- More than 4 categories
- More than 3 tools in chain
- Can't explain system in 2 minutes
- Fix takes longer than manual workaround

## 6.5 Future-Proofing

**Format:** Lecture (15 min)

### Treść konceptualna:

**What will change:**
- Tools (new agents, interfaces)
- Capabilities (more reliable, faster)
- Integration (seamless handoffs)

**What won't change:**
- Need for clear task definition
- Value of externalized context
- Importance of trust mechanisms
- Power of composable skills

**Future-proof principles:**
1. Skills are portable (just folders)
2. Context files are universal (markdown)
3. Principles > specific tools
4. Build for restart, not perfection

## 6.6 Final Integration

**Format:** Capstone Project (30 min)

### Capstone: Your Agentic Work System

**Requirements:**
1. Functional workspace with structure
2. AGENT.md with your context
3. Minimum 5 skills in library
4. One complete system (with building blocks)
5. Documentation for Day 30 continuation

**Presentation format:**
- 5-minute demo of your system
- Show one full workflow
- Explain what compounds over time

**Peer review:**
- Pairs exchange systems
- Test as "new user"
- Feedback on clarity

---

# APPENDICES

## Appendix A: Tool-Specific Implementation Notes

*Dla każdego modułu: jak zaimplementować w Claude/ChatGPT/Gemini/etc.*

## Appendix B: Skill Templates

*10 gotowych templates dla common use cases*

## Appendix C: System Blueprints

*5 gotowych blueprintów dla różnych profesji*

## Appendix D: Glossary

| Term | Definition |
|------|------------|
| **Agentic** | AI that executes multi-step plans autonomously |
| **Artifact** | Concrete output file, not conversation text |
| **Checkpoint** | Zapisanie artefaktu jako kotwicy dla dalszej pracy |
| **Context drift** | Degradacja jakości w długich sesjach przez ograniczenia kontekstu |
| **Context file** | Document providing background for agents |
| **Editing loop** | Human fixes AI output iteratively (inefficient) |
| **Inverse supervision** | Projektowanie systemu pod łatwość weryfikacji, nie wykonania |
| **Skill** | Folder with procedural knowledge for agents |
| **Slop** | Passable-looking output that wasn't properly verified |
| **Steering loop** | Human guides direction, agent executes (efficient) |
| **Task queue** | List of delegated tasks for async execution |
| **WIRE framework** | What-Input-Rules-Examples structure for task definition |

## Appendix E: Resources

- Awesome Claude Skills (GitHub)
- MCP Server Directory
- Community Skill Library
- Weekly Office Hours info

---

# Success Metrics

## For Participants

**By end of course, you can:**
- [ ] Explain why agent is not a knowledge source (and why it matters)
- [ ] Define tasks (not prompts) using WIRE framework
- [ ] Identify when to use chat vs agent on the spectrum
- [ ] Build and maintain an agent-friendly workspace
- [ ] Create reusable skills for recurring tasks
- [ ] Design systems with trust mechanisms
- [ ] Use checkpointing to prevent drift and slop
- [ ] Launch and manage parallel agent tasks

## For Course

**Tracking:**
- Completion rate per module
- Skill library size (avg per participant)
- System complexity achieved
- 30-day retention of practices
- NPS at end vs 30 days after

---

*Curriculum v2.0 - Styczeń 2026*
*Based on research from 20+ sources on agentic work patterns*
*Updated with framework synthesis: spectrum model, context drift, inverse supervision*
