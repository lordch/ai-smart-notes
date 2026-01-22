# Situational Leadership dla nadzoru agenta AI

Adaptacja modelu przywództwa sytuacyjnego Blancharda na Human-Agent Collaboration.

## Główna idea

Nie ma jednego "najlepszego" poziomu autonomii agenta — skuteczny operator dopasowuje styl nadzoru do **kompetencji agenta w danym zadaniu**.

## Kompetencje agenta są TASK-SPECIFIC

Kluczowy insight z Blancharda: kompetencje oceniamy per-zadanie, nie ogólnie.

**Nie:** "Claude jest D4"
**Tak:** "Claude z tym kontekstem, w tym zadaniu, jest D4"

### Co składa się na kompetencje agenta:

1. **Kontekst** — czy agent ma wiedzę potrzebną do TEGO zadania
2. **Capabilities modelu** — czy ten typ zadania jest w wheelhouse modelu

### Halo effect dla AI

Klasyczny błąd: "Claude świetnie pisze kod, więc ogarnie legal review"

Każde nowe zadanie = nowa diagnoza kompetencji.

### Regresja

Agent może "spaść" w kompetencjach gdy:
- Zadanie wychodzi poza kontekst → hallucynacje
- Edge case którego nie przewidziałeś
- Zmiana domeny/branży

## Style nadzoru

| Kompetencje agenta | Styl | Praktycznie |
|-------------------|------|-------------|
| **Niskie** (brak kontekstu, trudne zadanie) | S1 Directing | Step-by-step prompts, review każdego kroku, konkretne przykłady |
| **Średnie** (częściowy kontekst) | S2 Coaching | Instrukcje + "pokaż mi plan przed wykonaniem" |
| **Wysokie ale nowe** (dobry kontekst, nowy workflow) | S3 Supporting | "Zrób i pokaż, poprawimy razem" |
| **Wysokie i sprawdzone** (kontekst + przetestowany workflow) | S4 Delegating | Jeden prompt → review outputu |

## Directive behavior

**Wysokie directive** (niskie kompetencje agenta):
- Mówisz CO i JAK
- Konkretne kroki
- Częste checkpointy
- Dajesz przykłady

**Niskie directive** (wysokie kompetencje agenta):
- Mówisz CO, nie JAK
- Autonomia w metodzie
- Sprawdzasz output, nie proces

## Kluczowy wniosek

Im wyższe kompetencje agenta, tym rzadziej wchodzisz w PROCES, częściej oceniasz tylko OUTPUT.

**Context Engineering = budowanie kompetencji agenta per-task.**

---

*Inspiracja: Ken Blanchard, Situational Leadership II (SLII)*
