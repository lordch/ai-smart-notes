# Document Synthesis Agent

## Domena
Document Processing / Research / Report Generation

## Problem klienta
- Wiele źródeł do skonsolidowania w jeden raport
- Manual copy-paste + reformatowanie zajmuje godziny
- Trudność w utrzymaniu spójnej struktury
- Informacje rozsiane po różnych dokumentach
- "Znajdź wszystkie wzmianki o X w tych 15 plikach"

## Workflow agentowy

### Multi-pass processing

1. **Pass 1: Distillation**
   - Agent czyta wszystkie źródła
   - Ekstrahuje relevant information
   - Tworzy intermediate notes

2. **Pass 2: Organization**
   - Grupuje information by topic/section
   - Identyfikuje gaps i overlaps
   - Flaguje konflikty między źródłami

3. **Pass 3: Synthesis**
   - Pisze final document według template
   - Łączy information z wielu źródeł w coherent narrative
   - Dodaje citations/references

4. **Pass 4: Polish**
   - Formatting, consistency
   - Fact-checking (cross-reference)
   - Executive summary

## Przykładowy prompt
```
Synthesize a market analysis report from these sources:
- competitor_analysis.pdf
- market_research_2024.xlsx
- customer_interviews/folder (5 transcripts)
- industry_report.pdf

Template structure:
1. Executive Summary (1 page)
2. Market Overview
3. Competitor Landscape
4. Customer Insights
5. Opportunities & Threats
6. Recommendations

Rules:
- Cite sources for all claims
- Flag contradicting information
- Highlight data gaps
- Use tables for comparisons
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| Godziny na czytanie wszystkiego | Agent czyta parallel |
| Manual note-taking | Automated extraction |
| Trudność w cross-reference | Agent śledzi sources |
| Inconsistent formatting | Template-driven |
| "Czy coś pominąłem?" | Systematic coverage |

## ROI / Metryki
- Time: 8-16h manual → 1-2h (review + refinement)
- Coverage: 100% źródeł przeczytanych
- Accuracy: citations traceable to sources
- Consistency: spójny format zawsze

## Wymagania wdrożeniowe
- Dane: source documents (PDF, Word, Excel, text)
- Narzędzia: Claude Code z file access
- Complexity: **Medium-High** (zależy od complexity źródeł)
- Template: zdefiniowana struktura output document

## Przykładowe zastosowania

| Use case | Źródła | Output |
|----------|--------|--------|
| Due diligence | Financial statements, contracts, news | Investment memo |
| Research report | Papers, articles, interviews | Literature review |
| Client proposal | Past projects, requirements, pricing | Proposal document |
| Competitive analysis | Websites, reports, news | Comparison matrix |
| Meeting prep | Emails, notes, previous meetings | Briefing document |

## Warianty / Rozszerzenia
- Incremental updates: "Dodaj te nowe źródła do istniejącego raportu"
- Version tracking: "Co się zmieniło od poprzedniej wersji?"
- Multi-language: źródła w różnych językach → output w jednym
- Visual summaries: automatic charts/graphs from data
- Q&A mode: "Based on these sources, answer..."

## Failure Modes (uwaga!)
- Source quality: garbage in = garbage out
- Contradictions: agent może nie wykryć subtle conflicts
- Context: agent może nie rozumieć domain-specific nuances
- Length: bardzo długie źródła → może pominąć details
- Hallucinations: ZAWSZE verify key claims

## Tips for best results
1. **Provide clear template** — agent needs structure
2. **Specify what's important** — priorytetyzacja
3. **Request citations** — "cite source for each claim"
4. **Review intermediate output** — catch errors early
5. **Iterate** — first draft rarely perfect

## Źródło
[Matt Stockton - How I Prototype Agentic Workflows Before Writing Code](https://mattstockton.com/2025/11/25/how-i-prototype-agentic-workflows.html)
[Matt Stockton - Four Building Blocks for Document Generation Agents](https://mattstockton.com/2026/01/03/four-building-blocks-for-document-generation-agents.html)
[Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
