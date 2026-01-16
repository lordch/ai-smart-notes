# Czy praca nadaje się do Manual Context Curation?

Narzędzie diagnostyczne — osie oceny.

---

## Oś 1: Eksternalizowalność wiedzy

**Pytanie:** Czy wiedzę potrzebną do dobrego wykonania da się zapisać?

Praca się nadaje gdy:
- Wzorce "dobrego" outputu da się pokazać na przykładach
- Domain knowledge da się uchwycić w dokumentach
- "Jak to robimy" można opisać proceduralnie

Praca się NIE nadaje gdy:
- Sukces zależy od niewyrażalnej intuicji
- Know-how jest zbyt embodied (chirurgia, rzemiosło)

---

## Oś 2: Intermediate artifacts

**Pytanie:** Czy zadanie naturalnie dzieli się na checkpointy z artefaktami?

Leverage hierarchy: research → plan → execution.
Każdy etap powinien produkować artefakt który ma wartość standalone.

---

## Oś 3: Research vs execution

**Pytanie:** Gdzie jest ciężar pracy — w odkrywaniu co zrobić, czy w samym robieniu?

Im więcej pracy w "co" i "jak podejść" (upstream), tym większa dźwignia z context curation.

Praca czysto wykonawcza (downstream-heavy) → może bardziej skorzystać z prostej automatyzacji.

---

## Oś 4: Powtarzalność z wariacją

**Pytanie:** Czy to są podobne zadania, ale nigdy identyczne?

Sweet spot dla MCC:
- Pełna powtarzalność → zwykła automatyzacja
- Zero powtarzalności → brak możliwości budowania context library
- **Powtarzalność z wariacją** → akumulacja kontekstu działa

---

## Oś 5: Tolerancja na niedeterminizm

**Pytanie:** Czy "wystarczająco dobre" jest akceptowalne?

LLM-y są fallible. Human verification łapie błędy, ale nie eliminuje ich całkowicie.

Praca gdzie pomyłka jest katastrofą (i nie da się złapać w review) może nie pasować.

---

## Analiza przykładowych typów pracy

### Kancelaria prawna — research precedensów

| Oś | Ocena |
|----|-------|
| Eksternalizowalność | ✅ Wysoka — prawo spisane, precedensy to dokumenty |
| Intermediate artifacts | ✅ Naturalne — research → lista → analiza → draft |
| Research vs execution | ✅ Research-heavy — 70% to znajdowanie i rozumienie |
| Powtarzalność z wariacją | ✅ Idealna — każda sprawa inna, wzorce się powtarzają |
| Tolerancja | ⚠️ Średnia — błędy poważne, ale review jest standardem |

**Verdict: Świetny kandydat**

---

### Firma konsultingowa — deliverables

| Oś | Ocena |
|----|-------|
| Eksternalizowalność | ✅ Wysoka — frameworki, metodologie, poprzednie prace |
| Intermediate artifacts | ✅ Idealne — wywiady → synteza → hipotezy → rekomendacje |
| Research vs execution | ✅ Research-dominant — zrozumienie to 80% wartości |
| Powtarzalność z wariacją | ✅ Idealna — każdy klient inny, typy problemów się powtarzają |
| Tolerancja | ✅ Wysoka — rekomendacje to "best judgment" |

**Verdict: Idealny kandydat**

---

### Agencja marketingowa — content

| Oś | Ocena |
|----|-------|
| Eksternalizowalność | ✅ Wysoka — brand voice, persony, przykłady |
| Intermediate artifacts | ✅ Naturalne — brief → research → koncepty → draft |
| Research vs execution | ⚠️ Zależy — strategia ✅, produkcja postów ⚠️ |
| Powtarzalność z wariacją | ✅ Wysoka — te same formaty, różne tematy |
| Tolerancja | ✅ Wysoka — iteracje są normą |

**Verdict: Bardzo dobry**, szczególnie strategia i większe formy

---

### Księgowość — processing dokumentów

| Oś | Ocena |
|----|-------|
| Eksternalizowalność | ✅ Wysoka — zasady explicite |
| Intermediate artifacts | ⚠️ Słabe — dokument → zaksięgowanie, mało środka |
| Research vs execution | ❌ Execution-heavy — 90% to wprowadzanie według reguł |
| Powtarzalność z wariacją | ⚠️ Zbyt powtarzalna — faktura to faktura |
| Tolerancja | ❌ Niska — błąd ma konsekwencje prawne |

**Verdict: Słaby kandydat** — lepiej tradycyjna automatyzacja (OCR + rules)

Wyjątek: doradztwo podatkowe (interpretacje, optymalizacje) → to już research-heavy

---

### Software development

| Oś | Ocena |
|----|-------|
| Eksternalizowalność | ✅ Wysoka — kod to tekst, architektura da się opisać |
| Intermediate artifacts | ✅ Naturalne — requirements → design → plan → code → tests |
| Research vs execution | ⚠️ Zależy — nowa funkcjonalność ✅, bug fix ⚠️ |
| Powtarzalność z wariacją | ✅ Wysoka — wzorce architektoniczne się powtarzają |
| Tolerancja | ⚠️ Średnia — kod musi działać, ale testy łapią błędy |

**Verdict: Dobry kandydat**, najlepiej na feature development

---

## Pattern

**Idealny kandydat:**
- Consulting, prawo, strategia marketingowa
- Prace gdzie "zrozumienie problemu" dominuje nad "wykonaniem rozwiązania"

**Słaby kandydat:**
- Wysoko-wolumenowe, execution-heavy, niska tolerancja na błędy
- Klasyczna automatyzacja lepiej pasuje

**Szara strefa:**
- Software development, L2+ support
- Działa, ale wymaga świadomego projektowania checkpointów
