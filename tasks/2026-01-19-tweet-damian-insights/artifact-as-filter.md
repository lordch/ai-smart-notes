# Artefakt jako filtr (nie jako format)

type:: rozkmina
date-created:: 2026-01-19
source:: tweet @damianplayer, rozmowa o stream vs anchor
related:: [[brainstorming_stream_vs_anchor]]

---

## Kontekst

Tweet Damiana o "vibe coding" z Claude Code zawiera insight:
> "Błędy to nie porażka — to iteracja. Build, error, fix, repeat."

Ale jeśli iterujesz w chacie, **gromadziś błędy w kontekście**. Agent widzi historię twojego męczenia się.

To rozwija myśl z [[brainstorming_stream_vs_anchor]] o "Context Hygiene".

---

## Co było w stream vs anchor

Kluczowe punkty z poprzedniej notatki:

1. **Context Hygiene** — chat to "śmietnik myślowy", artefakt to "czysty stan"
2. **Surgical Precision** — chat ryzykuje rewrite, artefakt pozwala na diff
3. **Multi-Threading** — równoległe chaty, plik jako punkt styku
4. **Process State** — plik pamięta latami, chat zapomina

---

## Co ta notatka dodaje: Artefakt jako SELEKCJA

### Dwa tryby pracy iteracyjnej

W każdej pracy intelektualnej są dwa tryby:
1. **Eksploracja** — szukasz, próbujesz, błądzisz, produkujesz noise
2. **Eksploatacja** — masz coś dobrego, budujesz dalej

Chat jest świetny do eksploracji.
Ale kiedy przechodzisz do eksploatacji, chat staje się **ciężarem** — niesie bagaż eksploracji.

### Artefakt to granica

**Artefakt = świadoma decyzja: "TO jest warte zachowania"**

Kiedy zapisujesz do pliku, robisz selekcję. Filtr. Zostawiasz signal, odrzucasz noise.

W chacie nie ma tej granicy. Wszystko płynie w strumieniu. Append-only.

### Perspektywa agenta

| | Chat | Artefakt |
|---|---|---|
| Co widzi agent | Historię bólu | Tylko efekt |
| Następna sesja | Zaczyna z bagażem | Zaczyna czysto |
| Signal/noise | Wymieszane | Przefiltrowane |

> "Chat pamięta twoje błędy. Artefakt pamięta twój sukces."

---

## Implikacja dla wartości agentic workspace

To jest **uniwersalna wartość** — nie wymaga kodowania, nie wymaga techniczności.

Każdy knowledge worker:
- Iteruje nad tekstami, analizami, planami
- Produkuje noise w procesie
- Potrzebuje sposobu na odfiltrowanie noise'u

Chat zachowuje noise.
Artefakt go filtruje.

**To nie jest o narzędziach. To jest o higienie myślenia.**

---

## Sformułowania

> "Artefakt to garbage collection dla kontekstu."

> "Iterujesz w chacie, ale ZACHOWUJESZ w artefakcie. To różnica między burzą mózgów a decyzją."

> "Artefakt to checkpoint — następna sesja zaczyna od dobrego miejsca, nie od historii jak tam dotarłeś."
