# Dzielenie zadań na checkpointy

## Kluczowy insight: autonomy slider

Checkpoint = granica zaufania. Nie "obiektywna" struktura zadania, ale: **gdzie TY tracisz zaufanie, że agent zrobi dobrze bez weryfikacji?**

To jest dynamiczne:
- Na początku checkpointujesz często (nie wiesz gdzie agent się myli)
- Z czasem uczysz się jego "jagged intelligence"
- Eksternalizujesz wiedzę która wypełnia luki
- Przesuwasz slider

```
TYDZIEŃ 1                           TYDZIEŃ 8
[—•—•—•—•—•—•—•—•→]                [———•———•———→]
 gęste checkpointy                  rzadkie checkpointy
 niskie zaufanie                    wysokie zaufanie
 mało eksternalizacji               bogaty kontekst
```

---

## Feedback loop jako mechanizm uczenia

```
Checkpoint gęsto (niskie zaufanie)
    → Obserwujesz gdzie agent się myli
    → Eksternalizujesz brakujący kontekst (instrukcje, przykłady)
    → Następnym razem ten fragment działa lepiej
    → Możesz checkpointować rzadziej (wyższe zaufanie)
    → Repeat
```

To jest **in-context skill learning** — uczysz się budować kontekst, który sprawia, że agent jest coraz bardziej niezawodny w TWOIM workflow.

---

## Pomocnicze heurystyki (ale secondary do autonomy slider)

1. **Punkty decyzyjne** — przed wyborem kierunku, nie po
2. **Zmiana typu pracy** — research → selekcja → analiza → synteza → produkcja
3. **Test "gdybym kontynuował jutro"** — czego potrzebuję żeby nie zaczynać od zera?
4. **Gdzie pomyłka boli najbardziej** — gęściej checkpointuj przed high-leverage momentami

---

## Przykład: Prawnik — research precedensów

### Tydzień 1

**Workflow:**
1. Zapytanie → lista orzeczeń
2. **CHECKPOINT:** Czy orzeczenia istnieją? (halucynacje sygnatur)
3. Streszczenie każdego orzeczenia
4. **CHECKPOINT:** Czy streszczenie poprawne? (czytam oryginał)
5. Synteza
6. **CHECKPOINT:** Czy synteza oddaje niuanse?

**Gdzie agent zawiódł:**
- 3/15 sygnatur nie istniało
- 2 streszczenia pominęły ograniczenia stosowania
- Synteza za ogólna, gubiła różnice między liniami orzeczniczymi

### Eksternalizacja (tydzień 2-4)

```markdown
## Instrukcje dla researchu precedensów

1. Podawaj TYLKO orzeczenia których sygnatury możesz zweryfikować
2. Dla każdego orzeczenia:
   - Sygnatura, data, sąd
   - Stan faktyczny (2-3 zdania)
   - Ratio decidendi
   - OGRANICZENIA stosowania
3. W syntezie: grupuj po liniach orzeczniczych,
   explicite wskaż gdzie linie się RÓŻNIĄ
```

Plus: folder `/precedensy/` z poprzednimi researchami jako wzorzec.

### Tydzień 6

**Nowy workflow:**
1. Zapytanie + instrukcje + wzorcowe researchy
2. Agent zwraca listę z pełnym formatem
3. **CHECKPOINT:** Spot-check 2-3 losowych sygnatur (nie wszystkich)
4. Synteza
5. **CHECKPOINT:** Weryfikacja syntezy (tu nadal nie ufam)

**Co się zmieniło:**
- "Czy istnieją" → z 100% na spot-check
- "Czy streszczenie ok" → zniknął (format wymusza kompletność)
- "Synteza" → pozostał (judgment kluczowy)

---

## Przykład: Konsultant — analiza wywiadów

### Tydzień 1

8 transkryptów → analiza każdego osobno → synteza

**Gdzie zawiódł:**
- Równoważył juniora i CEO
- Gubił kontekst polityczny
- Synteza = lista, nie analiza

### Eksternalizacja

```markdown
## Kontekst organizacji klienta
- CEO: Nowak — sponsor, chce transformacji
- CFO: Kowalski — sceptyczny, blokuje budżety
- Head of Ops: Wiśniewska — realne problemy, mało władzy

## Instrukcje
1. Przy każdym problemie: KTO i jaka rola/władza
2. Zaznacz SPRZECZNOŚCI
3. W syntezie: kto ma problem, kto blokuje
```

### Tydzień 6

Wszystkie transkrypty + kontekst organizacji w jednym zapytaniu.
Checkpoint tylko na poziomie syntezy.

---

## Przykład: Marketer — posty LinkedIn

### Tydzień 1

3-4 iteracje na każdy post. Ton generyczny, brak hooków.

### Eksternalizacja

```markdown
## Brand voice
- Praktyk do praktyka, nie vendor do klienta
- Unikamy: "revolutionary", buzzwordy
- Używamy: konkretne liczby, przyznawanie do ograniczeń

## Struktura
- Hook: pytanie lub kontrowersja (nie "exciting news!")
- Problem: ból z rozmów z klientami
- Rozwiązanie: 1-2 zdania
- CTA: miękkie

## Przykłady
[3 dobre posty, 2 złe + dlaczego]
```

### Tydzień 6

0-1 iteracji. 30-sekundowy gut-check zamiast 20 minut.
