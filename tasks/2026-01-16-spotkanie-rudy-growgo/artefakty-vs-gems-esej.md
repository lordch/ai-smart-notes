# Strumień vs Kotwica: Dlaczego artefakty zmieniają naturę pracy z AI

*Notatka dla Rudy'ego — eksploracja intelektualna, nie pitch sprzedażowy*

---

## Podstawowa metafora

Wyobraź sobie dwa sposoby pisania książki.

**Sposób pierwszy (Strumień):** Siadasz z ghostwriterem i dyktujecie książkę od początku do końca w jednej rozmowie. Każde zdanie płynie z poprzedniego. Jeśli w rozdziale 7 zauważysz, że coś w rozdziale 2 wymaga zmiany — wracasz i opowiadasz od nowa. Ghostwriter pamięta całą rozmowę, ale ta pamięć się "zaśmieca" — pamięta też wszystkie twoje wahania, ślepe uliczki, momenty gdy zmieniałeś zdanie.

**Sposób drugi (Kotwica):** Masz folder z plikami. Rozdział 1, Rozdział 2, notatki o postaciach, outline całości. Ghostwriter może w każdej chwili zajrzeć do dowolnego pliku. Gdy chcesz zmienić coś w rozdziale 2 — otwierasz ten plik, zmieniasz konkretne zdanie, reszta pozostaje nienaruszona. Ghostwriter następnego dnia nie pamięta waszej wczorajszej rozmowy, ale ma dostęp do wszystkich plików — czyli do tego, co *zdecydowałeś zachować*.

Gem działa jak pierwszy sposób. System z artefaktami jak drugi.

---

## Gdzie Gem jest lepszy (i wystarczający)

Zanim przejdę do artefaktów, chcę uczciwie powiedzieć gdzie Gem wygrywa. Bo wygrywa — w wielu sytuacjach.

### Transakcyjne, jednorazowe zadania

Karolina z działu HR dostaje CV i ma napisać odpowiedź odmowną. Otwiera Gema "Odpowiedzi HR", wkleja CV, dostaje draft. Edytuje dwa słowa, wysyła. Całość trwa 3 minuty.

Tutaj artefakt byłby overkillem. Karolina nie potrzebuje "pamiętać" tej interakcji. Nie będzie wracać do tego CV za tydzień. To jest *transakcja*, nie *proces*.

### Standaryzowane formaty z jasnym inputem i outputem

Gem "Podsumowanie spotkania" dostaje transkrypt, zwraca bullet points w określonym formacie. Input jest jasny (transkrypt), output jest jasny (podsumowanie), transformacja jest zawsze taka sama.

To jest jak automat do kawy. Wrzucasz monetę, dostajesz kawę. Nie potrzebujesz "relacji" z automatem.

### Gdy użytkownik nie chce myśleć

I to jest kluczowe. Część ludzi *nie chce* zarządzać kontekstem. Nie chce decydować co jest ważne, co zapisać, jak zorganizować. Chce wpisać zapytanie i dostać odpowiedź.

Gem daje im to. System artefaktowy wymaga od nich więcej — wymaga *decyzji* o tym, co utrwalić.

---

## Scenariusze gdzie artefakt zmienia grę

### Scenariusz 1: Prawnik i due diligence

Marcin prowadzi due diligence przy przejęciu firmy. Ma 200 dokumentów do przejrzenia. 

**Wariant Gem:** 
Otwiera Gema "Analiza prawna", wkleja pierwszy dokument, dostaje analizę. Potem drugi. Potem trzeci. Każda analiza jest osobna. Gdy w dokumencie 47 znajdzie coś, co zmienia interpretację dokumentu 12 — musi wrócić, wkleić dokument 12 jeszcze raz, powiedzieć "pamiętaj że w dokumencie 47 było X".

Problem: Gem nie "pamięta" dokumentu 47 gdy analizuje dokument 12. Marcin musi być tym, który łączy kropki.

**Wariant artefakt:**
Marcin ma folder `due-diligence-przejecie-alfa/`. W środku:
- `findings.md` — rosnąca lista ustaleń
- `risk-flags.md` — rzeczy wymagające uwagi
- `document-summaries/` — po jednym pliku na dokument

Agent analizuje dokument 47, znajduje coś ważnego, zapisuje do `risk-flags.md`. Gdy analizuje dokument 12, ma dostęp do `risk-flags.md` — widzi flagę z dokumentu 47. Sam łączy kropki.

Ale jest coś głębszego. Po dwóch tygodniach Marcin idzie na spotkanie z klientem. Nie musi czytać 200 dokumentów ani pamiętać 200 sesji czatu. Otwiera `findings.md` i `risk-flags.md` — ma *destylat* dwóch tygodni pracy.

### Scenariusz 2: Kampania marketingowa przez kwartał

Ola zarządza kampanią dla nowego produktu. Trzy miesiące, dziesiątki materiałów, ewoluująca strategia.

**Tydzień 1:** Definiuje target audience, key messages, tone of voice.

**Wariant Gem:**
Ola spisuje to w dokumencie Google Docs. Gdy potrzebuje nowego materiału, otwiera Gema, wkleja "kontekst kampanii" z Google Docs, pisze "stwórz post na LinkedIn".

**Tydzień 6:** Okazuje się, że target audience jest inny niż zakładali. Key messages trzeba zmienić.

Ola aktualizuje Google Docs. Ale wszystkie poprzednie materiały były tworzone ze starym kontekstem. Każdy nowy materiał wymaga świadomego wklejenia nowego kontekstu. Jeśli Ola zapomni — Gem użyje swojego "wbudowanego" zrozumienia kampanii, które jest nieaktualne.

**Wariant artefakt:**
Ola ma folder `kampania-produkt-x/`:
- `strategy.md` — aktualny stan strategii
- `audience.md` — opis target audience
- `voice.md` — tone of voice
- `materials/` — wszystkie stworzone materiały

W `CLAUDE.md` (lub w nagłówku każdego pliku) jest: "Przed tworzeniem materiałów, przeczytaj `strategy.md` i `voice.md`."

Gdy w tygodniu 6 Ola aktualizuje `audience.md` — każdy kolejny materiał automatycznie korzysta z nowej wersji. Nie musi pamiętać żeby wklejać kontekst. Kontekst jest *żywy*.

Co więcej — może zobaczyć *historię* zmian. "Zobaczmy, jak opisywaliśmy audience w tygodniu 2 vs teraz." To jest niemożliwe w Gemie.

### Scenariusz 3: Chirurgiczna precyzja vs ryzyko rewrite'u

To jest subtelne, ale krytyczne dla korporacji.

Tomek pracuje nad umową. 47 stron, miesiąc negocjacji, każde słowo ważone przez prawników obu stron.

**Wariant Gem:**
Tomek wkleja umowę, mówi "zmień w paragrafie 12.3 słowo 'może' na 'musi'".

Gem generuje... całą umowę od nowa. Z tą zmianą. Ale też z subtelnymi różnicami w innych miejscach — może przestawił przecinek w paragrafie 8, może użył innego synonimu w paragrafie 23.

Tomek musi teraz PORÓWNAĆ 47-stronicowy dokument słowo po słowie. Albo zaufać, że Gem nic nie zmienił — a tego zaufania w kontekście prawnym *nie może mieć*.

**Wariant artefakt:**
Tomek ma plik `umowa-v7.md`. Mówi agentowi "zmień w paragrafie 12.3 słowo 'może' na 'musi'".

Agent robi *diff* — chirurgiczną zmianę jednego słowa. Tomek widzi dokładnie: "Zmieniono 1 linię. Przed: 'Strona może wypowiedzieć...' Po: 'Strona musi wypowiedzieć...'".

47 stron pozostaje *nienaruszone*. Nie ma ryzyka przypadkowej zmiany.

### Scenariusz 4: Równoległe ścieżki eksploracji

Ania pisze raport o wejściu na nowy rynek. Jest niepewna — są trzy możliwe strategie i chce zbadać każdą.

**Wariant Gem:**
Ania otwiera Gema, zaczyna dyskusję o strategii A. Gem się rozpisuje, Ania dopytuje, pojawiają się wątki za i przeciw. Potem mówi "a co gdybyśmy wybrali strategię B?".

Gem teraz ma w kontekście całą dyskusję o strategii A. Jego odpowiedź o strategii B jest *zakotwiczona* w poprzedniej rozmowie — może nieświadomie porównywać, może być biased przez argumenty które sam wcześniej wygenerował.

Co gorsza, gdy za dwa dni Ania chce wrócić do strategii A — musi albo przewijać długą rozmowę, albo zaczynać od nowa.

**Wariant artefakt:**
Ania otwiera trzy osobne "ścieżki":
- Sesja 1: "Zbadaj strategię A, zapisz wnioski do `strategy-a.md`"
- Sesja 2 (fresh context): "Zbadaj strategię B, zapisz wnioski do `strategy-b.md`"
- Sesja 3 (fresh context): "Zbadaj strategię C, zapisz wnioski do `strategy-c.md`"

Każda eksploracja jest *czysta* — nie zaśmiecona poprzednimi. Potem:
- Sesja 4: "Przeczytaj `strategy-a.md`, `strategy-b.md`, `strategy-c.md`. Porównaj i daj rekomendację."

To jest jak mieć trzech niezależnych analityków, z których każdy zbadał jedną opcję, a potem czwartego, który syntetyzuje ich prace. Każdy pracował "na czysto", bez wzajemnych biasów.

### Scenariusz 5: Wiedza która rośnie (knowledge compound)

To jest może najważniejszy scenariusz.

Filip jest konsultantem strategicznym. Przez 10 lat zrobił 50 projektów dla firm z sektora retail.

**Wariant Gem:**
Każdy projekt to osobne sesje z Gemem. Gem nie pamięta poprzednich projektów. Filip pamięta — w swojej głowie. Ale gdy odchodzi z firmy, wiedza odchodzi z nim.

**Wariant artefakt:**
Filip ma repozytorium:
- `retail-patterns.md` — wzorce które widział wielokrotnie
- `case-studies/` — folder z podsumowaniami projektów (zanonimizowane)
- `frameworks/` — sprawdzone podejścia do typowych problemów

Gdy zaczyna nowy projekt dla sieci sklepów, pisze: "Przeczytaj `retail-patterns.md`. Nowy klient to sieć 200 sklepów, problem: spadająca konwersja w weekendy."

Agent ma dostęp do 10 lat doświadczenia Filipa — nie dlatego że "pamięta", tylko dlatego że Filip *zeksternalizował* swoją wiedzę do plików.

Gdy Filip odchodzi z firmy — pliki zostają. Nowy konsultant może zacząć z tym samym kontekstem.

To jest **compound interest wiedzy**. Gem to single session. Artefakt to akumulacja.

---

## Szara strefa: gdzie nie jest oczywiste

### Gdy zadanie jest "prawie" jednosesyjne

Marta pisze artykuł na bloga firmowego. Powiedzmy 1500 słów. Mieści się w jednej sesji z Gemem. Czy potrzebuje artefaktu?

**Argument za Gemem:** Szybciej. Otwierasz, piszesz, dostajesz, gotowe.

**Argument za artefaktem:** A jeśli jutro szef poprosi o poprawki? Z Gemem — zaczynasz nową sesję, wklejasz artykuł, tłumaczysz co już było zmieniane. Z artefaktem — otwierasz plik, plik "pamięta" sam siebie, robisz inkrementalne zmiany.

Granica jest płynna. Dla jednorazowego artykułu — Gem. Dla artykułu który będzie ewoluował — artefakt.

### Gdy standaryzacja jest kluczowa, ale kontekst się zmienia

Dział obsługi klienta chce odpowiadać spójnie. 

**Argument za Gemem:** Każdy pracownik używa tego samego Gema, odpowiedzi są spójne.

**Argument za artefaktem:** A gdy zmienia się polityka firmy? W Gemie — aktualizujesz prompt, ale stare odpowiedzi zostały wysłane ze starą polityką i nie masz śladu co było zmieniane. W artefakcie — masz `policy.md` z historią zmian. Wiesz dokładnie który pracownik odpowiedział według której wersji polityki.

### Gdy prostota jest najważniejsza

Czasami odpowiedź brzmi: "Gem wystarczy, nie komplikuj."

Startup, pięć osób, tempo jest wszystkim. Czy naprawdę potrzebują "repozytorium kontekstu z version control"? Czy może wystarczy Gem "Nasz brand voice" i po prostu będą działać?

Odpowiedź zależy od fazy. Na początku — prostota wygrywa. Gdy zaczynasz mieć problem ze spójnością, ze skalą, z wiedzą która ucieka — wtedy artefakty zaczynają mieć sens.

---

## Głębsza implikacja: kto jest właścicielem wiedzy?

W modelu Gem, wiedza żyje w dwóch miejscach:
1. W głowie osoby która skonfigurowała Gema
2. W konfiguracji Gema (black box, trudno eksportować)

W modelu artefakt, wiedza żyje w plikach:
1. `strategy.md`
2. `brand-voice.md`
3. `customer-personas.md`

Pliki można:
- Wersjonować (git)
- Przeglądać (kto zmienił co, kiedy)
- Eksportować (zmiana providera AI nie oznacza utraty wiedzy)
- Współdzielić (nowy pracownik czyta te same pliki)
- Auditować (compliance, ISO)

To nie jest technikalia. To jest pytanie: **czy wiedza firmy jest zamknięta w narzędziu, czy jest przenośna?**

---

## Metafora końcowa: notatnik vs rozmowa

Możesz mieć genialną rozmowę przy kolacji. Pełna insightów, przełomowych myśli, błyskotliwych sformułowań. Następnego dnia pamiętasz może 20% — i to w wersji już przetworzonej przez twoją pamięć.

Możesz też pisać do notatnika. Wolniej, więcej wysiłku. Ale za rok — notatnik nadal ma te same słowa. Możesz wrócić, zacytować, zbudować na nich.

Gem to rozmowa. Artefakt to notatnik.

Obie formy mają sens. Ale budowanie firmy na rozmowach — które znikają po zamknięciu okna — to zupełnie inna architektura niż budowanie na notatnikach — które zostają.

---

## Pytania do dalszej eksploracji

1. **Hybrid model:** Czy można mieć Gema który *pod spodem* czyta i pisze do artefaktów? (Odpowiedź: tak, i to jest może najbardziej interesujący kierunek.)

2. **Granularność:** Gdzie jest granica między "to jest transakcja" a "to jest proces który wymaga artefaktu"?

3. **Adoption:** Jak przekonać organizację do pracy z plikami, gdy są przyzwyczajeni do "wpisz pytanie, dostań odpowiedź"?

4. **Koszty:** Czy artefakty wymagają więcej infrastruktury? (Odpowiedź: minimum to folder z plikami. Maksimum to git + CI/CD dla kontekstu.)

---

*To nie jest "moje podejście vs twoje". To jest pytanie: jaką architekturę wiedzy budujemy? I dla jakich zadań która architektura ma sens.*
