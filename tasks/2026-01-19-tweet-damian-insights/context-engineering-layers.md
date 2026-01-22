# Context Engineering: Warstwy i pułapki

type:: rozkmina
date-created:: 2026-01-19
source:: tweet @damianplayer, własne przemyślenia
related:: [[artifact-as-filter]], [[Human-Agent Collaboration Framework]]

---

## Definicja robocza

**Context engineering** = dostarczenie agentowi kontekstu z jak najwyższym signal-to-noise ratio.

To jest oś myślenia o pracy z AI. Nie "jak promptować" — ale "jak zbudować środowisko, w którym agent ma to, czego potrzebuje".

---

## Trzy warstwy context engineeringu

### Warstwa 1: Daj kontekst (maksymalizuj signal)

Kontekst pochodzi z dwóch źródeł:

**A. Zeksternalizowany** — już istnieje w formie plików, dokumentów, linków:
- Metodologie, frameworki
- Wiedza domenowa, case studies
- Kontekst organizacyjny (jak działamy, co ważne)
- Kontekst projektu (pliki, specyfikacje, historia)

To możesz po prostu **wrzucić, zalinkować, zorganizować w workspace**.

**B. W twojej głowie** — twoje intencje, wymagania, kryteria sukcesu:
- Co właściwie chcę osiągnąć?
- Jakie są moje preferencje?
- Co jest ważne, a co nice-to-have?
- Jakie są ograniczenia?

Tego **nie możesz wrzucić** — musisz to **wyartykułować**.

### Warstwa 2: Nie zaśmiecaj kontekstu (minimalizuj noise)

Tu wchodzi insight o chacie jako "zaśmiecaczu":

- Każda iteracja w chacie dodaje noise
- Każdy błąd, każda poprawka zostaje w kontekście
- Agent widzi historię bólu, nie tylko efekt

**Artefakt jako filtr** — zapisujesz tylko to, co warte zachowania.
(→ szczegóły w [[artifact-as-filter]])

### Warstwa 3: Izoluj konteksty (?)

Wstępna myśl:
- Różne zadania wymagają różnych kontekstów
- Mieszanie kontekstów może wprowadzać szum
- Multi-threading z pliku stream vs anchor: równoległe chaty, plik jako punkt styku

Do rozwinięcia.

---

## Pułapka: Assumptions manifest as bugs

Z tweeta Damiana:
> "AI makes assumptions. Lots of them. When you skip the planning step, those assumptions become bugs you fix later."

### Dlaczego agent robi założenia?

Agent jest **chętny do wykonania zadania**. To jest wbudowane w jego konstrukcję — helpfulness.

Kiedy czegoś nie wie (bo nie dałeś kontekstu), nie pyta — **zakłada**.

Im mniej kontekstu z warstwy 1B (twoje intencje), tym więcej założeń.

### Plan jako płaszczyzna weryfikacji

**Plan/spec to nie tylko struktura pracy — to płaszczyzna alignmentu.**

Kiedy agent pisze plan:
- Ujawnia swoje założenia
- Możesz zobaczyć gdzie się rozmijasz
- Możesz skorygować ZANIM zacznie implementować

> "Taniej zweryfikować krótki plan niż długą realizację."

### Kiedy to jest krytyczne?

Szczególnie w zadaniach:
- **Autonomicznych** — agent wykonuje wiele kroków bez twojej interwencji
- **Multi-step** — research w wielu źródłach, złożone analizy
- **Z ukrytą złożonością** — wyglądają prosto, ale mają wiele możliwych interpretacji

Ale nawet w one-shotach — weryfikacja planu unika iteracji, czyli unika zaśmiecania kontekstu (warstwa 2).

---

## Flow

```
1. Daj kontekst (maksymalizuj signal)
   - Zeksternalizowany → workspace, pliki
   - Z głowy → wyartykułuj wymagania

2. Nie zaśmiecaj (minimalizuj noise)
   - Artefakt jako filtr
   - Zapisuj tylko to, co warte zachowania

3. Weryfikuj założenia (alignment)
   - Plan przed realizacją
   - Spec jako kontrakt
   - Taniej skorygować plan niż realizację

4. Izoluj konteksty (?)
   - Różne zadania = różne konteksty
   - Do rozwinięcia
```

---

## Otwarte pytania

- Jak praktycznie izolować konteksty?
- Kiedy plan jest overhead, a kiedy oszczędnością?
- Jak uczyć tego ludzi bez technicznego backgroundu?
