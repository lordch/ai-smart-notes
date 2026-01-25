# Knowledge Management System Agent

## Domena
Consulting / Knowledge Work / Any role with multiple clients or projects

## Problem klienta
- Każda sesja z AI zaczyna się od zera — brak pamięci między sesjami
- Kontekst klienta/projektu trzeba za każdym razem wyjaśniać
- Preferencje, styl komunikacji, ustalenia — gubią się
- Brak visibility: "Co robiłem z tym klientem miesiąc temu?"
- Chat history w Claude/ChatGPT jest trudna do przeszukiwania i nie kumuluje się

## Kluczowy insight

> "Claude Code runs locally and can see all your files" — to nie jest chat, to **local AI agent z persistent memory w plikach**.

## Workflow agentowy

### Struktura folderów
```
workspace/
├── CLAUDE.md              # Globalne preferencje i instrukcje
├── clients/
│   ├── client-a/
│   │   ├── CLAUDE.md      # Preferencje tego klienta
│   │   ├── work_log.md    # Dziennik pracy
│   │   ├── meetings/      # Notatki ze spotkań
│   │   └── deliverables/  # Outputy
│   └── client-b/
│       └── ...
└── templates/             # Szablony dokumentów
```

### Komponenty systemu

1. **CLAUDE.md** — instrukcje dla agenta
   - Kto to jest klient, jaki ma kontekst
   - Styl komunikacji (formalny/nieformalny)
   - Preferowane formaty dokumentów
   - Procesy i workflows

2. **Work logs** — automatyczny dziennik
   - Co zrobiono w każdej sesji
   - Timestamp, krótki opis
   - Linki do stworzonych plików
   - Agent aktualizuje po każdej sesji

3. **Git history** — persistent memory
   - Commit messages jako "dlaczego" zmian
   - Możliwość powrotu do poprzednich wersji
   - Agent może przeszukać historię

4. **Structured documents** — deliverables
   - Każdy output w pliku (nie w chacie)
   - Spójne formatowanie
   - Możliwość iteracji

### Przykładowy CLAUDE.md dla klienta
```markdown
# Client: Acme Corp

## Context
- Industry: Manufacturing
- Main contact: John Smith (VP Operations)
- Project: Process automation initiative

## Communication style
- Formal tone in documents
- John prefers bullet points over paragraphs
- Always include executive summary

## Current focus
- Phase 2: Inventory management automation
- Deadline: March 15

## File conventions
- Meeting notes: meetings/YYYY-MM-DD-topic.md
- Deliverables: deliverables/YYYY-MM-DD-name.md
- Always update work_log.md after each session
```

## Before / After
| Bez systemu | Z systemem |
|-------------|------------|
| Każda sesja od zera | Agent zna kontekst klienta |
| "Przypomnij mi o preferencjach..." | Agent czyta CLAUDE.md |
| Brak historii | Work log + git history |
| Chat ginie | Wszystko w plikach |
| Wiedza w głowie | Wiedza zeksternalizowana |

## ROI / Metryki
- Context switching: minuty zamiast 15-30 min na "wejście" w projekt
- Consistency: spójny output zgodny z preferencjami klienta
- Onboarding: nowy team member może przeczytać CLAUDE.md i kontynuować
- Compounding: każda sesja buduje na poprzedniej

## Wymagania wdrożeniowe
- Narzędzia: Claude Code z dostępem do file system
- Dane: struktura folderów, CLAUDE.md files
- Complexity: **Low** (setup) / **Medium** (utrzymanie)
- Dyscyplina: aktualizacja work logów, git commits

## Warianty / Rozszerzenia
- Automatyczne generowanie weekly/monthly summaries z work logów
- Cross-client insights: "Jakie patterns widzę across wszystkich klientów?"
- Templates library: szablony dokumentów per typ deliverable
- Slash commands: `/status` dla quick status update, `/meeting` dla meeting notes

## Compounding Effect

Kluczowa wartość tego systemu to **compounding** — każda interakcja wzbogaca kontekst:

1. Sesja 1: Agent uczy się preferencji → zapisuje do CLAUDE.md
2. Sesja 2: Agent stosuje preferencje + uczy się nowych → aktualizuje
3. Sesja N: Agent zna wszystkie preferencje, historię, kontekst

Im więcej pracy, tym agent jest bardziej użyteczny dla tego klienta.

## Failure Modes (uwaga!)
- CLAUDE.md out of date → agent używa starych preferencji
- Brak dyscypliny w work logach → luki w historii
- Za dużo kontekstu → agent się gubi (keep it focused)
- Sensitive data → użyj .claudeignore dla poufnych plików

## Źródło
[Matt Stockton - How Claude Code Became My Knowledge Management System](https://mattstockton.com/2025/09/19/how-claude-code-became-my-knowledge-management-system.html)
[Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
