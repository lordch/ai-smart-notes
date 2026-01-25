# Automated Monthly Reports Agent

## Domena
Finance / Operations / Executive reporting

## Problem klienta
- Comiesięczne raporty zajmują 4-8 godzin
- Dane z wielu źródeł: CRM, accounting, spreadsheets
- Powtarzalna praca: te same kroki co miesiąc
- Łatwo o błąd przy ręcznym kopiowaniu danych
- Formatowanie i wykresy pochłaniają czas
- Opóźnienia w raportach = opóźnione decyzje

## Workflow agentowy
1. Agent wczytuje dane z określonych źródeł:
   - Sales data z CRM export (CSV)
   - Expense data z accounting (CSV)
   - KPIs z innych spreadsheetów
2. Przetwarza i agreguje:
   - Revenue trends
   - Expense breakdown
   - Key metrics vs targets
   - Month-over-month comparison
3. Generuje:
   - Executive summary (kluczowe insights w 3-5 bullet points)
   - Szczegółowe tabele z danymi
   - Wykresy trendów
   - Alerts: co wymaga uwagi
4. Formatuje jako profesjonalny PDF/Excel
5. Zapisuje proces do powtórzenia następnego miesiąca

## Przykładowy prompt
```
Create an automated monthly report system that:
1. Reads sales data from sales_export.csv (columns: date, client, amount, product)
2. Processes expense data from accounting.csv (columns: date, category, amount, vendor)
3. Generates:
   - Revenue by product line
   - Revenue by client (top 10)
   - Expense breakdown by category
   - Net margin calculation
   - Month-over-month trends
4. Creates executive summary (3-5 key insights)
5. Highlights anything unusual:
   - Revenue drop >10% vs last month
   - Any category expense spike >20%
   - Top clients with declining spend
6. Outputs as Excel with charts + PDF executive summary

Save this as a reusable workflow I can run each month with new data files.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 4-8h na raport miesięczny | 30 min (data prep + review) |
| Błędy przy copy-paste | Zero błędów w kalkulacjach |
| Subiektywne "insights" | Systematyczna analiza |
| Opóźnienia w delivery | Raport gotowy w minuty |
| Formatowanie zajmuje czas | Automatyczne formatowanie |

## ROI / Metryki
- Czas: 6h/miesiąc → 30 min (92% redukcja)
- Accuracy: eliminacja błędów ręcznych
- Timeliness: raport 5. dnia miesiąca zamiast 15.
- Insights: systematyczne wykrywanie anomalii

## Wymagania wdrożeniowe
- Dane: regularne exporty z systemów (CSV/Excel)
- Narzędzia: Claude Code
- Complexity: **Medium**
- Setup: jednorazowy (template do reużycia)

## Warianty / Rozszerzenia
- Scheduled execution (automatyczne uruchomienie 1. dnia miesiąca)
- Email distribution do stakeholders
- Dashboard zamiast static report
- Forecasting: przewidywanie następnego miesiąca
- Drill-down reports per department/region

---

## Wariant: Interactive Dashboards (Streamlit)

### Kontekst (Matt Stockton)
Zamiast statycznych raportów, Stockton buduje interaktywne dashboardy Streamlit dla klientów small/medium business. Claude Code generuje cały kod dashboardu.

### Kiedy dashboard zamiast raportu?
- Stakeholder potrzebuje filtrowania i drill-down
- Dane zmieniają się częściej niż miesięcznie
- Różni użytkownicy patrzą na różne widoki
- "What if" analysis

### Workflow
1. Rozmowa ze stakeholderem: "Pokaż mi jak dziś budujesz ten raport"
2. Exploratory data analysis — Claude pisze pandas kod, szuka outlierów
3. Claude generuje Streamlit app z:
   - Interaktywne filtry (daty, kategorie, klienci)
   - Wykresy z drill-down
   - Summary metrics na górze
   - Export do CSV/Excel
4. Iteracja na podstawie feedbacku

### Przykładowy prompt
```
Build a Streamlit dashboard for sales data analysis:
1. Load sales_data.csv
2. Create date range filter (sidebar)
3. Create product category filter (multiselect)
4. Show KPIs at top: Total Revenue, Avg Order Value, Top Customer
5. Chart 1: Revenue over time (line)
6. Chart 2: Revenue by category (bar)
7. Table: Top 10 customers with drill-down
8. Export filtered data to CSV button

Use clean styling. Add caching for performance.
```

### Target audience
- Small/medium business z targeted reporting needs
- Ktoś techniczny może zwalidować SQL i business logic
- Stakeholderzy bez technical skills mogą korzystać

### Źródło
[Matt Stockton - How I Build Dashboards Now with Claude Code](https://mattstockton.com/2026/01/06/custom-dashboards-with-claude-code.html)

---

## Źródła
- Nate B. Jones - Getting Started with Claude Code for Non-Coders
- [Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
