# @pm - Project Management Dashboard

Uruchamia lokalny serwer z dashboardem do zarządzania projektami.

## Użycie

```
@pm
```

## Co robi

1. Instaluje zależności (jeśli potrzeba)
2. Uruchamia serwer FastAPI na porcie 8787
3. Dashboard: http://localhost:8787

## Instrukcja dla agenta

Gdy użytkownik wywoła `@pm`:

1. Sprawdź czy serwer już działa:
   ```bash
   curl -s http://localhost:8787/api/all > /dev/null 2>&1 && echo "running" || echo "not running"
   ```

2. Jeśli nie działa, zainstaluj zależności i uruchom:
   ```bash
   venv/bin/pip install -q -r .cursor/skills/pm/requirements.txt
   venv/bin/python .cursor/skills/pm/server.py &
   ```

3. Poinformuj użytkownika:
   > **Dashboard:** http://localhost:8787
   >
   > **Widoki:**
   > - **Tasks** - Kanban z drag & drop
   > - **Projects** - Pipeline projektów z podpiętymi folderami
   > - **People** - Pipeline relacji (Lead → Client)
   >
   > **Nawigacja:**
   > - Klik w kartę → widok szczegółów z renderowanym markdown
   > - Foldery projektu → przeglądanie plików z podglądem
   > - Copy Path → kopiuje ścieżkę do schowka

## Struktura danych

```
pm/
├── people/      # Person - {Nazwa}.md
├── projects/    # Project - {Nazwa}.md
├── tasks/       # Task - {Nazwa}.md
└── README.md    # Pełna dokumentacja
```

## Inne komendy

| Komenda | Opis |
|---------|------|
| `@pm status` | Pokaż ile jest osób, projektów, tasków |
| `@pm add person {Nazwa}` | Stwórz nową osobę |
| `@pm add project {Nazwa}` | Stwórz nowy projekt |
| `@pm add task {Nazwa}` | Stwórz nowy task |

## Zatrzymanie

```bash
pkill -f "pm/server.py"
```

Lub Ctrl+C w terminalu.
