# HR Policy Q&A Bot

## Domena
HR / People Operations / Employee Support

## Problem klienta
- HR staff odpowiada na te same pytania wielokrotnie
- 50+ stronicowy handbook - trudno znaleźć odpowiedź
- Employees czekają godzinami/dniami na odpowiedź
- Niespójność: różni HR reps dają różne odpowiedzi
- Onboarding: nowi pracownicy gubią się w procesie

## Workflow agentowy
1. Agent wczytuje Employee Handbook (policy documents)
2. Dla pytań employees:
   - Szuka odpowiedzi w handbook
   - Cytuje konkretną sekcję
   - Jeśli niepewny - odsyła do HR person
3. Dla onboarding:
   - Prowadzi interaktywny proces krok po kroku
   - Odpowiada na pytania w trakcie
   - Trackuje completed tasks per employee
   - Persistuje progress między sesjami
4. Loguje unanswered questions dla HR review

## Przykładowy prompt
```
You are Hal, the HR Assistant AI for our company.

Roles:
A) Policy Q&A - Answer employee questions about HR policies (leave, travel, expenses, benefits) 
   based on employee_handbook.txt. Be accurate. If uncertain, say so or refer to HR person.

B) Onboarding Guide - For new hires:
   - Provide step-by-step onboarding plan from onboarding_checklist.csv
   - Answer questions about each step
   - Mark tasks as done when employee confirms
   - Track progress per employee (by email as ID)
   - Remember where they left off between sessions

Constraints:
- No confidential employee data exposure
- Log unanswered questions to unanswered_questions.txt
- If policy question not in handbook, defer to HR

Use persistent memory: remember completed onboarding tasks and policy clarifications.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| Employees czekają godzinami | Instant 24/7 answers |
| HR staff repeat same answers | Freed from routine Q&A |
| Inconsistent answers | Single source of truth |
| Onboarding: długie manuale | Interactive guided process |
| Manual task tracking | Automated tracking |
| Scaling = hire more HR | AI scales infinitely |

## ROI / Metryki
- Response time: hours/days → instant
- HR time saved: thousands of hours (Brex example: expense policy enforcement)
- Employee satisfaction: "HR is so responsive now"
- Compliance: proactive warnings before policy violations

## Wymagania wdrożeniowe
- Dane: Employee Handbook (text file), Onboarding Checklist
- Narzędzia: Claude Code
- Complexity: **Medium**
- Integration: Slack/Teams (opcjonalnie, dla chat interface)

## Warianty / Rozszerzenia
- Integration z HRIS (automatyczne update statusów)
- Multi-language support
- Scheduled reminders ("Complete your training by Friday")
- Analytics: what questions are asked most (insights dla HR)
- Proactive notifications: "Your PTO balance is low"

## Real Examples
- **Anthropic**: Integrated Claude into Slack for operational knowledge sharing - field technicians ask about safety protocols, get instant answers
- **Brex**: Finance teams upload policy documents, AI interprets for expense approvals - people don't translate policies into code

## Źródło
"Claude Code Isn't for Code" - HR section
