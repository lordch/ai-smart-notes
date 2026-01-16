# Workshop Curriculum — luźne notatki

## Updateowanie CLAUDE.md vs inne formy

Pytanie: kiedy updateować CLAUDE.md, kiedy tworzyć:
- skill?
- subagenta?
- osobną notatkę (reference material)?

Teresa Torres (Product Talk) — three-layer system:
1. **Global preferences** — ~/.claude/CLAUDE.md, zawsze ładowane
2. **Project instructions** — ./CLAUDE.md, per projekt
3. **Reference context** — osobne pliki, ładowane on-demand

Kryterium: CLAUDE.md = reguły i preferencje (zwięzłe). Reference = szczegółowy kontekst (może być długi).

TODO: sprawdzić czy ma więcej w innych artykułach z cyklu

---

## Pattern: tasks jako miejsce na robocze notatki

Problem: agent chce tworzyć notatki, albo ja chcę, ale:
- nie pasuje do systemu wiedzy
- zaśmieca
- zajmuje dużo czasu żeby znaleźć dobre miejsce
- a to nie jest na to moment

Rozwiązanie: `tasks/YYYY-MM-DD-opis/` jako "parking" dla intermediate artifacts. Może zostać, może być wypromowane, może być usunięte. Bez presji.

---

## Feedback loop i reviewability

Kluczowe: artefakt pośredni musi być **łatwy do zweryfikowania**.

> Łatwiej zweryfikować 100 linijek planu niż 10000 linijek kodu.

To jest kolejne kryterium na "kiedy checkpointować":
- Czy output tego kroku jestem w stanie zreviewować w rozsądnym czasie?
- Jeśli nie → podziel na mniejsze kroki

---

## Psychologia pracy z agentami

Pułapka: łatwo dać się ponieść, dać agentowi dużo pracy, olać sprawdzanie.

To się źle kończy — błędy się kumulują, potem trudno wrócić.

Uczciwe pytanie do siebie: "Czy naprawdę to zreviewuję, czy tylko kliknę OK?"

Jeśli odpowiedź brzmi "kliknę OK" → albo:
- podziel na mniejsze kawałki (żebyś CHCIAŁ reviewować)
- albo przyznaj się, że ufasz agentowi na tym etapie (świadomy autonomy slider)

Świadome "ufam" ≠ leniwe "olałem".
