# Narracja: Jak naprawdę działa praca z AI agentem

*Synteza storytellingu z community Claude Cowork, przełożona na tool-agnostic Human-Agent Collaboration*

---

## Główna teza

**Chat był formą przejściową.**

Przez ostatnie dwa lata rozmawialiśmy z AI jak z doradcą: pytasz → odpowiada → pytasz znowu. To był pierwszy krok, bo modele potrafiły generować tekst, zanim nauczyły się wykonywać plany.

Ale to już nie jest prawda.

Teraz możesz powiedzieć agentowi co chcesz osiągnąć, on zrobi plan, pokaże ci ten plan, wykona go autonomicznie, i wciągnie cię tylko gdy potrzebuje decyzji. A ty w tym czasie możesz robić coś innego.

**To nie jest rozmowa z asystentem. To zarządzanie wykonawcą.**

---

## Zmiana relacji

| Stary model (chat) | Nowy model (workspace) |
|--------------------|-----------------------|
| AI jako **respondent** | AI jako **worker** |
| Prompt → Answer → Prompt | Delegate → Execute → Review |
| Synchroniczna rozmowa | Asynchroniczna delegacja |
| "Co mam napisać dalej?" | "Co naprawdę muszę zrobić?" |
| Output = tekst do skopiowania | Output = gotowy plik |

Ludzie inaczej zarządzają pracownikami niż rozmawiają z doradcami. Kiedy rozmawiasz z doradcą, oczekujesz perspektywy, sugestii, dialogu. Kiedy delegujesz pracownikowi, oczekujesz wykonania.

**Przejście od "editing loop" do "steering loop".**

W editing loop korygujesz output — przeklejasz tekst do dokumentu, formatujesz, dodajesz brakujące elementy. W steering loop definiujesz kierunek — a ciężką robotę wykonuje ktoś inny.

---

## Jak to działa w praktyce

### Workspace, nie okno chatu

Agent potrzebuje widzieć to samo co ty. Nie wyciąg z dokumentu wklejony w prompt — cały folder z plikami, kontekstem, historią.

> "To nie jest standardowa inteligencja chatbota. To inteligencja na poziomie folderu."

Kiedy wskazujesz agentowi folder na swoim komputerze, on:
- Czyta wszystkie pliki
- Buduje zrozumienie struktury
- Odpowiada na pytania wymagające połączenia informacji z wielu źródeł
- Tworzy nowe pliki w tym samym miejscu

**Folder = projekt = workspace = przestrzeń współpracy.**

### Artefakty, nie odpowiedzi

> "Nie chcę odpowiedzi w oknie chatu. Chcę pliki, których mogę użyć."

Różnica jest fundamentalna:
- Chat produkuje tekst, który musisz gdzieś przenieść
- Workspace produkuje artefakty — prezentacje, arkusze, dokumenty — gotowe do użycia

Kiedy prosisz o analizę danych zakupowych i spersonalizowane emaile, nie dostajesz "oto sugerowana treść emaila". Dostajesz folder `/emails/` z 44 plikami, po jednym na każdego klienta.

**Output to deliverable, nie draft.**

### Asynchroniczność

> "Po raz pierwszy, jeśli nie jesteś techniczny, możesz poprosić komputer o coś i odejść na chwilę."

Agent może pracować godzinami. Przegląda twój kalendarz z ostatniego miesiąca i porównuje z celami kwartalnymi? To zajmuje czas. Ale ty nie musisz na to patrzeć.

Możesz:
- Uruchomić zadanie i pójść na kawę
- Mieć kilka zadań działających równolegle
- Dodawać informacje w trakcie pracy agenta (agent replanuje)

**"Set it and forget it" — ale z możliwością steering w dowolnym momencie.**

### Widoczność procesu

Agent pokazuje:
- Co załadował do kontekstu (jakie pliki przeczytał)
- Jaki ma plan (lista kroków)
- Gdzie jest w wykonaniu (checkboxy postępu)
- Co wyprodukował (artefakty)

> "Nadzorujesz przez obserwowanie, nie przez odpytywanie."

To jest kluczowe dla zaufania. Nie musisz pytać "co zrobiłeś?". Widzisz to w czasie rzeczywistym.

---

## Nadzór to kuracja kontekstu

Najważniejsza praca nie polega na klikaniu "zatwierdź" przy każdej akcji.

**Najważniejsza praca to kształtowanie tego, co agent widzi, zanim zacznie działać.**

Hierarchia dźwigni:
- Jeśli research jest zły → tysiące linii złego kodu
- Jeśli plan jest zły → setki linii do poprawy
- Jeśli pojedyncza linia jest zła → jedna poprawka

Supervision przez context curation oznacza:
1. **Definiujesz co agent wie** — jakie pliki ma dostępne, jaki kontekst
2. **Definiujesz jak agent działa** — procedury, zasady, ograniczenia
3. **Definiujesz cel** — outcome, nie kolejne kroki

> "Nie możesz mgliście poprosić o pomoc z wydatkami. Musisz wskazać prawdziwy folder z prawdziwymi plikami."

Ta konieczność specyficzności to feature, nie bug. Wymusza przemyślenie zadania.

---

## Uczenie przez pokazywanie

Zamiast pisać instrukcje, możesz pokazać.

Nagrywasz sekwencję akcji:
1. Otwieram Google Analytics
2. Kopiuję liczbę odwiedzin
3. Otwieram arkusz
4. Wklejam w kolumnę B

Agent obserwuje. Zapamiętuje. Od teraz może to powtarzać.

> "Nie musiałem niczego kodować. Nie musiałem używać Zapiera. Nie musiałem bawić się z API. Po prostu pokazałem raz i teraz działa na zawsze."

**Skill to zeksternalizowana procedura** — trwały artefakt, który możesz używać, modyfikować, dzielić.

---

## Agent jako interfejs

Niektóre narzędzia są skomplikowane. PostHog, Google Analytics, Salesforce — mają dziesiątki opcji, zakładek, filtrów.

> "Właściwie nie wiem, jak używać PostHog. Jest super skomplikowany. Ale mam agenta, który może to zrobić za mnie."

Agent staje się warstwą abstrakcji. Zamiast uczyć się interfejsu narzędzia, mówisz agentowi czego potrzebujesz. On nawiguje, klika, eksportuje.

**Nie musisz znać narzędzia. Musisz umieć zdefiniować cel.**

---

## ROI w praktyce

Przykład z życia: analiza 100 transkryptów podcastów + tysiące wierszy danych YouTube + wygenerowanie strategii wzrostu + prezentacja z wykresami.

Tradycyjnie: 1-2 dni pracy.
Z agentem: 15-20 minut.

> "Co byś zapłacił za strategię wzrostu dla ważnego projektu? Dużo więcej niż 100 dolarów. A ja właśnie to zrobiłem w 15 minut."

Ale uwaga — to nie jest magia. To działa, bo:
- Kontekst był przygotowany (folder z transkryptami, CSV z danymi)
- Cel był jasny (więcej subskrybentów)
- Human zwalidował output

**Agent wykonuje ciężką robotę. Człowiek definiuje cel i ocenia wynik.**

---

## Suwak autonomii

Nie wszystkie zadania wymagają tego samego poziomu nadzoru.

| Zadanie | Autonomia | Nadzór |
|---------|-----------|--------|
| Organizacja plików | Wysoka | Niski — sprawdź na końcu |
| Prezentacja sprzedażowa | Średnia | Review przed wysłaniem |
| Email do klienta | Średnia | Przeczytaj przed wysłaniem |
| Strategia biznesowa | Niska | Współpraca krok po kroku |

Zacznij od niskiego ryzyka. Organizacja chaotycznego folderu. Podsumowanie dokumentów. Ekstrakcja danych.

Zbuduj zaufanie. Poznaj jak agent myśli. Potem zwiększaj autonomię.

> "To jest dekada agentów, nie rok. Stopniowa progresja z weryfikacją."

---

## Twoja rola się zmienia, nie znika

To nie jest automatyzacja, która cię zastępuje. To delegacja, która cię wzmacnia.

Zamiast robić research, **nadzorujesz** research.
Zamiast pisać pierwszy draft, **refinujesz** draft.
Zamiast przeklejać dane, **interpretujesz** dane.

> "Agent ma ręce. Człowiek ma osąd, gdzie je skierować."

**Pracujesz PRZEZ agenta, nie OBOK niego.**

---

## Co to wymaga od ciebie

1. **Umiejętność definiowania intencji** — nie "pomóż mi z X", ale "chcę osiągnąć Y, mam do dyspozycji Z"

2. **Organizacja kontekstu** — struktura folderów, nazewnictwo plików, dokumentacja procedur

3. **Weryfikacja outputu** — czy wynik jest poprawny? czy zadanie było dobrze sformułowane?

4. **Thoughtfulness** — przemyślenie czego naprawdę potrzebujesz, zanim poprosisz

> "To wymaga przemyślenia. A przemyślenie to anti-slop."

---

## Bottom line

**Narzędzia się zmieniają. Zasady pozostają.**

Czy to Claude Cowork, czy Cursor, czy przyszły produkt którego jeszcze nie ma — sposób pracy jest ten sam:

1. **Workspace jako powierzchnia współpracy** — folder z plikami, nie okno chatu
2. **Artefakty jako medium** — praca żyje w plikach, nie w konwersacjach
3. **Nadzór przez kontekst** — kształtujesz input, nie poprawiasz output
4. **Autonomia dopasowana do zaufania** — zacznij nisko, zwiększaj stopniowo
5. **Człowiek jako kierownik** — definiujesz cel, oceniasz wynik, podejmujesz decyzje

To nie jest umiejętność obsługi konkretnego narzędzia.

**To jest umiejętność organizacji pracy z AI — context engineering — i można ją wdrażać systematycznie.**

---

*Narracja oparta na analizie 8 źródeł community: First Look, Task Queues, Vibe Check (z Felixem z Anthropic), Master 99%, 24h Test, 5 Use Cases, 8 Use Cases, 7 Days of Work.*
