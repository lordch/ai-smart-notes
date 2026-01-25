# Meeting Notes → Action Items Agent

## Domena
Project Management / Operations / Any team

## Problem klienta
- Notatki ze spotkań to chaos: luźne zdania, mieszanka ustaleń i dyskusji
- Action items gubią się w tekście
- Niejasne przypisania ("ktoś powinien to zrobić")
- Deadline'y wspominane mimochodem, łatwo przeoczyć
- Po tygodniu nikt nie pamięta co ustalono

## Workflow agentowy
1. Agent wczytuje notatki ze spotkania (tekst, Word, PDF, nawet zdjęcie tablicy)
2. Identyfikuje:
   - Decyzje podjęte
   - Action items (zadania do wykonania)
   - Osoby odpowiedzialne (nawet jeśli wspomniane nieformalnie)
   - Deadline'y (nawet nieformalne: "do końca miesiąca")
   - Ryzyka / blocker'y
3. Generuje uporządkowany output:
   - Master task list z deadline'ami
   - Przypisania per osoba
   - Timeline / milestones
   - Open questions / decisions needed

## Przykładowy prompt
```
Review my meeting notes from the "Project Phoenix" folder and create:
1. Master task list with deadlines
2. Assignment by team member
3. Risk assessment (overlapping deadlines, unclear responsibilities)
4. Weekly milestone tracker

Rules for extraction:
- If someone says "I'll handle X" - assign to them
- If deadline mentioned casually ("by month-end", "next week") - convert to specific date
- If responsibility unclear ("someone should...") - flag as UNASSIGNED
- If dependency mentioned ("after X is done") - note the dependency

Output as Markdown with clear sections. Flag any conflicts or risks.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 30-60 min na przetworzenie notatek | 5 min |
| Action items gubią się | Wszystkie wyekstrahowane |
| "Ktoś miał to zrobić" | Jasne przypisania |
| Deadline'y zapomniane | Skonsolidowana lista |
| Brak visibility na konflikty | Automatyczne wykrywanie ryzyk |

## ROI / Metryki
- Czas: 45 min/spotkanie → 5 min (89% redukcja)
- Missed action items: spadek z ~20% do <5%
- Accountability: jasne przypisania = lepsza realizacja
- Project visibility: natychmiastowy status zamiast "muszę sprawdzić notatki"

## Wymagania wdrożeniowe
- Dane: notatki ze spotkań (dowolny format tekstowy)
- Narzędzia: Claude Code
- Complexity: **Low-Medium**
- Opcjonalnie: lista uczestników z rolami

## Warianty / Rozszerzenia
- Integracja z kalendarzem (tworzenie eventów dla deadline'ów)
- Sync z task manager (Asana, Trello, Linear)
- Automatyczne follow-up emails do assignees
- Weekly digest: "Te taski z poprzednich spotkań są overdue"
- Transkrypcja audio → notatki → action items (pełny pipeline)

---

## Wariant: Voice-to-Document Pipeline

### Kontekst (Matt Stockton)
Stockton używa Claude Code do przetwarzania nagrań audio w ustrukturyzowane dokumenty. Zamiast pisać notatki, nagrywa siebie opisującego co się stało na spotkaniu.

### Workflow
1. Nagranie audio (telefon, komputer) — chaotyczny opis spotkania
2. Transkrypcja (Whisper, inny tool)
3. Claude Code przetwarza transcript:
   - Rozpoznaje uczestników
   - Ekstrahuje decyzje i action items
   - Formatuje według template'u
4. Automatyczne zapisanie do work log + odpowiedniego folderu klienta

### Przykładowa komenda `/meeting-summary`
```
Read the transcript from my_recording.txt and create:
1. Meeting summary (3-5 bullet points)
2. Decisions made
3. Action items with owners and deadlines
4. Open questions for next meeting

Save to client_folder/meetings/YYYY-MM-DD-meeting.md
Update work_log.md with entry about this meeting.
```

### Czas
- Manual: 30 min na przetworzenie chaotycznych notatek
- Z agentem: 5 min (nagranie + review outputu)

### Źródło
[Matt Stockton - How I Use Claude Code for Non-Technical Work](https://mattstockton.com/2026/01/07/claude-code-for-non-technical-work.html)

---

## Źródła
- Nate B. Jones - Getting Started with Claude Code for Non-Coders
- [Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
