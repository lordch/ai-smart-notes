# Plan sesji z tatą i zespołem

## Cel

Nauczyć metodologii pracy workspace'owej przez wspólne wykonanie ich realnego projektu (analiza obszaru "odporność").

**Ja**: metodolog, uczę JAK pracować
**Oni**: eksperci domenowi, wiedzą CO badać i jak interpretować

## Proponowana struktura workspace'u dla nich

```
hos-resilience-analysis/
├── CLAUDE.md                 # Instrukcje dla agenta (kontekst HoS, cel projektu)
├── brief.md                  # Pytania biznesowe, scope, kryteria sukcesu
├── research/
│   ├── methodology.md        # Czym jest resilience - frameworki, wymiary, narzędzia
│   ├── market-poland.md      # Rynek w Polsce
│   ├── market-global.md      # Trendy globalne
│   ├── competitors.md        # Kto oferuje co
│   └── corporate-spend.md    # Na co firmy wydają (L&D budżety)
├── synthesis/
│   ├── opportunities.md      # Szanse dla HoS
│   ├── risks.md              # Ryzyka wejścia
│   └── positioning-options.md # Opcje pozycjonowania
└── recommendation.md         # Decyzja + uzasadnienie
```

---

## Sesja 1: Setup + Brief (1.5-2h)

### Cele sesji
- Pokazać strukturę i zasadę pracy
- Wspólnie zdefiniować pytania biznesowe
- Rozłożyć projekt na etapy

### Agenda

1. **Intro** (15 min)
   - Po co to robimy (testowanie metodologii)
   - Zasada: artefakty jako checkpointy, nie chat jako medium pracy
   - Rola agenta: wykonawca, nie ekspert

2. **Setup workspace'u** (15 min)
   - Pokazuję strukturę folderów
   - Tłumaczę logikę: research → synthesis → recommendation
   - Zakładamy folder

3. **Brief** (45 min)
   - RAZEM spisujemy pytania biznesowe
   - Co chcą wiedzieć? Jakie decyzje mają podjąć?
   - Jakie są kryteria sukcesu?
   - Zapisujemy do brief.md

4. **Decomposition** (30 min)
   - RAZEM rozbijamy na obszary research
   - Oni decydują co jest ważne (ekspertyza domenowa)
   - Ja pokazuję jak to strukturyzować

5. **Demo** (15 min)
   - Pokazuję jak wygląda praca z agentem na jednym kawałku
   - Np. research metodologii - jedno pytanie

### Co oni widzą / uczą się
- Externalization: myśli do plików
- Decomposition: duże pytanie na małe
- Brief jako kontrakt: najpierw zdefiniuj co chcesz wiedzieć

### Homework przed sesją 2
- Wykonać 2-3 chunki research (z agentem lub bez)
- Zapisać do plików według struktury

---

## Sesja 2: Review + Steering (1-1.5h)

### Cele sesji
- Przegląd co znaleźliśmy
- Korekta kierunku jeśli trzeba
- Pokazać wartość checkpointingu

### Agenda

1. **Review research** (45 min)
   - Przeglądamy każdy plik research
   - Czy to odpowiada na pytania z brief?
   - Czego brakuje? Co wymaga pogłębienia?
   - Oni oceniają jakość (ekspertyza domenowa)

2. **Steering** (30 min)
   - Decyzje: co pogłębić, co pominąć, co dodać
   - Korekta struktury jeśli trzeba
   - Aktualizacja brief.md jeśli zmieniły się pytania

3. **Planowanie synthesis** (15 min)
   - Jak z research przejść do wniosków
   - Kto robi co przed sesją 3

### Co oni widzą / uczą się
- Checkpointing: można przerwać, przejrzeć, skorygować
- Supervision przez inspekcję artefaktów (nie przez approval każdej akcji)
- Taniej poprawić na etapie research niż na etapie rekomendacji

### Homework przed sesją 3
- Dokończyć research jeśli trzeba
- Zacząć synthesis (opportunities, risks)

---

## Sesja 3: Synthesis + Recommendation (1.5h)

### Cele sesji
- Przejść od research do wniosków
- Wspólnie sformułować rekomendację
- Podsumować czego się nauczyli

### Agenda

1. **Review synthesis** (30 min)
   - Przeglądamy opportunities, risks, positioning options
   - Czy wynikają z research? Czy są kompletne?

2. **Recommendation workshop** (45 min)
   - RAZEM formułujemy recommendation.md
   - Framework decyzyjny: wchodzić/nie/jak
   - Oni decydują (ekspertyza), ja strukturyzuję

3. **Meta-reflection** (15 min)
   - Co zadziałało w tej metodzie pracy?
   - Co było trudne?
   - Czy chcieliby tak pracować dalej?

### Co oni widzą / uczą się
- Cumulation: research służy wielu celom
- Audytowalność: wiadomo skąd wnioski
- Wartość struktury przy złożonych zadaniach

---

## Materiały do przygotowania

Przed sesją 1:
- [ ] Template CLAUDE.md dla ich projektu
- [ ] Przykładowy brief.md (jako inspiracja)
- [ ] Krótki dokument "zasady pracy" (1-pager)

---

## Pytania otwarte

- Czy robią research sami (z agentem) czy ja robię i pokazuję?
- Jaki tool? (Claude, Cursor, coś innego)
- Ile czasu mają między sesjami?
- Czy cały zespół 3-osobowy uczestniczy czy tylko tata?
