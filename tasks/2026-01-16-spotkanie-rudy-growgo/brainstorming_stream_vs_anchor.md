# Brainstorming: Stream vs Anchor (Chat vs Artifact)

To jest kluczowa różnica dla biznesu, nie "Action vs Advice", ale **"Mutable Stream vs Immutable Anchor"**.

## 1. Context Hygiene (Higiena Myślenia)
- **Chat/Gem (Stream):** "Śmietnik myślowy". Każda dygresja, pomyłka, poprawka zostaje w kontekście. Model "widzi" historię błędów, co zwiększa szansę na ich powtórzenie.
- **Artifact (Anchor):** "Czysty stan". Plik na dysku zawiera tylko to, co *zaakceptowaliśmy*.
    - **Proces:** Agent czyta czysty plik -> Wykonuje zadanie -> Zapisuje.
    - W następnym kroku agent nie widzi "bólu rodzenia" tego pliku, widzi tylko efekt. To drastycznie podnosi jakość (Garbage Collection dla kontekstu).

## 2. Surgical Precision vs Rewrite Risk
- **Chat:** "Zmień punkt 3". Model często generuje cały tekst od nowa. Ryzyko: przy okazji zmieni słowo w punkcie 1, co w korporacji (umowy!) jest niedopuszczalne.
- **Artifact (Filesystem):** Agent robi "chirurgiczną zmianę" (diff) w pliku. Reszta dokumentu jest *nienaruszona*. To jest **bezpieczeństwo procesu**.

## 3. Multi-Threading & Distillation
- **Koncept:** "Utrwalasz tylko to, co warte utrwalenia".
- Możliwość pracy **równoległej**:
    - Otwierasz Chat A: "Wymysł mi 10 nagłówków do tego artykułu". Wybierasz jeden, zapisujesz w pliku.
    - Otwierasz Chat B: "Sprawdź ten artykuł pod kątem prawnym".
    - Chat A nie widzi uwag prawnych, Chat B nie widzi burzy mózgów o nagłówkach.
    - **Plik jest punktem styku (Checkpointem), a nie historia czatu.**

## 4. Process State Management
- Gem "zapomina" stan po zamknięciu okna (lub po przekroczeniu limitu tokenów).
- Plik markdown w folderze projektu "pamięta" stan przez lata.
- To pozwala na procesy trwające tygodniami (Long-running processes), a nie minutami.

## 5. Granica Decyzyjna: "Single Session Viability Test"
Kiedy Gem/Chat wystarczy, a kiedy potrzebny jest Context Engineering (Filesystem)?

**Kryterium:** Czy zadanie da się wykonać w **jednej sesji czatu**, bez przenoszenia kontekstu i bez utraty jakości (zapominania szczegółów)?

- **TAK (Single Session Safe):**
    - Użyj Gema / Custom GPT.
    - Przykłady: "Napisz maila", "Przeanalizuj wklejony CSV", "Wytłumacz pojęcie".
    - Kontekst jest ulotny i to jest OK.

- **NIE (Multi-Session Required):**
    - Użyj Context Engineering (System Plików).
    - Przykłady: "Napisz książkę", "Zarządzaj projektem przez kwartał", "Stwórz specyfikację systemu", "Rozwijaj bazę wiedzy firmy".
    - Tutaj "Stream" (Chat) staje się wrogiem ("Context Rot"), a "Anchor" (Plik) jest koniecznością.
    - Context Engineering to technologia umożliwiająca **przekraczanie granic pojedynczej sesji**.
