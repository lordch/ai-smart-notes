# Praca z Agentami AI: Pełna Narracja

*Wersja dla konsultantów i knowledge workers*

---

## Część I: Fundamentalny Insight

### Modele są zdolne

Zacznijmy od czegoś, co może być zaskakujące:

Współczesne AI (Claude, GPT-4, Gemini) potrafią naprawdę dużo. Potrafią analizować złożone dokumenty, porównywać źródła, pisać raporty, stosować metodologie, syntetyzować informacje z wielu miejsc.

To nie jest kwestia "czy AI umie". AI umie.

To jest kwestia **warunków**.

---

### Warunek: Odpowiedni kontekst

Wyobraź sobie, że zatrudniasz nowego analityka. Świetne CV, dobre rekomendacje, inteligentny człowiek.

Dajesz mu zadanie: "Przygotuj analizę konkurencji".

I zostawiasz go samego. Bez dostępu do wewnętrznych dokumentów. Bez kontekstu o branży. Bez przykładu jak wyglądały poprzednie analizy. Bez informacji kto będzie to czytał.

Co dostaniesz? Coś generycznego. Może nawet dobrze napisanego - ale nie tego, czego potrzebowałeś.

A teraz wyobraź sobie, że:
- Dajesz mu teczkę z dokumentami o konkurentach
- Pokazujesz poprzednią analizę jako wzór
- Mówisz, że to dla zarządu, więc bez żargonu
- Wyjaśniasz, na czym zależy klientowi

Ten sam analityk. To samo zadanie. Zupełnie inny wynik.

**Z AI jest dokładnie tak samo.**

AI wykonuje zadanie dobrze, **jeśli** dostanie odpowiedni kontekst:
- Wie na czym pracuje (źródła, dane, dokumenty)
- Wie co ma zrobić (zadanie, wymagania, format)
- Wie jak ma to zrobić (metodologia, przykłady, styl)
- Rozumie intencję (cel, odbiorca, ograniczenia)

---

### Prawdziwy problem

Dostarczenie "odpowiedniego kontekstu" brzmi prosto. Ale nie jest.

To nie jest trywialne zadanie typu "wrzuć więcej tekstu". To jest **cały problem** pracy z AI.

Jak dostarczyć kontekst, żeby AI nie wymyślał?
Jak przekazać wymagania, żeby output był użyteczny?
Jak utrzymać spójność, gdy rozmowa się wydłuża?
Jak nie przekroczyć limitów tego, ile AI może "widzieć"?

Reszta tego dokumentu to rozwinięcie tych pytań i propozycje odpowiedzi.

---

## Część II: Spectrum Podejść

### Dwa bieguny

Gdy pracujesz z AI, możesz podejść do tego na różne sposoby. Wyobraź sobie spectrum:

```
CHAT ◄────────────────────────────────────────────► AUTONOMICZNY AGENT
(ty w pętli)                                        (ty poza pętlą)
```

**Lewy biegun - Chat:**

Ty piszesz prompt. AI odpowiada. Czytasz odpowiedź, nie do końca to. Poprawiasz prompt. AI poprawia. Znowu nie tak. I tak dalej.

Wyobraź sobie: Piszesz do AI "pomóż mi z prezentacją dla klienta". Dostajesz jakieś sugestie. "Nie, bardziej konkretnie". Dostajesz coś innego. "Może struktura inaczej". Kolejna wersja. 30 minut później masz coś używalnego.

To jest tryb konwersacji. Ciągła interakcja, ciągła kontrola.

**Prawy biegun - Autonomiczny agent:**

Dajesz zadanie. AI robi wszystko samo. Dostajesz wynik.

Wyobraź sobie: "Przeanalizuj te 50 plików i stwórz raport". Idziesz na kawę. Wracasz - raport gotowy.

Brzmi świetnie, ale: nie widziałeś co AI robił. Nie mogłeś interweniować. Jeśli źle zrozumiał zadanie na początku - cała praca do śmieci.

---

### Problemy z chatem

Tryb konwersacyjny ma swoje pułapki:

**Historia błędów zostaje**

Wyobraź sobie: przez 20 minut próbowaliście różnych podejść do raportu. Każde "nie, spróbuj inaczej" zostaje w historii. AI widzi całą tę ścieżkę ślepych uliczek. Kontekst jest zaśmiecony waszymi wspólnymi pomyłkami.

**Im dłużej rozmawiasz, tym gorzej**

Ustalenia z początku rozmowy "toną". Instrukcja którą dałeś w trzeciej wiadomości ma coraz mniejszą wagę, gdy jesteś przy wiadomości trzydziestej.

**Zamykasz okno - wszystko znika**

Spędziłeś godzinę tłumacząc AI kontekst projektu. Następnego dnia otwierasz nowy chat. Zaczynasz od zera.

**Ciągłe poprawianie jest wyczerpujące**

Nie pracujesz NAD zadaniem. Pracujesz nad poprawianiem odpowiedzi AI. To zupełnie inna praca.

---

### Problemy z pełną autonomią

Tryb "AI robi wszystko" też ma pułapki:

**Nie widzisz co się dzieje**

AI pracuje gdzieś "w tle". Nie możesz interweniować. Nie możesz powiedzieć "nie, idź w inną stronę" w połowie.

**AI zakłada zamiast pytać**

Gdy AI czegoś nie wie, nie przychodzi do ciebie z pytaniem. Zakłada. Wypełnia luki własnymi domysłami. I idzie dalej.

Wyobraź sobie: Zlecasz raport. Nie sprecyzowałeś dla kogo. AI zakłada że dla techników i pisze żargonem. A to było dla zarządu.

**Trudno zweryfikować duży output**

Dostajesz 40-stronicowy dokument naraz. Gdzie sprawdzić? Wszystko? Wyrywkowo? Co jeśli błąd jest w środku?

**Błąd na początku psuje całość**

Jeśli AI źle zrozumiał na początku, każdy następny krok pogłębia ten błąd. A ty dowiadujesz się na samym końcu.

---

### Środek: Steering zamiast Editing

Jest trzecia droga. Ani ciągła konwersacja, ani pełna autonomia.

```
CHAT ◄──────────[TUTAJ]──────────────────────────► AUTONOMICZNY AGENT
               steering + artefakty + checkpointing
```

**Na czym to polega:**

1. Definiujesz zadanie precyzyjnie na początku
2. AI pokazuje plan - weryfikujesz kierunek
3. AI wykonuje - możesz interweniować gdy trzeba
4. Zapisujesz wynik do pliku
5. Następne zadanie - świeży kontekst, ale budujesz na poprzednim

**Różnica między editing a steering:**

| Pętla edycji | Pętla sterowania |
|--------------|------------------|
| AI robi → ty poprawiasz output | Ty definiujesz → AI robi → ty weryfikujesz |
| Kontrola na końcu | Kontrola na początku |
| Wysiłek w poprawianiu tekstu | Wysiłek w definiowaniu zadania |
| Kontekst rośnie i rośnie | Kontekst się resetuje |

**Wyobraź sobie to tak:**

Pętla edycji: Dajesz stażyście zadanie "zrób prezentację" i stoisz mu nad ramieniem. "Ten slajd przesuń, tu zmień kolor, tutaj dodaj wykres..."

Pętla sterowania: Dajesz stażyście brief. "15 slajdów, dla zarządu, o wynikach Q4, struktura jak poprzednia prezentacja którą znajdziesz tutaj. Jak skończysz, pokaż mi przed wysłaniem."

Ta sama praca. Inny rozkład wysiłku. Inny poziom stresu.

---

### Czat jako miejsce pracy

Zanim przejdziemy dalej - ważne wyjaśnienie.

Czat nie jest "złym trybem" którego unikamy. **Czat jest miejscem pracy:**

- **Eksternalizacja** - wyciągasz intencję z głowy do słów
- **Sterowanie** - dajesz kierunek, koregujesz, doprecyzowujesz
- **Krystalizacja** - odkrywasz czego właściwie chcesz
- **Weryfikacja** - sprawdzasz, dopytujeszz, upewniasz się
- **Iteracja** - poprawiasz, ulepszasz

Tu dzieje się prawdziwa praca. Tu eksternalizujesz swoją wiedzę i intencje.

**Problem nie jest w czacie.** Problem jest w tym, że **kontekst puchnie**:
- Historia rośnie z każdą wiadomością
- Wcześniejsze ustalenia "toną"
- Ślepe uliczki zostają w pamięci

**Rozwiązanie: checkpointing.** Pracujesz w czacie → zapisujesz wynik do pliku → nowa sesja z czystym kontekstem.

Wyobraź sobie:

> "Czat to kokpit. Siedzisz w nim i sterujesz. Tylko co jakiś czas 'czyścisz kokpit' żeby znowu widzieć przez szybę."

Czat + checkpointing = najlepsze z obu światów. Kontrola + czysty kontekst.

---

## Część III: Cztery Problemy Kontekstu

### Meta-framing

Wszystkie problemy z AI przy złożonych zadaniach to są **problemy z kontekstem**. Ale kontekst ma różne wymiary, i każdy pęka inaczej.

| Problem | Typ kontekstu | Co się dzieje |
|---------|---------------|---------------|
| **Halucynacje** | Faktyczny | AI nie ma źródeł → wymyśla |
| **Slop** | Intencji | AI nie zna twoich wymagań → robi "jakkolwiek" |
| **Drift** | Alignment | Zrozumienie degraduje się w czasie → AI "odpływa" |
| **Ograniczenia** | Fizyczny | Za dużo kontekstu → nie mieści się |

Przejdźmy przez każdy.

---

### Problem 1: Halucynacje (brak kontekstu faktycznego)

**Jak to wygląda:**

Pytasz AI o statystykę rynkową. Dostajesz konkretną liczbę z konkretnego źródła. Sprawdzasz - takie źródło nie istnieje. Liczba jest zmyślona.

Albo: prosisz o streszczenie dokumentu. AI "dodaje" wnioski których nie ma w tekście, ale brzmią sensownie.

**Dlaczego się pojawia:**

Używasz AI jako **źródła wiedzy** zamiast jako **procesora wiedzy**.

Kiedy pytasz "co wiesz o X", AI nie ma skąd wziąć faktów. Ale musi odpowiedzieć. Więc generuje tekst który *brzmi* jak fakty. To jest jego natura - przewiduje prawdopodobny ciąg dalszy. Jeśli nie dasz mu faktów, wygeneruje coś co wygląda jak fakty.

**Wyobraź sobie:**

Nowy pracownik. Pytasz go "co wiesz o naszym kliencie?". Nie ma dostępu do dokumentów. Ale chce zrobić dobre wrażenie. Więc mówi coś, co brzmi sensownie na podstawie ogólnej wiedzy o branży.

To samo robi AI. Tyle że AI robi to bardzo przekonująco.

**Jak naprawiać:**

- Daj AI materiały do przetworzenia, nie pytaj co "wie"
- "Przeanalizuj **ten raport**" zamiast "co wiesz o tym temacie"
- Proś o cytaty i odniesienia - "pokaż fragment źródła"
- Pracuj w środowisku gdzie widzisz te same pliki co AI

---

### Problem 2: Slop (brak kontekstu intencji)

**Jak to wygląda:**

Dostajesz od AI dokument. Profesjonalnie sformatowany, poprawny językowo, wygląda jak z dużej firmy konsultingowej. Wysyłasz klientowi.

Klient dzwoni: "To jest bardzo ogólne. Gdzie konkrety które omawialiśmy?"

Albo: prezentacja wygląda świetnie, ale treść jest... nijaka. Poprawna, ale nijaka. Mogłaby być o czymkolwiek.

"Slop" to output który **wygląda** profesjonalnie, ale nie **jest** tym czego potrzebujesz.

**Dlaczego się pojawia:**

AI nie zna twoich wymagań jakościowych. Nie wie co dla ciebie znaczy "dobry raport". Nie zna stylu który preferujesz, standardów klienta, kontekstu projektu.

Więc optymalizuje pod jedyne kryterium które ma: "wygląda profesjonalnie".

**Dlaczego TY wypuszczasz slop:**

- Sprawdzenie 20-stronicowego dokumentu jest żmudne
- Masz deadline
- "Wygląda OK, pewnie jest OK"
- Klient pewnie nie zauważy

A potem klient zauważa.

**Wyobraź sobie:**

Zlecasz komuś raport. Mówisz "zrób raport o konkurencji". Nie mówisz dla kogo, w jakim stylu, co jest ważne, co można pominąć, jak wyglądały poprzednie.

Dostajesz coś. Technicznie to jest "raport o konkurencji". Ale nie to, czego potrzebowałeś.

**Jak naprawiać:**

Jest spectrum formułowania zadania:

```
TY SPECYFIKUJESZ ◄────────────────────► AGENT FORMUŁUJE
PRECYZYJNIE                              Z KONTEKSTU
```

**Możesz być bardzo precyzyjny** (gdy wiesz dokładnie czego chcesz):
- "Zrób raport PDF, 10 stron, z wykresami, format jak poprzedni"

**Możesz dać agentowi kontekst i poprosić o sformułowanie** (gdy masz dużo materiałów):
- "Zobacz poprzednie raporty w /reports. Zaproponuj strukturę. Dopytaj mnie o to czego ci brakuje"

**Możesz mieszać:**
- "Chcę analizę konkurencji dla zarządu. Zobacz jak wyglądały poprzednie. Powiedz jak rozumiesz zadanie"

**Gdzie jesteś na spectrum zależy od:**
- Ile kontekstu agent ma (pliki, przykłady, poprzednie prace)
- Jak dobrze wiesz czego chcesz
- Czy to powtarzalne zadanie

**Kluczowe:** Przerzuć część pracy formułowania na agenta gdy ma dobry kontekst. Twoja rola: korekta, nie pełna specyfikacja.

---

### Problem 3: Drift (degradacja kontekstu alignment)

**Jak to wygląda:**

Zaczynasz rozmowę. Wyjaśniasz kontekst projektu, specyfikę klienta, swój styl pracy. Pierwsze odpowiedzi są celne.

Godzinę później, po 30 wymianach, AI produkuje coś co ignoruje połowę ustaleń z początku. Przypominasz. Poprawia. Za chwilę znowu zapomina.

**Dlaczego się pojawia:**

**Drift techniczny:** Im dłuższy kontekst, tym mniejszą wagę mają wcześniejsze fragmenty. Instrukcje z początku "toną" w morzu późniejszych wiadomości.

**Drift alignment:** AI zrozumiał inaczej niż myślałeś. Od początku poszedł w kierunku który mu się wydawał sensowny - ale nie w twój kierunek. I im dłużej pracował, tym dalej od intencji.

**Drift intencji:** Ty sam nie wiedziałeś dokładnie czego chcesz na początku. Intencja krystalizowała się w trakcie. AI pracuje na starej wersji twojego rozumienia.

**Kluczowy insight:**

AI jest "eager" - chętny do działania. Nie pyta gdy czegoś nie wie. Zakłada. Wypełnia luki. I idzie dalej.

Jeśli czegoś nie dopowiedziałeś, AI nie przyjdzie z pytaniem. AI wymyśli odpowiedź i będzie działać jakby to była prawda.

**Wyobraź sobie:**

Pracownik który nigdy nie pyta. Zawsze mówi "jasne, zrozumiałem" i idzie robić. Czasem trafia. Czasem kompletnie mija się z tym, co miałeś na myśli.

**Jak naprawiać:**

- Przed startem: "Powiedz swoimi słowami jak rozumiesz to zadanie"
- Wydobywaj założenia: "Jakie masz założenia? Co zakładasz o odbiorcy?"
- Regularny reset: zapisuj wynik, zaczynaj świeżą sesję
- Korekta kierunku: interweniuj gdy widzisz że odpływa

---

### Problem 4: Ograniczenia kontekstu (fizyczny limit)

**Jak to wygląda:**

Masz 200 stron materiałów do analizy. Chcesz wrzucić wszystko. AI ma limit - nie przyjmie tyle naraz. Albo przyjmie, ale jakość spada.

Chcesz dać AI pełny obraz: briefy, poprzednie raporty, feedback, notatki. Za dużo. Musisz wybierać. Zawsze brakuje czegoś ważnego.

**Dlaczego się pojawia:**

AI ma fizyczny limit tego, ile może "widzieć" naraz. To jak krótkoterminowa pamięć robocza.

**Problem emergentny:**

Żeby rozwiązać problemy 1-3, dajesz więcej kontekstu:
- Więcej źródeł (przeciw halucynacjom)
- Więcej wymagań i przykładów (przeciw slop)
- Więcej wyjaśnień (przeciw drift)

Czyli rozwiązując problemy 1-3, pogłębiasz problem 4. Kontekst puchnie.

**Wyobraź sobie:**

Biurko. Możesz mieć na nim pewną ilość dokumentów naraz. Jeśli położysz więcej - zaczyna się chaos. Nie widzisz co ważne.

**Jak naprawiać:**

- Dziel zadania na mniejsze (każde ze swoim kontekstem)
- Zapisuj wyniki do plików (checkpoint)
- Nowa sesja czyta plik, nie całą historię
- Ładuj stopniowo - najpierw nagłówki, potem szczegóły gdy potrzebne

---

### Mapa problemów

```
        PROBLEMY KONTEKSTU
               │
   ┌───────────┼───────────┬───────────┐
   ▼           ▼           ▼           ▼
HALUCYNACJE   SLOP       DRIFT    OGRANICZENIA
(faktyczny) (intencji) (alignment)  (fizyczny)
   │           │           │           │
   ▼           ▼           ▼           ▼
 Daj        Zdefiniuj   Sprawdzaj    Dziel
źródła      precyzyjnie zrozumienie  i zapisuj
```

---

## Część IV: Mechanizmy Rozwiązań

Rozwiązania z poprzedniej części można ująć jako **mechanizmy** - powtarzalne wzorce które stosujesz w różnych sytuacjach.

---

### Mechanizm 1: Transparentność

**Co to jest:**

Pracujesz w środowisku gdzie widzisz dokładnie to samo co AI. Żadnej "czarnej skrzynki".

**Jak to wygląda praktycznie:**

AI pracuje na plikach na twoim komputerze. Możesz otworzyć każdy plik który AI czyta. Gdy AI mówi "na podstawie raportu wnioskuję że X" - możesz otworzyć ten raport i sprawdzić.

**Dlaczego to pomaga:**

- Możesz zweryfikować źródła (przeciw halucynacjom)
- Widzisz na czym AI pracuje (przeciw drift)
- Nadzór jest możliwy

**Wyobraź sobie:**

Różnica między "AI powiedział że tak jest" a "AI powiedział że tak jest, a ja otworzyłem dokument i sprawdziłem że faktycznie na stronie 15 jest ten cytat".

---

### Mechanizm 2: Checkpointing

**Co to jest:**

Regularne zapisywanie stanu pracy do pliku. Reset kontekstu bez utraty pracy.

**Jak to wygląda praktycznie:**

```
Pracujesz w chacie → [STOP: zapisz do pliku] → Nowa sesja czyta plik
```

Zamiast ciągnąć 50-wiadomościową konwersację, co jakiś czas mówisz: "Zapisz aktualny draft do pliku draft-v1.md".

Nowa sesja. "Przeczytaj draft-v1.md i kontynuuj."

Świeży kontekst. Bez balastu.

**Dlaczego to pomaga:**

- Reset driftu (świeży start)
- Mniejszy kontekst (tylko przefiltrowany wynik)
- Praca nie ginie (artefakt zostaje)
- Łatwiejsza weryfikacja (mniejsze kawałki)

**Kiedy checkpointować:**

- Po zakończeniu fazy (research → checkpoint → analiza)
- Gdy chat się wydłuża
- Gdy zauważasz drift
- Na koniec każdej sesji

**Wyobraź sobie:**

Zamiast jednego długiego dokumentu Google Docs z całą historią komentarzy i zmian, masz czyste wersje: v1, v2, v3. Każda jest "checkpointem".

---

### Mechanizm 3: Alignment (wydobycie założeń)

**Co to jest:**

Upewnienie się że AI rozumie zadanie tak jak ty, zanim zacznie wykonywać.

**Jak to wygląda praktycznie:**

1. Dajesz zadanie
2. Mówisz: "Zanim zaczniesz, powiedz swoimi słowami jak to rozumiesz. Jakie masz założenia?"
3. AI formułuje swoje rozumienie
4. Sprawdzasz, koregujesz
5. Dopiero potem: "OK, zaczynaj"

**Dlaczego to pomaga:**

AI jest "eager" - chętny do działania. Nie pyta, zakłada. Musisz **aktywnie wydobyć** te założenia, bo sam ich nie ujawni.

**Wyobraź sobie:**

Delegujesz zadanie pracownikowi. Nie mówisz tylko "zrób to". Mówisz "powiedz jak to rozumiesz, żebym wiedział że się zgadzamy".

Magiczne zdanie: *"Zanim zaczniesz wykonywać, powiedz jak rozumiesz to zadanie i jakie masz założenia."*

---

### Mechanizm 4: Steering (kontrola kierunku)

**Co to jest:**

Definiowanie kierunku przed wykonaniem. Korekta kierunku w trakcie.

**Jak to wygląda praktycznie:**

**Przed:** Sformułowane zadanie - przez ciebie precyzyjnie, lub przez agenta z kontekstu, lub mix.

**W trakcie:** Możesz interweniować:
- "Skup się bardziej na aspekcie finansowym"
- "Pomiń sekcję o technologii"
- "Zmień kierunek - idź bardziej w stronę X"

**Różnica od edycji:**

| Edycja | Steering |
|--------|----------|
| "Skróć ten akapit" | "Idź bardziej w kierunek X" |
| Poprawiasz tekst | Koregujesz kierunek |
| Po fakcie | W trakcie lub przed |

**Wyobraź sobie:**

Edycja: Poprawiasz tekst czerwonym długopisem.
Steering: Mówisz pracownikowi "wiesz co, idź bardziej w stronę analizy finansowej, mniej o operacjach".

---

### Mechanizm 5: Dekompozycja

**Co to jest:**

Rozbijanie dużego zadania na mniejsze, zarządzalne części.

**Jak to wygląda praktycznie:**

```
DUŻE ZADANIE
      │
      ├── Podzadanie 1 → [checkpoint]
      ├── Podzadanie 2 → [checkpoint]
      └── Podzadanie 3 → [checkpoint]
```

Zamiast: "Zrób 50-stronicowy raport strategiczny"

Robisz:
1. "Zbierz dane o rynku z tych źródeł" → zapisz
2. "Zbierz dane o konkurencji" → zapisz
3. "Przeanalizuj oba i wyciągnij wnioski" → zapisz
4. "Napisz executive summary" → zapisz
5. "Połącz w całość"

**Dlaczego to pomaga:**

- Mniejszy kontekst per zadanie
- Checkpoint między krokami
- Błąd nie propaguje się przez całość
- Łatwiejsza weryfikacja

**Wyobraź sobie:**

Zamiast budować dom jednym ruchem, budujesz fundamenty, potem ściany, potem dach. Po każdym etapie możesz sprawdzić czy wszystko OK.

---

### Mechanizm 6: Progressive Disclosure

**Co to jest:**

Ładowanie kontekstu stopniowo, na żądanie, po wstępnej ocenie.

**Jak to wygląda praktycznie:**

Masz 50 dokumentów do analizy. Zamiast wrzucać wszystkie naraz:

1. AI widzi: tytuły i krótkie opisy dokumentów
2. AI ocenia: które są relevantne?
3. Dla relevantnych: załaduj pełną treść
4. Analiza na zawężonym zbiorze

**Dlaczego to pomaga:**

- Nie ładujesz niepotrzebnych rzeczy
- Kontekst zostaje czysty
- AI decyduje co jest ważne (pod twoim nadzorem)

**Wyobraź sobie:**

Nie czytasz całej biblioteki żeby napisać raport. Najpierw przeglądasz tytuły i spisy treści. Potem sięgasz po konkretne książki.

---

### Mechanizm 7: Context Isolation

**Co to jest:**

Separacja różnych wątków w osobnych sesjach.

**Jak to wygląda praktycznie:**

Masz CV do oceny. Chcesz perspektywę rekrutera i perspektywę managera.

Zamiast jednej sesji gdzie AI próbuje być oboma:

```
[CV.pdf]
    │
    ├── Sesja A: "Jesteś rekruterem. Oceń to CV."
    │
    └── Sesja B: "Jesteś hiring managerem. Oceń to CV."
```

Dwie osobne, czyste perspektywy. Nie mieszają się.

**Dlaczego to pomaga:**

- Brak zanieczyszczenia między wątkami
- Czysty kontekst per perspektywa
- Różne "persony" nie interferują

**Wyobraź sobie:**

Pytasz o opinię dwóch różnych osób. Nie w jednej rozmowie, gdzie jedna słyszy co powiedziała druga. W osobnych rozmowach.

---

### Mechanizm 8: Artefakty (stan vs strumień)

**Co to jest:**

Praca zapisana w plikach, nie w historii chatu.

**Jak to wygląda praktycznie:**

```
CHAT = Strumień (co się dzieje teraz, znika gdy zamkniesz)
ARTEFAKT = Stan (co mamy, zostaje, można otworzyć)
```

Każdy znaczący output → zapisz do pliku.
Nie zostawiaj wniosków tylko w chacie.

**Dlaczego to pomaga:**

- Persystuje między sesjami
- Możesz zweryfikować (otwierasz plik)
- Nowa sesja czyta plik, nie historię
- Praca się kumuluje

**Wyobraź sobie:**

Chat to rozmowa telefoniczna. Kończy się - znika.
Artefakt to dokument na biurku. Kończysz rozmowę - dokument zostaje.

**Artefakt to:**
- Filtr (tylko wynik, bez szumu negocjacji)
- Kotwica (punkt odniesienia przeciw drift)
- Interfejs (widzisz co AI widzi)
- Akumulator (wiedza się kumuluje)

---

### Mapa: Mechanizmy i problemy

| Mechanizm | Halucynacje | Slop | Drift | Ograniczenia |
|-----------|:-----------:|:----:|:-----:|:------------:|
| Transparentność | ✓ | ✓ | ✓ | |
| Checkpointing | | ✓ | ✓ | ✓ |
| Alignment | | ✓ | ✓ | |
| Steering | | ✓ | ✓ | |
| Dekompozycja | | ✓ | ✓ | ✓ |
| Progressive Disclosure | ✓ | | | ✓ |
| Context Isolation | | | ✓ | ✓ |
| Artefakty | ✓ | ✓ | ✓ | ✓ |

Zauważ: **Checkpointing** i **Artefakty** pojawiają się wszędzie. To są meta-mechanizmy.

---

## Część V: Lifecycle Tasku

Każde złożone zadanie przechodzi przez fazy. Zrozumienie tych faz pozwala stosować mechanizmy we właściwym momencie.

---

### Faza 1: Gromadzenie kontekstu

**Co się dzieje:**

Zbierasz materiały potrzebne do zadania. Źródła, dane, dokumenty, przykłady.

**Kto to robi:**

- Ty (wybierasz pliki)
- AI (robi research)
- Kombinacja (AI szuka, ty filtrujesz)

**Uwaga:**

Gdy AI robi research, generuje dużo tekstu w chacie - linki, streszczenia, oceny. To zaśmieca kontekst.

**Dlatego:**

Po research → checkpoint. "Zapisz listę źródeł do pliku sources.md". Nowa sesja do analizy.

**Wyobraź sobie:**

Zanim zaczniesz pisać raport, zbierasz wszystkie dokumenty na biurku. To jest ta faza.

---

### Faza 2: Formułowanie zadania

**Co się dzieje:**

Określasz co AI ma zrobić. Ale nie musisz wszystkiego formułować sam.

**Spectrum formułowania:**

```
TY SPECYFIKUJESZ ◄────────────────────► AGENT FORMUŁUJE
PRECYZYJNIE                              Z KONTEKSTU
```

**Co agent może wiedzieć sam (z kontekstu):**
- Struktura poprzednich raportów (jeśli ma dostęp do plików)
- Styl komunikacji (jeśli widzi przykłady)
- Specyfika projektu (jeśli ma brief/dokumenty)

**Co musisz powiedzieć ty:**
- Cel (co chcesz osiągnąć)
- Dla kogo (odbiorca)
- Priorytety (co jest ważne)

**Co agent może sformułować za ciebie:**
- "Przejrzyj kontekst i powiedz jak rozumiesz zadanie"
- "Dopytaj mnie o to, czego ci brakuje"
- "Zaproponuj strukturę na podstawie poprzednich raportów"

**Przykłady na spectrum:**

❌ Za mało: "Przeanalizuj dane sprzedażowe"

✅ Ty specyfikujesz: "Przeanalizuj pliki CSV w /sales-q4. Top 10 produktów po revenue. Raport PDF, format jak q3-report.pdf"

✅ Agent formułuje: "Mam zrobić analizę Q4. Pliki w /data, poprzednie raporty w /reports. Powiedz jak rozumiesz zadanie i dopytaj mnie"

✅ Mix: "Chcę raport Q4 dla zarządu. Zaproponuj strukturę na podstawie poprzedniego"

---

### Faza 3: Alignment

**Co się dzieje:**

Upewniasz się że AI rozumie zadanie tak jak ty.

**Alignment to droga dwukierunkowa:**

1. Ty możesz specyfikować → AI potwierdza rozumienie
2. AI może formułować z kontekstu → ty koregujesz
3. Mix: ty dajesz kierunek, AI doprecyzowuje, ty zatwierdzasz

**Jak to zrobić:**

1. Dajesz zadanie (precyzyjnie lub prosisz o sformułowanie)
2. AI formułuje swoje rozumienie: "Rozumiem że mam..., zakładam że..."
3. Sprawdzasz: Czy rozumie cel? Czy założenia OK? Czy użyje właściwych źródeł?
4. Koregujesz jeśli trzeba
5. Dopiero potem: "OK, teraz zrób plan"

**Checkpoint:**

Po alignment możesz zapisać brief jako "kontrakt" na resztę zadania.

**Wyobraź sobie:**

Przekazujesz pracownikowi projekt. Może mu dać szczegółowy brief. Albo może pokazać poprzedni projekt i powiedzieć "zrób podobnie". W obu przypadkach prosisz żeby powiedział własnymi słowami co zrozumiał.

---

### Faza 4: Planowanie

**Co się dzieje:**

AI proponuje jak wykona zadanie. Ty weryfikujesz podejście.

**Dlaczego plan jest ważny:**

- Możesz zweryfikować kierunek zanim AI zainwestuje czas
- Łapiesz błędy wcześnie
- Plan jest kotwicą dla wykonania

**Co powinien zawierać:**

- Kroki wykonania
- Jakie źródła użyje
- Jaka struktura outputu
- Jakie założenia

**Wyobraź sobie:**

Pracownik przed zrobieniem dużego projektu mówi: "Myślę żeby podejść do tego tak: najpierw X, potem Y, na koniec Z. Co myślisz?"

---

### Faza 5: Wykonanie

**Co się dzieje:**

AI pracuje według planu. Produkuje output.

**Twoja rola:**

- Możesz obserwować postęp
- Możesz interweniować (steering) gdy widzisz że odpływa
- Nie musisz (ale możesz)

**Steering w trakcie:**

- "Skup się bardziej na X"
- "Pomiń sekcję o Y"
- "Użyj innego podejścia do Z"

Steering ≠ editing. Steering to korekta kierunku, nie poprawianie tekstu.

---

### Faza 6: Review (weryfikacja)

**Co się dzieje:**

AI skończył. Sprawdzasz wynik.

**Ile editing potrzebujesz:**

Zależy od jakości wcześniejszych faz.
- Dobry alignment + dobry plan = mało editing
- Słaby alignment = dużo editing

**Uwaga:**

Każda korekta w chacie to więcej tekstu w kontekście. Dlatego po editing → checkpoint.

Artefakt po editing = czysty stan. Następna sesja nie widzi historii poprawek.

---

### Faza 7: Checkpoint i dalej

**Co się dzieje:**

Zapisujesz finalny artefakt. Zaczynasz następne zadanie z czystym kontekstem.

**Jak to działa:**

"Zapisz finalną wersję jako analysis-v1.md"

Następne zadanie: nowa sesja. "Przeczytaj analysis-v1.md. Klient chce dodać sekcję o X."

Świeży kontekst. Budujesz na poprzednim. Bez balastu procesu.

---

### Schemat całości

```
GROMADZENIE KONTEKSTU
        │
   [checkpoint: źródła]
        │
FORMUŁOWANIE (ty ↔ agent)
        │
ALIGNMENT ("jak to rozumiesz?")
        │
   [checkpoint: brief]
        │
PLANOWANIE
        │
   [checkpoint: plan]
        │
WYKONANIE (+ steering w razie potrzeby)
        │
REVIEW
        │
   [checkpoint: artefakt]
        │
NASTĘPNE ZADANIE
```

Każdy checkpoint to:
- Reset kontekstu
- Filtracja (tylko signal)
- Kotwica dla następnej fazy
- Możliwość weryfikacji

---

## Część VI: Rola Czatu

### Czat jako warstwa kontroli

Czat nie jest "trybem pracy" (vs agent mode). Czat jest **interfejsem kontroli** - medium przez które sterujesz AI.

```
┌─────────────────────────────┐
│     TY (intencja)           │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│     CZAT (kontrola)         │
│  • eksternalizacja intencji │
│  • steering                 │
│  • weryfikacja              │
│  • korekta                  │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│     AI (wykonanie)          │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│     ARTEFAKT (stan)         │
└─────────────────────────────┘
```

---

### Czat PRZED wykonaniem

**Do czego służy:**

- Eksternalizacja intencji (z głowy do słów)
- Krystalizacja niejasnych wymagań
- Alignment z AI
- Definiowanie zadania

**Dlaczego to ważne:**

Nie zawsze wiesz czego chcesz. Intencja jest:
- W głowie, nie wyartykułowana
- Niejasna (wiesz mniej-więcej, nie precyzyjnie)
- Ewoluująca (zmienia się gdy widzisz opcje)

Czat pozwala to wyciągnąć i skrystalizować.

**Wyobraź sobie:**

Mówisz: "Chcę coś takiego jak... no wiesz... raport ale nie całkiem raport...". Przez rozmowę krystalizuje się: "Aha, chcesz executive summary z rekomendacjami, max 3 strony, dla zarządu".

---

### Czat PO wykonaniu

**Do czego służy:**

- Weryfikacja outputu
- Korekta ("nie to miałem na myśli")
- Dopytywanie ("czemu tak zrobiłeś?")
- Editing (poprawki)

**Dlaczego to ważne:**

Intencja ewoluuje gdy widzisz output. Oceniasz w trakcie. Odkrywasz czego chcesz przez zobaczenie czego NIE chcesz.

---

### Czat jako źródło bałaganu

**Problem:**

Czat zaśmieca kontekst:
- Historia negocjacji
- Ślepe uliczki
- Poprawki i re-generacje
- Wszystko append-only

**Rozwiązanie:**

Po każdej znaczącej fazie → checkpoint.

```
Czat (alignment) → [checkpoint: brief]
Czat (review) → [checkpoint: artefakt]
```

Checkpoint = filtracja. Tylko sygnał zostaje. Szum znika.

---

### Model: Stan i Sygnał

```
ARTEFAKT = Stan (rzeczownik)
    - Co jest teraz
    - Persystuje
    - Weryfikowalny

CZAT = Sygnał (czasownik)
    - Co zmienić
    - Efemeryczny
    - Intencja, korekta

AI = Transformacja (funkcja)
    - Stan + Sygnał → Nowy Stan
```

**Formuła:**

```
nowy_artefakt = AI(obecny_artefakt, sygnał_z_czatu)
```

Czat mówi CO ZMIENIĆ.
Artefakt jest TYM CO SIĘ ZMIENIA.

---

### Gdyby nie czat

Bez czatu AI byłby w pełni autonomiczny:
- Zadanie → wykonanie → output
- Zero steering, zero feedback
- Ty poza pętlą

Czat daje kontrolę:
- Przed: precyzujesz intencję
- W trakcie: koregujesz kierunek
- Po: weryfikujesz i poprawiasz

> "Czat to kokpit. Bez niego AI leci na autopilocie."

---

## Część VII: Podsumowanie

### Model całościowy

```
┌───────────────────────────────────────────────────────┐
│              PROBLEMY KONTEKSTU                        │
│   Halucynacje • Slop • Drift • Ograniczenia           │
└───────────────────────────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────┐
│                   MECHANIZMY                           │
│ Transparentność • Checkpointing • Alignment • Steering│
│ Dekompozycja • Progressive Disclosure • Isolation     │
└───────────────────────────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────┐
│                LIFECYCLE TASKU                         │
│ Kontekst → Zadanie → Alignment → Plan → Wykonanie     │
│          ↓           ↓           ↓               ↓    │
│     [checkpoint] [checkpoint] [checkpoint]  [checkpoint]│
└───────────────────────────────────────────────────────┘
                          │
                          ▼
┌───────────────────────────────────────────────────────┐
│                 WARSTWY SYSTEMU                        │
│ Intencja (ty) → Kontrola (czat) → Wykonanie (AI)      │
│                        ↓                               │
│                   Stan (artefakty)                     │
└───────────────────────────────────────────────────────┘
```

---

### Siedem zasad

**1. AI nie jest źródłem wiedzy - jest procesorem**

Daj mu materiały do przetworzenia, nie pytaj co "wie".

**2. Wszystkie problemy to problemy kontekstu**

Halucynacje, slop, drift - wszystko sprowadza się do kontekstu. Rozwiązujesz je przez zarządzanie kontekstem.

**3. Checkpointing jest meta-rozwiązaniem**

Rozwiązuje drift, ograniczenia, zaśmiecanie kontekstu. Stosuj często.

**4. AI jest "eager"**

Zakłada zamiast pytać. Wydobywaj założenia przed wykonaniem.

**5. Steering > Editing**

Definiuj precyzyjnie na początku. Mniej poprawiania na końcu.

**6. Czat to kontrola, artefakt to stan**

Czat mówi co zmienić. Artefakt jest tym co się zmienia.

**7. Transparentność umożliwia nadzór**

Widzisz co AI widzi. Możesz weryfikować.

---

### Jedno zdanie

> **"Dostarcz odpowiedni kontekst, zapewnij alignment, checkpointuj często, weryfikuj przyrostowo."**

---

### Twój następny krok

Nie musisz wszystkiego naraz. Zacznij od jednej rzeczy:

**Na najbliższe zadanie:**

1. Daj AI kontekst (pliki, przykłady) i cel - nie musisz specyfikować wszystkiego, agent może wyciągnąć z kontekstu
2. Po wpisaniu zadania dodaj: "Zanim zaczniesz, powiedz jak to rozumiesz i jakie masz założenia. Dopytaj mnie o to czego ci brakuje"
3. Przed zamknięciem sesji: "Zapisz wynik do pliku X"

Trzy małe zmiany. Jeden raz. Zobacz różnicę.

---

*Praca z Agentami AI: Pełna Narracja*
*Wersja dla konsultantów i knowledge workers*
*Styczeń 2026*
