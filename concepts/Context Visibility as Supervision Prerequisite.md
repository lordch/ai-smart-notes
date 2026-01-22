# Context Visibility as Supervision Prerequisite

Żeby skutecznie nadzorować agenta, musisz widzieć co agent wie.

## Główna teza

Situational Leadership (Blanchard) mówi: dobierz styl zarządzania do kompetencji pracownika w danym zadaniu.

Dla agenta AI, kompetencje = **kontekst + capabilities modelu**.

Capabilities modelu znasz (to stała). Kontekst — musisz widzieć.

**Jeśli nie widzisz kontekstu, nie możesz wybrać stylu nadzoru.**

## Workspace vs Autonomous Agent

| Wymiar | Agentic Workspace | Autonomous Agent (RAG/Gems) |
|--------|-------------------|----------------------------|
| Widzisz kontekst? | Tak — pliki w folderze | Nie — black box retrieval |
| Możesz dodać kontekst? | Tak — edytujesz pliki | Częściowo — system prompt |
| Możesz usunąć kontekst? | Tak — nowa sesja / usuń plik | Nie wiesz co usunąć |
| Możesz dobrać styl nadzoru? | Tak | Zgadujesz |

## Epistemic transparency

Workspace daje **epistemic transparency** — wiesz co agent wie, więc:
1. Możesz dobrać styl nadzoru (S1-S4)
2. Możesz dodać brakujący kontekst
3. Możesz zaufać outputowi (bo znasz input)

Autonomous agent z automatycznym retrieval to **epistemic black box**.

## Implikacja

Manual context curation to nie "ograniczenie do przezwyciężenia". To **warunek konieczny** efektywnego nadzoru.

---

*Powiązane:*
- [[Situational Leadership dla nadzoru agenta AI]]
- [[Manual context curation is the work]]
- [[Supervision is context curation, not action approval]]
