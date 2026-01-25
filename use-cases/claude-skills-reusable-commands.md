# Claude Skills / Reusable Commands Agent

## Domena
Productivity / Automation / Any repetitive workflow

## Problem klienta
- Ad-hoc workflows działają, ale trzeba je za każdym razem opisywać
- CLAUDE.md rośnie w nieskończoność (wszystko w jednym pliku)
- Instrukcje rozproszone, trudne do utrzymania
- Brak standaryzacji między projektami
- "Jak ja to ostatnio zrobiłem?" — odtwarzanie workflow

## Kluczowy insight

> **Skill = markdown file z instrukcjami**, który Claude Code może załadować jako slash command (`/meeting-summary`, `/code-review`, etc.)

## Workflow agentowy

### Faza 1: Interactive prototyping
1. Opisujesz agentowi co chcesz osiągnąć
2. Agent eksperymentuje, pyta o feedback
3. Iterujecie aż output jest zadowalający
4. Agent "nauczył się" workflow

### Faza 2: Konwersja do skill
1. Zapisanie instrukcji do markdown file
2. Dodanie jako slash command
3. Testowanie na nowych danych
4. Refinement na podstawie edge cases

### Faza 3: Reuse
1. `/skill-name` uruchamia workflow
2. Spójne wyniki za każdym razem
3. Możliwość udostępnienia team members

## Przykładowa struktura skill

```markdown
# /meeting-summary

## Purpose
Convert meeting recordings/transcripts into structured summaries.

## Input
- Audio transcript (text file)
- Meeting context (optional: attendees, topic)

## Process
1. Read transcript from provided file
2. Identify participants (from dialogue patterns)
3. Extract:
   - Key decisions made
   - Action items with owners
   - Open questions
   - Next steps
4. Format according to template below

## Output template
```
## Meeting Summary: [Topic]
**Date**: [extracted or today]
**Attendees**: [list]

### Key Decisions
- [decision 1]
- [decision 2]

### Action Items
| Owner | Task | Deadline |
|-------|------|----------|
| ... | ... | ... |

### Open Questions
- [question 1]

### Next Steps
- [step 1]
```

## Rules
- If deadline mentioned casually ("next week"), convert to specific date
- If owner unclear, mark as "TBD"
- Keep summary concise (max 1 page)
```

## Before / After
| Bez skills | Ze skills |
|------------|-----------|
| Opisywanie workflow za każdym razem | `/command` i gotowe |
| Niespójne wyniki | Standaryzowany output |
| CLAUDE.md = wszystko | Modular, organized |
| Tylko Ty wiesz jak | Team może używać |
| Trudne do utrzymania | Wersjonowane w git |

## ROI / Metryki
- Setup time per task: minuty (opisywanie) → sekundy (slash command)
- Consistency: 100% zgodność z template
- Onboarding: team member może używać od razu
- Maintenance: zmiany w jednym miejscu

## Wymagania wdrożeniowe
- Narzędzia: Claude Code ze Skills feature
- Dane: instrukcje zapisane jako markdown
- Complexity: **Low** (basic) / **Medium** (advanced skills)
- Repozytorium skills (folder lub centralne repo)

## Przykłady skills

| Skill | Opis |
|-------|------|
| `/meeting-summary` | Transcript → structured notes |
| `/code-review` | Review code with specific guidelines |
| `/commit` | Generate commit message from diff |
| `/weekly-status` | Generate status update from work logs |
| `/client-email` | Draft email in client's preferred style |
| `/doc-template` | Generate document from template |

## Warianty / Rozszerzenia
- Shared skills repository (team-wide)
- Parameterized skills (`/email --tone=formal`)
- Chained skills (`/meeting → /action-items → /calendar`)
- Analytics: "Które skills używam najczęściej?"

## Failure Modes (uwaga!)
- Over-engineering: zbyt skomplikowane skills
- Outdated: skill nie nadąża za zmianami w workflow
- Too rigid: brak flexibility dla edge cases
- Naming conflicts: spójne nazewnictwo jest ważne

## Źródło
[Matt Stockton - Claude Skills: Organization for Agent Instructions](https://mattstockton.com/2025/10/17/claude-skills-better-organization-for-agent-instructions.html)
[Matt Stockton - How I Prototype Agentic Workflows Before Writing Code](https://mattstockton.com/2025/11/25/how-i-prototype-agentic-workflows.html)
[Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
