# Notatka z rozmowy z Claude (2026-01-18)

## Kontekst

Dagny Krankowska — koleżanka, lekarka. Chcę na niej przetestować koncepcję warsztatów z pracy z agentami do kodowania (Claude Code, Cursor) dla pracy innej niż programistyczna.

## Profil Dagny

- **Stanowisko:** Lekarz, asystent w Klinice Chorób Zakaźnych, Tropikalnych i Hepatologii, WUM
- **Stopień:** Doktor nauk medycznych (nadany 06.11.2024)
- **Temat doktoratu:** "Zależność między systematyczną opieką nad osobami z HIV, a występowaniem wybranych chorób oportunistycznych"
- **Obszary badawcze:** HIV, sepsa, neuroinfekcje, choroby tropikalne, epidemiologia chorób zakaźnych
- **Publikacje:** systematic review dot. HPV u kobiet z HIV w Europie ([PubMed](https://pubmed.ncbi.nlm.nih.gov/)), profil na [ResearchGate](https://www.researchgate.net/)

Źródła:
- https://bip.wum.edu.pl/doktorat-lub-habilitacja/dh-lek-dagny-krankowska
- https://ppm.edu.pl/info/author/WUM625d288494594fdf9d9548be57b70724

---

## Jej faktyczny workflow (badanie retrospektywne)

Dagny nie robi systematic review jako główną działalność — robi **retrospektywne badania kliniczne** oparte na danych szpitalnych.

### Pipeline:

```
Hipoteza kliniczna → Literature review (uzasadnienie) → Zbieranie danych z systemu szpitalnego → Statystyka → Paper
```

### Etapy szczegółowo:

#### 1. Hipoteza kliniczna
Przykład: "Pacjenci z HIV i niskim CD4 częściej rozwijają neuroinfekcje oportunistyczne"

Powstaje z obserwacji klinicznych, intuicji, rozmów z kolegami.

#### 2. Literature review (mały, celowany)
- Cel: Sprawdzić co już wiadomo, znaleźć lukę, uzasadnić badanie
- Nie setki paperów — raczej 20-50 kluczowych
- **Artefakt:** Notatki/tabela z kluczowymi findings, draft sekcji Introduction/Background

#### 3. Protokół badania + etyka
- Napisanie protokołu
- Zgoda komisji bioetycznej (na badania retrospektywne zwykle uproszczona)

#### 4. Zbieranie danych (TUTAJ JEST BÓL)
Studenci siedzą przy szpitalnym komputerze i:
- Przeszukują system szpitalny (Clininet, AMMS lub podobny)
- Szukają pacjentów spełniających kryteria
- **Ręcznie przepisują do Excela:** wiek, płeć, daty, wyniki badań, rozpoznania, leki...

**Ograniczenia:**
- Nie można wyeksportować (RODO, regulacje szpitalne)
- Nie można podłączyć zewnętrznych narzędzi
- Dane muszą zostać zanonimizowane

**Artefakt:** Excel z danymi pacjentów (np. 100-500 wierszy, 30-100 kolumn)

#### 5. Analiza statystyczna (OUTSOURCOWANA)
Dagny daje Excel komuś kto umie statystykę. Ta osoba robi:
- Czyszczenie danych
- "Table 1" (charakterystyka demograficzna grupy)
- Testy statystyczne (chi-kwadrat, t-test, regresja logistyczna...)
- Wykresy (Kaplan-Meier, forest plots...)

**Artefakty:** Tabele wyników, p-values, figury

#### 6. Pisanie paperu
Introduction → Methods → Results → Discussion

---

## Potencjał agentów w jej workflow

| Etap | Aktualny stan | Potencjał agenta |
|------|---------------|------------------|
| Literature review | Ręczne szukanie w PubMed | ✅ Wyszukiwanie, ekstrakcja findings, draft tabel |
| Zbieranie danych | Studenci przepisują ręcznie | ❌ Zablokowane (dane zostają w szpitalu) |
| Czyszczenie Excela | Ktoś inny | ✅ Agent może oczyścić, ustandaryzować |
| Statystyka | Outsourcowana | ✅✅✅ **MEGA SZANSA** |
| Table 1 | Ktoś robi ręcznie | ✅ Agent generuje automatycznie |
| Pisanie | Dagny pisze | ✅ Drafty, formatowanie |

---

## Killer use case dla warsztatu

> "Masz Excel z danymi pacjentów. Agent zrobi Ci statystykę."

### Scenariusz:
Dagny daje Excelkę, mówi:
- "Porównaj grupę A vs grupę B"
- "Zrób Table 1 z demografią"
- "Sprawdź czy wiek wpływa na outcome"
- "Zrób Kaplan-Meier dla przeżycia"

### Agent (Claude Code / Cursor):
1. Wczytuje Excel
2. Robi EDA (exploratory data analysis)
3. Generuje Table 1 (n, %, mediana, IQR — tak jak w paperach medycznych)
4. Robi testy statystyczne
5. Generuje wykresy publication-ready
6. Eksportuje do Worda/LaTeXa

### Dlaczego to 10x lepsze niż wysyłanie do statystyka:
- **Natychmiastowe**
- **Iterowalne** ("a teraz dodaj jeszcze tę zmienną")
- **Dagny rozumie co się dzieje** (bo rozmawia z agentem)

---

## Następne kroki (pomysły)

- [ ] Przygotować mock scenariusz warsztatu
- [ ] Stworzyć fikcyjną Excelkę z danymi pacjentów (syntetyczne)
- [ ] Przykładowa sesja z agentem — co Dagny mówi, co agent robi
- [ ] Jakie artefakty powstają (Table 1, wykresy, kod R/Python)

---

## Kontekst: Etapy Systematic Review (dla odniesienia)

W medycynie formal systematic review ma inną strukturę (używa PICO, search strategies dla wielu baz, PRISMA, etc.) — ale to nie jest główny workflow Dagny. Zostawiam tu dla porównania gdyby temat wrócił.
