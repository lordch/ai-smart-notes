# Lead Enrichment & Outreach Agent

## Domena
Sales / Business Development / RevOps

## Problem klienta
- Research leadów zajmuje 10-15 min per lead
- Personalizacja emaili wymaga czasu (5 min per email)
- Przy 50+ leadach = 2-3 dni pracy
- Łatwo o błędy przy copy-paste personalizacji
- Follow-up'y często zapominane

## Workflow agentowy
1. Agent wczytuje CSV z leadami (Name, Company, Title, LinkedIn URL)
2. Dla każdego leada:
   - Web search: recent company news, funding, milestones
   - LinkedIn: recent posts, content, activity
   - Enrichment: infer location from phone, validate emails
3. Generuje personalized email (100-150 words):
   - References specific company news
   - Mentions lead's content/posts
   - Ties to product value prop
   - Unique dla każdego leada
4. Tworzy CRM note (TL;DR dla wewnętrznych rekordów)
5. Output: CSV z emailami + notes

## Przykładowy prompt
```
You are an AI Sales Assistant that takes raw lead lists and turns them into personalized outreach.

Workflow:
1. Read leads.csv (columns: Name, Company, Title, LinkedIn URL, Email)
2. For each lead:
   - Search web for recent company news (funding, product launches, milestones)
   - If LinkedIn URL provided, summarize their recent posts/activity
   - Validate email format
3. Generate personalized email (100-150 words):
   - Reference specific company news or milestone
   - Mention something from their LinkedIn content
   - Tie to our product value prop
   - Professional but friendly tone
4. Create one-sentence CRM note: who they are, what they might need
5. Output CSV with: Name, Company, Personalized Email, CRM Note

Ensure no two emails are identical. Make them genuinely personalized.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| 10-15 min research per lead | Automatyczny research w sekundach |
| 5 min per email writing | 60 emails w 2 minuty |
| 2-3 dni na 60 leadów | 30 min total (run + review) |
| Copy-paste errors | Zero błędów |
| Follow-ups manual | Można zautomatyzować |

## ROI / Metryki
- Czas: 15-20h → 30 min (97% redukcja)
- Real case (Steve Kaplan): 63 contacts w <30 min, saved $500-1000 outsourcing costs
- Accuracy: 100% correctness vs 85-90% manual
- Response rates: Clay users report Claude emails sound "more human and natural"

## Wymagania wdrożeniowe
- Dane: CSV z leadami (min: Name, Company, Email)
- Narzędzia: Claude Code + web search access
- Complexity: **Medium**
- Opcjonalnie: LinkedIn API access (lub manual paste content)

## Warianty / Rozszerzenia
- Integration z CRM (Hubspot, Salesforce) - auto-create records
- Email sending automation (z safeguards)
- Follow-up sequences (scheduled reminders)
- Lead scoring: prioritize based on company size, funding, role
- Multi-channel: LinkedIn messages + emails

## Real Case Studies
- **Clay**: "Claygent" scrapes web for prospect thought leadership, generates highly personalized emails. Users report better response rates.
- **Steve Kaplan**: Automated 63 sales contacts, 100% accuracy in data merge, saved 15-20 hours.

## Źródło
"Claude Code Isn't for Code" - Sales section
