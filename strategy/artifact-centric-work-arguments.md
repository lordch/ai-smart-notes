# Argumentacja: Dlaczego Artefakty? (vs Chat)

**Cel:** Syntetyczne zestawienie argumentów za pracą na plikach (Agentic Workspace), wsparte konkretnymi przykładami z kursu `ccforeveryone`.
**Dla kogo:** Dla osób wahających się między "szybkim chatem" (ChatGPT/Gemini) a "systemem pracy" (Claude Code/Cursor).

---

## 1. Higiena Kontekstu: "Stream vs Anchor"
*Teoria: [[brainstorming_stream_vs_anchor]], [[artifact-as-filter]]*

### Argument
Chat to **strumień** (Stream). Pamięta wszystko: Twoje błędy, wahania, literówki i ślepe uliczki ("nie, jednak zrób to inaczej"). Model "widzi" historię Twojego męczenia się, co "zatruwa" kontekst (Context Rot).
Artefakt to **kotwica** (Anchor). To "czysty stan", który zapisałeś. Odcina historię powstawania.

### Dowód z `ccforeveryone`
*   **Case: "Interview Planning" (Ross Mike)**
    *   **Proces:** Długa, chaotyczna rozmowa (wywiad), w której użytkownik miota się co do wymagań.
    *   **Mechanizm:** Zamiast kazać agentowi "pamiętać rozmowę", finałem jest plik `REQUIREMENTS.md`.
    *   **Zysk:** Agent wykonawczy (Builder) dostaje CZYSTY plik `REQUIREMENTS.md`. Nie widzi 40 minut wahań użytkownika. Dzięki temu kod jest czysty, a nie "zbiasedowany" wątpliwościami z czatu.
    *   **Metafora:** Artefakt to "Garbage Collection" dla Twoich myśli.

---

## 2. Pamięć Instytucjonalna: "Compounding Knowledge"
*Teoria: [[teresa-torres-arguments]], [[artefakty-vs-gems-esej]]*

### Argument
Chat jest **transakcyjny** (Single Session). Wiedza znika (lub staje się nieosiągalna) po zamknięciu okna. Zaczynasz od zera.
Artefakty są **kumulatywne**. Każdy projekt buduje na poprzednim. Wiedza "procentuje".

### Dowód z `ccforeveryone`
*   **Case: "Turnaround Manager" (Basecamp Coffee)**
    *   **Proces:** Nowy manager "dziedziczy" chaos po poprzedniku.
    *   **Mechanizm:** Zamiast pytać chata "jak naprawić program lojalnościowy" (generic advice), agent czyta folder `old-campaigns/` (co nie zadziałało?) i `company-context/` (kim jesteśmy?).
    *   **Zysk:** Agent nie hallucinationsuje rozwiązań ogólnych. Proponuje rozwiązania osadzone w historii firmy, której "nauczył się" w 30 sekund czytając pliki. Tej historii nie dałoby się wkleić do chata za każdym razem.

---

## 3. Przejrzystość Nadzoru: "Epistemic Transparency"
*Teoria: [[Context Visibility as Supervision Prerequisite]]*

### Argument
W chacie z "wbudowaną wiedzą" (RAG/Gems) nadzór jest niemożliwy, bo nie wiesz, co agent wie. To "Black Box".
W systemie plikowym (Workspace) masz "Epistemic Transparency" — widzisz dokładnie te same pliki, co agent.

### Dowód z `ccforeveryone`
*   **Case: "Logic vs Implementation" (Vibe Coding)**
    *   **Mechanizm:** Użytkownik definiuje logikę w pliku tekstowym (np. w punkcie X -> idź do Y). Agent to implementuje.
    *   **Zysk:** Gdy aplikacja działa źle, użytkownik nie musi zgadywać "dlaczego model tak pomyślał?". Otwiera plik z logiką i widzi błąd w SWOJEJ definicji.
    *   **Kontrola:** Możesz poprawić plik (input), a nie kłócić się z modelem (output).

---

## 4. Wielowątkowość: "Multi-threading without Pollution"
*Teoria: [[brainstorming_stream_vs_anchor]]*

### Argument
W chacie nie możesz robić dwóch rzeczy naraz na tym samym temacie bez mieszania wątków ("teraz zapomnij o tamtym i skup się na tym").
Na plikach możesz "nasłać" 5 agentów na ten sam dokument. Są od siebie odizolowani.

### Dowód z `ccforeveryone`
*   **Case: "Advisory Board" (Sub-agents)**
    *   **Proces:** Recenzja CV / Dokumentu.
    *   **Mechanizm:** Agent A (Rekruter) ocenia plik `cv.md`. Agent B (Manager) ocenia ten sam plik `cv.md`.
    *   **Zysk:** Rekruter nie widzi komentarzy Managera (nie sugeruje się nimi). Każdy pracuje w czystym, izolowanym wątku, ale na WSPÓLNYM stanie (pliku). To symuluje pracę zespołu, a nie schizofreniczną rozmowę z jedną osobą udającą 5 głosów.

---

## 5. Chirurgiczna Precyzja: "Diff vs Rewrite"
*Teoria: [[artefakty-vs-gems-esej]]*

### Argument
Chat ma tendencję do "Hallucinated Rewrites" — prosisz o zmianę przecinka, a model przepisuje cały paragraf, zmieniając przy okazji kluczowe słowo. Ryzykowne w prawie/biznesie.
Agent na plikach może robić `diff` — zmienić tylko to, co trzeba.

### Dowód z `ccforeveryone`
*   **Case: "Deep Synthesis" (Report Generation)**
    *   **Mechanizm:** "Weź dane z pliku A, wstaw do szablonu B".
    *   **Zysk:** Struktura dokumentu jest nienaruszona (szablon). Zmieniają się tylko dane. W chacie model często "płynie" i gubi strukturę szablonu przy każdym generowaniu. Tutaj "szkielet" (plik) trzyma formę w ryzach.

---

## Podsumowanie Strategiczne

| Cecha | Chat (Stream) | Artefakt (Anchor) |
| :--- | :--- | :--- |
| **Pamięć** | Zapomina po zamknięciu okna | Pamięta latami (Folder) |
| **Edycja** | Przepisuje całość (Ryzyko) | Chirurgiczny Diff (Bezpieczeństwo) |
| **Kontekst** | Brudny (Historia błędów) | Czysty (Tylko sukcesy) |
| **Skala** | Jednoosobowa sesja | Zespół / Firma / Lata |
| **Nadzór** | Zgadywanie (Black Box) | Widoczność (Pliki) |

**Werdykt:** Chat służy do **eksploracji** (szukania pomysłu). Artefakty służą do **eksploatacji** (budowania wartości). Profesjonalista musi umieć przejść z jednego w drugie.
