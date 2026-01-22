# Vision: Human-Agent Collaboration

type:: [[Vision]]
status:: Active
date-created:: 2026-01-19
related:: [[AI Workspace Build]], [[Workflow Implementation Sprints]], [[Human-Agent Collaboration Framework]]

---

## Trzy podejścia do pracy z AI

### 1. Chat (jak większość pracuje teraz)

Rozmawiasz z AI. Wklejasz kontekst, dostajesz odpowiedź, wyciągasz coś z rozmowy.

- Każda sesja zaczyna się od zera
- Kontekst ręcznie wklejany
- Output = coś co "wyciągasz" z rozmowy
- Po zamknięciu okna — zapomniane
- AI jako rozmówca, doradca

**Problem:** Nie skaluje się. Nie kumuluje wiedzy. Każdy raz od nowa.

### 2. Autonomous Agents (jak obiecuje hype)

AI robi wszystko samo. Human out of the loop. "Ustaw i zapomnij."

- Pełna autonomia agenta
- Człowiek tylko definiuje cel
- AI samo planuje i wykonuje
- Minimalna ingerencja człowieka

**Problem:** Nie działa. 70%+ failure rate w enterprise. Wymaga perfekcyjnie zdefiniowanych zadań. Brak kontroli, brak zaufania.

### 3. Human-Agent Collaboration (jak robią praktycy)

Człowiek steruje, agent wykonuje. Ani chat, ani pełna autonomia — **współpraca**.

- Agent ma kontekst (nie wklejasz — agent czyta)
- Człowiek kieruje (nie micromanagement, nie autonomia)
- Artefakty jako medium (nie chat — pliki)
- Iteracja (poprawiasz fragment, nie "od nowa")
- Wiedza kumuluje się (sesja buduje na poprzedniej)
- Checkpointy (człowiek review'uje, zatwierdza, kieruje)

**To jest trzecia droga.**

---

## Co to znaczy w praktyce?

| Chat | Autonomia | Collaboration |
|------|-----------|---------------|
| Ty piszesz, AI pomaga | AI robi, ty czekasz | Ty sterujesz, agent wykonuje |
| Kontekst w głowie | Kontekst "jakoś" | Kontekst w plikach |
| Output = fragment rozmowy | Output = "magia" | Output = artefakt |
| Każda sesja od zera | Agent sam pamięta (?) | Pliki pamiętają |
| Kontrola pełna | Kontrola żadna | Kontrola przez checkpointy |

---

## Nasza wizja

**Human-Agent Collaboration** — sposób pracy gdzie:

1. **Człowiek jest kierownikiem** — decyduje co, po co, czy dobrze
2. **Agent jest wykonawcą** — produkuje output, robi research, iteruje
3. **Kontekst jest zeksternalizowany** — wiedza w plikach, nie w głowie
4. **Artefakty są medium** — praca żyje w plikach, nie w chatach
5. **Wiedza się kumuluje** — każda sesja buduje na poprzedniej

To nie jest automatyzacja (zastępowanie ludzi).
To jest **amplifikacja** (ludzie robią więcej, lepiej, szybciej).

---

## Nasza metoda: Building Agentic Workspaces

Żeby Human-Agent Collaboration działała, potrzebne jest **środowisko** które ją umożliwia.

**Agentic Workspace** = struktura + kontekst + instrukcje + szablony

```
workspace/
├── CLAUDE.md           # Instrukcje dla agenta
├── context/            # Wiedza domenowa
├── templates/          # Szablony artefaktów
├── skills/             # Zdefiniowane workflow'y
└── projects/           # Aktywna praca
```

**Co daje workspace:**
- Agent "zna" twój kontekst bez wklejania
- Masz szablony dla powtarzalnych artefaktów
- Workflow'y są zdefiniowane i powtarzalne
- Wiedza kumuluje się w plikach

**My budujemy takie workspace'y.**

---

## Dla kogo to jest

### Idealny klient

**Knowledge worker / mały zespół ekspertów** który:
- Robi złożoną pracę intelektualną
- Ma specjalistyczną wiedzę domenową
- Tworzy powtarzalne typy artefaktów
- Chce pracować efektywniej z AI
- Jest gotowy na zmianę sposobu pracy

### Przykłady

- Lekarz-badacz (papers, analizy, literature review)
- Prawnik (opinie prawne, due diligence, umowy)
- Konsultant (analizy, rekomendacje, strategie)
- Researcher (synteza, raporty)

### Antyprofil

- "Zróbcie za mnie" — chcą outsource, nie capability
- "AI ma działać samo" — oczekują autonomii która nie działa
- Brak czasu na współpracę przy budowie

---

## Nasze oferty

**[[AI Workspace Build]]**
Budujemy kompletne środowisko pracy z AI. Struktura, kontekst, szablony, skille. Klient wychodzi z działającym workspace'em i umiejętnością jego rozwijania.

**[[Workflow Implementation Sprints]]**
Wdrażamy jeden konkretny workflow. Głęboko, porządnie, z dokumentacją i szkoleniem.

**Productized Workspaces** *(w rozwoju)*
Gotowe workspace'y z wbudowaną metodologią ekspercką. Metodologia + infrastruktura w jednym.

---

## Key Vocabulary

**Human-Agent Collaboration**
Sposób pracy gdzie człowiek steruje, agent wykonuje. Trzecia droga między chatem a autonomią.

**Agentic Workspace**
Środowisko (folder + pliki + instrukcje) w którym collaboration działa. Zawiera kontekst, szablony, workflow'y.

**Context Engineering**
Umiejętność organizacji wiedzy tak, żeby agent mógł jej użyć.

**Artefakt**
Plik który jest outputem pracy. Checkpoint, deliverable. Przeciwieństwo "rozmowy w chacie".

---

## Links

- [[concepts/Human-Agent Collaboration Framework]] — teoretyczny framework
- [[strategy/offers/AI Workspace Build]] — główna oferta
- [[strategy/offers/Workflow Implementation Sprints]] — oferta workflow'owa
- [[strategy/positioning/Strategy - Show Dont Tell Demo Approach]] — jak sprzedajemy
