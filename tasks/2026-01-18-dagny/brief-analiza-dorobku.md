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

## Źródła do analizy

1. **Rozprawa doktorska:** "Zależność między systematyczną opieką nad osobami z HIV, a występowaniem wybranych chorób oportunistycznych"
   - Źródło: [BIP WUM](https://bip.wum.edu.pl/doktorat-lub-habilitacja/dh-lek-dagny-krankowska)
   - Dostępne: streszczenie PL, streszczenie EN, wersja utajona rozprawy

2. **Recenzje:** prof. Garlicki, prof. Moniuszko-Malinowska, prof. Inglot
   - Mogą zawierać cenne obserwacje o mocnych stronach i kontekście pracy

## Pytania do odpowiedzenia

### 1. Domena ekspercka

- Jakie **konkretne zagadnienia medyczne** obejmuje jej badanie?
- Jakie **choroby oportunistyczne** są przedmiotem analizy?
- Jaki jest **kontekst kliniczny** (ambulatoryjna opieka? hospitalizacja? profilaktyka?)
- Jakie są **kluczowe wnioski** jej badań?

### 2. Terminologia specjalistyczna

- Jakie **terminy medyczne** są centralne dla jej pracy?
- Jakie **akronimy i skróty** używa (np. ART, CD4, viral load)?
- Jakie **koncepcje kliniczne** agent powinien rozumieć bez wyjaśniania?
- Stwórz **mini-glosariusz** (10-20 kluczowych terminów z definicjami)

### 3. Metodologia badawcza

- Jakie **metody badawcze** stosuje (retrospektywne? prospektywne? kohortowe?)
- Jakie **źródła danych** wykorzystuje (rejestry pacjentów? bazy danych? ankiety?)
- Jakie **narzędzia statystyczne** prawdopodobnie używa?
- Jak **strukturyzuje argumentację** naukową?

### 4. Pytania badawcze i problemy

- Jakie **hipotezy** testowała w doktoracie?
- Jakie **praktyczne implikacje** mają jej wyniki dla opieki nad pacjentami?
- Jakie **otwarte pytania** zostają po jej badaniu (potencjalne kierunki dalszych badań)?

### 5. Styl i forma

- Jak pisze - **formalność**, **struktura**, **długość zdań**?
- Jakie **konwencje** stosuje (cytowania, formatowanie)?
- Czy są charakterystyczne **wzorce** w jej pisaniu?

### 6. Sieć współpracy

- Kim są **recenzenci** i jaka jest ich ekspertyza?
- Jakie **instytucje** pojawiają się w kontekście jej pracy?
- To buduje obraz jej **środowiska profesjonalnego**

## Oczekiwany output

Stwórz dokument `profil-domenowy.md` zawierający:

```markdown
# Profil domenowy - dr Dagny Krankowska

## Streszczenie eksperckie
(2-3 akapity: kim jest, co bada, dlaczego to ważne)

## Mapa domeny
(Kluczowe obszary jej ekspertyzy w formie listy/hierarchii)

## Glosariusz
(Tabela: termin | definicja | kontekst użycia)

## Metodologia
(Jak pracuje, jakie podejścia stosuje)

## Pytania badawcze
(Jakie problemy ją interesują)

## Implikacje dla agenta
(Konkretne wnioski: co agent powinien wiedzieć, rozumieć, umieć)
```

## Jak wykorzystamy te informacje

1. **System prompt** - agent będzie wiedział, że pracuje z lekarzem-badaczem HIV/AIDS
2. **Terminologia** - agent nie będzie prosił o wyjaśnienie podstawowych pojęć z jej dziedziny  
3. **Kontekst zadań** - agent zrozumie typowe zadania (przegląd literatury, analiza danych, pisanie publikacji)
4. **Styl komunikacji** - agent dopasuje się do jej sposobu formułowania myśli
5. **Proaktywne wsparcie** - agent będzie mógł przewidywać potrzeby na podstawie znajomości workflow

## Ważne uwagi

- Szukamy **praktycznych informacji** do budowania kontekstu, nie akademickiego streszczenia
- Priorytet: **terminologia** i **sposób myślenia** nad szczegółami wyników badań
- Jeśli rozprawa jest utajona/niedostępna, pracuj ze streszczeniami i recenzjami
- Zaznacz wyraźnie, co jest **faktem** z dokumentów, a co **wnioskiem/interpretacją**
