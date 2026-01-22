# Brief: Analiza dorobku naukowego dr Dagny Krankowskiej

## Kontekst projektu

Przygotowujemy wdrożenie **agentic workspace** dla dr Dagny Krankowskiej - lekarki i badaczki z Warszawskiego Uniwersytetu Medycznego, specjalizującej się w HIV/AIDS i chorobach zakaźnych.

Agentic workspace to środowisko pracy z AI, w którym agent ma dostęp do dobrze zorganizowanego kontekstu domenowego, rozumie specyfikę pracy użytkownika i może efektywnie wspierać codzienne zadania.

## Cel analizy

Zbudowanie **profilu domenowego** Dagny, który posłuży jako fundament kontekstu dla jej agenta. Chcemy zrozumieć:
- W jakiej przestrzeni intelektualnej pracuje
- Jakim językiem się posługuje
- Jakie problemy rozwiązuje
- Jak wygląda jej workflow badawczy

---

## Źródła do analizy

Wszystkie źródła są dostępne lokalnie w folderze `publikacje/`.

### Doktorat (BIP WUM) - pliki PDF

| Plik | Opis | Priorytet |
|------|------|-----------|
| `streszczenie-pl.pdf` | Streszczenie polskie - najważniejsze do zrozumienia głównego tematu | ⭐⭐⭐ |
| `streszczenie-en.pdf` | Streszczenie angielskie | ⭐⭐ |
| `doktorat-wersja-utajona.pdf` | Pełna rozprawa (106 stron) - może być częściowo utajona | ⭐⭐⭐ |
| `recenzja-garlicki.pdf` | Recenzja prof. Garlickiego - zawiera ocenę i kontekst | ⭐⭐ |
| `recenzja-moniuszko.pdf` | Recenzja prof. Moniuszko-Malinowskiej | ⭐⭐ |
| `recenzja-inglot.pdf` | Recenzja prof. Inglot | ⭐⭐ |

**Jak odczytać PDF:** `pdftotext nazwa_pliku.pdf -` (wypisuje tekst na stdout)

### Artykuły naukowe (PMC) - pliki XML

Pełne teksty artykułów w formacie JATS XML. Zawierają: abstrakt, wprowadzenie, metody, wyniki, dyskusję, bibliografię.

| Plik | Rok | Tematyka | Priorytet |
|------|-----|----------|-----------|
| `PMC5577695-art-treatment-efficacy-poland.xml` | 2017 | Skuteczność ART w Polsce (cel WHO 90%) | ⭐⭐⭐ |
| `PMC6186319-heparin-binding-peritonitis.xml` | 2018 | Diagnostyka zapalenia otrzewnej (biomarkery) | ⭐ |
| `PMC7229562-erysipelas-cellulitis-risk.xml` | 2020 | Czynniki ryzyka róży i cellulitis | ⭐ |
| `PMC7520378-children-covid-warsaw.xml` | 2021 | Dzieci i COVID-19 w Warszawie | ⭐ |
| `PMC9412590-adenovirus36-hiv-cardiovascular.xml` | 2022 | Adenovirus 36 u osób z HIV - ryzyko sercowo-naczyniowe | ⭐⭐ |
| `PMC9540674-wellbeing-hiv.xml` | 2022 | Interwencja psychologiczna u osób z HIV | ⭐⭐ |
| `PMC9877591-delayed-hiv-covid.xml` | 2022 | Opóźniona diagnoza HIV w pandemii COVID | ⭐⭐⭐ |
| `PMC10148112-late-hiv-migrants.xml` | 2023 | Późna diagnoza HIV u migrantek w Europie | ⭐⭐⭐ |

**Jak odczytać XML:** Pliki są w formacie JATS - można je parsować lub czytać bezpośrednio (tekst jest czytelny między tagami XML).

**Kluczowe tagi w XML:**
- `<article-title>` - tytuł
- `<abstract>` - abstrakt
- `<body>` - główna treść (sekcje: intro, methods, results, discussion)
- `<kwd>` - słowa kluczowe
- `<ref-list>` - bibliografia

---

## Pytania do odpowiedzenia

### 1. Domena ekspercka

- Jakie **konkretne zagadnienia medyczne** obejmuje jej badanie?
- Jakie **choroby oportunistyczne** są przedmiotem analizy?
- Jaki jest **kontekst kliniczny** (ambulatoryjna opieka? hospitalizacja? profilaktyka?)
- Jakie są **kluczowe wnioski** jej badań?
- Jak ewoluowały jej zainteresowania badawcze od 2017 do 2023?

### 2. Terminologia specjalistyczna

- Jakie **terminy medyczne** są centralne dla jej pracy?
- Jakie **akronimy i skróty** używa (np. ART, CD4, viral load, PLWH)?
- Jakie **koncepcje kliniczne** agent powinien rozumieć bez wyjaśniania?
- Stwórz **glosariusz** (20-30 kluczowych terminów z definicjami)
- Uwzględnij terminy z różnych obszarów: HIV, infekcje, diagnostyka, psychologia zdrowia

### 3. Metodologia badawcza

- Jakie **metody badawcze** stosuje (retrospektywne? prospektywne? kohortowe? systematic review?)
- Jakie **źródła danych** wykorzystuje (rejestry pacjentów? bazy danych? ankiety?)
- Jakie **narzędzia statystyczne** prawdopodobnie używa?
- Jak **strukturyzuje argumentację** naukową?
- Czy preferuje badania ilościowe czy jakościowe?

### 4. Pytania badawcze i problemy

- Jakie **hipotezy** testowała w różnych pracach?
- Jakie **praktyczne implikacje** mają jej wyniki dla opieki nad pacjentami?
- Jakie **otwarte pytania** zostają po jej badaniach?
- Jakie są **wspólne wątki** łączące jej publikacje?

### 5. Styl i forma

- Jak pisze - **formalność**, **struktura**, **długość zdań**?
- Jakie **konwencje** stosuje (cytowania, formatowanie)?
- Czy są charakterystyczne **wzorce** w jej pisaniu?
- Porównaj styl w artykułach polskich vs angielskich

### 6. Sieć współpracy

- Kim są **współautorzy** i jaka jest ich ekspertyza?
- Jakie **instytucje** pojawiają się w kontekście jej pracy?
- W jakich **projektach międzynarodowych** uczestniczy?

---

## Oczekiwany output

Stwórz dokument `profil-domenowy.md` zawierający:

```markdown
# Profil domenowy - dr Dagny Krankowska

## Streszczenie eksperckie
(2-3 akapity: kim jest, co bada, dlaczego to ważne)

## Ewolucja zainteresowań badawczych
(Timeline: 2017-2023, jak zmieniały się tematy)

## Mapa domeny
(Kluczowe obszary jej ekspertyzy w formie listy/hierarchii)
- HIV/AIDS
  - ART i adherencja
  - Choroby oportunistyczne
  - Zdrowie kobiet z HIV
  - ...
- Choroby zakaźne
  - ...

## Glosariusz
(Tabela: termin | definicja | kontekst użycia w jej pracach)

## Metodologia
(Jak pracuje, jakie podejścia stosuje, preferowane metody)

## Pytania badawcze
(Jakie problemy ją interesują - lista z przykładami z publikacji)

## Implikacje dla agenta
(Konkretne wnioski: co agent powinien wiedzieć, rozumieć, umieć)
```

---

## Jak wykorzystamy te informacje

1. **System prompt** - agent będzie wiedział, że pracuje z lekarzem-badaczem HIV/AIDS
2. **Terminologia** - agent nie będzie prosił o wyjaśnienie podstawowych pojęć z jej dziedziny  
3. **Kontekst zadań** - agent zrozumie typowe zadania (przegląd literatury, analiza danych, pisanie publikacji)
4. **Styl komunikacji** - agent dopasuje się do jej sposobu formułowania myśli
5. **Proaktywne wsparcie** - agent będzie mógł przewidywać potrzeby na podstawie znajomości workflow

---

## Ważne uwagi

- Szukamy **praktycznych informacji** do budowania kontekstu, nie akademickiego streszczenia
- Priorytet: **terminologia** i **sposób myślenia** nad szczegółami wyników badań
- Analizuj **wszystkie dostępne publikacje** - nie tylko doktorat
- Szukaj **wzorców** i **powtarzających się tematów** w jej dorobku
- Zaznacz wyraźnie, co jest **faktem** z dokumentów, a co **wnioskiem/interpretacją**
- Glosariusz powinien być **praktyczny** - terminy które agent napotka w codziennej pracy z Dagny
