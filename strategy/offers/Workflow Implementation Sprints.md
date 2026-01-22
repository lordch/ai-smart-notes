# Workflow Implementation Sprints

type:: [[Offer]]
status:: Draft
date-created:: 2026-01-19
related:: [[Context Engineering Skill Development Program]], [[AI Workspace Build]], [[Strategy - AI Consultancy for Polish SME Knowledge Work]]

---

## Esencja

**Wdrażam jeden konkretny workflow z AI w 2-4 tygodnie.**

Nie uczę ogólnych zasad (to szkolenia). Nie buduję całej infrastruktury (to Workspace Build). **Biorę jeden powtarzalny proces i sprawiam, że działa z AI.**

Klient wychodzi z:
- Działającym workflow'em (testowanym na realnej pracy)
- Dokumentacją procesu
- Prompt template'ami i artefaktami pośrednimi
- Przeszkolonym zespołem (2-5 osób)
- 30-dniowym wsparciem follow-up

---

## Pozycjonowanie

| Szkolenia | **Workflow Sprints** | Workspace Build |
|-----------|----------------------|-----------------|
| Uczą zasad | Wdrażają jeden proces | Budują całe środowisko |
| Wiedza w głowach | Działający workflow | Infrastruktura + wiele workflow'ów |
| "Wiem jak" | "Mam jeden działający flow" | "Mam fundament" |
| Szerokie, płytkie | Wąskie, głębokie | Szerokie, głębokie |

**Workflow Sprint to chirurgiczne wdrożenie** — jeden proces, ale zrobiony porządnie.

---

## Kto jest klientem

### Profil idealny

Firma/zespół który:
- Ma **zidentyfikowany, powtarzalny proces** który chce zoptymalizować
- Robi ten proces **regularnie** (min. kilka razy/miesiąc)
- Ma **jasny input i output** (wie co wchodzi, co ma wyjść)
- Jest gotowy na **2-4 tygodnie intensywnej współpracy**
- Ma **2-5 osób** które będą używać workflow'u

### Przykłady workflow'ów

| Branża | Workflow | Input → Output |
|--------|----------|----------------|
| **Prawo** | Case research | Pytanie prawne → Opinia z precedensami |
| **Prawo** | Due diligence | Dokumenty spółki → Raport DD |
| **Consulting** | Client discovery | Wywiady → Problem statement + rekomendacje |
| **Finance** | Document review | Umowy/sprawozdania → Ekstrakcja danych + analiza |
| **Marketing** | Content production | Brief → Research → Draft → Final |
| **HR** | Candidate screening | CV + JD → Ranking + uzasadnienie |
| **Research** | Literature review | Pytanie badawcze → Search strategy → Extraction table → Synthesis |
| **Research** | Data analysis | Excel z danymi → Table 1 + statystyka + wykresy |

### Antyprofil (kiedy NIE)

- Nie wiedzą jaki proces chcą wdrożyć ("pomóż nam znaleźć" → to Audit)
- Proces jest jednorazowy lub bardzo rzadki
- Brak czasu na współpracę (potrzebne ~10-15h przez 2-4 tyg)
- Oczekują że AI zrobi wszystko autonomicznie

---

## Co dostarczamy

### 1. Działający workflow

Przetestowany na realnej pracy klienta. Nie "teoretycznie powinno działać" — **działa**.

### 2. Dokumentacja procesu

```markdown
# Workflow: [Nazwa]

## Cel
Co ten workflow osiąga.

## Kiedy używać
W jakich sytuacjach uruchamiamy ten workflow.

## Input
Co potrzebujemy na starcie:
- [Input 1]
- [Input 2]

## Kroki
1. [Krok 1] — co robi human, co robi AI
2. [Krok 2]
3. [Krok 3]

## Artefakty pośrednie
- Po kroku 2: [Artefakt A] — checkpoint do review
- Po kroku 4: [Artefakt B]

## Output
Co dostajemy na końcu:
- [Deliverable]
- [Format]

## Typowe pułapki
- [Na co uważać]
- [Czego nie robić]
```

### 3. Prompt templates

Gotowe prompty dla każdego kroku workflow'u:
- Testowane, działające
- Z placeholderami do wypełnienia
- Z przykładami użycia

### 4. Artefakty pośrednie (templates)

Szablony dokumentów tworzonych w trakcie workflow'u:
- Formularze ekstrakcji
- Checkpointy do review
- Formaty outputów

### 5. Struktura folderów

```
workflow-[nazwa]/
├── README.md              # Dokumentacja workflow'u
├── prompts/
│   ├── step-1-[nazwa].md
│   ├── step-2-[nazwa].md
│   └── ...
├── templates/
│   ├── input-template.md
│   ├── checkpoint-1.md
│   └── output-template.md
├── examples/
│   ├── example-input/
│   └── example-output/
└── archive/               # Zrealizowane instancje
```

### 6. Training session

2-3h hands-on z zespołem:
- Walkthrough całego workflow'u
- Każdy wykonuje workflow na realnym zadaniu
- Q&A, troubleshooting

### 7. 30-day follow-up support

- Async pytania przez email/chat
- 2 krótkie check-iny (30 min)
- Drobne korekty jeśli potrzebne

---

## Metodologia

### Faza 1: Discovery (Dzień 1-3)

**Cel:** Zrozumieć workflow w szczegółach.

**Spotkanie kickoff (2h):**
- Jak wygląda proces teraz? (step-by-step)
- Kto robi co?
- Co jest inputem, co outputem?
- Gdzie są bottlenecki?
- Jakie są edge cases?

**Zbieranie materiałów:**
- 3-5 przykładów zrealizowanego procesu
- Istniejące template'y/checklisty
- Typowe problemy i błędy

**Moja analiza (async):**
- Mapowanie procesu
- Identyfikacja gdzie AI może pomóc
- Draft workflow'u z AI

### Faza 2: Build (Dzień 4-10)

**Cel:** Zbudować i przetestować workflow.

**Iteracja 1:**
- Buduję workflow na podstawie analizy
- Testuję na przykładowych danych
- Tworzę prompt templates i artefakty

**Sesja review (1.5h):**
- Pokazuję draft workflow'u
- Klient daje feedback
- Identyfikujemy luki

**Iteracja 2-3:**
- Poprawki na podstawie feedbacku
- Testowanie na realnych zadaniach (klient dostarcza)
- Dopracowanie edge cases

### Faza 3: Pilot (Dzień 11-20)

**Cel:** Przetestować workflow w realnych warunkach.

**Pilot run:**
- Klient używa workflow'u na 2-3 realnych zadaniach
- Ja obserwuję / wspieram async
- Zbieramy feedback

**Sesja retrospektywna (1h):**
- Co zadziałało?
- Co nie zadziałało?
- Jakie korekty?

**Finalizacja:**
- Ostatnie poprawki
- Kompletna dokumentacja

### Faza 4: Handoff (Dzień 21-28)

**Cel:** Przekazać workflow zespołowi.

**Training session (2-3h):**
- Full walkthrough
- Hands-on practice
- Q&A

**Dokumentacja:**
- Wszystkie pliki w folderze workflow'u
- README z instrukcjami
- Troubleshooting guide

**Kickoff follow-up:**
- Plan na 30 dni
- Kanał komunikacji dla pytań

---

## Timeline

```
Day 1-3      Day 4-10     Day 11-20    Day 21-28    Day 29-58
[Discovery] → [Build] →   [Pilot] →    [Handoff] → [Follow-up]
   3 dni       7 dni        10 dni        7 dni       30 dni
```

**Całkowity czas:** 3-4 tygodnie aktywnej pracy + 30 dni support
**Zaangażowanie klienta:** ~10-15h

---

## Przykład: Legal Case Research

### Workflow przed

```
1. Prawnik dostaje pytanie od klienta
2. Szuka w LEX/Legalis ręcznie
3. Czyta orzeczenia, robi notatki (gdzie? różnie)
4. Pisze opinię w Wordzie
5. Review przez partnera
6. Wysyłka do klienta

Czas: 4-8h
Problem: notatki rozproszone, każdy robi inaczej
```

### Workflow po wdrożeniu

```
1. Prawnik wpisuje pytanie do template'u (5 min)
2. AI generuje search strategy + listę keywords (10 min)
3. Prawnik szuka w LEX, AI pomaga ekstrahować z orzeczeń (1h)
4. AI generuje draft struktury opinii z cytatami (20 min)
5. Prawnik pisze/edytuje opinię (1-2h)
6. Review przez partnera
7. Wysyłka

Czas: 2-4h
Bonus: notatki ustrukturyzowane, reusable
```

### Deliverables dla tego workflow'u

- `prompts/search-strategy.md` — generowanie strategii wyszukiwania
- `prompts/extract-ruling.md` — ekstrakcja z orzeczenia
- `prompts/draft-opinion.md` — draft struktury opinii
- `templates/question-intake.md` — formularz pytania
- `templates/extraction-form.md` — notatki z orzeczeń
- `templates/opinion-structure.md` — szablon opinii
- `examples/` — 2-3 przykładowe realizacje

---

## Pricing

### Standard Sprint

**Zakres:** Jeden workflow, 2-5 osób
**Czas:** 3-4 tygodnie + 30 dni support
**Moje zaangażowanie:** ~30-40h

**Cena:** 25,000 - 35,000 PLN

### Complex Sprint

**Zakres:** Workflow z wieloma wariantami/edge cases
**Czas:** 4-6 tygodni + 30 dni support
**Moje zaangażowanie:** ~45-60h

**Cena:** 40,000 - 50,000 PLN

### Light Sprint

**Zakres:** Prosty workflow, 1-2 osoby, mniej support'u
**Czas:** 2 tygodnie + 14 dni support
**Moje zaangażowanie:** ~20h

**Cena:** 15,000 - 20,000 PLN

---

## Value calculation

### Przykład: Case Research (kancelaria)

**Przed:**
- 6h × 400 PLN/h = 2,400 PLN/case
- 50 cases/rok = 120,000 PLN

**Po:**
- 3h × 400 PLN/h = 1,200 PLN/case
- 50 cases/rok = 60,000 PLN

**Oszczędność:** 60,000 PLN/rok
**Cena wdrożenia:** 30,000 PLN
**ROI:** 6 miesięcy

Plus:
- Lepsza jakość (systematyczność)
- Mniej stresu (jasny proces)
- Onboarding nowych prawników (dokumentacja)

---

## Kiedy Workflow Sprint vs inne oferty

| Sytuacja | Rekomendacja |
|----------|--------------|
| "Chcemy zoptymalizować jeden konkretny proces" | **Workflow Sprint** ✓ |
| "Nie wiemy od czego zacząć" | Audit → potem Sprint |
| "Chcemy zbudować całą infrastrukturę AI" | Workspace Build |
| "Chcemy przeszkolić zespół w zasadach pracy z AI" | Szkolenia |
| "Mamy kilka workflow'ów do wdrożenia" | Workspace Build + Sprinty |

---

## Gwarancje

1. **Działający workflow** — jeśli po pilotcie nie działa, poprawiamy bez dodatkowych kosztów
2. **30-dniowy support** — wliczony w cenę
3. **Dokumentacja** — wszystko opisane, nie "w głowie konsultanta"

---

## Następne kroki (dla zainteresowanego klienta)

1. **Discovery call (30 min, free)** — zrozumienie procesu, wstępna ocena czy sprint ma sens
2. **Propozycja** — zakres, timeline, cena
3. **Kickoff** — start Discovery phase

---

## Powiązania

- Po Sprintcie → **Advisory retainer** (ongoing support, nowe workflow'y)
- Przed Sprinttem → **Audit** (jeśli nie wiedzą który proces)
- Równolegle/po → **Workspace Build** (jeśli chcą całą infrastrukturę)
- Dla zespołu → **Szkolenia** (jeśli więcej osób ma się nauczyć zasad)
