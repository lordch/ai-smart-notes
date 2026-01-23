# Mapowanie Framework'u Human-Agent Collaboration na Narzędzia

## Narzędzia w analizie

| Narzędzie | Charakterystyka |
|-----------|-----------------|
| **Chat** | ChatGPT web, Claude.ai bez projektów — czysta konwersacja |
| **CustomGPT/Gem** | Skonfigurowany chat z instrukcjami i opcjonalnie plikami |
| **Copilot** | M365 integration, dostęp do SharePoint, tworzy dokumenty |
| **Cowork** | Claude z task queue, MCP connectorami, skills |
| **Claude Code CLI** | Agent z filesystem access, bez GUI file browser |
| **Agentic IDE** | Cursor, CC w VS Code, Antigravity — pełna integracja |

---

## Część I: Mechanizmy Frameworku × Narzędzia

### Legenda
- ✓ = obsługuje natywnie
- ~ = częściowo / z workaroundem
- ✗ = nie obsługuje

### Tabela główna

| Mechanizm | Chat | GPT/Gem | Copilot | Cowork | CC CLI | Agentic IDE |
|-----------|:----:|:-------:|:-------:|:------:|:------:|:-----------:|
| **Transparentność** | ✗ | ✗ | ~ | ~ | ✓ | ✓ |
| **Checkpointing** | ✗ | ✗ | ~ | ~ | ✓ | ✓ |
| **Alignment** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Steering** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Dekompozycja** | ✗ | ✗ | ~ | ✓ | ✓ | ✓ |
| **Progressive Disclosure** | ✗ | ~ | ~ | ~ | ✓ | ✓ |
| **Context Isolation** | ✗ | ~ | ~ | ✓ | ✓ | ✓ |
| **Artefakty (persistence)** | ✗ | ✗ | ~ | ✓ | ✓ | ✓ |

### Tabela: Wymagania UX (Dual Interface)

| Wymóg UX | Chat | GPT/Gem | Copilot | Cowork | CC CLI | Agentic IDE |
|----------|:----:|:-------:|:-------:|:------:|:------:|:-----------:|
| **Chat** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| **File reader** | ✗ | ~ | ✓ | ✓ | ✓ | ✓ |
| **File editor** | ✗ | ✗ | ✗ | ~ | ✓ | ✓ |
| **File browser** | ✗ | ✗ | ~ | ✗ | ✗ | ✓ |
| **Dual editability** | ✗ | ✗ | ✗ | ~ | ✓ | ✓ |
| **Diff visibility** | ✗ | ✗ | ✗ | ? | ✓ | ✓ |
| **Drag & drop context** | ✗ | ~ | ~ | ~ | ✗ | ✓ |
| **Wszystko w 1 oknie** | ✓ | ✓ | ~ | ✓ | ~ | ✓ |

---

## Część II: Szczegółowa analiza per narzędzie

### 1. Chat (ChatGPT web, Claude.ai)

**Co ma:**
- Konwersacja (alignment, steering)
- Szybki start, zero setup

**Czego brakuje:**
- Wszystkiego poza chatem
- Artefakty = historia chatu (giną, nie można edytować)
- Zero persistence między sesjami

**Konsekwencje braków:**
- Context rot nieunikniony
- Każda sesja od zera
- Copy-paste jako jedyny "checkpoint"
- Drift bez kotwicy

**Nadaje się do:**
- Jednorazowe pytania
- Brainstorming bez konsekwencji
- Szybkie transformacje tekstu

---

### 2. CustomGPT / Gem

**Co ma:**
- Instrukcje persystentne (pseudo-CLAUDE.md)
- Upload plików jako kontekst
- Alignment i steering przez chat

**Czego brakuje:**
- Edycja artefaktów (output = tekst w chacie)
- File browser (nie widzisz struktury)
- Diff visibility
- Prawdziwy checkpointing

**Konsekwencje braków:**
- "Zmień punkt 3" → regeneruje cały dokument
- Context rot po ~30 wymianach
- Brak chirurgicznej edycji
- Copy-paste między Gemami = manual context transfer

**Nadaje się do:**
- Powtarzalne zadania z ustalonym formatem
- Single-session work (mail, tłumaczenie, analiza)
- Prototypowanie workflow'ów

---

### 3. Copilot (M365)

**Co ma:**
- Integracja z SharePoint (kontekst "out of the box")
- Dostęp do plików organizacji
- Tworzy dokumenty

**Czego brakuje:**
- Edycja istniejących dokumentów
- File browser + chat + editor w jednym oknie
- Diff visibility
- Izolacja kontekstu (brak task queue)

**Konsekwencje braków:**
- Brak iteracji na artefakcie — każda zmiana = nowy dokument
- Trudna weryfikacja (musisz otworzyć Word/Excel osobno)
- Context switching między aplikacjami
- Nie nadaje się do long-running tasks z wieloma źródłami

**Nadaje się do:**
- Szybkie drafty w kontekście firmy
- Summarization dokumentów SharePoint
- Q&A po bazie wiedzy organizacji
- Użytkownicy nietechniczni w ekosystemie M365

---

### 4. Cowork

**Co ma:**
- Task queue (izolacja kontekstu per task)
- MCP connectors (Google Slides, browser, etc.)
- Skills (nauczanie przez nagranie)
- Artefakty per task

**Czego brakuje:**
- File browser w interfejsie
- Wiele wątków w jednym tasku
- Diff visibility (?)
- Manualne przeciąganie plików do kontekstu

**Konsekwencje braków:**
- Checkpointing = zamknięcie taska + nowy task
- Nie widzisz struktury workspace'u
- Trudniej o progressive disclosure (nie przeglądasz plików)
- Context isolation wymaga manualnego zarządzania taskami

**Nadaje się do:**
- Automatyzacja z connectorami (Slides, Sheets)
- Task-based work (jasno zdefiniowane zadania)
- Workflow'y z narzędziami zewnętrznymi
- Użytkownicy chcący agenta bez IDE

---

### 5. Claude Code CLI

**Co ma:**
- Pełny dostęp do filesystem (read, write, edit)
- Dual editability (agent i ty edytujecie te same pliki)
- Diff visibility (git integration)
- Checkpointing natywny (pliki)
- Context isolation (nowa sesja = czysty kontekst)
- CLAUDE.md jako instrukcje

**Czego brakuje:**
- GUI file browser (musisz znać ścieżki lub agent nawiguje)
- Drag & drop context (dodajesz pliki przez @mention lub polecenie)
- Wizualne "jedno okno" (terminal + edytor osobno)

**Konsekwencje braków:**
- Wyższy próg wejścia (CLI comfort required)
- Mniej intuicyjne dodawanie kontekstu
- Context switching: terminal ↔ edytor ↔ browser

**Nadaje się do:**
- Praca z kodem
- Power users comfortable z CLI
- Long-running projects z git
- Maksymalna kontrola nad kontekstem

---

### 6. Agentic IDE (Cursor, CC w VS Code, Antigravity)

**Co ma:**
- Wszystko w jednym oknie: chat + file browser + editor
- Drag & drop plików do kontekstu
- Diff visibility natywny
- Dual editability
- Checkpointing przez pliki
- Context isolation (nowe okno/projekt)
- Progressive disclosure (przeglądasz, wybierasz co dodać)
- CLAUDE.md / .cursorrules

**Czego brakuje:**
- Wymaga instalacji i konfiguracji
- Learning curve dla nie-programistów
- Mniej intuicyjne dla użytkowników Word/Google Docs

**Konsekwencje braków:**
- Nie dla każdego odbiorcy
- Trudniejsza sprzedaż do korporacji
- Wymaga zmiany nawyków (IDE zamiast Word)

**Nadaje się do:**
- Złożone projekty z wieloma źródłami
- Long-running work (tygodnie/miesiące)
- Pełna kontrola i przejrzystość
- Knowledge work wymagający iteracji

---

## Część III: Mapa Mechanizmów → Konsekwencje Braków

| Brakujący mechanizm | Konsekwencja |
|---------------------|--------------|
| **Transparentność** | Nie wiesz na czym agent pracuje → trudna weryfikacja → ryzyko halucynacji |
| **Checkpointing** | Context rot → drift → każda sesja od zera |
| **Artefakty** | Output ginie w chacie → brak kumulacji → copy-paste hell |
| **File editor** | "Zmień X" = regeneruj całość → ryzyko regresji → brak chirurgii |
| **File browser** | Nie widzisz struktury → trudny progressive disclosure → ślepe dodawanie kontekstu |
| **Diff visibility** | Nie wiesz co się zmieniło → trudna weryfikacja → przepuszczasz błędy |
| **Dual editability** | Tylko agent edytuje LUB tylko ty → brak prawdziwej collaboration |
| **Context isolation** | Historia jednego zadania zaśmieca drugie → drift między taskami |

---

## Część IV: Rekomendacje — Które Narzędzie do Jakiej Pracy

### Single Session Viability Test

> Czy zadanie da się wykonać w jednej sesji bez utraty jakości?

**TAK → Chat / Gem / Copilot**
- Email, tłumaczenie, analiza CSV
- Brainstorming, ideacja
- Q&A po dokumentach

**NIE → Cowork / CC CLI / Agentic IDE**
- Projekty wielodniowe
- Dokumenty wymagające iteracji
- Research z wieloma źródłami
- Workflow'y z checkpointami

### Matryca: Typ pracy × Narzędzie

| Typ pracy | Rekomendacja | Dlaczego |
|-----------|--------------|----------|
| **Jednorazowy draft** | Chat, Gem | Szybko, zero setup |
| **Powtarzalny format** | Gem, Copilot | Instrukcje persystentne |
| **Q&A po dokumentach firmy** | Copilot | SharePoint integration |
| **Automatyzacja z narzędziami** | Cowork | MCP connectors |
| **Kod, development** | CC CLI, Agentic IDE | Full filesystem access |
| **Long-running knowledge work** | Agentic IDE | Wszystkie mechanizmy |
| **Research z wieloma źródłami** | Agentic IDE | Progressive disclosure + isolation |
| **Iteracyjny dokument** | Agentic IDE | Dual editability + diff |
| **Wniosek grantowy** | Agentic IDE | Checkpointing + wiele źródeł |
| **Strategia/analiza** | Agentic IDE | Context isolation + artefakty |

### Matryca: Odbiorca × Narzędzie

| Odbiorca | Rekomendacja | Dlaczego |
|----------|--------------|----------|
| **Każdy** | Chat | Zero setup |
| **Powtarzalni użytkownicy** | Gem | Custom instructions |
| **Pracownik korporacji M365** | Copilot | Już w ekosystemie |
| **Tech-savvy, nie-programista** | Cowork | Task queue bez IDE |
| **Developer** | CC CLI | Naturalny workflow |
| **Knowledge worker power user** | Agentic IDE | Maksymalna kontrola |

---

## Część V: Podsumowanie — Spektrum Narzędzi

```
MNIEJ KONTROLI ←―――――――――――――――――――――――――――→ WIĘCEJ KONTROLI
NIŻSZY PRÓG    ←―――――――――――――――――――――――――――→ WYŻSZY PRÓG

Chat → Gem/GPT → Copilot → Cowork → CC CLI → Agentic IDE
 │        │         │         │        │          │
 │        │         │         │        │          └── Wszystko w 1 oknie
 │        │         │         │        └── Filesystem, brak GUI
 │        │         │         └── Task queue, connectors
 │        │         └── M365 integration, brak edycji
 │        └── Instrukcje, brak persistence
 └── Czysta konwersacja
```

### Kluczowy insight

**Im bardziej złożone zadanie, tym więcej mechanizmów potrzebujesz.**

- Proste zadanie (email) → wystarczy chat
- Średnie zadanie (raport) → Gem/Copilot + manualne checkpointy
- Złożone zadanie (strategia) → Agentic IDE z pełnym frameworkiem

**Agentic IDE to jedyne narzędzie które natywnie wspiera wszystkie mechanizmy frameworku.**

Pozostałe narzędzia wymagają workaroundów (copy-paste, manualne zarządzanie, context switching) które:
- Zwiększają cognitive load
- Wprowadzają ryzyko błędu
- Ograniczają skalę możliwych zadań

---

*Mapowanie v1.0 — Styczeń 2026*
