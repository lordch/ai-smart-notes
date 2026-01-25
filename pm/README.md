# PM - Project Management System

Lokalny system zarządzania projektami oparty na plikach markdown z interaktywnym dashboardem.

## Uruchomienie

```bash
# Instalacja (jednorazowo)
venv/bin/pip install -r .cursor/skills/pm/requirements.txt

# Start serwera
venv/bin/python .cursor/skills/pm/server.py
```

**Dashboard:** http://localhost:8787

## Struktura

```
pm/
├── people/      # Osoby (klienci, partnerzy, leady)
├── projects/    # Projekty (klienckie i wewnętrzne)
├── tasks/       # Taski Kanban
└── README.md
```

## Widoki dashboardu

| Tab | Kolumny | Opis |
|-----|---------|------|
| **Tasks** | Todo, In Progress, Blocked, Done | Kanban tasków |
| **Projects** | Backlog, Active, On Hold, Done | Status projektów |
| **People** | Lead, Partner, Network, Client | Pipeline relacji |

## Schemas

### Person (`pm/people/Person - {Nazwa}.md`)

```yaml
---
type: Person
role: Client | Partner | Lead | Network
status: Active | Dormant | Lost
company: "nazwa firmy"
date-created: 2026-01-25
tags: []
---

# Nazwa

## Why this matters
Dlaczego ta relacja jest ważna.

## Context
Kontekst, historia, notatki.
```

### Project (`pm/projects/Project - {Nazwa}.md`)

```yaml
---
type: Project
status: Backlog | Active | On Hold | Done
person: "[[Person - X]]"           # opcjonalne
priority: High | Medium | Low
date-created: 2026-01-25
tags: []
folders:                           # foldery z artefaktami
  - tasks/2026-01-XX-nazwa-projektu
---

# Nazwa Projektu

## Why this matters
Dlaczego ten projekt jest ważny.

## Cel
Co chcemy osiągnąć.

## Deliverables
- Deliverable 1
- Deliverable 2

## Status
Aktualny stan projektu.
```

### Task (`pm/tasks/Task - {Nazwa}.md`)

```yaml
---
type: Task
status: Todo | In Progress | Blocked | Done
project: "[[Project - X]]"         # opcjonalne
person: "[[Person - X]]"           # opcjonalne
priority: High | Medium | Low
date-created: 2026-01-25
due: 2026-01-28                    # opcjonalne
tags: []
---

Opis zadania - co trzeba zrobić.
```

## Interakcje w UI

- **Drag & drop** - przeciągnij kartę między kolumnami (zmienia status w pliku)
- **Klik w kartę** - otwiera widok szczegółów z renderowanym markdown
- **Klik w folder** - pokazuje pliki w folderze projektu
- **Klik w plik** - podgląd zawartości z renderowanym markdown
- **Copy Path** - kopiuje ścieżkę do schowka (do otwarcia w edytorze)

## Dodawanie nowych elementów

### Przez UI
Dashboard jest tylko do przeglądania i zmiany statusów. Nowe elementy twórz ręcznie lub przez agenta.

### Przez agenta
```
Stwórz nową osobę: GSSP Kancelaria, Lead, kancelaria prawna
Stwórz nowy projekt: Research dla GSSP, powiązany z GSSP Kancelaria
```

### Ręcznie
```bash
# Nowa osoba
touch "pm/people/Person - Jan Kowalski.md"

# Nowy projekt
touch "pm/projects/Project - Nowy Projekt.md"

# Nowy task
touch "pm/tasks/Task - Zrób coś.md"
```

## API Endpoints

| Endpoint | Metoda | Opis |
|----------|--------|------|
| `/api/all` | GET | Wszystkie encje |
| `/api/people` | GET | Lista osób |
| `/api/projects` | GET | Lista projektów |
| `/api/tasks` | GET | Lista tasków |
| `/api/tasks/{id}` | PATCH | Zmiana statusu taska |
| `/api/projects/{id}` | PATCH | Zmiana statusu projektu |
| `/api/people/{id}` | PATCH | Zmiana statusu osoby |
| `/api/folder?path=X` | GET | Lista plików w folderze |
| `/api/file?path=X` | GET | Zawartość pliku |

## Integracja z tasks/

Projekty mogą mieć pole `folders:` wskazujące na foldery robocze w `tasks/`:

```yaml
folders:
  - tasks/2026-01-22-porter
  - tasks/2026-01-19-strategia-biznesu
```

Te foldery są widoczne w widoku szczegółów projektu - można przeglądać pliki bez opuszczania dashboardu.
