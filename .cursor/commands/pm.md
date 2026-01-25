# @pm - Project Management Dashboard

Uruchamia lokalny serwer z dashboardem do zarządzania projektami.

## Użycie

```
@pm
```

## Co robi

1. Sprawdza czy zależności są zainstalowane
2. Uruchamia serwer FastAPI na porcie 8787
3. Otwiera dashboard w przeglądarce

## Instrukcja dla agenta

Gdy użytkownik wywoła `@pm`:

1. Sprawdź czy venv istnieje i ma zainstalowane zależności:
   ```bash
   venv/bin/pip install -r .cursor/skills/pm/requirements.txt
   ```

2. Uruchom serwer:
   ```bash
   venv/bin/python .cursor/skills/pm/server.py
   ```

3. Poinformuj użytkownika:
   > Dashboard dostępny pod: http://localhost:8787
   >
   > - **Tasks**: Kanban z taskami (drag & drop)
   > - **People**: Pipeline osób (Lead → Client)
   > - **Projects**: Lista projektów
   >
   > Kliknij kartę aby skopiować ścieżkę do pliku.

## Zatrzymanie

Ctrl+C w terminalu lub zamknij terminal.
