# Praca z Agentami AI: Pełna Narracja v2

---

## Część I: Fundamentalny Insight

### Modele są zdolne

Współczesne modele rozumujące (Claude, GPT-4, Gemini) są zdolne do wykonywania bardzo złożonych zadań. Potrafią analizować, syntetyzować, porównywać, pisać kod, stosować metodologie, tworzyć dokumenty.

To nie jest kwestia możliwości. To kwestia **warunków**.

### Warunek: Odpowiedni kontekst

Model wykonuje zadanie dobrze **jeśli** dostanie odpowiedni kontekst:
- Wie na czym pracuje (źródła, dane)
- Wie co ma zrobić (zadanie, wymagania)
- Wie jak ma to zrobić (metodologia, przykłady)
- Rozumie intencję (cel, constraints)

### Problem: Jak dostarczyć idealny kontekst?

Tu zaczyna się prawdziwa praca.

Dostarczenie "idealnego kontekstu" to nie jest trywialne zadanie. To jest **cały problem** pracy z agentami AI.

Reszta tego dokumentu to rozwinięcie tego problemu i propozycje rozwiązań.

---

## Część II: Spectrum Podejść

### Dwa bieguny

```
CHAT MODE ←――――――――――――――――→ AUTONOMICZNY AGENT
(człowiek w pętli)            (człowiek poza pętlą)
```

**Chat mode (lewy biegun):**
- Człowiek pisze prompt → model odpowiada → człowiek poprawia → model poprawia
- Ciągła interakcja, ciągła kontrola
- Editing loop: poprawiasz output

**Autonomiczny agent (prawy biegun):**
- Człowiek daje zadanie → agent wykonuje samodzielnie → człowiek dostaje rezultat
- Minimalna interakcja, maksymalna autonomia
- Brak kontroli w trakcie wykonania

### Problemy z chatem

| Problem | Opis |
|---------|------|
| **Context rot** | Historia błędów, wahań, ślepych uliczek zaśmieca kontekst |
| **Drift** | Im dłuższa rozmowa, tym bardziej agent "zapomina" początek |
| **Brak kumulacji** | Zamykasz okno, wiedza znika. Każda sesja od zera |
| **Editing loop** | Ciągłe poprawianie = wysoki cognitive load |
| **Brak artefaktów** | Output ginie w historii chatu |

### Problemy z pełną autonomią

| Problem | Opis |
|---------|------|
| **Brak kontroli** | Nie widzisz co agent robi, nie możesz interweniować |
| **Brak alignment** | Agent może źle zrozumieć intencję i pójść w złą stronę |
| **Agent jest eager** | Nie pyta - zakłada. Wypełnia luki swoimi założeniami |
| **Trudna weryfikacja** | Duży output na raz, nie wiadomo co sprawdzić |
| **Ryzyko** | Błąd na początku propaguje się przez całe wykonanie |

### Nasze podejście: Środek

```
CHAT MODE ←――――[TUTAJ]――――――→ AUTONOMICZNY AGENT
              steering + artefakty + checkpointing
```

**Steering loop zamiast editing loop:**
- Definiujesz zadanie precyzyjnie → agent wykonuje → weryfikujesz rezultat
- Kontrola na początku (steering) zamiast na końcu (editing)
- Interwencja gdy potrzebna, nie ciągła

**Artefakty zamiast strumienia:**
- Output zapisany w plikach, nie w historii chatu
- Persystuje, kumuluje się, można weryfikować

**Checkpointing:**
- Regularny zapis stanu
- Reset kontekstu bez utraty pracy
- Weryfikacja przyrostowa

---

## Część III: Cztery Problemy Kontekstu

### Meta-framing

Wszystkie problemy z AI przy złożonych zadaniach to są **problemy z kontekstem**. Ale kontekst ma różne wymiary.

| Problem | Typ kontekstu | Co brakuje/szwankuje |
|---------|---------------|----------------------|
| **Halucynacje** | Kontekst faktyczny | Brak źródeł → agent wymyśla |
| **Slop** | Kontekst intencji | Brak precyzji → agent robi "jakkolwiek" |
| **Drift** | Kontekst alignment | Degradacja w czasie → agent odpływa |
| **Ograniczenia** | Kontekst fizyczny | Za dużo → nie mieści się w window |

---

### Problem 1: Halucynacje (brak kontekstu faktycznego)

**Co to jest:**
Agent generuje informacje które brzmią wiarygodnie, ale nie są prawdziwe. Wymyśla źródła, fakty, cytaty.

**Dlaczego się pojawia:**
Agent jest używany jako **źródło wiedzy** zamiast jako **procesor wiedzy**. Pytasz "co wiesz o X" zamiast "przeanalizuj te materiały o X".

**Mechanizm:**
Kiedy agent nie ma źródeł, wypełnia lukę generowanym tekstem. To jest jego natura - generuje prawdopodobny ciąg dalszy. Jeśli nie dasz mu faktów, wygeneruje coś co *brzmi* jak fakty.

**Rozwiązania:**

1. **Agent na źródłach, nie jako źródło**
   - Dostarczasz materiały (pliki, dane, dokumenty)
   - Agent przetwarza, nie wymyśla
   - "Przeanalizuj to" zamiast "co wiesz o tym"

2. **Infrastruktura przejrzystości**
   - System plikowy: widzisz te same pliki co agent
   - Możesz zweryfikować na jakiej podstawie coś twierdzi
   - Epistemic transparency: żadnego black box

3. **Źródła inline**
   - Agent podaje skąd wie
   - Cytaty, referencje do konkretnych fragmentów
   - Weryfikacja staje się możliwa

4. **Separation of concerns**
   - Agent gromadzi źródła (research)
   - Potem checkpoint
   - Agent przetwarza źródła (analiza)
   - Research i analiza to osobne fazy

---

### Problem 2: Slop (brak kontekstu intencji)

**Co to jest:**
Output który wygląda profesjonalnie, ale nie spełnia rzeczywistych wymagań. "Passable-looking output" który przechodzi bo nikt nie ma czasu sprawdzić.

**Dlaczego się pojawia:**
Agent nie wie czego naprawdę chcesz. Nie zna twoich wymagań jakościowych, stylu, standardów. Robi "jakkolwiek" bo nie powiedziałeś jak.

**Mechanizm:**
Agent optymalizuje pod "wygląda dobrze" bo nie ma innych kryteriów. Generuje coś co statystycznie pasuje do wzorca "profesjonalny dokument" - ale to nie znaczy że pasuje do TWOICH potrzeb.

**Dlaczego TY wypuszczasz slop:**
- Sprawdzenie wielkiego outputu jest żmudne
- Lenistwo + presja czasu
- "Wygląda profesjonalnie, pewnie jest OK"

**Rozwiązania:**

1. **Precyzyjne wymagania upfront (WIRE)**
   - **W**hat: Co konkretnie ma powstać (format, struktura, długość)
   - **I**nput: Z czego (jakie źródła, dane)
   - **R**ules: Jakie zasady (styl, constraints, must-have)
   - **E**xamples: Jak ma wyglądać (reference, anti-examples)

2. **Steering przed wykonaniem**
   - Definiujesz jakość na początku, nie poprawiasz na końcu
   - Agent wie czego oczekujesz zanim zacznie

3. **Checkpointing dla weryfikacji przyrostowej**
   - Mniejsze kawałki = łatwiej sprawdzić
   - Łapiesz błędy wcześniej
   - Nie marnujesz pracy

4. **Visible planning**
   - Agent pokazuje plan przed wykonaniem
   - Możesz redirect zanim zainwestuje czas
   - Weryfikujesz podejście, nie tylko rezultat

5. **Inverse supervision**
   - Projektujesz system pod łatwość weryfikacji
   - Bottleneck to TWOJA zdolność sprawdzenia
   - Małe kroki, źródła inline, jasna struktura

---

### Problem 3: Drift (degradacja kontekstu alignment)

**Co to jest:**
Agent stopniowo "odpływa" od twojej intencji. Na początku rozumiecie się, pod koniec robi coś innego niż chciałeś.

**Dlaczego się pojawia:**
- W długim chacie wcześniejsze instrukcje tracą wagę
- Agent zapomina ustalenia z początku
- Twoja intencja ewoluuje ale agent tego nie widzi
- Agent zakłada (jest eager) zamiast pytać

**Trzy wymiary drift:**

1. **Drift techniczny (context window)**
   - Im dłuższy kontekst, tym mniejsza waga wcześniejszych fragmentów
   - Instrukcje z początku "toną" w szumie

2. **Drift alignment (rozumienie)**
   - Agent zrozumiał inaczej niż myślałeś
   - Założył coś czego nie powiedziałeś
   - Poszedł w kierunku który mu się wydawał sensowny

3. **Drift intencji (twoja ewolucja)**
   - Ty sam nie wiedziałeś czego chcesz na początku
   - Intencja krystalizuje się w trakcie
   - Agent pracuje na starej wersji intencji

**Rozwiązania:**

1. **Alignment przed zadaniem**
   - Agent formułuje założenia swoimi słowami
   - Ty weryfikujesz że rozumiecie się tak samo
   - Dopiero potem plan i wykonanie

2. **Wydobycie założeń (agent jest eager)**
   - Agent nie pyta - zakłada
   - Musisz aktywnie wydobyć co założył
   - "Powiedz jak rozumiesz to zadanie" przed "Zrób to zadanie"

3. **Checkpointing jako reset**
   - Checkpoint = nowy początek z czystym kontekstem
   - Agent czyta artefakt, nie historię chatu
   - Drift się resetuje

4. **Steering w trakcie (course correction)**
   - Możliwość interwencji gdy widzisz że odpływa
   - Redirect bez przerywania całego zadania
   - Korekta kierunku, nie poprawianie outputu

5. **Plan jako artefakt pośredni**
   - Plan jest checkpoint przed wykonaniem
   - Weryfikujesz podejście
   - Łapiesz drift zanim agent zainwestuje czas

---

### Problem 4: Ograniczenia kontekstu (fizyczny limit)

**Co to jest:**
Context window ma limit. Nie możesz załadować wszystkiego. Im więcej ładujesz, tym większy szum i koszt.

**Dlaczego się pojawia:**
Żeby rozwiązać problemy 1-3 (halucynacje, slop, drift), dostarczasz więcej kontekstu:
- Więcej źródeł (przeciw halucynacjom)
- Więcej wymagań i przykładów (przeciw slop)
- Więcej wyjaśnień i alignmentu (przeciw drift)

**Problem emergentny:**
> Rozwiązując problemy 1-3, pogłębiasz problem 4. Kontekst puchnie.

**Rozwiązania:**

1. **Checkpointing (context offloading)**
   - Zapisujesz stan do pliku
   - Nowa sesja czyta plik, nie całą historię
   - Kontekst się "resetuje" bez utraty pracy

2. **Dekompozycja zadań**
   - Duże zadanie → mniejsze podzadania
   - Każde podzadanie ma swój kontekst
   - Checkpoint między podzadaniami

3. **Progressive disclosure**
   - Nie ładujesz wszystkiego na raz
   - Agent najpierw ocenia źródło (tytuł, abstrakt)
   - Dopiero potem ładuje pełną treść jeśli relevant
   - Filtracja przed załadowaniem

4. **Context isolation**
   - Różne wątki w osobnych sesjach
   - Każda sesja ma czysty, dedykowany kontekst
   - Brak zanieczyszczenia między wątkami

5. **Selektywna edycja**
   - Edit konkretnego fragmentu, nie rewrite całości
   - Mniejszy kontekst potrzebny do zmiany
   - Precyzja zamiast regeneracji

---

### Podsumowanie: Mapa Problemów i Rozwiązań

```
                    PROBLEMY KONTEKSTU
                           │
       ┌───────────┬───────┴───────┬───────────┐
       ▼           ▼               ▼           ▼
   HALUCYNACJE    SLOP          DRIFT     OGRANICZENIA
   (faktyczny)  (intencji)   (alignment)   (fizyczny)
       │           │               │           │
       ▼           ▼               ▼           ▼
   • źródła     • WIRE          • alignment  • checkpoint
   • transparen • steering      • założenia  • dekompozycja
   • inline     • checkpoint    • checkpoint • progressive
   • separation • planning      • steering   • isolation
```

**Zauważ:** Checkpointing pojawia się wszędzie. To jest meta-rozwiązanie.

---

## Część IV: Mechanizmy Rozwiązań

### Katalog mechanizmów

Rozwiązania z poprzedniej części można skatalogować jako **mechanizmy** - powtarzalne wzorce które adresują problemy.

---

#### Mechanizm 1: Transparentność (Epistemic Transparency)

**Co to jest:**
Widzisz dokładnie to samo co agent. Żadnego black box.

**Jak działa:**
- System plikowy jako interfejs
- Źródła w plikach, nie w "pamięci" agenta
- Możesz otworzyć każdy plik który agent czyta

**Jakie problemy rozwiązuje:**
- Halucynacje (weryfikacja źródeł)
- Slop (weryfikacja czy użył właściwych materiałów)
- Drift (widzisz na czym agent pracuje)

**Praktycznie:**
- Workspace z plikami zamiast chatu z RAG
- Agent cytuje konkretne fragmenty
- "Pokaż mi źródło" zawsze możliwe

---

#### Mechanizm 2: Checkpointing (Context Offloading)

**Co to jest:**
Regularne zapisywanie stanu do artefaktu. Reset kontekstu bez utraty pracy.

**Jak działa:**
```
Praca w chacie → [CHECKPOINT] → Artefakt zapisany
                                      ↓
Nowa sesja ← czyta artefakt (czysty kontekst)
```

**Jakie problemy rozwiązuje:**
- Drift (reset, świeży start)
- Ograniczenia (offloading do plików)
- Context rot (filtracja - tylko signal zostaje)
- Slop (mniejsze kawałki do weryfikacji)

**Kiedy checkpointować:**
- Po fazie research (zanim analiza)
- Po alignment (zanim plan)
- Po planie (zanim wykonanie)
- Po wykonaniu (zanim następne zadanie)
- Gdy czat się wydłuża
- Gdy zauważasz drift

---

#### Mechanizm 3: Alignment (Wydobycie Założeń)

**Co to jest:**
Upewnienie się że agent rozumie zadanie tak jak ty, zanim zacznie wykonywać.

**Jak działa:**
1. Dajesz zadanie
2. Prosisz agenta: "Powiedz swoimi słowami jak to rozumiesz"
3. Agent formułuje założenia
4. Weryfikujesz, koregujesz
5. Dopiero potem: "OK, teraz zrób plan"

**Jakie problemy rozwiązuje:**
- Drift (alignment na początku)
- Agent eager (wydobywasz ukryte założenia)
- Slop (agent zna intencję)

**Dlaczego to ważne:**
Agent jest **eager** - nie pyta, zakłada. Jeśli czegoś nie powiesz, wypełni lukę swoim założeniem. Musisz aktywnie wydobyć te założenia.

---

#### Mechanizm 4: Steering (Kontrola Kierunku)

**Co to jest:**
Definiowanie kierunku przed wykonaniem. Korekta kierunku w trakcie.

**Jak działa:**
- Precyzyjne zadanie upfront (WIRE)
- Plan jako checkpoint do weryfikacji
- Możliwość redirect w trakcie
- Course correction gdy drift

**Różnica od editing:**

| Editing Loop | Steering Loop |
|--------------|---------------|
| Agent robi → ty poprawiasz output | Ty definiujesz → agent robi → ty weryfikujesz |
| Kontrola na końcu | Kontrola na początku |
| Zaśmieca kontekst | Nie zaśmieca kontekstu |
| Wysoki cognitive load | Niższy cognitive load |

**Steering nie eliminuje editing:**
- Steering zmniejsza POTRZEBĘ editing
- Ale editing czasem jest konieczne
- Po editing → checkpoint (żeby nie zaśmiecać)

---

#### Mechanizm 5: Dekompozycja

**Co to jest:**
Rozbijanie dużego zadania na mniejsze, zarządzalne części.

**Jak działa:**
```
Duże zadanie
     ↓
┌────┴────┐────────┐
▼         ▼        ▼
Podzadanie 1 → [checkpoint] → Podzadanie 2 → [checkpoint] → Podzadanie 3
```

**Jakie problemy rozwiązuje:**
- Ograniczenia kontekstu (każde podzadanie ma swój kontekst)
- Drift (reset między podzadaniami)
- Slop (weryfikacja przyrostowa)
- Ryzyko (błąd nie propaguje się przez całość)

---

#### Mechanizm 6: Progressive Disclosure

**Co to jest:**
Ładowanie kontekstu stopniowo, na żądanie, po wstępnej ocenie.

**Jak działa:**
```
Źródło dostępne
      ↓
Agent widzi: tytuł, abstrakt, metadane
      ↓
Agent ocenia: relevant? wiarygodne?
      ↓
   TAK → ładuj pełną treść
   NIE → pomiń
```

**Jakie problemy rozwiązuje:**
- Ograniczenia kontekstu (nie ładujesz wszystkiego)
- Halucynacje (filtracja źródeł)
- Context rot (tylko relevant materiały)

**Praktycznie:**
- Research w dwóch fazach: skanowanie → głębokie czytanie
- Agent najpierw raportuje co znalazł
- Ty decydujesz co warto załadować

---

#### Mechanizm 7: Context Isolation

**Co to jest:**
Separacja różnych wątków/perspektyw w osobnych sesjach.

**Jak działa:**
```
                    [PLIK: dokument.md]
                    /        |        \
          [Sesja A]     [Sesja B]    [Sesja C]
          Perspektywa 1 Perspektywa 2 Perspektywa 3
                    \        |        /
                    [Trzy niezależne analizy]
```

**Jakie problemy rozwiązuje:**
- Context rot (brak zanieczyszczenia między wątkami)
- Drift (każda sesja ma czysty kontekst)
- Ograniczenia (mniejszy kontekst per sesja)

**Use cases:**
- Różne perspektywy na ten sam dokument
- Równoległe podzadania
- A/B testing podejść

---

#### Mechanizm 8: Artefakty (Stan vs Strumień)

**Co to jest:**
Zapisywanie outputu w plikach zamiast zostawiania w strumieniu chatu.

**Jak działa:**
- Chat = strumień (append-only, ginie)
- Artefakt = stan (persystuje, edytowalny)
- Każdy znaczący output → plik

**Jakie problemy rozwiązuje:**
- Context rot (artefakt to przefiltrowany signal)
- Drift (artefakt to kotwica)
- Ograniczenia (offloading)
- Brak kumulacji (artefakty zostają)
- Brak przejrzystości (artefakt można otworzyć)

**Artefakt to:**
- Filtr (tylko signal, nie noise)
- Kotwica (punkt odniesienia przeciw drift)
- Interfejs (przejrzystość - widzisz co agent widzi)
- Izolator (wspólny stan dla osobnych sesji)
- Akumulator (kumulacja wiedzy)

---

### Podsumowanie: Mechanizmy i Problemy

| Mechanizm | Halucynacje | Slop | Drift | Ograniczenia |
|-----------|:-----------:|:----:|:-----:|:------------:|
| Transparentność | ✓ | ✓ | ✓ | |
| Checkpointing | | ✓ | ✓ | ✓ |
| Alignment | | ✓ | ✓ | |
| Steering | | ✓ | ✓ | |
| Dekompozycja | | ✓ | ✓ | ✓ |
| Progressive Disclosure | ✓ | | | ✓ |
| Context Isolation | | | ✓ | ✓ |
| Artefakty | ✓ | ✓ | ✓ | ✓ |

---

## Część V: Lifecycle Tasku

### Anatomia zadania

Każde złożone zadanie przechodzi przez fazy. Zrozumienie tych faz pozwala na systematyczne stosowanie mechanizmów.

```
┌─────────────────────────────────────────────────────────────────┐
│                     LIFECYCLE TASKU                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. GROMADZENIE KONTEKSTU                                       │
│     └── źródła, dane, materiały                                 │
│                    ↓                                            │
│            [checkpoint]                                         │
│                    ↓                                            │
│  2. FORMUŁOWANIE ZADANIA                                        │
│     └── WIRE: What, Input, Rules, Examples                      │
│                    ↓                                            │
│  3. ALIGNMENT                                                   │
│     └── agent formułuje założenia, człowiek weryfikuje          │
│                    ↓                                            │
│            [checkpoint: brief/task]                             │
│                    ↓                                            │
│  4. PLANOWANIE                                                  │
│     └── agent proponuje plan, człowiek weryfikuje               │
│                    ↓                                            │
│            [checkpoint: plan]                                   │
│                    ↓                                            │
│  5. WYKONANIE                                                   │
│     └── agent pracuje na artefaktach                           │
│                    ↓                                            │
│  6. REVIEW (editing loop)                                       │
│     └── weryfikacja, korekty (ile potrzeba)                    │
│                    ↓                                            │
│            [checkpoint: artefakt finalny]                       │
│                    ↓                                            │
│  7. NASTĘPNE ZADANIE                                            │
│     └── nowa sesja, czysty kontekst, artefakt jako input       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

### Faza 1: Gromadzenie Kontekstu

**Co się dzieje:**
Zbierasz materiały potrzebne do zadania - źródła, dane, dokumenty, przykłady.

**Kto to robi:**
- Ty (ręcznie wybierasz pliki)
- Agent (research - szuka źródeł)
- Kombinacja (agent szuka, ty filtrujesz)

**Uwaga - agent research zaśmieca:**
Gdy agent robi research, generuje dużo tekstu w chacie - linki, streszczenia, oceny. To zaśmieca kontekst.

**Dlatego:**
```
Agent research → [CHECKPOINT: lista źródeł] → Nowa sesja do analizy
```

**Progressive disclosure:**
- Agent najpierw skanuje (tytuły, abstrakty)
- Raportuje co znalazł
- Ty decydujesz co warto załadować głęboko

---

### Faza 2: Formułowanie Zadania

**Co się dzieje:**
Definiujesz co agent ma zrobić. Precyzyjnie.

**Framework WIRE:**

| Element | Pytanie | Przykład |
|---------|---------|----------|
| **W**hat | Co ma powstać? | "Raport PDF, 10 stron, z wykresami" |
| **I**nput | Z czego? | "Pliki w /data/sales-q4/" |
| **R**ules | Jakie zasady? | "Tylko top 10 produktów, format jak Q3" |
| **E**xamples | Jak ma wyglądać? | "Zobacz /reports/q3-report.pdf" |

**Słaby vs dobry task:**

❌ "Przeanalizuj dane sprzedażowe"

✅ "Przeanalizuj pliki CSV w /data/sales-q4. Znajdź top 10 produktów po revenue. Stwórz raport PDF z wykresami trendów. Format jak /reports/q3-report.pdf. Zapisz w /reports/q4-analysis.pdf"

---

### Faza 3: Alignment

**Co się dzieje:**
Upewniasz się że agent rozumie zadanie tak jak ty.

**Dlaczego to kluczowe:**
Agent jest **eager**. Nie pyta - zakłada. Jeśli czegoś nie dopowiesz, wypełni lukę swoim założeniem. I pójdzie w tym kierunku.

**Jak to robić:**

1. Dajesz zadanie (WIRE)
2. Mówisz: "Zanim zaczniesz, powiedz swoimi słowami jak rozumiesz to zadanie. Jakie masz założenia?"
3. Agent formułuje rozumienie
4. Weryfikujesz:
   - Czy rozumie cel?
   - Czy założenia są OK?
   - Czy użyje właściwych źródeł?
5. Koregujesz jeśli trzeba
6. Dopiero potem: "OK, teraz zrób plan"

**Checkpoint:**
Po alignment - zapisz brief/task jako artefakt. To jest "kontrakt" na resztę zadania.

---

### Faza 4: Planowanie

**Co się dzieje:**
Agent proponuje jak wykona zadanie. Ty weryfikujesz podejście.

**Dlaczego plan jest artefaktem:**
- Plan to checkpoint przed wykonaniem
- Możesz zweryfikować podejście zanim agent zainwestuje czas
- Łapiesz drift/błędy wcześnie
- Plan jest kotwicą dla wykonania

**Co powinien zawierać plan:**
- Kroki wykonania
- Jakie źródła użyje
- Jaka struktura outputu
- Jakie założenia

**Weryfikacja planu:**
- Czy kroki mają sens?
- Czy użyje właściwych źródeł?
- Czy struktura odpowiada wymaganiom?
- Czy coś pominął?

---

### Faza 5: Wykonanie

**Co się dzieje:**
Agent pracuje według planu. Produkuje output.

**Tryb pracy:**
- Agent pracuje na plikach (źródła jako input, artefakt jako output)
- Możesz obserwować postęp
- Możesz interweniować (steering) jeśli widzisz że odpływa

**Steering w trakcie:**
- "Skup się bardziej na X"
- "Pomiń sekcję o Y"
- "Użyj innego podejścia do Z"

Steering ≠ editing. Steering to korekta kierunku, nie poprawianie outputu.

---

### Faza 6: Review (Editing Loop)

**Co się dzieje:**
Agent skończył. Weryfikujesz output. Poprawiasz jeśli trzeba.

**Ile editing potrzebujesz:**
Zależy od jakości wcześniejszych faz.
- Dobry alignment + dobry plan = mało editing
- Słaby alignment = dużo editing

**Editing zaśmieca kontekst:**
Każda korekta w chacie to więcej tekstu w kontekście. Dlatego:
- Po editing → checkpoint
- Artefakt po editing = czysty stan
- Następna sesja nie widzi historii poprawek

**Selektywna edycja:**
- Edit konkretnego fragmentu, nie regeneracja całości
- Mniejszy kontekst potrzebny
- Mniejsze ryzyko że agent zmieni coś innego

---

### Faza 7: Checkpoint i Dalej

**Co się dzieje:**
Zapisujesz finalny artefakt. Zaczynasz następne zadanie z czystym kontekstem.

**Dlaczego checkpoint:**
- Context reset (bez historii editing, research, wahań)
- Artefakt jako input do następnego zadania
- Kumulacja (artefakt zostaje, chat ginie)

**Następne zadanie:**
- Nowa sesja
- Agent czyta artefakt z poprzedniego zadania
- Czysty kontekst
- Buduje na poprzednim bez bagażu procesu

---

### Podsumowanie: Checkpointy w Lifecycle

```
Gromadzenie kontekstu
        ↓
   [checkpoint: źródła]
        ↓
Formułowanie + Alignment
        ↓
   [checkpoint: brief/task]
        ↓
    Planowanie
        ↓
   [checkpoint: plan]
        ↓
    Wykonanie
        ↓
      Review
        ↓
   [checkpoint: artefakt]
        ↓
  Następne zadanie
```

Każdy checkpoint to:
- Reset kontekstu
- Filtracja (tylko signal)
- Kotwica dla następnej fazy
- Możliwość weryfikacji

---

## Część VI: Rola Czatu

### Czat jako warstwa kontroli

Czat nie jest "trybem pracy" (vs agent mode). Czat jest **interfejsem kontroli** - medium przez które człowiek steruje agentem.

```
┌─────────────────────────────────────────┐
│          CZŁOWIEK (intencja)            │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│          CZAT (warstwa kontroli)        │
│  • eksternalizacja intencji             │
│  • steering                             │
│  • weryfikacja                          │
│  • course correction                    │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│          AGENT (wykonanie)              │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│          ARTEFAKT (stan)                │
└─────────────────────────────────────────┘
```

### Czat PRZED wykonaniem

**Funkcje:**
- Eksternalizacja intencji (z głowy do słów)
- Krystalizacja niejasnych wymagań
- Alignment z agentem
- Definiowanie zadania

**Dlaczego to ważne:**
Nie zawsze wiesz czego chcesz. Intencja jest:
- Zinternalizowana (w głowie, nie wyartykułowana)
- Niejasna (mgliście wiesz, nie precyzyjnie)
- Ewoluująca (zmienia się gdy widzisz opcje)

Czat pozwala to wyciągnąć i skrystalizować.

### Czat PO wykonaniu

**Funkcje:**
- Weryfikacja outputu
- Course correction ("nie to miałem na myśli")
- Dopytywanie ("czemu tak zrobiłeś?")
- Editing (korekty)

**Dlaczego to ważne:**
Intencja ewoluuje gdy widzisz output. Oceniasz w trakcie. Odkrywasz czego chcesz przez zobaczenie czego NIE chcesz.

### Czat jako źródło context rot

**Problem:**
Czat zaśmieca kontekst:
- Historia negocjacji, wahań, błędów
- Editing loop (poprawki, re-generacje)
- Research (linki, streszczenia)
- Wszystko append-only

**Rozwiązanie:**
Po każdej znaczącej fazie kontroli → checkpoint.

```
Czat (alignment) → [checkpoint: brief]
Czat (review) → [checkpoint: artefakt]
```

Checkpoint = filtracja. Tylko signal zostaje.

### Model: Stan i Sygnał

```
ARTEFAKT = Stan (noun)
    - Co jest teraz
    - Persystuje
    - Weryfikowalny

CZAT = Sygnał (verb)
    - Co zmienić
    - Efemeryczny
    - Intencja, korekta

AGENT = Transformacja (function)
    - Stan + Sygnał → Nowy Stan
```

**Formuła:**
```
nowy_artefakt = agent(obecny_artefakt, sygnał_z_czatu)
```

Czat mówi CO ZMIENIĆ.
Artefakt jest TYM CO SIĘ ZMIENIA.

### Gdyby nie czat

Bez czatu agent byłby w pełni autonomiczny:
- Task → wykonanie → output
- Zero steering, zero feedback
- Człowiek poza pętlą

Czat daje kontrolę:
- Przed: precyzujesz intencję
- W trakcie: koregujesz kierunek
- Po: weryfikujesz i poprawiasz

> "Czat to kokpit. Bez niego agent leci na autopilocie."

---

## Część VII: Podsumowanie

### Model całościowy

```
┌─────────────────────────────────────────────────────────────┐
│                    PROBLEMY KONTEKSTU                        │
│  Halucynacje • Slop • Drift • Ograniczenia                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      MECHANIZMY                              │
│  Transparentność • Checkpointing • Alignment • Steering     │
│  Dekompozycja • Progressive Disclosure • Isolation          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   LIFECYCLE TASKU                            │
│  Kontekst → Zadanie → Alignment → Plan → Wykonanie → Review │
│           ↓           ↓           ↓                    ↓    │
│      [checkpoint] [checkpoint] [checkpoint]       [checkpoint]│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   WARSTWY SYSTEMU                            │
│  Intencja (człowiek) → Kontrola (czat) → Wykonanie (agent)  │
│                              ↓                               │
│                      Stan (artefakty)                        │
└─────────────────────────────────────────────────────────────┘
```

### Kluczowe zasady

1. **Agent nie jest źródłem wiedzy** - jest procesorem. Dostarczasz materiały, on przetwarza.

2. **Kontekst jest wszystkim** - halucynacje, slop, drift to problemy kontekstu. Rozwiązujesz je przez zarządzanie kontekstem.

3. **Checkpointing jest meta-rozwiązaniem** - rozwiązuje drift, ograniczenia, context rot. Stosuj często.

4. **Agent jest eager** - zakłada zamiast pytać. Wydobywaj założenia przed wykonaniem.

5. **Steering > Editing** - definiuj precyzyjnie na początku. Mniej poprawiania na końcu.

6. **Czat to kontrola, artefakt to stan** - czat mówi co zmienić, artefakt jest tym co się zmienia.

7. **Transparentność umożliwia nadzór** - widzisz co agent widzi. Możesz weryfikować.

### Jedno zdanie

> "Dostarcz odpowiedni kontekst, zapewnij alignment, checkpointuj często, weryfikuj przyrostowo."

---

*Narracja v2.0 - Styczeń 2026*
*Struktura: Problemy → Mechanizmy → Lifecycle → Warstwy*
