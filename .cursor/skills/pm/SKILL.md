# Skill: Project Management Dashboard

Lokalny system zarządzania projektami z interaktywnym UI w przeglądarce.

## Uruchomienie

```bash
# Instalacja zależności (jednorazowo)
venv/bin/pip install -r .cursor/skills/pm/requirements.txt

# Uruchomienie serwera
venv/bin/python .cursor/skills/pm/server.py
```

Otwórz: **http://localhost:8787**

## Struktura danych

```
strategy/
├── people/          # Osoby (klienci, partnerzy, leady, network)
├── projects/        # Projekty
└── pm-tasks/        # Zadania (Kanban)
```

## Schemas

### Person (`strategy/people/Person - {Nazwa}.md`)

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

**Role:**
- `Client` — płacący klient
- `Partner` — współpraca, referrale (np. Rudy)
- `Lead` — potencjalny klient w rozmowach
- `Network` — kontakt, może kiedyś

### Project (`strategy/projects/Project - {Nazwa}.md`)

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

### Task (`strategy/pm-tasks/Task - {Nazwa}.md`)

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

## UI Features

### Widoki

1. **Tasks (Kanban)** — 4 kolumny: Todo, In Progress, Blocked, Done
2. **People (Pipeline)** — 4 kolumny: Lead, Partner, Network, Client
3. **Projects** — 4 kolumny: Backlog, Active, On Hold, Done

### Interakcje

- **Drag & drop** — przeciągnij kartę do innej kolumny, status w pliku się zaktualizuje
- **Klik** — kopiuje ścieżkę do pliku (do otwarcia w Cursor)
- **Filtry** — w widoku Tasks: by person, by project

## Workflow

1. Uruchom serwer: `venv/bin/python .cursor/skills/pm/server.py`
2. Otwórz http://localhost:8787 w przeglądarce Cursor
3. Przeciągaj karty między kolumnami
4. Kliknij kartę → skopiowana ścieżka → otwórz w Cursor do edycji treści

## Dodawanie nowych elementów

Stwórz nowy plik markdown z odpowiednim frontmatterem:

```bash
# Nowa osoba
touch "strategy/people/Person - Jan Kowalski.md"

# Nowy projekt
touch "strategy/projects/Project - Nowy Projekt.md"

# Nowy task
touch "strategy/pm-tasks/Task - Zrób coś.md"
```

Lub poproś agenta o stworzenie.

## API

- `GET /api/people` — lista osób
- `GET /api/projects` — lista projektów
- `GET /api/tasks` — lista tasków
- `GET /api/all` — wszystko
- `PATCH /api/tasks/{id}` — update statusu taska
- `PATCH /api/projects/{id}` — update statusu projektu
- `PATCH /api/people/{id}` — update statusu osoby
