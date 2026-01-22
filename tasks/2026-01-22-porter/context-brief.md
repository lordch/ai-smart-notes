# Brief: Analiza Jobs to Be Done

## Meta-cel

Dogfooding — testowanie frameworku Human-Agent Collaboration przy jednoczesnej korzyści strategicznej.

---

## Pytanie strategiczne

> **Dla których "prac" (jobs) jestem najlepszą opcją — i jak to komunikować, zanim prosty interfejs (Copilot, Gems, Claude Cowork) stanie się "wystarczająco dobry"?**

---

## Profil Biznesu

### Kim jestem
Konsultant budujący praktykę w obszarze **Human-Agent Collaboration** — sposobu pracy gdzie człowiek steruje, agent wykonuje. Trzecia droga między chatem (każda sesja od zera) a pełną autonomią (nie działa).

### Oferty

| Oferta | Target | Czas |
|--------|--------|------|
| **AI Workspace Build** | Solo/małe zespoły (1-10 osób) | 4-8 tyg |
| **Workflow Implementation Sprints** | Zespoły z konkretnym problemem | 2-4 tyg |
| **Context Engineering Training** | Power users, liderzy | 16-20h |
| **Advisory/Retainer** | Founderzy | Ongoing |

### Unikalne wyróżniki
1. **Kompetencja zostaje u klienta** — nie dependency od narzędzia
2. **Artefakty jako medium** — nie chat który znika
3. **Izolacja kontekstu** — złożone zadania bez "context rot"
4. **Filesystem-based** — przejrzystość, wersjonowanie, audytowalność

### Kluczowa wartość (dowód)
> "Wczoraj z tatą zrobiliśmy research resilience teoretyczny w 2h, który zająłby tydzień wysoko opłacanego konsultanta."

---

## Rynek

**Definicja**: Wdrożenia AI dla knowledge workers w Polsce

**Geografia**: Polska (z opcją produktyzacji na eksport)

**Potencjalni klienci** (nie ograniczaj się do tej listy):
- Knowledge workers w SME
- Freelancerzy z intensive knowledge work
- Zespoły research/analityka
- Konsultanci, prawnicy, badacze
- Każdy kto robi "złożone zadania z wieloma źródłami"

---

## Obawy do zbadania

### Główna obawa: Substytuty

| Substytut | Zagrożenie | Pytanie |
|-----------|------------|---------|
| **Copilot** | Integracja z M365 "out of the box" | Dla jakich jobs Copilot wystarcza? |
| **Gems / Custom GPTs** | "Productized consulting" — łatwy start | Kiedy "zamrożona metodologia" nie wystarcza? |
| **Claude Cowork** | Natywne środowisko od Anthropic | Co daje workspace build czego Cowork nie da? |
| **DIY** | Ludzie nauczą się sami (jak mama) | Ile czasu zajmuje DIY vs ile wart jest accelerator? |

### Hipoteza do zwalidowania
> "Prosty interfejs wystarcza dla prostych zadań. Dla złożonych (długich, wieloźródłowych, wymagających kontroli) — nie. Moja wartość jest w *złożonych*."

---

## Framework: Jobs to Be Done

### Co to jest JTBD
Klienci nie kupują produktów — "zatrudniają" rozwiązania do wykonania konkretnej "pracy" (job). Job ma wymiar:
- **Funkcjonalny** — co chcę osiągnąć
- **Emocjonalny** — jak chcę się czuć
- **Socjalny** — jak chcę być postrzegany

### Pytania do zbadania

1. **Jakie "prace" mają knowledge workers w Polsce?**
   - Co próbują osiągnąć?
   - Gdzie się frustrują?
   - Co zajmuje im nieproporcjonalnie dużo czasu?

2. **Jak teraz rozwiązują te prace?**
   - Copilot? ChatGPT? Manual? Junior? Outsourcing?
   - Co działa? Co nie?

3. **Dla których prac prosty interfejs NIE wystarcza?**
   - Złożoność? Kontrola? Audytowalność? Wiedza organizacyjna?

4. **Jak komunikować wartość dla tych prac?**
   - Messaging który rezonuje
   - Dowody (case studies, ROI)

---

## Struktura checkpointów

Task podzielony na fazy. Każda faza kończy się artefaktem (checkpoint). Agent zaczyna nową fazę z fresh context + checkpoint z poprzedniej.

```
┌─────────────────────────────────────────────────────────────┐
│  FAZA 1: RESEARCH                                           │
│  Input: brief (ten plik)                                    │
│  Output: research-raw.md                                    │
│  Cel: Zebrać surowe dane o klientach, problemach,          │
│       jak teraz rozwiązują                                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  FAZA 2: JOBS EXTRACTION                                    │
│  Input: research-raw.md                                     │
│  Output: jobs-map.md                                        │
│  Cel: Wyciągnąć listę "prac" z researchu                   │
│       Skategoryzować (funkcjonalne/emocjonalne/socjalne)   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  FAZA 3: ALTERNATIVES ANALYSIS                              │
│  Input: jobs-map.md                                         │
│  Output: alternatives.md                                    │
│  Cel: Jak alternatywy (Copilot, Gems, DIY) adresują       │
│       każdy job. Gdzie wystarczają, gdzie nie.             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  FAZA 4: SYNTHESIS                                          │
│  Input: jobs-map.md + alternatives.md                       │
│  Output: analysis.md (final)                                │
│  Cel: Które jobs wygrywam? Jak komunikować?                │
│       Rekomendacje strategiczne.                           │
└─────────────────────────────────────────────────────────────┘
```

---

## Instrukcje dla agenta

### Faza 1: Research

**Źródła do przeszukania:**
1. **Workspace autora** — pliki w strategy/, concepts/, literature/, tasks/
2. **Web search** — "AI dla biznesu Polska", "wdrożenia AI", "szkolenia AI"
3. **LinkedIn** — polscy konsultanci AI, posty o AI w pracy
4. **Raporty** — stan adopcji AI w polskich firmach

**Co zbierać:**
- Cytaty od knowledge workers o ich problemach
- Jak opisują swoje frustracje
- Jakich narzędzi używają
- Co działa, co nie
- Cenniki konkurencji (jeśli publiczne)

**Output: `research-raw.md`**
- Surowe notatki, cytaty, linki
- Bez analizy — tylko materiał

### Faza 2: Jobs Extraction

**Input:** research-raw.md

**Proces:**
1. Przeczytaj surowy research
2. Zidentyfikuj powtarzające się wzorce
3. Sformułuj jako "jobs" w formacie:
   > "Kiedy [sytuacja], chcę [motywacja], żeby [oczekiwany outcome]"

**Kategoryzacja:**
- Funkcjonalne (co chcę osiągnąć)
- Emocjonalne (jak chcę się czuć)
- Socjalne (jak chcę być postrzegany)

**Output: `jobs-map.md`**
- Lista jobs z kategoryzacją
- Priorytetyzacja (częstość, intensywność bólu)

### Faza 3: Alternatives Analysis

**Input:** jobs-map.md

**Dla każdego job:**
1. Jak adresuje go Copilot?
2. Jak adresują go Gems/Custom GPTs?
3. Jak adresuje go Claude Cowork?
4. Jak adresuje go DIY (self-learning)?
5. Jak adresuję go ja (Agentic Workspace)?

**Ocena:**
- ✅ Dobrze adresuje
- ⚠️ Częściowo adresuje
- ❌ Nie adresuje

**Output: `alternatives.md`**
- Tabela jobs × alternatywy
- Analiza luk

### Faza 4: Synthesis

**Input:** jobs-map.md + alternatives.md

**Pytania do odpowiedzi:**
1. **Które jobs wygrywam?** — gdzie mam przewagę vs alternatywy
2. **Które jobs przegrywam?** — gdzie nie warto konkurować
3. **Jak komunikować?** — messaging dla wygrywanych jobs
4. **Kto jest idealnym klientem?** — profil osoby z "moimi" jobs
5. **Timeline risk** — jak szybko alternatywy mogą zamknąć lukę?

**Output: `analysis.md`**
- Podsumowanie strategiczne
- Rekomendacje
- Propozycja messaging/pozycjonowania

---

## Pliki źródłowe w workspace

### Kluczowe do przeczytania
- [dwa-modele-consulting.md](../2026-01-16-spotkanie-rudy-growgo/dwa-modele-consulting.md) — Productized vs Empowerment
- [artifacts_vs_gems_deep_dive.md](../2026-01-16-spotkanie-rudy-growgo/artifacts_vs_gems_deep_dive.md) — kiedy Gems wystarczają
- [rozmowa-mama-agnieszka](../2026-01-19-rozmowa-mama-agnieszka/notes.md) — Copilot, DIY
- [Human-Agent Collaboration Framework.md](../../concepts/Human-Agent%20Collaboration%20Framework.md) — główny framework

### Strategia
- [AI Workspace Build.md](../../strategy/offers/AI%20Workspace%20Build.md)
- [Workflow Implementation Sprints.md](../../strategy/offers/Workflow%20Implementation%20Sprints.md)
- [Strategy - AI Consultancy for Polish SME.md](../../strategy/plans/Strategy%20-%20AI%20Consultancy%20for%20Polish%20SME%20Knowledge%20Work.md)
