# Research Checkpoints — Case Study: Epidemiologia Sepsy

Konkretny przykład podziału researchu na checkpointy. Kontekst: Scope Fluidics (biotech venture builder) ocenia opportunity w diagnostyce POC sepsy.

---

## Zadanie końcowe

*"Zbierz dane epidemiologiczne o sepsie potrzebne do oceny opportunity w diagnostyce POC."*

---

## Krok 1: Zdefiniuj pytania badawcze

**Agent:** Zaproponuj listę pytań epidemiologicznych które musimy odpowiedzieć.

**Oczekiwany output:**
```
1. Jaka jest roczna incydencja sepsy? (per region: US, EU, global)
2. Jaka jest śmiertelność (mortality rate)?
3. Jak incydencja rozkłada się po setting? (hospital-acquired vs community-acquired)
4. Które populacje są najbardziej dotknięte? (wiek, comorbidities)
5. Jaki jest trend czasowy? (rośnie/spada)
6. Jakie są koszty hospitalizacji?
```

**Checkpoint:** Czy lista pytań jest kompletna? Czy czegoś brakuje?
- Ty dodajesz/usuwasz pytania
- To zajmuje 2 minuty
- Błąd tu = zły kierunek całego researchu

---

## Krok 2: Zidentyfikuj źródła

**Agent:** Dla każdego pytania — jakie źródła byłyby autorytatywne?

**Oczekiwany output:**
```
| Pytanie | Potencjalne źródła |
|---------|-------------------|
| Incydencja US | CDC, AHRQ HCUP, Sepsis Alliance |
| Incydencja EU | ECDC, Lancet regional studies |
| Mortality | WHO, systematic reviews (JAMA, Lancet) |
| Demographics | Published cohort studies, registries |
```

**Checkpoint:** Czy źródła istnieją i są wiarygodne?
- Agent może halucynować nazwy organizacji/baz
- Weryfikujesz: "czy AHRQ HCUP to realne źródło?" (tak)
- Nie czytasz jeszcze danych, tylko sprawdzasz czy źródła realne

---

## Krok 3: Wyciągnij dane ze źródeł

**Agent:** Dla każdego pytania — znajdź konkretne liczby z konkretnych źródeł.

**Oczekiwany output:**
```
## Incydencja US
- 1.7 miliona przypadków/rok (CDC, 2020)
- 270,000 zgonów/rok (Sepsis Alliance, 2023)

## Incydencja EU
- 3.4 miliona przypadków/rok (Lancet Infectious Diseases, 2020)
- Znaczna zmienność między krajami (2-4x)

[...etc...]
```

**Checkpoint:** Spot-check 2-3 kluczowych liczb
- Wybierasz najważniejsze (np. incydencja US, mortality rate)
- Sprawdzasz czy źródło mówi to co agent twierdzi
- NIE sprawdzasz wszystkiego — tylko high-leverage facts

---

## Krok 4: Reconcile & synthesize

**Agent:** Gdzie źródła się różnią? Jakie są przyczyny różnic? Co rekomendujesz jako "working numbers"?

**Oczekiwany output:**
```
## Rozbieżności
- CDC mówi 1.7M, Sepsis Alliance mówi 1.9M
- Przyczyna: różne definicje sepsy (Sepsis-2 vs Sepsis-3)

## Rekomendowane working numbers dla dalszej analizy
| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| US incidence | 1.7M/yr | CDC | High |
| US mortality | 270K/yr | CDC | High |
| EU incidence | 3.4M/yr | Lancet | Medium |
```

**Checkpoint:** Czy reconciliation ma sens?
- Tu sprawdzasz LOGIKĘ, nie fakty
- Czy wyjaśnienie rozbieżności jest sensowne?
- Czy wybór "working numbers" jest rozsądny?

---

## Krok 5: Format for use case

**Agent:** Przygotuj podsumowanie epidemiologii gotowe do włączenia do większego raportu.

**Output:** Gotowy artifact — 1-2 strony z kluczowymi liczbami, źródłami, caveats.

**Checkpoint:** Light review — czy czytelne, czy nic nie zginęło.

---

## Podsumowanie: 5 kroków, 5 checkpointów

| Krok | Co sprawdzasz | Czas |
|------|---------------|------|
| 1. Pytania | Kompletność listy | 2 min |
| 2. Źródła | Czy istnieją | 3 min |
| 3. Dane | Spot-check 2-3 liczb | 5-10 min |
| 4. Reconcile | Logika, nie fakty | 3 min |
| 5. Format | Czytelność | 1 min |

**Total:** ~15-20 min twojej pracy, zamiast 2h researchu od zera albo 1h sprawdzania wszystkiego.

---

## Meta-obserwacje

### Dlaczego ten podział działa

1. **Wczesne checkpointy są tanie** — 2 min na pytania, 3 min na źródła, ale błąd tu = cały research w złym kierunku

2. **Spot-check zamiast full review** — nie sprawdzasz wszystkich 20 liczb, tylko 2-3 najważniejsze

3. **Różne typy weryfikacji** — fakty vs logika vs kompletność

4. **Każdy krok ma jasny output** — wiesz co dostaniesz, łatwo ocenić

### Failure modes które łapiemy

| Krok | Failure mode |
|------|--------------|
| 1 | Zły framing, pominięte pytania |
| 2 | Halucynowane źródła |
| 3 | Halucynowane liczby |
| 4 | Błędna interpretacja rozbieżności |
| 5 | Zgubione informacje przy formatowaniu |

---

## Related

- [[Strategy - Scope Fluidics]]
- Case study dla [[Context Engineering Skill Development Program]]
