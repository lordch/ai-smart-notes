# File Organization Agent

## Domena
Operations / Personal Productivity

## Problem klienta
- Foldery pełne nieuporządkowanych plików (Downloads, Desktop, projekty)
- Manualne sortowanie: 2-4 godziny tygodniowo
- Niespójne nazewnictwo plików
- Trudność w znajdowaniu dokumentów
- Pliki giną w chaosie

## Workflow agentowy
1. Agent skanuje wskazany folder
2. Czyta zawartość każdego pliku (PDF, Word, Excel)
3. Rozpoznaje typ dokumentu po treści (faktura, umowa, raport, notatka)
4. Tworzy strukturę folderów (np. Invoices/, Contracts/, Reports/)
5. Przenosi pliki do odpowiednich folderów
6. Opcjonalnie: zmienia nazwy na spójny format (data + typ + opis)
7. Generuje raport: "Przeniesiono 15 faktur, 8 paragonów, 3 umowy"

## Przykładowy prompt
```
Organize my Downloads folder - move all invoices to an Invoices folder, 
receipts to Receipts, and contracts to Contracts. 

For each file:
1. Read the content to determine document type
2. Create target folder if it doesn't exist
3. Rename to format: YYYY-MM-DD_Type_Description.ext
4. Move to appropriate folder
5. Report what was done

Never delete original files - always create copies first.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 2-4h tygodniowo na sortowanie | 5-10 minut na uruchomienie + review |
| Niespójne nazewnictwo | Jednolity format nazw |
| Pliki gubią się w chaosie | Wszystko w logicznych folderach |
| Wymaga dyscypliny (często odkładane) | Agent robi to automatycznie |

## ROI / Metryki
- Czas: 2-4h/tydzień → 10 min/tydzień (90% redukcja)
- Znajdowanie plików: minuty → sekundy
- Stres: znacząca redukcja "cyfrowego bałaganu"

## Wymagania wdrożeniowe
- Dane: dostęp do folderu z plikami
- Narzędzia: Claude Code z dostępem do file system
- Complexity: **Low** - dobry na start

## Warianty / Rozszerzenia
- Automatyczne uruchamianie co tydzień (scheduled task)
- Integracja z cloud storage (Dropbox, Google Drive)
- Rozpoznawanie klientów po treści i tworzenie folderów per-klient
- OCR dla skanowanych dokumentów
- Archiwizacja starszych plików (>1 rok) do osobnego folderu

## Źródło
Nate B. Jones - Getting Started with Claude Code for Non-Coders
