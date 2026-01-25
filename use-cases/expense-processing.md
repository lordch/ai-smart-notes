# Expense Processing Agent

## Domena
Finance / Accounting / Small Business

## Problem klienta
- Ręczne kategoryzowanie wydatków z wyciągów bankowych
- Przygotowanie do rozliczeń podatkowych zajmuje dni
- Brak widoczności w strukturę wydatków
- Łatwo przeoczyć wydatki do odliczenia
- Porównania month-over-month wymagają ręcznych obliczeń

## Workflow agentowy
1. Agent wczytuje CSV z wyciągu bankowego
2. Dla każdej transakcji: kategoryzuje (Office Supplies, Travel, Meals, etc.)
3. Identyfikuje wydatki tax-deductible
4. Generuje raport miesięczny:
   - Suma per kategoria
   - Porównanie z poprzednim miesiącem
   - Największe wydatki do review
   - Lista wydatków do odliczenia
5. Tworzy wykresy pokazujące trendy
6. Zapisuje do Excel z osobnymi arkuszami

## Przykładowy prompt
```
Process my bank statement CSV and categorize all expenses. Create a monthly report showing:
- Total spending by category
- Comparison to last month  
- Largest expenses that need review
- Tax-deductible items separated

Categories to use:
- Office Supplies
- Software & Subscriptions
- Travel
- Business Meals (with client)
- Personal Meals (not deductible)
- Professional Services
- Marketing
- Other

For meals, if description contains "client" or known client names, mark as Business Meals.
Output as Excel with separate sheets for summary, details, and tax-deductible items.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 4-6h miesięcznie na kategoryzację | 15 min review |
| Przygotowanie do podatków: 2-3 dni | 1 godzina |
| Brak porównań month-over-month | Automatyczne trendy |
| Łatwo przeoczyć odliczenia | Agent wyłapuje wszystkie |
| Niespójne kategorie | Jednolita kategoryzacja |

## ROI / Metryki
- Czas: 6h/miesiąc → 30 min (92% redukcja)
- Znalezione odliczenia: często 5-15% więcej niż manualnie
- Błędy kategoryzacji: spadek z ~10% do <2%
- Przygotowanie do podatków: dni → godziny

## Wymagania wdrożeniowe
- Dane: CSV/Excel z wyciągami bankowymi
- Narzędzia: Claude Code
- Complexity: **Low-Medium**
- Opcjonalnie: lista klientów do rozpoznawania business meals

## Warianty / Rozszerzenia
- Integracja z API banku (automatyczny import)
- Połączenie z systemem faktur (matchowanie płatności)
- Alerty: "Wydatki na X przekroczyły budżet"
- Forecasting: przewidywanie wydatków na kolejny miesiąc
- Multi-currency support dla międzynarodowych transakcji

## Źródło
Nate B. Jones - Getting Started with Claude Code for Non-Coders
