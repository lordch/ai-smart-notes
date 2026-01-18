# Artefakty z sesji agentowej (analiza danych klinicznych)

Opis konkretnych outputów które powstają gdy lekarz-badacz pracuje z agentem (Claude Code / Cursor) nad analizą danych pacjentów z Excela.

---

## 1. Table 1 — Charakterystyka demograficzna

Standardowy format w publikacjach medycznych. Agent generuje automatycznie.

**Struktura:**

| Zmienna | Grupa A (n=X) | Grupa B (n=Y) | p-value |
|---------|---------------|---------------|---------|
| Wiek, mediana (IQR) | 45 (38-52) | 48 (41-55) | 0.12 |
| Płeć męska, n (%) | 67 (54%) | 72 (58%) | 0.34 |
| CD4 < 200, n (%) | 23 (18%) | 45 (36%) | 0.002 |
| ... | ... | ... | ... |

**Wymogi:**
- Zmienne ciągłe: mediana + IQR (lub średnia ± SD)
- Zmienne kategoryczne: n (%)
- p-value z odpowiedniego testu (Mann-Whitney, chi-kwadrat, Fisher)
- Formatowanie zgodne z czasopismem docelowym

---

## 2. Wykresy publication-ready

### Kaplan-Meier (krzywe przeżycia)
- Porównanie grup (np. HIV+ vs HIV-)
- Log-rank test p-value
- Censoring marks
- Number at risk table pod wykresem

### Forest plot
- Dla meta-analiz lub subgroup analysis
- Odds ratio / hazard ratio z 95% CI
- Wagi badań

### Boxplot / Violin plot
- Porównanie rozkładów między grupami
- Zaznaczone outliers

### Bar chart z error bars
- Proporcje między grupami
- 95% CI

**Format eksportu:** PNG/PDF 300 DPI, wymiary zgodne z journal guidelines

---

## 3. Tabele wyników testów statystycznych

### Regresja logistyczna (univariate + multivariate)

| Zmienna | Crude OR (95% CI) | p | Adjusted OR (95% CI) | p |
|---------|-------------------|---|----------------------|---|
| Wiek (per 10 lat) | 1.23 (1.05-1.44) | 0.01 | 1.18 (0.98-1.42) | 0.08 |
| Płeć męska | 1.45 (0.89-2.36) | 0.13 | 1.52 (0.91-2.54) | 0.11 |
| CD4 < 200 | 2.87 (1.67-4.93) | <0.001 | 2.54 (1.43-4.51) | 0.001 |

### Cox proportional hazards

| Zmienna | HR (95% CI) | p |
|---------|-------------|---|
| ... | ... | ... |

---

## 4. Kod R/Python (reprodukowalny)

Agent generuje czysty, komentowany kod który można:
- Uruchomić ponownie z nowymi danymi
- Zmodyfikować parametry
- Dołączyć do supplementary materials

**Przykład struktury:**

```python
# 1. Wczytanie danych
df = pd.read_excel("dane_pacjentow.xlsx")

# 2. Czyszczenie
df = clean_data(df)

# 3. Table 1
table1 = generate_table1(df, groupby="grupa", 
                          continuous=["wiek", "cd4"],
                          categorical=["plec", "hiv_status"])

# 4. Analiza
model = logistic_regression(df, outcome="outcome", 
                            predictors=["wiek", "plec", "cd4"])

# 5. Wykresy
plot_kaplan_meier(df, time="czas_obs", event="zgon", group="grupa")

# 6. Eksport
export_to_word(table1, "table1.docx")
```

---

## 5. Eksporty do Worda/LaTeXa

Agent formatuje tabele i wykresy gotowe do wklejenia:

- **Word (.docx)** — dla współautorów, do komentowania
- **LaTeX (.tex)** — dla journali wymagających tego formatu
- **CSV** — surowe wyniki do archiwum

---

## 6. Raport EDA (Exploratory Data Analysis)

Przed właściwą analizą — przegląd danych:

- Ile rekordów, ile zmiennych
- Missing values (które zmienne, ile %)
- Rozkłady zmiennych (histogramy, summary stats)
- Korelacje między zmiennymi
- Potencjalne outliers
- Red flags (niespójności w danych)

---

## Workflow sesji

```
1. Dagny: "Wczytaj dane z pliku pacjenci_hiv.xlsx"
   → Agent: wczytuje, pokazuje preview, raportuje strukturę

2. Dagny: "Zrób Table 1, porównaj grupę z CD4<200 vs CD4>=200"
   → Agent: generuje tabelę, dobiera testy, formatuje

3. Dagny: "Sprawdź czy CD4 wpływa na ryzyko neuroinfekcji"
   → Agent: regresja logistyczna, OR z CI, p-value

4. Dagny: "Zrób Kaplan-Meier dla czasu do neuroinfekcji"
   → Agent: wykres, log-rank test, export PNG

5. Dagny: "Eksportuj wszystko do Worda"
   → Agent: pakuje tabele + wykresy do .docx
```

---

## Wartość dla Dagny

| Bez agenta | Z agentem |
|------------|-----------|
| Wysyła Excel do statystyka | Sama robi analizę |
| Czeka dni/tygodnie | Natychmiast |
| Iteracja = kolejne dni | "Dodaj jeszcze tę zmienną" → 30 sekund |
| Nie rozumie kodu | Rozmawia, rozumie, uczy się |
| Zależność od innych | Autonomia |
