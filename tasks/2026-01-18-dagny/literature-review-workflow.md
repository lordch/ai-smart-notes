# Literature Review Workflow (lekarz-badacz)

Realistyczny opis jak wygląda "mały" przegląd literatury przed badaniem retrospektywnym — nie formal systematic review, ale celowane szukanie 20-50 kluczowych paperów.

---

## Kontekst

Dagny ma hipotezę kliniczną, np.:
> "Pacjenci z HIV i CD4 < 200 częściej rozwijają kryptokokowe zapalenie opon mózgowych"

Zanim zbierze dane i zrobi badanie, musi:
- Sprawdzić co już wiadomo
- Znaleźć lukę (gap) którą jej badanie wypełni
- Napisać uzasadnienie (Introduction/Background)

To nie jest systematic review z PRISMA i przeszukiwaniem 5 baz. To pragmatyczne szukanie kluczowej literatury.

---

## Status quo: Jak to wygląda teraz

### Krok 1: Wstępne rozpoznanie (orientacja)

**Co robi:**
- Otwiera PubMed (pubmed.ncbi.nlm.nih.gov)
- Wpisuje proste query: `HIV cryptococcal meningitis`
- Przegląda pierwsze 2-3 strony wyników
- Szuka review articles żeby złapać "lay of the land"

**Cel:** Zorientować się co w ogóle istnieje, jakie są główne wątki

**Czas:** 30-60 min

---

### Krok 2: Budowanie zapytania (iteracyjne)

**Co robi:**
- Zawęża/rozszerza query na podstawie tego co znalazła
- Dodaje filtry: ostatnie 10 lat, English, humans
- Próbuje różnych kombinacji słów kluczowych
- Czasem używa MeSH terms (kontrolowany słownik PubMed)

**Przykładowe iteracje:**
```
HIV cryptococcal meningitis
→ za dużo (3000 wyników)

HIV cryptococcal meningitis CD4
→ lepiej (800 wyników)

HIV cryptococcal meningitis CD4 prophylaxis
→ bardziej specific (200 wyników)

"HIV Infections"[MeSH] AND "Cryptococcosis"[MeSH] AND "CD4 Lymphocyte Count"[MeSH]
→ precyzyjnie (150 wyników)
```

**Czas:** 30-60 min (rozłożone, wraca do tego)

---

### Krok 3: Screening abstraktów

**Co robi:**
- Przegląda listę wyników w PubMed
- Czyta tytuły, potem abstrakty
- Mentalnie (lub fizycznie) taguje: "relevant", "maybe", "skip"
- Otwiera interesujące w nowych kartach

**Kryteria (w głowie):**
- Czy dotyczy mojej populacji?
- Czy bada podobne pytanie?
- Czy ma dane które mogę porównać?
- Czy to dobry journal?

**Friction:**
- Abstrakt często nie mówi wszystkiego
- Musi otworzyć full text żeby ocenić
- Dużo paperów odpada po przeczytaniu 2 akapitów

**Czas:** 2-4 godziny (często rozłożone na kilka dni)

---

### Krok 4: Pozyskiwanie pełnych tekstów

**Co robi:**
- Część jest Open Access → pobiera PDF
- Część wymaga dostępu → loguje się przez bibliotekę uczelnianą
- Część niedostępna → szuka na Sci-Hub, ResearchGate, pisze do autorów

**Friction:**
- Paywall frustracja
- Różne formaty (PDF, HTML)
- Organizacja pobranych plików

**Czas:** 1-2 godziny (rozłożone)

---

### Krok 5: Czytanie i notowanie

**Co robi:**
- Czyta pełne teksty (lub przynajmniej Methods + Results + Discussion)
- Robi notatki — ALE GDZIE?

**Typowe miejsca na notatki:**
- Bezpośrednio w PDF (highlights, komentarze) — Acrobat, Preview
- W reference managerze (Zotero/Mendeley notes)
- W osobnym dokumencie Word/Google Doc
- W Excelu (tabela z kolumnami: autor, rok, n, metoda, wyniki, komentarz)
- Na karteczkach / w zeszycie (tak, nadal się zdarza)

**Co notuje:**
- Główne findings
- Wielkość próby, metodologia
- Ograniczenia
- Cytaty które może użyć
- "To potwierdza moją hipotezę" / "To przeczy"

**Friction:**
- Notatki rozproszone
- Ciężko potem znaleźć "gdzie to było"
- Brak struktury — każdy paper notowany inaczej
- Nie pamięta co już przeczytała

**Czas:** 4-8 godzin (główny czas lit review)

---

### Krok 6: Organizacja referencji

**Co robi:**
- Dodaje papery do reference managera (Zotero, Mendeley, EndNote)
- Tworzy folder/kolekcję dla tego projektu
- Taguje (opcjonalnie)

**Friction:**
- Import czasem nie działa (błędne metadane)
- Ręczne poprawianie autorów, tytułów
- Duplikaty

**Czas:** 30-60 min

---

### Krok 7: Snowballing (łańcuch cytowań)

**Co robi:**
- Z kluczowych paperów sprawdza:
  - **References** (co oni cytowali?) — backward snowballing
  - **Cited by** (kto ich cytuje?) — forward snowballing
- Znajduje papery których nie złapała w PubMed search

**Narzędzia:**
- Google Scholar "Cited by"
- PubMed "Similar articles"
- Connected Papers (wizualizacja)

**Czas:** 1-2 godziny

---

### Krok 8: Synteza i pisanie

**Co robi:**
- Przegląda notatki
- Grupuje papery tematycznie
- Pisze sekcję Background/Introduction:
  - Co wiadomo o HIV i infekcjach oportunistycznych
  - Co wiadomo o kryptokokozie
  - Co wiadomo o roli CD4
  - **Luka:** "However, limited data exist on [X] in [Y] population"
  - "Therefore, we aimed to..."

**Friction:**
- Trudno ogarnąć 30+ paperów
- "Czy czegoś nie pominęłam?"
- Pisanie jest żmudne
- Formatowanie cytowań

**Czas:** 4-8 godzin

---

## Całkowity czas

| Etap | Czas |
|------|------|
| Orientacja | 1h |
| Budowanie query | 1h |
| Screening abstraktów | 3h |
| Pozyskiwanie PDF | 1.5h |
| Czytanie + notowanie | 6h |
| Organizacja referencji | 0.5h |
| Snowballing | 1.5h |
| Synteza + pisanie | 6h |
| **RAZEM** | **~20 godzin** |

Rozłożone na 2-4 tygodnie, między dyżurami, kliniką, życiem.

---

## Główne bóle

1. **Czas** — 20h to dużo dla pracującego lekarza
2. **Rozproszenie** — notatki w 5 miejscach, nie pamięta co gdzie
3. **Powtarzalność** — każdy paper czytany od zera, te same informacje wyciągane ręcznie
4. **Brak struktury** — notatki nieporównywalne między paperami
5. **Paywall hell** — dostęp do PDF-ów
6. **"Czy czegoś nie pominęłam?"** — anxiety że luka w literaturze
7. **Pisanie** — od notatek do prozy to skok

---

## Wizja z agentem

### Krok 1: Orientacja
**Teraz:** Ręcznie przegląda PubMed
**Z agentem:** "Daj mi przegląd literatury o HIV i kryptokokowym zapaleniu opon. Co wiadomo? Jakie są główne wątki? Gdzie są luki?"
→ Agent daje structured summary z kluczowymi referencjami

### Krok 2: Search strategy
**Teraz:** Trial-and-error z query
**Z agentem:** "Zbuduj mi search query do PubMed dla mojego pytania badawczego: [PICO]"
→ Agent generuje query z MeSH terms, operatorami, filtrami

### Krok 3: Screening
**Teraz:** Czyta setki abstraktów
**Z agentem:** "Mam listę 200 abstraktów. Przefiltruj pod kątem: [kryteria]. Daj mi top 30 najbardziej relevant."
→ Agent rankuje, uzasadnia, sugeruje

### Krok 4: PDF retrieval
**Teraz:** Polowanie na PDF-y
**Z agentem:** Ograniczone (paywall to paywall), ale agent może:
- Sprawdzić które są Open Access
- Podać linki do legal sources
- Zidentyfikować preprint wersje

### Krok 5: Czytanie + ekstrakcja
**Teraz:** Ręczne czytanie, rozproszone notatki
**Z agentem:** "Przeczytaj ten PDF i wyciągnij: population, methods, key findings, limitations, relevance to my question"
→ Agent wypełnia ustrukturyzowany formularz
→ Wszystkie papery w tym samym formacie
→ Porównywalne, przeszukiwalne

### Krok 6: Synteza
**Teraz:** Ręczne grupowanie, pisanie od zera
**Z agentem:** "Na podstawie tych 30 paperów, napisz draft sekcji Background. Pokaż co wiadomo, zidentyfikuj lukę, uzasadnij moje badanie."
→ Agent pisze draft z cytowaniami
→ Dagny edytuje, doprecyzowuje

---

## Przykładowe prompty

```
"Szukam literatury o związku między liczbą CD4 a ryzykiem kryptokokozy u pacjentów z HIV. 
Zbuduj mi search strategy do PubMed. Interesują mnie badania z ostatnich 15 lat, 
w języku angielskim, na ludziach dorosłych."
```

```
"Mam PDF artykułu [załączony]. Wyciągnij:
- Populacja (n, kryteria włączenia)
- Design badania
- Główne wyniki (liczby, p-values)
- Ograniczenia które autorzy wymieniają
- Czy wspierają czy przeczą hipotezie że niskie CD4 zwiększa ryzyko kryptokokozy"
```

```
"Mam tabelę z 25 paperami które przeczytałam [załączona]. 
Napisz draft sekcji Introduction (500-700 słów) który:
- Podsumowuje stan wiedzy
- Pokazuje lukę którą moje badanie wypełnia
- Kończy się zdaniem 'Therefore, we aimed to...'"
```

---

## Artefakty pośrednie

1. **Search strategy document** — query do PubMed z uzasadnieniem
2. **Screening log** — lista abstraktów z decyzjami (include/exclude + powód)
3. **Paper extraction table** — ustrukturyzowane notatki z każdego paperu

| ID | Autor | Rok | Populacja | n | Design | Key findings | Limitations | Relevance |
|----|-------|-----|-----------|---|--------|--------------|-------------|-----------|
| 1 | Smith | 2019 | HIV+ adults | 234 | Retrospective | CD4<100 → 3x risk | Single center | High |
| 2 | ... | ... | ... | ... | ... | ... | ... | ... |

4. **Synthesis notes** — grupowanie tematyczne, główne wnioski
5. **Draft Introduction** — tekst gotowy do edycji

---

## Wartość dla Dagny

| Aspekt | Teraz | Z agentem |
|--------|-------|-----------|
| Czas | ~20h | ~5-8h |
| Struktura notatek | Chaotyczna | Ujednolicona tabela |
| "Czy coś pominęłam?" | Anxiety | Agent może sprawdzić coverage |
| Od notatek do prozy | Duży skok | Draft gotowy |
| Iteracja | Zaczynać od zera | "Dodaj jeszcze te 5 paperów do syntezy" |
