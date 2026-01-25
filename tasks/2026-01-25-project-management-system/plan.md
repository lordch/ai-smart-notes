# Plan: Project Management System

## Cel

Zbudować lokalny system zarządzania projektami z:
- Interaktywnym UI w przeglądarce (Kanban, filtry)
- Danymi w plikach markdown + YAML frontmatter
- Edycją statusów przez drag & drop

## Decyzje

| Aspekt | Decyzja |
|--------|---------|
| Taski | Oddzielne pliki `.md` |
| Loose tasks | Dozwolone (bez projektu) |
| Tech | FastAPI + Alpine.js + Tailwind |
| Hosting | Lokalnie |
| Edycja z UI | Tylko statusy |

## Struktura plików

```
strategy/
├── people/
│   ├── Person - Rudy.md
│   ├── Person - Dagny.md
│   ├── Person - Agnieszka.md
│   └── Person - Gumis.md
│
├── projects/
│   ├── Project - Dagny Discovery.md
│   ├── Project - AI Slop Research.md
│   ├── Project - News Monitoring.md
│   └── Project - Scope Research.md
│
└── tasks/
    ├── Task - Plan spotkania Gumis.md
    ├── Task - Research AI slop sources.md
    └── ...

.cursor/skills/pm/
├── SKILL.md
├── server.py
├── requirements.txt
└── ui/
    ├── index.html
    ├── style.css
    └── app.js
```

## Schemas

### Person
```yaml
---
type: Person
role: Client | Partner | Lead | Network
status: Active | Dormant | Lost
company: "nazwa firmy"
date-created: 2026-01-25
tags: []
---
```

### Project
```yaml
---
type: Project
status: Backlog | Active | On Hold | Done
person: "[[Person - X]]"  # opcjonalne
priority: High | Medium | Low
date-created: 2026-01-25
tags: []
---
```

### Task
```yaml
---
type: Task
status: Todo | In Progress | Blocked | Done
project: "[[Project - X]]"  # opcjonalne
person: "[[Person - X]]"    # opcjonalne
priority: High | Medium | Low
date-created: 2026-01-25
due: 2026-01-28             # opcjonalne
tags: []
---
```

## Plan implementacji

### Faza 1: Struktura danych ✅
- [x] Utworzyć folder `strategy/people/`
- [x] Utworzyć folder `strategy/projects/`
- [x] Utworzyć folder `strategy/pm-tasks/` (dla PM, oddzielny od głównego tasks/)
- [ ] Migrować istniejące pliki klientów (GrowGo, Scope, mspark) — do zrobienia ręcznie
- [x] Utworzyć pliki dla: Rudy, Dagny, Agnieszka, Gumis, Scope Fluidics
- [x] Utworzyć projekty z przykładów
- [x] Utworzyć taski z przykładów

### Faza 2: Backend (FastAPI) ✅
- [x] Utworzyć `.cursor/skills/pm/`
- [x] `requirements.txt` - dependencies
- [x] `server.py` - endpoints:
  - GET /api/people - lista osób
  - GET /api/projects - lista projektów
  - GET /api/tasks - lista tasków
  - PATCH /api/tasks/{id} - update statusu
  - PATCH /api/projects/{id} - update statusu
- [x] Parsowanie YAML frontmatter (python-frontmatter)
- [x] Zapis zmian do plików

### Faza 3: Frontend (Alpine.js + Tailwind) ✅
- [x] `ui/index.html` - struktura
- [x] `ui/app.js` - logika Alpine.js
- [x] Widok Kanban dla tasków (4 kolumny: Todo, In Progress, Blocked, Done)
- [x] Widok Pipeline dla osób (4 kolumny: Lead, Partner, Network, Client)
- [x] Lista projektów z filtrami
- [x] Drag & drop (Sortable.js)
- [x] Filtry: by person, by project
- [x] Klik → kopiuje ścieżkę do clipboardu (do otwarcia w Cursor)

### Faza 4: Integracja ✅
- [x] Komenda `@pm` w `.cursor/commands/`
- [x] SKILL.md dokumentacja
- [x] Test end-to-end

## Aktualne dane do wprowadzenia

### People
| Nazwa | Role | Company | Notes |
|-------|------|---------|-------|
| Rudy | Partner | GrowGo (narzędzia górnicze) | Pośrednik, może przynosić klientów |
| Dagny | Lead | ? | Lekarka, research o publikacjach |
| Agnieszka | Network | ? | Rozmowa, use case na przyszłość |
| Gumis | Lead | ? | Plan na spotkanie |
| Scope Fluidics | Client | Scope Fluidics | Istniejący w bazie |

### Projects
| Nazwa | Person | Status |
|-------|--------|--------|
| Dagny Discovery | Dagny | Active |
| AI Slop Research | - | Active |
| News Monitoring | - | Backlog |
| Scope Research | Scope Fluidics | Active |

### Tasks
| Nazwa | Project | Person | Status |
|-------|---------|--------|--------|
| Plan spotkania Gumis | - | Gumis | Todo |
| Research AI slop sources | AI Slop Research | - | Todo |
| News monitoring setup | News Monitoring | - | Todo |
| Research Scope use cases | Scope Research | Scope Fluidics | In Progress |

## Uruchomienie

```bash
venv/bin/python .cursor/skills/pm/server.py
```

Otwórz: **http://localhost:8787**

## Status

**GOTOWE** — system zaimplementowany i przetestowany.

### Co działa:
- 5 osób (Rudy, Dagny, Agnieszka, Gumis, Scope Fluidics)
- 4 projekty (Dagny Discovery, AI Slop Research, News Monitoring, Scope Research)
- 4 taski (Plan spotkania Gumis, Research AI slop, News monitoring setup, Research Scope)
- Kanban z drag & drop
- Pipeline osób
- Filtry

### Do zrobienia później:
- Migracja starych plików z `strategy/clients/`
- Więcej filtrów (by tag, by deadline)
- Quick-add z UI
