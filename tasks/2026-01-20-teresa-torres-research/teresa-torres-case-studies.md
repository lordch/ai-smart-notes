# Case Studies: Claude Code w Praktyce (wg Teresy Torres)

Konkretne przykłady użycia terminalowego AI (Claude Code) omawiane przez Teresę Torres, pokazujące przejście od "klikania" do "zarządzania systemem".

## Case Study 1: Analiza Konkurencji (The "Parallel" Agent)
*To jest jej "flagowy" przykład pokazujący przewagę terminala nad czatem.*

### Problem
Product Manager musi przeanalizować 5 konkurentów pod kątem nowej funkcjonalności (np. "Pricing Grid").
*   **Tradycyjnie:** Otwierasz 5 kart w przeglądarce, kopiujesz cenniki do Excela, robisz screenshoty.
*   **Wersja Chat AI:** Wklejasz tekst ze strony konkurenta X do ChatGPT i prosisz o analizę. Powtarzasz 5 razy.

### Rozwiązanie w Claude Code
1.  **Przygotowanie (System):** Tworzysz folder `market-research/` i plik `competitors.md` z listą URLi oraz `criteria.md` z pytaniami, które chcesz zadać (ceny, limity, UX).
2.  **Egzekucja (Komenda):** Wpisujesz w terminalu jedną komendę, np.:
    `claude "Analizuj konkurentów z competitors.md wg kryteriów z criteria.md i zapisz wynik w matrix.csv"`
3.  **Skalowanie:** Claude Code może uruchomić **wiele agentów równolegle**. Jeden analizuje konkurenta A, drugi B, trzeci C – w tym samym czasie.
4.  **Wynik:** Gotowa tabela porównawcza wygenerowana w minutę, bez ręcznego kopiowania.
5.  **Długi Ogon (Long Tail):** Za miesiąc, gdy wchodzi Konkurent F, dopisujesz go do listy i uruchamiasz tę samą komendę. System "pamięta" kryteria.

---

## Case Study 2: Migracja Systemu Pracy (Trello -> Markdown)
*Przykład na "Data Ownership" i budowanie osobistej bazy wiedzy.*

### Problem
Torres używała Trello do zarządzania zadaniami. Zauważyła, że wiedza o projektach "umiera" w zamkniętych kartach Trello – trudno ją przeszukać, trudno połączyć wątki z różnych lat.

### Rozwiązanie
Przeniosła cały system do plików tekstowych (Markdown), którymi zarządza z poziomu terminala/edytora tekstu.
*   **Struktura:** Każdy projekt to folder. Każde zadanie to plik.
*   **Automatyzacja:** Zamiast klikać "Przesuń do Done", używa skryptów lub poleceń Claude Code: `claude "Zarchiwizuj zakończone projekty z Q4 i stwórz podsumowanie ich wyników w pliku 2025-Q4-Review.md"`.
*   **Wartość:** AI ma dostęp do *całej* historii jej pracy. Może zapytać: *"Jakie problemy z rekrutacją mieliśmy w ciągu ostatnich 3 lat?"* – i AI to znajdzie, bo to zwykłe pliki tekstowe (grepable), a nie zamknięta baza danych w chmurze.

---

## Case Study 3: Synteza Wywiadów (Continuous Discovery)
*Przykład na automatyzację żmudnej pracy analitycznej.*

### Problem
W modelu Continuous Discovery przeprowadzasz rozmowy z użytkownikami co tydzień. Po miesiącu masz 4 godziny nagrań i notatek. Nikt nie ma czasu tego czytać ponownie.

### Rozwiązanie
Zamiast trzymać notatki w Google Docs, trzymasz transkrypcje w folderze `interviews/`.
1.  **Skill (Procedura):** Definiujesz "Skill" dla Claude Code o nazwie `extract-opportunities`.
2.  **Działanie:** Komenda `claude -p extract-opportunities interviews/2026-01-*.txt`.
3.  **Efekt:** Agent czyta tylko wywiady ze stycznia, wyciąga z nich "Szansę" (Opportunities) zgodnie ze strukturą Opportunity Solution Tree (OST) i zapisuje je w pliku `opportunities_backlog.md`.
4.  **Siła:** Nie musisz tłumaczyć AI za każdym razem, czym jest "Opportunity Solution Tree". To jest zapisane w definicji "Skilla".

---

## Podsumowanie Wartości
We wszystkich przypadkach schemat jest ten sam:
1.  **Zdefiniuj proces raz** (w pliku konfiguracyjnym/promptcie systemowym).
2.  **Uruchamiaj wielokrotnie** (na nowych danych).
3.  **To jest programowanie**, ale zamiast kodu w Pythonie, piszesz instrukcje w języku naturalnym i strukturę w plikach i folderach.
