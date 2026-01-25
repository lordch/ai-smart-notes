# Contract Review Agent

## Domena
Legal / Procurement / Operations

## Problem klienta
- Każda nowa umowa wymaga szczegółowego review (1-2h per kontrakt)
- Porównanie z template'em firmy jest żmudne
- Łatwo przeoczyć nietypowe klauzule gdy reviewer jest zmęczony
- Niespójność: różni reviewerzy flagują różne rzeczy
- Stack 10 kontraktów = 10-20 godzin pracy

## Workflow agentowy
1. Agent wczytuje firmowy template kontraktu (standard clauses)
2. Wczytuje nowy kontrakt do review
3. Dzieli na sekcje (Parties, Payment, Termination, Liability, etc.)
4. Dla każdej sekcji:
   - Porównuje z template'em
   - Flaguje odchylenia od standardu
   - Ocenia ryzyko odchylenia (Low/Medium/High)
5. Identyfikuje:
   - Brakujące klauzule
   - Nietypowe zapisy nieobecne w template
   - Potencjalnie problematyczne sformułowania
6. Generuje raport z Overall Risk Assessment

## Przykładowy prompt
```
You are a Contract Analysis Agent. Compare contracts against our standard template.

For each contract I provide:
1. Identify main sections: Parties, Payment Terms, Termination, Liability, IP, Confidentiality, Indemnification
2. Extract the text of each section
3. Compare with our standard clause language from template.txt
4. Flag deviations:
   - CRITICAL: liability caps, indemnification, IP ownership
   - HIGH: payment terms, termination rights
   - MEDIUM: notice periods, governing law
   - LOW: formatting, minor wording differences
5. Note any unusual clauses not in our template
6. Provide Overall Risk Rating (Low/Medium/High/Critical)

Output structured report. For each deviation, explain:
- What our standard says
- What this contract says
- Why it matters
- Recommended action (accept/negotiate/reject)
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 1-2h per kontrakt | 10-15 min (review agent output) |
| Reviewer fatigue = missed issues | Consistent thoroughness |
| Każdy reviewer inaczej | Jednolite kryteria |
| Notes w marginesach | Strukturalny raport |
| 10 kontraktów = 20h | 10 kontraktów = 2h review |

## ROI / Metryki
- Czas: 90% redukcja (2h → 15 min per kontrakt)
- Consistency: 100% (te same kryteria zawsze)
- Missed clauses: spadek do ~0% (agent sprawdza wszystko)
- Risk reduction: wcześniejsze wykrywanie problematycznych zapisów

## Wymagania wdrożeniowe
- Dane: firmowy template kontraktu, kontrakty do review (PDF/Word)
- Narzędzia: Claude Code
- Complexity: **Medium-High**
- Setup: definicja kryteriów oceny ryzyka

## Warianty / Rozszerzenia
- Sugerowanie alternatywnych sformułowań dla problematycznych klauzul
- Database poprzednich kontraktów (jak negocjowaliśmy podobne zapisy)
- Integration z document management system
- Batch processing wielu kontraktów
- Tracking: które klauzule najczęściej negocjujemy

## Failure Modes (uwaga!)
- Niekompletny template = agent nie wie co sprawdzać
- Niestandardowe formatowanie kontraktu może utrudnić parsing
- Subtelności prawne wymagają human review
- Agent to first-pass screening, nie zastępuje prawnika

## Źródło
"Claude Code Isn't for Code" - Legal section
Real example: Anthropic lawyers built custom tools without dev resources
