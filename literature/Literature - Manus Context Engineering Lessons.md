# Literature - Manus: Context Engineering for AI Agents

**Zrodlo:** https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
**Data przeczytania:** 2026-01-26

---

## 1. O Manus - co to za produkt

Manus to platforma AI agentowa, ktora dziala poprzez **in-context learning** zamiast fine-tuningu modeli. Kluczowe cechy:

- Swiadomy wybor architektury: in-context learning pozwala na szybkie iteracje (shipping w godzinach zamiast tygodni)
- Niezaleznosc od ulepszen modeli bazowych - "jesli postep modeli to przypływ, chcemy byc łodka, nie słupem wbitym w dno"
- Typowe zadanie w Manus wymaga ok. 50 wywolan narzedzi
- Stosunek tokenow input:output wynosi ok. 100:1 (dlugi kontekst, krotkie outputy)
- Manus został przejęty przez Meta

**Filozofia:** Zamiast trenowac wlasne modele, zespol postawil na **context engineering** - celowe kształtowanie sposobu prezentacji informacji frontierowym LLM-om.

---

## 2. Pieć kluczowych zasad/lekcji

### Zasada 1: Projektuj wokol KV-Cache Hit Rate

Najwazniejsza metryka optymalizacji dla produkcyjnych agentow. Wplywa zarowno na latency jak i koszty.

> "Cached tokens kosztuja ok. 1/10 ceny uncached tokens w frontier modelach"

### Zasada 2: Maskuj zamiast usuwac narzedzia

Dynamiczne dodawanie narzedzi w trakcie iteracji:
- Invaliduje KV-cache
- Dezorientuje model gdy poprzednie obserwacje odwoluja sie do niezdefiniowanych narzedzi

Rozwiazanie: state machines z logit masking.

### Zasada 3: System plikow jako pamiec

Nowoczesne LLM-y maja duze okna kontekstu (128K+), ale to stwarza problemy:
- Obserwacje moga byc ogromne
- Wydajnosc spada z dlugoscia
- Dlugie inputy sa kosztowne mimo cachowania

> "Compression strategies are always designed to be restorable"

### Zasada 4: Manipuluj uwaga poprzez recytacje

Automatyczne tworzenie i aktualizowanie todo.md podczas wykonywania zadan. To nie kosmetyka - to **celowy mechanizm manipulacji uwaga**.

### Zasada 5: Zachowuj dowody bledow

Kontr-intuicyjne: ukrywanie bledow agenta **pogarsza** wydajnosc. Model musi widziec nieudane akcje i stacktrace'y.

> "Error recovery is one of the clearest indicators of true agentic behavior"

### Zasada 6: Zapobiegaj few-shot brittleness

Powtarzalne wzorce kontekstu powoduja, ze agenty naśladuja waskie zachowania. Przy przegladaniu 20 CV agenty wpadaly w rytm, powtarzajac akcje tylko dlatego, ze kontekst zawieral podobne przyklady.

---

## 3. Praktyczne techniki

### KV-Cache Optimization

| Technika | Dlaczego |
|----------|----------|
| Stabilne system prompty | Nawet jednoTokenowa roznica invaliduje cache |
| Unikaj timestampow w promptach | Niszcza efektywnosc cache |
| Append-only context structure | Zachowuje prefiks |
| Deterministyczna serializacja JSON | Zachowuje spojnosc cache |
| Prefix caching (vLLM) | Framework-level support |
| Routing po session ID | Konsystencja w rozproszonych workerach |

### File System as Memory

- Model uczy sie czytac i pisac pliki on demand
- Strategie kompresji zawsze "restorable" - URL-e pozostaja dostepne nawet gdy content strony jest usuniety
- Sciezki plikow zachowuja dostep do dokumentow gdy ich zawartosc jest tymczasowo usunieta

**Ciekawa obserwacja:** State Space Models (SSM), ktore naturalnie maja problem z long-range dependencies, moga doskonale sprawdzic sie jako agentic systems jesli opanuja file-based memory zamiast context-based storage.

### Recitation (todo.md)

- Automatyczne tworzenie i aktualizowanie todo.md podczas wykonywania zadan
- Przez ciagłe przepisywanie celow na koncu kontekstu, system pcha cele w recent attention span modelu
- Zapobiega "lost-in-the-middle" phenomenon ktore powoduje goal drift

### Tool Management

Trzy tryby function-calling:
1. **Auto** - model wybiera czy wywolac funkcje
2. **Required** - model musi wywolac funkcje
3. **Specified** - model wybiera z predefiniowanego podzbioru

**Tip:** Nazywaj narzedzia z konsystentymi prefiksami (browser_, shell_) - umozliwia wymuszanie constraintow bez stateful processors.

### Controlled Variation

Wprowadzaj strukturalna wariancie:
- Rozne szablony serializacji
- Alternatywne sformułowania
- Drobne zmiany formatowania

> "Controlled randomness helps break the pattern"

---

## 4. Bledy ktore popelnili i czego sie nauczyli

### Blad 1: Fine-tuning zamiast in-context learning (poprzedni startup)

Poprzednie proby trenowania modeli dla open information extraction staly sie przestarzale gdy GPT-3 i Flan-T5 pokazaly mozliwosci in-context learning.

**Lekcja:** Wolne feedback loops sa katastrofalne dla pre-PMF startupow.

### Blad 2: Dynamiczne dodawanie/usuwanie narzedzi

Powodowalo invalidacje cache i dezorientacje modelu.

**Lekcja:** Maskuj zamiast usuwac.

### Blad 3: Ukrywanie bledow agenta

Intuicyjnie wydaje sie, ze czysty kontekst jest lepszy.

**Lekcja:** Model musi widziec bledy zeby sie z nich uczyc w-context.

### Blad 4: Powtarzalnosc w kontekscie

Przy powtarzalnych zadaniach (np. review 20 CV) agent wpadal w rytm i powtarzal te same akcje.

**Lekcja:** Wprowadz controlled randomness w formatowaniu.

### Proces iteracji

Zespol przebudowal framework agentowy **4 razy**. Nazywaja swoj proces "Stochastic Gradient Descent" - manualne architecture searching przez empiryczny guesswork. Testowali zasady na milionach real-world user interactions.

---

## 5. Relevance dla praktycznego budowania agentow

### Dla mojej praktyki Human-Agent Collaboration:

1. **KV-cache jako metryka** - wazne dla produkcyjnych deploymentow, mniej dla eksploracyjnych sesji. Ale zasada "append-only context" jest uniwersalna.

2. **File system as memory** - bezposrednio wspiera moja koncepcje "externalized context". Agent ktory pisze i czyta pliki to agent ktory buduje knowledge base.

3. **Recitation/todo.md** - doskonale wpisuje sie w moj framework. To nie tylko organization ale active attention management. Moze byc templatem dla moich taskow.

4. **Error preservation** - wazne dla designu promptow. Nie czysc kontekstu z bledow.

5. **Controlled variation** - przy repetytywnych zadaniach wprowadzaj wariancie zeby uniknac overfittingu do wzorcow.

### Praktyczne wnioski:

| Insight | Zastosowanie |
|---------|--------------|
| In-context > fine-tuning | Dla szybkich iteracji, in-context learning pozwala shipowac szybciej |
| Cache-aware prompting | Stabilne system prompty, unikaj timestampow |
| Files as external memory | Traktuj file system jako rozszerzenie context window |
| Active attention management | Powtarzaj cele na koncu kontekstu |
| Learn from failures | Zachowuj bledy w kontekscie |

### Cytaty do zapamietania:

> "If model progress is the rising tide, we want Manus to be the boat, not the pillar stuck to the seabed."

> "Compression strategies are always designed to be restorable."

> "Error recovery is one of the clearest indicators of true agentic behavior."

---

## Powiazania

- [[Human-Agent Collaboration Framework]] - file system as memory wspiera externalized context
- [[Context Engineering]] - artykul definiuje context engineering jako "deliberate shaping of information presentation"
