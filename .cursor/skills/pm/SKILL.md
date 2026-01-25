# Skill: Project Management Dashboard

Lokalny system zarządzania projektami z interaktywnym UI w przeglądarce.

## Uruchomienie

```bash
# Instalacja zależności (jednorazowo)
venv/bin/pip install -r .cursor/skills/pm/requirements.txt

# Uruchomienie serwera
venv/bin/python .cursor/skills/pm/server.py
```

**Dashboard:** http://localhost:8787

## Struktura danych

```
pm/
├── people/      # Osoby (klienci, partnerzy, leady, network)
├── projects/    # Projekty (klienckie i wewnętrzne)
├── tasks/       # Zadania (Kanban)
└── README.md    # Pełna dokumentacja
```

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
Kontekst, historia.
```

**Role:**
- `Client` — płacący klient
- `Partner` — współpraca, referrale
- `Lead` — potencjalny klient w rozmowach
- `Network` — kontakt, może kiedyś

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
  - tasks/2026-01-XX-nazwa
---

# Nazwa Projektu

## Why this matters
Dlaczego ten projekt jest ważny.

## Cel
Co chcemy osiągnąć.

## Deliverables
- Deliverable 1
- Deliverable 2
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

Opis zadania.
```

## UI Features

### Widoki

1. **Tasks (Kanban)** — 4 kolumny: Todo, In Progress, Blocked, Done
2. **Projects** — 4 kolumny: Backlog, Active, On Hold, Done
3. **People (Pipeline)** — 4 kolumny: Lead, Partner, Network, Client

### Nawigacja

- **Klik w kartę** → pełnoekranowy widok szczegółów
- **Widok szczegółów** → lewa strona: opis (renderowany markdown), prawa: foldery i pliki
- **Klik w folder** → lista plików
- **Klik w plik** → podgląd z renderowanym markdown
- **Copy Path** → kopiuje ścieżkę do schowka
- **Back** → powrót do poprzedniego widoku

### Drag & Drop

- Przeciągnij kartę między kolumnami → status w pliku się aktualizuje

### Filtry (Tasks)

- Filtruj po osobie
- Filtruj po projekcie

## Integracja z tasks/

Projekty mogą mieć pole `folders:` wskazujące na foldery robocze:

```yaml
folders:
  - tasks/2026-01-22-porter
  - tasks/2026-01-19-strategia
```

Pliki z tych folderów są przeglądane bezpośrednio w dashboardzie.

## API

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

## Komenda

```
@pm
```

Uruchamia serwer i informuje o dostępności dashboardu.
