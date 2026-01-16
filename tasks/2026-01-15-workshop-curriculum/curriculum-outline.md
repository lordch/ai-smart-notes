# Context Engineering z Claude Code — Curriculum Outline

Praktyczne umiejętności pracy z agentem, od podstaw do zaawansowanych wzorców.

---

## Level 0: Pierwsze kroki — Od chatu do agenta z plikami

**Dla kogo:** Używał ChatGPT/Claude w przeglądarce

### Dlaczego "context engineering"?

LLM-y halucynują. Właśnie dlatego nasza praca to **organizowanie im kontekstu** — nie pytanie "co jest prawdą", tylko dawanie wiedzy do opracowania.

- Agent to narzędzie, nie źródło wiedzy
- Ty dostarczasz kontekst, agent przetwarza
- Agent szuka w internecie, bazach, dokumentach — to źródła, nie on sam
- Z czasem nabierzesz feeling: gdzie ufać, gdzie kontrolować (to też autonomy slider)
- Nowe modele myślące są znacznie lepsze w unikaniu halucynacji

**Context engineering = umiejętność organizowania wiedzy tak, żeby agent działał niezawodnie.**

### Tematy:

**0.1 Dlaczego agent z plikami (vs chat w przeglądarce)**
- Agent który WIDZI twoje pliki i MOŻE je edytować
- Chat gubi kontekst z początku sesji
- Przepisywanie tekstu = ryzyko niezamierzonych zmian w tym, co już ustalone
- Dyskusje o szczegółach "zaśmiecają" kontekst
- Artefakt = utrwalasz tylko to, co warte utrwalenia
- Punktowe edycje zamiast "przepisz mi całość"
- Demo: "przeczytaj ten folder i powiedz mi co tu jest"

**0.2 Podstawowa interakcja**
- Jak zadawać pytania
- Jak pokazywać pliki (@file, drag & drop)
- Jak prosić o edycję ("zmień X na Y w pliku Z")

**0.3 Czytanie vs pisanie**
- Agent może czytać wszystko
- Agent pyta o pozwolenie przed zapisem
- Kiedy mówić "tak", kiedy "nie", kiedy "pokaż mi najpierw"
- Diff = widzisz dokładnie CO się zmienia (nie "cały nowy tekst")
- Zmniejszanie płaszczyzny alignmentu — zatwierdzasz zmianę, nie produkt

**0.4 Podwójny interfejs**
- CC w VSCode: przeglądarka plików + edytor + chat w jednym oknie
- Ty możesz edytować sam — agent jest dodatkiem, nie koniecznością
- Autonomy slider ≈ 0: sam piszesz, agent tylko asystuje (korekta, stylistyka)
- Możesz tylko rozmawiać o notatkach, bez zmian

**0.5 Praktyka: pierwszy workflow**
- Wybierz realne zadanie (mail, notatka, dokument)
- Wykonaj z agentem od początku do końca
- Refleksja: co poszło dobrze, co źle

**Rezultat:** Komfort w podstawowej pracy z Claude Code

---

## Level 1: Kontekst — Co agent wie i skąd

### Tematy:

**1.1 Skąd agent wie**
- Context window — "pamięć robocza" sesji
- Co się tam znajduje: twoje wiadomości + pliki które załadowałeś + system prompt
- Więcej ≠ lepiej (context rot)

**1.2 Ładowanie kontekstu**
- Explicite: @file, @folder, wklejenie tekstu
- Implicite: agent sam czyta pliki gdy potrzebuje
- Decyzja: kiedy dać z góry, kiedy pozwolić szukać

**1.3 Typy kontekstu (co agent potrzebuje wiedzieć)**
- O zadaniu: co konkretnie ma zrobić
- O domenie: specyficzna wiedza którą ty masz, a on nie
- O jakości: jak wygląda "dobrze", jak wygląda "źle"
- O ograniczeniach: czego NIE robić

**1.4 Rozszerzanie źródeł kontekstu**
- Agent może szukać w internecie (web search, web fetch)
- MCP servers — podłączanie zewnętrznych źródeł
- Przykłady: PubMed dla biotech, GitHub, Notion, bazy danych
- Praktyka: skonfiguruj 1-2 MCPs przydatne w twojej pracy

**1.5 Praktyka: świadome ładowanie**
- To samo zadanie, różne konteksty
- Porównanie outputów
- Nauka: jaki kontekst miał największy wpływ

**Rezultat:** Świadome zarządzanie tym, co agent wie

---

## Level 2: Checkpointy — Praca w krokach

### Tematy:

**2.1 Problem z "zrób wszystko na raz"**
- Demo: duże zadanie bez checkpointów → błędy się kumulują
- Łatwiej zweryfikować plan niż gotowy produkt
- Checkpoint = miejsce gdzie SPRAWDZASZ zanim idziesz dalej

**2.2 Autonomy slider**
- Gdzie TY tracisz zaufanie, że agent zrobi dobrze?
- Tam checkpoint — PRZED, nie po
- Nie ma uniwersalnej odpowiedzi — zależy od ciebie, zadania, doświadczenia

**2.3 Artefakty pośrednie**
- Co zapisać między krokami
- Plik jako checkpoint — można wrócić, można kontynuować jutro
- Agent proponuje → ty zatwierdzasz/edytujesz → agent kontynuuje
- Jeden plik, wiele chatów — praca z różnych kątów
- W jednym chacie dopytujesz o szczegół, w drugim kontynuujesz główną pracę
- Uniezależnianie kontekstu między sesjami

**2.4 Praktyka: zaprojektuj workflow**
- Realne złożone zadanie uczestnika
- Podział na kroki z checkpointami
- Wykonanie z weryfikacją na każdym etapie

**Rezultat:** Umiejętność dzielenia pracy na kontrolowane kroki

---

## Level 3: CLAUDE.md — Pamięć projektu

### Tematy:

**3.1 Co to jest CLAUDE.md**
- Plik który agent czyta NA STARCIE każdej sesji
- "Instrukcja obsługi" tego projektu/folderu
- Demo: praca bez CLAUDE.md vs z CLAUDE.md

**3.2 Co tam wpisać**
- Kontekst projektu (o czym to jest)
- Konwencje (jak tu robimy rzeczy)
- Ograniczenia (czego NIE robić)
- Częste zadania (jak je wykonywać)

**3.3 Hierarchia CLAUDE.md**
- Globalny: ~/.claude/CLAUDE.md (twoje preferencje wszędzie)
- Projektowy: ./CLAUDE.md (specyfika tego projektu)
- Zagnieżdżony: ./subfolder/CLAUDE.md (specyfika podfolderu)

**3.4 Kiedy aktualizować**
- Agent zrobił coś źle → czego brakowało w instrukcji?
- Nowy pattern który chcesz zachować
- "Poproś agenta o update CLAUDE.md" — on sam może to zrobić

**3.5 Praktyka: stwórz CLAUDE.md dla swojego projektu**
- Audit: jakie informacje powtarzasz agentowi?
- Zapisanie do CLAUDE.md
- Test: czy teraz nie musisz powtarzać?

**Rezultat:** Projekt który "pamięta" jak z nim pracować

---

## Level 4: Reference Files — Kontekst on-demand

### Tematy:

**4.1 Problem z wielkim CLAUDE.md**
- CLAUDE.md ładowany ZAWSZE → nie może być za duży
- Ale niektóry kontekst jest potrzebny tylko czasem
- Rozwiązanie: osobne pliki, ładowane gdy trzeba

**4.2 Struktura reference files**
- `context/` folder na materiały referencyjne
- Przykłady: brand-voice.md, target-customers.md, competitors.md
- W CLAUDE.md: opisz CO istnieje, agent sam załaduje gdy potrzebuje

**4.3 Przykłady good/bad**
- Jeden z najsilniejszych typów kontekstu
- `examples/good/` i `examples/bad/` z komentarzem dlaczego
- Agent uczy się z przykładów lepiej niż z opisów

**4.4 Tasks folder — parking na robocze rzeczy**
- Problem: gdzie zapisać coś co jeszcze "nie ma miejsca"
- Pattern: `tasks/YYYY-MM-DD-opis/`
- Może zostać, może być wypromowane, bez presji

**4.5 Praktyka: zaprojektuj strukturę kontekstu**
- Co powinno być w CLAUDE.md (zawsze)?
- Co powinno być w reference files (on-demand)?
- Implementacja dla projektu uczestnika

**Rezultat:** Skalowalna struktura wiedzy dla agenta

---

## Level 5: Skills — Powtarzalne przepływy

### Tematy:

**5.1 Co to jest skill**
- Zapisany przepływ pracy który można wywołać komendą
- `/my-skill` zamiast tłumaczenia od nowa
- Skill = prompt + kontekst + instrukcje

**5.2 Kiedy skill, kiedy CLAUDE.md**
- CLAUDE.md: "zawsze rób tak" (globalne reguły)
- Skill: "teraz zrób konkretną rzecz" (workflow na żądanie)
- Skill może ładować dodatkowy kontekst którego CLAUDE.md nie ma

**5.3 Anatomia skilla**
- Nazwa i opis
- Instrukcje dla agenta
- Kontekst do załadowania
- Przykłady użycia

**5.4 Przykłady użytecznych skilli**
- `/research [temat]` — zbierz informacje według określonego schematu
- `/draft [typ]` — stwórz draft dokumentu w określonym formacie
- `/review` — przejrzyj i skrytykuj według kryteriów
- `/summarize` — podsumuj według szablonu

**5.5 Praktyka: stwórz skill dla powtarzalnego zadania**
- Zidentyfikuj zadanie które robisz często
- Zapisz jako skill
- Test i iteracja

**Rezultat:** Biblioteka własnych komend do częstych zadań

---

## Level 6: Subagenci — Delegowanie złożonych zadań

### Tematy:

**6.1 Kiedy subagent**
- Zadanie wymaga dużo autonomii w jednym obszarze
- Chcesz izolować kontekst (subagent ma "czystą kartę")
- Chcesz równoległości (kilka rzeczy naraz)

**6.2 Jak działa subagent**
- Główny agent spawnuje subagenta z zadaniem
- Subagent pracuje, wraca z wynikiem
- Główny agent kontynuuje

**6.3 Projektowanie zadania dla subagenta**
- Jasny, zamknięty cel
- Określony output
- Kontekst który subagent potrzebuje (bo nie ma dostępu do całej rozmowy)

**6.4 Patterns**
- Research agent: "zbierz informacje o X, zapisz w pliku Y"
- Drafting agent: "napisz draft według specyfikacji Z"
- Review agent: "przejrzyj dokument, daj feedback"

**6.5 Praktyka: workflow z subagentami**
- Złożone zadanie podzielone na części
- Każda część = subagent ze specyficznym celem
- Orkiestracja przez głównego agenta

**Rezultat:** Umiejętność delegowania złożonych zadań

---

## Level 7: Feedback Loop — Systematyczne usprawnianie

### Tematy:

**7.1 Obserwacja błędów**
- Gdzie agent regularnie zawodzi?
- Jagged intelligence — ma mocne i słabe strony
- Prowadzenie mentalnego (lub explicite) rejestru

**7.2 Diagnoza**
- Agent zawiódł → czego brakowało w kontekście?
- Czy to brak wiedzy faktycznej?
- Czy to brak instrukcji proceduralnych?
- Czy to brak przykładów?

**7.3 Naprawa**
- Dodanie do CLAUDE.md
- Stworzenie reference file
- Stworzenie/update skilla
- Dodanie przykładów good/bad

**7.4 Przesuwanie autonomy slider**
- Po naprawie: czy mogę checkpointować rzadziej?
- Test: puść więcej autonomii, obserwuj
- Iteracja

**7.5 Praktyka: retrospektywa i improvement**
- Przegląd ostatniego tygodnia/miesiąca pracy
- Identyfikacja powtarzających się problemów
- Implementacja fix-ów
- Plan testowania

**Rezultat:** Ciągłe usprawnianie współpracy z agentem

---

## Zależności

```
Level 0-1: Podstawy (każdy)
    ↓
Level 2-3: Intermediate (praktyk)
    ↓
Level 4-5: Advanced (power user)
    ↓
Level 6-7: Expert (budowanie systemów)
```

---

## Do przemyślenia / rozwinięcia

- Hooks — automatyczne akcje przy eventach
- Multi-agent workflows — kiedy i jak
- Integracja z innymi narzędziami (git, API, etc.)
- Praca zespołowa — shared context między ludźmi
