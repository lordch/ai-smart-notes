# User Feedback Triage Agent

## Domena
Product Management / Customer Success / UX Research

## Problem klienta
- Setki feedback items tygodniowo (app reviews, support tickets, sales notes)
- Manual categorization zajmuje godziny
- Trudno zobaczyć patterns w chaosie
- Roadmap tracking: łatwo przeoczyć slipping deadlines
- Feedback nie jest linked do roadmap items

## Workflow agentowy
1. Agent wczytuje feedback z różnych źródeł (CSV, text dumps)
2. Dla każdego feedback item:
   - Klasyfikuje: feature/component + sentiment (Positive/Neutral/Negative)
   - Ekstraktuje key issue/request
   - Mapuje do roadmap items (jeśli relevant)
3. Maintains running summary:
   - Top 5 recurring issues/requests (z counts)
   - Trends week-over-week
   - Critical issues (spike in negative feedback)
4. Roadmap tracking:
   - Czyta ProjectUpdates.txt (engineering status)
   - Cross-references z Roadmap.csv
   - Flaguje items at risk of delay
5. Output: weekly reports (feedback_report.md, roadmap_status.md)

## Przykładowy prompt
```
You are PM-Aide, an AI Product Management assistant.

Functions:
1) Feedback Triage - Continuously ingest user feedback from various sources.
   For each item:
   - Classify by feature/component and sentiment (Positive/Neutral/Negative)
   - Extract key issue or request
   - Map to relevant roadmap item if possible
   - Maintain top 5 recurring issues/requests each week (with counts)
   - Output weekly feedback_report.md with trends and critical issues

2) Roadmap Tracker - Using Roadmap.csv and ProjectUpdates.txt:
   - Identify items at risk of delay
   - Flag scope changes
   - Output roadmap_status.md: items due next month, on-track/delayed status, risks

Both reports persist and update weekly. Remember previous trends to see if issues persist or resolve.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| Hours reading feedback | Minutes reviewing summary |
| Inconsistent categorization | Systematic classification |
| Patterns hard to see | Trends automatically surfaced |
| Roadmap slips unnoticed | Early warning system |
| Feedback disconnected from roadmap | Automatic linking |

## ROI / Metryki
- Czas: 1 dzień/tydzień → 1 godzina (87% redukcja)
- Accuracy: manual tagging 50-70% → AI 90%+
- Coverage: reads every piece (no sampling bias)
- Early detection: catch roadmap risks before they become problems

## Wymagania wdrożeniowe
- Dane: Feedback sources (CSV/text), Roadmap.csv, ProjectUpdates.txt
- Narzędzia: Claude Code
- Complexity: **Medium**
- Setup: definicja kategorii/komponentów produktu

## Warianty / Rozszerzenia
- Integration z support tools (Zendesk, Intercom) - auto-import tickets
- Integration z app stores - auto-fetch reviews
- Sentiment analysis per feature over time
- User quote extraction (representative quotes w summary)
- Predictive: "If this trend continues, churn risk increases"

## Real Examples
- **Clay**: Used Claude internally to categorize customer feedback - manual tagging had 50-70% accuracy, AI does it more accurately and tirelessly
- **Anthropic product teams**: Used Claude to map error states and logic flows during design, saving hours of later debugging

## Pro Tip
Close the loop: use agent output to drive action. If "Android performance" is red flag 2 weeks in a row, bring to sprint planning with concrete data. Track if complaint volume drops after fixes.

## Źródło
"Claude Code Isn't for Code" - Product section
