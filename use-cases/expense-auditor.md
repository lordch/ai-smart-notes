# Expense Auditor Agent

## Domena
Finance / Accounting / Compliance

## Problem klienta
- Audit expense reports zajmuje godziny (tylko spot-checking możliwy)
- Policy compliance trudna do enforce'owania przy 100% coverage
- Manual review = human fatigue = missed violations
- Non-technical finance staff nie może wykonać complex analysis
- Ad-hoc questions ("Q2 travel spend vs budget?") wymagają IT/data team

## Workflow agentowy
1. Agent wczytuje Expense Policy document (plain English)
2. Wczytuje expense reports (CSV/Excel)
3. Dla każdego line item:
   - Sprawdza compliance z policy
   - Flaguje violations (over limits, missing receipts, wrong categories)
   - Ocenia risk level
4. Generuje audit summary:
   - Compliance score per report
   - Lista violations z explanations
   - Overall company compliance %
5. Financial Q&A mode: odpowiada na natural language questions o danych

## Przykładowy prompt
```
You are FinAssist, an AI finance analyst.

Roles:
1) Expense Auditor - Continuously audit expense reports for policy compliance.
   - Read ExpensePolicy.txt and expense_report.csv
   - Flag violations: over spending limits, missing receipts (>$25), out-of-policy categories
   - Produce audit summary with compliance score per report
   - Explain each violation

2) Financial Q&A - Answer finance questions using provided data files.
   - Users ask in natural language: "Show Q2 travel spend by department vs budget"
   - Translate to computation, perform calculations
   - Output clearly with assumptions noted
   - Use DataDict.txt for account code meanings

Keep persistent memory of definitions. Log all queries to fin_assist_log.txt.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| Spot-checking only (10-20% coverage) | 100% coverage |
| 1-2h per report review | 5-10 min per report |
| Human fatigue = missed violations | Consistent thoroughness |
| Policy changes = manual retraining | Update text file = done |
| Ad-hoc analysis: wait for IT | Self-service Q&A |

## ROI / Metryki
- Real example (Brex): 94% compliance rate vs 70% industry standard
- 75% of expense reports automated
- 169,000 hours/month saved across customers
- 100% transaction review with AI anomaly detection

## Wymagania wdrożeniowe
- Dane: Expense Policy (text), Expense Reports (CSV/Excel), Budget data
- Narzędzia: Claude Code
- Complexity: **Medium**
- Security: sensitive financial data - use .claudeignore, isolated environment

## Warianty / Rozszerzenia
- Integration z accounting system (automatyczny import)
- Proactive warnings: "This purchase might violate policy" before submission
- Multi-currency support
- Receipt OCR validation
- Trend analysis: "Travel expenses up 20% this quarter"

## Failure Modes (uwaga!)
- Policy grey areas ("reasonable meals") - need clear definitions
- Statistical/logical errors - always human review important outputs
- Security: financial data is sensitive - proper access controls critical

## Real Case Study
**Brex**: Finance teams upload policy documents directly, AI interprets for expense approvals. "Finance teams with no coding experience can now execute complex data workflows independently."

## Źródło
"Claude Code Isn't for Code" - Finance section
