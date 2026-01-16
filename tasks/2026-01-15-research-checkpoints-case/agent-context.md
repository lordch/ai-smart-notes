# Kontekst dla agenta: Epidemiologia Sepsy

Przykład context file który ładujemy agentowi przed rozpoczęciem researchu.

---

## Cel projektu

Scope Fluidics (biotech venture builder) ocenia opportunity w **point-of-care diagnostyce sepsy**. Potrzebujemy danych epidemiologicznych jako input do dalszej analizy (segmentacja rynku, sizing).

## Twoje zadanie

Zbierz dane epidemiologiczne o sepsie. Output posłuży do oceny wielkości rynku i identyfikacji najbardziej obiecujących segmentów.

## Pytania do odpowiedzenia

1. Jaka jest roczna incydencja sepsy? (US, EU, global osobno)
2. Jaka jest śmiertelność (mortality rate)?
3. Jak incydencja rozkłada się po setting? (hospital-acquired vs community-acquired)
4. Które populacje są najbardziej dotknięte? (wiek, comorbidities)
5. Jaki jest trend czasowy? (rośnie/spada/stabilny)
6. Jakie są koszty hospitalizacji per case?

## Wymagania dotyczące źródeł

**Akceptowalne źródła:**
- Agencje rządowe (CDC, ECDC, WHO)
- Peer-reviewed journals (preferowane: Lancet, JAMA, NEJM, Critical Care Medicine)
- Rejestry kliniczne i bazy danych (HCUP, MIMIC)
- Raporty organizacji branżowych (Sepsis Alliance) — jako secondary source

**NIE akceptowalne:**
- Artykuły prasowe bez primary source
- Strony firm diagnostycznych (conflict of interest)
- Wikipedia (ok jako starting point, ale nie jako źródło)
- Dane starsze niż 2018 (chyba że brak nowszych)

## Format outputu

Dla każdej liczby podaj:
```
[FAKT]: konkretna liczba
[ŹRÓDŁO]: autor/organizacja, tytuł, rok
[CONFIDENCE]: High/Medium/Low
[CAVEAT]: jeśli są istotne ograniczenia (np. tylko US, specyficzna populacja)
```

**Przykład:**
```
[FAKT]: 1.7 miliona przypadków sepsy rocznie w US
[ŹRÓDŁO]: CDC, "Sepsis Data & Reports", 2023
[CONFIDENCE]: High
[CAVEAT]: Definicja wg Sepsis-3 criteria
```

## Czego NIE robić

- NIE zgaduj liczb jeśli nie masz źródła — napisz "nie znalazłem wiarygodnego źródła"
- NIE uśredniaj różnych źródeł bez wyjaśnienia — jeśli CDC mówi 1.7M a WHO mówi 2.1M, podaj oba i wyjaśnij różnicę
- NIE pomijaj confidence/caveats — to krytyczne dla dalszej analizy
- NIE dawaj jednego globalnego numeru jeśli masz breakdown per region

## Rozbieżności między źródłami

Jeśli źródła się różnią:
1. Podaj OBA numery z źródłami
2. Wyjaśnij prawdopodobną przyczynę różnicy (definicja, populacja, rok, metodologia)
3. Zarekomenuj "working number" z uzasadnieniem

## Output structure

```
# Epidemiologia Sepsy — Research Output

## 1. Incydencja
### US
[fakty + źródła]

### EU
[fakty + źródła]

### Global
[fakty + źródła]

## 2. Mortality
[...]

## 3. Setting breakdown
[...]

## 4. Demographics
[...]

## 5. Trends
[...]

## 6. Costs
[...]

## 7. Reconciliation & Working Numbers
[tabela z rekomendowanymi liczbami]

## 8. Gaps & Limitations
[czego nie udało się znaleźć, gdzie confidence jest niskie]
```

---

## Meta: Dlaczego ten kontekst

| Element | Po co |
|---------|-------|
| Cel projektu | Agent rozumie downstream use — wie co jest ważne |
| Lista pytań | Zapobiega pominięciom i scope creep |
| Wymagania źródeł | Redukuje halucynacje, wymusza quality |
| Format outputu | Łatwa weryfikacja, explicite confidence |
| Czego NIE robić | Adresuje znane failure modes |
| Output structure | Przewidywalny format, łatwy review |
