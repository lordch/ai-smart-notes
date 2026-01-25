# Customer Database Cleanup Agent

## Domena
Sales / CRM / Operations

## Problem klienta
- Dane klientów rozrzucone po wielu plikach (Excel, CSV, exporty z różnych systemów)
- Duplikaty: ten sam klient w różnych wariantach nazwiska/maila
- Niekompletne rekordy (brak telefonu, nieprawidłowy email)
- Niespójne formaty (daty, telefony, adresy)
- Nieaktualne statusy (klient oznaczony jako "active" mimo braku kontaktu od 2 lat)

## Workflow agentowy
1. Agent wczytuje wszystkie źródła danych (CSV, Excel)
2. Identyfikuje duplikaty po: email, telefon, nazwa firmy + osoba
3. Merguje duplikaty, zachowując najnowsze/najpełniejsze dane
4. Waliduje formaty:
   - Email: sprawdza poprawność składni
   - Telefon: ujednolica format
   - Data: konwertuje do YYYY-MM-DD
5. Flaguje niekompletne rekordy
6. Aktualizuje statusy na podstawie last_contact_date
7. Segmentuje: Active / Prospects / Needs Follow-up / Inactive
8. Eksportuje czystą bazę + raport jakości danych

## Przykładowy prompt
```
I have three files with customer data: customers-2024.csv, prospects.csv, and client-contacts.xlsx.

Combine them into one clean database:
1. Remove duplicates (match by email, phone, or company+name)
2. Validate email format (flag invalid ones)
3. Standardize phone numbers to +XX XXX XXX XXX format
4. Use MM/DD/YYYY for dates
5. Mark customers with no contact in 90+ days as "Needs Follow-up"
6. Mark customers with no contact in 365+ days as "Inactive"

Create separate sheets for:
- Active customers (contact within 90 days)
- Prospects (never purchased)
- Contacts needing follow-up (90-365 days)
- Inactive (365+ days)

Output summary: total contacts, duplicates removed, invalid emails found, status breakdown.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 1-2 dni na merge i cleanup | 30 minut |
| ~85-90% accuracy (błędy ludzkie) | 100% consistency |
| Duplikaty zostają niezauważone | Wszystkie wykryte |
| Ręczne sprawdzanie emaili | Automatyczna walidacja |
| Statusy nieaktualne | Auto-update na podstawie dat |

## ROI / Metryki
- Czas: 8-16h → 30 min (97% redukcja)
- Accuracy: 85% → 99%+
- Duplikaty: typowo 5-15% bazy to duplikaty
- Dane do follow-up: odkrycie "zapomnianych" leadów

## Wymagania wdrożeniowe
- Dane: pliki CSV/Excel z danymi klientów
- Narzędzia: Claude Code
- Complexity: **Medium**
- Dodatkowe: definicja co oznacza "duplikat" w kontekście firmy

## Warianty / Rozszerzenia
- Scheduled weekly cleanup (utrzymanie jakości)
- Enrichment: dodawanie danych z LinkedIn, company info
- Integration z CRM API (Hubspot, Salesforce)
- Scoring: automatyczne przypisywanie lead score
- GDPR compliance: identyfikacja rekordów do usunięcia

## Źródło
Nate B. Jones - Getting Started with Claude Code for Non-Coders
