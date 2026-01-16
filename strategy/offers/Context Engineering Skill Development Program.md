type:: [[Framework]]
status:: Draft
date-created:: 2026-01-14
context:: Training/consultancy offering - Future Skills with AI
related:: [[Context Engineering]], [[Context Continuity Engineering]], [[Strategy - AI Consultancy for Polish SME Knowledge Work]]

# Context Engineering Skill Development Program

---

## The Skill

**Context Engineering** jako jedna z kluczowych "Future Skills" w erze AI.

> "Context is the new moat. Same model, different results. The team that can externalize what they know and feed it to agents in a structured way will build things competitors can't copy."
> — Saboo Shubham

Umiejętność świadomego, systematycznego dostarczania odpowiedniego kontekstu agentom AI - nie jako jednorazowa czynność, ale jako **kumulująca się kompetencja**.

---

## Dlaczego to permanentna umiejętność

Z [[Context Engineering]]:
> "As long as we're dealing with quadratic transformer attention, you're always going to benefit from doing the deterministic engineering that allows you to keep the context window as small as possible for a given task."
> — Dex Horthy

Modele będą się zmieniać. Context engineering pozostanie.

---

## Poziomy kompetencji

### Level 0: Single Session Mastery
**"Jak dać dobry kontekst w jednej sesji"**

**Umiejętności:**
- Rozumienie ograniczeń context window
- Typy kontekstu i kiedy je stosować
- Kiedy ładować pliki vs pisać w prompt
- Formatowanie dla maksymalnej gęstości informacji
- Rozpoznawanie kiedy kontekst się "rozmywa" (context rot)

**Typy kontekstu** (za Saboo Shubham):
| Typ | Opis | Przykład |
|-----|------|----------|
| **User context** | Kim są użytkownicy, czego potrzebują | "Nasi użytkownicy to devs którzy chcą szybko prototypować" |
| **Domain context** | Specyficzne wzorce i ograniczenia dziedziny | "W multi-agent systems koordynator nie woła tools bezpośrednio" |
| **Historical context** | Co próbowaliśmy, co nie zadziałało | "W Q2 2025 próbowaliśmy single-prompt, context window się przepełniał" |
| **Quality context** | Przykłady co jest dobre, co złe | "Ta odpowiedź była pomocna. Ta zmyliła użytkowników." |
| **Constraint context** | Realne ograniczenia | "Musi działać na free tier API, latency < 2s" |

**Narzędzia:**
- Prosty prompt engineering
- Kopiowanie plików do chata
- Manualne zarządzanie kontekstem

**Rezultat:** Efektywna pojedyncza sesja z AI

---

### Level 1: Multi-Session Continuity
**"Praca nad zadaniem w wielu sesjach z użyciem artefaktów pośrednich"**

**Umiejętności:**
- Dzielenie złożonych zadań na sesje
- Tworzenie artefaktów pośrednich jako checkpointów
- Decyzja: kiedy izolować kontekst, kiedy dzielić
- Operowanie na różnych poziomach abstrakcji
- Organizacja workspace'u dla AI

**Kluczowe pytania:**
- Jak podzielić to zadanie żeby każda sesja była samodzielna?
- Jakie artefakty pośrednie pozwolą mi wrócić do pracy?
- Co musi być w kontekście następnej sesji?
- Jak przekazać "stan" między sesjami?

**Wzorce:**
- Progressive disclosure - pokazuj metadata, ładuj szczegóły on-demand
- Checkpoint files - podsumowania stanu po każdej sesji
- Structured handoff - co zostało zrobione, co dalej, co ważne

**Narzędzia:**
- Pliki markdown jako intermediate artifacts
- Organizacja folderów (jeden folder = jeden kontekst)
- Naming conventions dla łatwego odnajdywania

**Rezultat:** Efektywna praca nad złożonym zadaniem przez wiele sesji

---

### Level 2: Persistent Memory
**"Kontekst reużywalny między projektami"**

**Umiejętności:**
- Projektowanie memory systems
- Rozróżnianie: co zawsze ładować vs co ładować on-demand
- Utrzymywanie aktualności memory files
- Capture learnings z sesji do trwałej wiedzy

**Three-Layer Memory System** (za Teresa Torres):

| Warstwa | Plik | Ładowanie | Zawartość |
|---------|------|-----------|-----------|
| **Global** | `~/.claude/CLAUDE.md` | Zawsze | Preferencje użytkownika, styl pracy |
| **Project** | `./CLAUDE.md` | W projekcie | Architektura, konwencje, stack |
| **Reference** | `./context/*.md` | On-demand | Szczegółowy kontekst (users, products, examples) |

**Hierarchical Loading** (za Thomas Landgraf):
- Claude szuka CLAUDE.md w górę drzewa katalogów
- Subdirectory memory ładowane tylko gdy pracujesz w tym katalogu
- On-demand = oszczędność tokenów

**Maintenance prompts:**
- Session Learning Capture - "Co się nauczyliśmy? Zapisz do CLAUDE.md"
- Directory Deep Dive - "Zbadaj architekturę, stwórz dokumentację"
- Spring Cleaning - "Zweryfikuj memory files vs aktualny kod"

**Narzędzia:**
- CLAUDE.md / AGENTS.md / GEMINI.md
- Slash commands (`/competitive-research`)
- Custom agents
- Skills

**Rezultat:** AI "pamięta" kontekst między projektami, sesjami, zadaniami

---

### Level 3: Organizational Moat
**"Gromadzenie wiedzy jako przewaga konkurencyjna"**

**Umiejętności:**
- Designing shared context systems
- Knowledge externalization workflows
- Team onboarding through context
- Context as institutional memory

**Insight:**
> "Context accumulates over time. Every project you do, every failure you document, every user insight you capture, every example you collect adds to your context library."
> — Saboo Shubham

**Flywheel:**
```
Good context 
    → Better outputs 
        → Learning what context mattered 
            → Improved context docs 
                → Repeat
```

**Team A vs Team B:**
| Team A | Team B |
|--------|--------|
| Każdy projekt od zera | Maintains context docs |
| Generic outputs | Better results on day one |
| Learning stays in heads | Learning captured in files |
| Hours on corrections | Minutes on refinement |

**Organizational patterns:**
- Shared context libraries (brand voice, user personas, domain knowledge)
- Context review as part of project retrospectives
- New hire onboarding through context files
- Context quality as KPI

**Rezultat:** Organizacyjna przewaga konkurencyjna - "context can't be downloaded, it has to be earned"

---

## Curriculum Overview

| Level | Czas | Dla kogo | Rezultat |
|-------|------|----------|----------|
| **0** | 2-3h | Każdy | Efektywna pojedyncza sesja |
| **1** | 4-6h | Knowledge workers | Złożone zadania w wielu sesjach |
| **2** | 6-8h | Power users, founders | Personal knowledge system |
| **3** | 4-6h | Teams, leaders | Organizational capability |

**Full program:** 16-20h (4-5 warsztatów)
**Modular:** Można brać pojedyncze poziomy

---

## Narzędzie: Claude Code

Program używa **Claude Code** jako primary tool:

**Dlaczego Claude Code:**
- Filesystem access = natural context management
- CLAUDE.md = built-in memory system
- Terminal-based = gdzie kontekst żyje
- Slash commands = reusable workflows

**Ale zasady są tool-agnostic:**
- Te same wzorce działają z Cursor, Windsurf, Codex
- Context files można używać z różnymi narzędziami
- Metodologia > narzędzie

---

## Źródła

- [[Product Talk - Claude Code What It Is How Its Different and Why Non-Technical People Should Use It]]
- [[Product Talk - Stop Repeating Yourself Give Claude Code a Memory]]
- [[Thomas Landgraf - Claude Code's Memory Working with AI in Large Codebases]]
- [[Saboo Shubham - Context is the new Moat (Twitter)]]
- [[YouTube - Chatting agents, context engineering and more with Dex Horthy (@dexhorthy)]]

---

## Related

- [[Context Engineering]]
- [[Context Continuity Engineering]]
- [[Strategy - AI Consultancy for Polish SME Knowledge Work]]
- [[Strategy - mspark Accelerator Collaboration Opportunity]]

