# Literature - Anthropic Context Engineering

**Źródło:** [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
**Autor:** Anthropic Engineering
**Data dostępu:** 2026-01-26

---

## 1. Definicja Context Engineering

**Context** = zbiór tokenów dostarczanych do modelu podczas inferencji.

**Context engineering** = strategiczne kuratorowanie i utrzymywanie optymalnego zestawu tokenów podczas działania LLM. Obejmuje: system instructions, tools, external data, message history.

> Kluczowa zasada: "finding the smallest set of high-signal tokens that maximize the likelihood of desired outcome."

Context engineering to naturalna ewolucja prompt engineeringu — przejście od tworzenia pojedynczych promptów do **zarządzania całym stanem informacyjnym** w wieloturowych interakcjach agenta.

---

## 2. Kluczowe Strategie

### 2.1 System Prompts

- Używaj prostego, bezpośredniego języka na "właściwej wysokości" — wystarczająco konkretnie żeby kierować zachowaniem, ale elastycznie żeby model mógł sam rozumować
- Unikaj kruchej logiki if-else i zbyt ogólnych wskazówek
- Organizuj w wyraźne sekcje używając tagów XML lub nagłówków Markdown (`<background_information>`, `<instructions>`, `## Tool guidance`)
- **Zacznij minimalnie**, potem dodawaj instrukcje bazując na obserwowanych failure modes

### 2.2 Tools

- Projektuj **self-contained tools** z minimalnym nakładaniem się funkcjonalności
- Zapewnij jasność co do intended use i parametrów
- Unikaj rozdętych zestawów narzędzi tworzących niejednoznaczne punkty decyzyjne
- **Test:** jeśli człowiek nie wie którego narzędzia użyć, agent też będzie miał problem

### 2.3 Few-Shot Prompting

- Kuratoruj **diverse, canonical examples** zamiast wyczerpujących list edge cases
- Przykłady działają jak "obrazki" — komunikują oczekiwane zachowanie efektywniej niż opis

### 2.4 Context Retrieval: Just-In-Time

Zamiast pre-loadować wszystkie relevantne dane, utrzymuj **lightweight identifiers** (file paths, URLs, queries) i dynamicznie pobieraj informacje w runtime używając tools.

Naśladuje ludzką kognicję i umożliwia:
- **Progressive disclosure** przez incremental discovery
- Zmniejszenie obciążenia working memory
- **Metadata-driven behavior** — hierarchie folderów, konwencje nazewnictwa, timestamps dają ważne sygnały

**Trade-off:** Runtime exploration jest wolniejszy niż pre-computed retrieval, ale redukuje context pollution.

---

## 3. Techniki dla Long-Horizon Tasks

### 3.1 Compaction

Podsumowuj historię konwersacji gdy zbliżasz się do limitów kontekstu:
- Zachowuj **architekturalne decyzje** i nierozwiązane problemy
- Usuwaj redundantne outputy
- Zacznij od maksymalizacji recall, potem iteruj żeby poprawić precision
- **Tool result clearing** = lekka wersja compaction

### 3.2 Structured Note-Taking

Agenty utrzymują **zewnętrzne pliki pamięci** (NOTES.md, to-do lists) śledzące progress w złożonych zadaniach.

> Przykład: Claude grający w Pokémon utrzymywał precyzyjne tallies przez tysiące kroków, umożliwiając koherencję w wielogodzinnych taskach.

### 3.3 Sub-Agent Architectures

Wyspecjalizowani agenci obsługują focused tasks z czystymi context windows, zwracając **condensed summaries** (1,000-2,000 tokenów) do koordynującego agenta.

Korzyść: izolacja detailed exploration od high-level synthesis.

---

## 4. Cytaty warte zapisania

> "finding the smallest set of high-signal tokens that maximize the likelihood of desired outcome"

> Context engineering = "strategically curating and maintaining the optimal token set during LLM operation"

> "do the simplest thing that works"

> "Smarter models require less prescriptive engineering, enabling greater autonomy"

> Context to "precious, finite resource"

---

## 5. Relevance dla budowania AI Workspace

### Potwierdzenia mojego podejścia

1. **Context is the work** — Anthropic potwierdza że kuratorowanie kontekstu to kluczowy lever dla performance agentów. Moja teza o "manual context curation is the work" jest zgodna z ich framingiem.

2. **Metadata matters** — hierarchie folderów, konwencje nazewnictwa jako sygnały dla agenta. Moja struktura `sources/ → literature/ → concepts/ → strategy/` to dokładnie taki metadata-driven design.

3. **Structured note-taking** — zewnętrzne pliki pamięci (NOTES.md, to-do) jako technika dla long-horizon tasks. Mój folder `tasks/` z checkpointami to implementacja tej zasady.

4. **Just-in-time retrieval** — lepsze niż pre-loading wszystkiego. Moje podejście z CLAUDE.md jako "entry point" + agentyczne eksplorowanie folderów jest zgodne.

### Implikacje dla oferty

1. **AI Workspace Build** = implementacja context engineering principles:
   - Struktura folderów = metadata layer
   - CLAUDE.md = system prompt dla workspace
   - Konwencje nazewnictwa = navigational signals
   - Tasks = structured note-taking infrastructure

2. **Context rot** jako argument biznesowy — wyjaśnia dlaczego duże context windows nie rozwiązują problemu. Klient potrzebuje **organizacji**, nie tylko pojemności.

3. **"Right altitude"** jako zasada projektowania instrukcji — wystarczająco konkretnie żeby kierować, elastycznie żeby agent mógł rozumować. Przydatne do projektowania CLAUDE.md dla klientów.

### Terminologia do adopcji

- **Context engineering** (zamiast prompt engineering) — lepiej opisuje co robimy
- **Context rot** — użyteczny termin na wyjaśnianie problemów z długimi sesjami
- **Progressive disclosure** — opisuje jak agent powinien eksplorować workspace

---

## Linki do moich konceptów

- [[Human-Agent Collaboration Framework]] — context engineering to implementacja "Factual context curation"
- [[Agentic Workspace]] — workspace jako medium dla context engineering
