# Ad Variation Generator Agent

## Domena
Marketing / Growth / Digital Advertising

## Problem klienta
- A/B testing wymaga wielu wariantów copy (setki adów)
- Ręczne tworzenie wariantów zajmuje dni pracy copywriterów
- Trudno utrzymać brand voice przy masowej produkcji
- Platform constraints (character limits) łatwo przeoczyć
- Analiza performance i iteracja to żmudny proces

## Workflow agentowy
1. Agent wczytuje CSV z performance data (ad text, CTR, conversions)
2. Identyfikuje bottom 10% performers
3. Analizuje dlaczego underperformują:
   - Słaby call-to-action
   - Nudny headline
   - Niejasna oferta
   - Zły tone
4. Generuje 3-5 nowych wariantów dla każdego słabego ad'a:
   - Różne angle'y (urgency, benefit, curiosity)
   - Respektuje character limits platformy
   - Utrzymuje brand voice
5. Output: nowy CSV z wariantami + summary report

## Przykładowy prompt
```
You are a Marketing Assistant Agent that iterates on ad campaigns.

Workflow:
1. Read ad_performance.csv (columns: ad_id, headline, body, ctr, conversions)
2. Identify bottom 10% performing ads
3. For each underperformer, analyze why:
   - Weak CTA?
   - Boring headline?
   - Unclear value prop?
4. Generate 5 new ad copy variations for each, following:
   - Headline ≤ 30 chars
   - Body ≤ 90 chars
   - Brand tone: friendly, action-oriented
   - Each variant should try different angle (urgency, benefit, curiosity)
5. Output new CSV with suggested ads mapped to original ad_id
6. Summary report: common themes among underperformers and how new variants address them

Ensure no two ads are identical. Make them genuinely personalized.
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| Copywriterzy: 2-3 dni na 100 wariantów | 100 wariantów w 2-3 minuty |
| Character limits sprawdzane ręcznie | Automatycznie respektowane |
| Brand voice trudny do utrzymania przy skali | Konsystentny tone |
| Analiza performance: subiektywna | Systematyczna analiza |
| Iteracja: tygodnie | Minuty |

## ROI / Metryki
- Czas: dni → minuty (99% redukcja)
- Volume: 10-20 wariantów → 100+ wariantów
- Real example: Anthropic marketing team - "hours of copy-pasting to half a second per batch"
- Advolve case: 90% workload reduction, 15% higher ROAS

## Wymagania wdrożeniowe
- Dane: CSV z performance metrics
- Narzędzia: Claude Code
- Complexity: **Medium**
- Dodatkowe: brand guidelines, platform constraints

## Warianty / Rozszerzenia
- Sub-agents: jeden do headlines, drugi do descriptions
- Integration z ad platforms API (automatyczne upload)
- Learning loop: feedback z performance → lepsze warianty
- Multi-platform: różne warianty dla Google vs Facebook vs LinkedIn
- Visual variants: integration z design tools (Figma plugin)

## Real Case Study
Anthropic Growth Marketing team: generated hundreds of ad variations in minutes using Claude Code + sub-agents. One marketer: "80% of Sales/Marketing work today is manual, laborious data work. In the era of AI, humans can focus on truly human, creative work."

## Źródło
"Claude Code Isn't for Code" - Marketing section
