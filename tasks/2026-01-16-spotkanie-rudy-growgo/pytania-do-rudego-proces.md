# Pytania do Rudy'ego o proces dywersyfikacji

*Kontekst: Rudy przysłał opis procesu "do przeprowadzenia z wykorzystaniem AI". Chcę zrozumieć jak wyobraża sobie realizację.*

---

## Poziom 0: Podstawowy model — kto, co, jak

*Zanim wejdziemy w szczegóły, chcę upewnić się że dobrze rozumiem ogólną wizję.*

### Kto jest operatorem?

1. **Kto fizycznie "klika" w AI podczas tego procesu?** 
   - Ty jako konsultant?
   - Ktoś z firmy klienta?
   - Wspólnie na warsztatach?

2. **Jeśli klient — to kto konkretnie?** Prezes? Dyrektor strategii? Analityk? Czy ta osoba umie pracować z AI?

3. **Jaka jest twoja rola w tym procesie?** Facylitator warsztatów? Operator Gemów? Recenzent outputów? Wszystko po trochu?

### Poziom automatyzacji vs ludzkiej pracy

4. **Czy oczekujesz, że AI "wykona" te kroki, czy że "wesprze" człowieka który je wykonuje?**
   - Wariant A: Wrzucam dane → AI daje gotowy output → idę dalej
   - Wariant B: Wrzucam dane → AI daje draft → człowiek iteruje, poprawia, dopytuje → dopiero potem idziemy dalej

5. **Jak wyobrażasz sobie np. Krok 1 (Ewaluacja Zasobów) w praktyce?**
   - Czy Gem dostaje dokumentację firmy i "sam" robi analizę VRIO?
   - Czy raczej człowiek robi warsztat, a Gem pomaga uporządkować wnioski?

6. **Czy ten proces da się zrobić "asynchronicznie"** (klient sam klika przez tydzień), **czy wymaga synchronicznych sesji** (warsztaty z tobą)?

### Checkpointy i iteracje

7. **Gdzie są momenty "zatrzymania i weryfikacji"?** Czy po każdym kroku ktoś sprawdza output, czy lecicie "na automacie" przez cały proces?

8. **Co się dzieje gdy output jest słaby?** Np. analiza VRIO jest płytka. Poprawiasz prompt? Dodajesz kontekst? Edytujesz ręcznie?

9. **Czy przewidujesz iteracje wewnątrz kroków** (kilka rund z Gemem zanim output jest OK), **czy jeden strzał i idziemy dalej?**

### Realność vs wizja

10. **Czy już przeprowadziłeś taki proces (lub podobny) z klientem używając AI?** Jak wyglądało w praktyce?

11. **Jeśli nie — co cię powstrzymuje?** Brak narzędzi? Brak klienta który chce? Brak pewności że zadziała?

12. **Gdybyś miał to robić za miesiąc — co byś potrzebował mieć przygotowane?**

---

## Poziom 1: Głębsza eksploracja (jeśli podstawy będą jasne)

*Te pytania warto zadać gdy zrozumiemy podstawowy model.*

### Przepływ i pamięć

- Jak kontekst przechodzi między krokami? Kopiujesz output z jednego Gema do drugiego?
- Gdzie fizycznie żyją deliverables (Raport, Teczki Projektowe)? Google Docs?
- Co gdy Zarząd każe wrócić do wcześniejszego kroku? Gem "pamięta" poprzednie analizy?

### Jakość i kontekst branżowy

- Skąd Gem wie co jest "rzadkie" w branży klienta? Kto dostarcza ten kontekst?
- Jak weryfikujesz jakość outputu? Czy klient potrafi ocenić czy analiza Portera jest dobra?

### Architektura

- Ile Gemów przewidujesz? Jeden per krok? Per technikę (VRIO, Porter, TAM/SAM/SOM)?
- Czy rozważałeś model z jednym "agentem-orkiestratorem" który prowadzi cały proces?

### Hipoteza do zweryfikowania

**Czy problem który rozwiązujesz to "przyspieszenie pracy konsultanta" czy "umożliwienie klientowi samodzielnej pracy"?** 

To są fundamentalnie różne produkty:
- Jeśli **przyspieszenie konsultanta** → Gems jako twoje narzędzia, ty integrujesz
- Jeśli **samodzielność klienta** → potrzebna jest "pamięć" między krokami, inaczej klient się zgubi

---

## Pytanie otwierające ideację

**Gdybyś miał nieograniczone możliwości techniczne — jak wyobrażasz sobie idealne narzędzie do tego procesu?**
