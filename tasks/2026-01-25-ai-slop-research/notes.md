# AI Slop Research - Notatki i refleksje

date-created:: 2026-01-25
status:: Working

---

## Źródła

1. **Structural limitations of AI in knowledge work** (Compass/Deep Research)
   - Synteza badań 2024-2025
   - Mocne dane empiryczne, cytowania

2. **AI Slop in High-Value Knowledge Work** (ChatGPT)
   - Obszerny raport z self-audit
   - Uwaga: sam przyznaje że może wykazywać cechy slop

---

## Kluczowe ustalenia

### Matematyczne ograniczenia kreatywności

- **Cropley (2025)**: LLM mają ceiling na kreatywność = 0.25 (skala 0-1)
- Granica między "little-c" (amatorskie) a "Pro-c" (profesjonalne)
- Mechanizm: novelty i effectiveness są odwrotnie skorelowane w systemach probabilistycznych
- Empiryczna walidacja: AI stories/solutions konsekwentnie w 40-50 percentylu

### Korelacja z critical thinking

- **SBS Swiss Business School (2025)**: 666 UK knowledge workers
  - r = -0.68: użycie AI ↔ spadek critical thinking
  - r = +0.72: użycie AI ↔ cognitive offloading
  - r = -0.75: cognitive offloading ↔ critical thinking
- **MIT Media Lab EEG study**: ChatGPT users = najniższe brain engagement
- Z czasem "got lazier with each subsequent essay, often resorting to copy-and-paste"

### Homogenizacja

- **Georgetown/Stanford**: "each additional human-written essay contributed more new ideas than each additional GPT-4 essay"
- Prompt modifications i parameter adjustments "do not mitigate the diversity gap"
- "Creative scar" — homogenizacja utrzymuje się miesiące po ekspozycji

### Tryby współpracy (BCG/Harvard)

| Tryb | % | Opis | Outcome |
|------|---|------|---------|
| **Centaurs** | 14% | Jasny podział human/AI | Upskilling w domenie |
| **Cyborgs** | 60% | Fused co-creation | "Newskilling" w AI |
| **Self-Automators** | 26% | Delegują całe taski | Brak skill development |

Centaurs i Cyborgs działają. Self-Automators produkują workslop.

### "Workslop" — Stanford/HBR 2025

- AI-generated work that "masquerades as good work, but lacks the substance"
- 40% pracowników otrzymuje taki content miesięcznie
- Koszt: $186/pracownika → $9M+ rocznie dla dużych organizacji
- Problem: "shifts cognitive burden downstream"

---

## Kategorie problemów (do zaradzania)

| Kategoria | Manifestacja | Mechanizm źródłowy |
|-----------|--------------|-------------------|
| **Superficial coverage** | Dotyka wielu punktów, brak głębi | Probabilistic = "most likely continuation" |
| **Averaging of perspectives** | Blend into consensus | RLHF optimizes for "what most prefer" |
| **Apparent completeness** | Wygląda kompletnie, nic nowego | Format mimicry > substance |
| **Lack of intellectual courage** | Hedging, safe middle-ground | Alignment penalizes controversy |
| **Homogenization** | Wszystkie outputy podobne | Single statistical voice |
| **Hallucinated depth** | Cytaty/fakty zmyślone | No grounding mechanism |

### Red flags do rozpoznawania

- Overly generic language, clichés
- Brak konkretnych przykładów/danych
- Apparent completeness with no depth
- Missing citations for bold claims
- One-sided or "middle of the road" perspective
- Uniform style, lack of voice

---

## Połączenie z Human-Agent Collaboration Framework

### Bezpośrednie mapowanie

| Slop research | HAC Framework |
|---------------|---------------|
| Self-Automator mode | "Autonomia która nie działa" |
| Centaur/Cyborg mode | Human-Agent Collaboration |
| Workslop | Output bez kuracji kontekstu |
| "Taste as the new skill" | Manual context curation is the work |

### Pytanie do przemyślenia

Czy **dobry kontekst** wystarczy żeby zapobiec slop?

Raporty sugerują że problem jest głębszy:
- Probabilistic nature: AI z definicji dąży do średniej
- RLHF bias: trenowane na preferencje, nie prawdę
- Architectural limits: problemy z kompozycją rozumowania

**Implikacja**: Nawet z perfekcyjnym kontekstem, AI może produkować "averaging of perspectives".

**Możliwe odpowiedzi:**
1. Templates i struktura wymuszają głębię (forma jako constraint)
2. Checkpointy wyłapują powierzchowność przed final output
3. Human judgment dodaje "intellectual courage" którego AI nie ma
4. Procedural context ("challenge assumptions", "give dissenting view") może przeciwdziałać?

---

## Co jest aktualne vs. przestarzałe

### Ostrożność wobec źródeł 2023

- Capability AI zmieniło się znacząco
- Centaur/Cyborg framing pochodzi z 2023 (BCG study) — ale logika może być aktualna
- Hallucination rates różnią się między modelami i wersjami

### Prawdopodobnie trwałe

- Fundamental architectural limits (probabilistic, averaging)
- RLHF bias toward consensus
- Homogenization effect at group level
- Cognitive offloading pattern

---

## Potencjalne użycia

1. **Argumenty sprzedażowe**: "Bez infrastruktury kontekstowej produkujesz workslop"
2. **Framework extension**: Dodać kategorię "slop prevention" do procedural context
3. **Content**: Post o tym dlaczego AI workspace > AI chat
4. **Positioning**: Human-Agent Collaboration jako antidotum na slop

---

## Otwarte pytania

- Czy "taste" można rozwijać/uczyć? Czy to tacit knowledge?
- Jak mierzyć czy workspace zapobiega slop?
- Które elementy infrastruktury najbardziej chronią przed którymi kategoriami slop?
- Czy jest różnica między modelami (Claude vs GPT vs Gemini) w tendencji do slop?

---

## Następne kroki

- [ ] Przerobić na notatkę w literature/ (gdy wyklaruje się co jest ważne)
- [ ] Zidentyfikować konkretne mechanizmy zaradzania dla każdej kategorii
- [ ] Sprawdzić aktualność Centaur/Cyborg framingu
- [ ] Draft contentu na temat slop vs collaboration
