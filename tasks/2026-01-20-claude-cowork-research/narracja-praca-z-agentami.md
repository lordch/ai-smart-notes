# Praca z Agentami AI: Pełna Narracja

Dokument łączący wszystkie wątki w spójną całość.

---

## Część I: Zmiana Paradygmatu

### Problem: AI jako wyrocznia

Większość ludzi używa AI jak encyklopedii. Pytają "co wiesz o X". Traktują ChatGPT jako źródło wiedzy.

To jest fundamentalny błąd.

Kiedy pytasz AI "co wiesz", prosisz o halucynację. Model generuje tekst który *brzmi* jak wiedza, ale nie ma zakotwiczenia w rzeczywistości. Stąd bierze się nieufność: "AI kłamie", "AI wymyśla źródła", "nie można mu ufać".

**Reframe:** To nie wina AI. To zły tryb użycia.

### Insight: Agent nie jest źródłem wiedzy

Agent to **procesor**, nie **źródło**.

Kiedy dajesz agentowi materiały i prosisz o ich przetworzenie - ekstrakcję, syntezę, porównanie, framing - halucynacje dramatycznie maleją. Agent ma konkret. Pracuje NA czymś, nie Z niczego.

| Tryb | Co robisz | Ryzyko halucynacji |
|------|-----------|-------------------|
| AI jako źródło | "Co wiesz o X?" | Wysokie |
| AI jako procesor | "Przeanalizuj te pliki pod kątem X" | Niskie |

**Fundamentalna zmiana:** Nie pytaj co AI wie. Daj mu materiały i powiedz co ma z nimi zrobić.

### Podział odpowiedzialności

Ta zmiana przesuwa odpowiedzialności:

**Twoje zadania (człowiek):**
- Zapewnienie kontekstu (źródła, wiedza domenowa)
- Zapewnienie intencji (co chcesz osiągnąć)
- Dekompozycja na kroki
- Weryfikacja jakości i źródeł
- Decyzje kierunkowe

**Zadania agenta:**
- Ekstrakcja informacji ze źródeł
- Interpretacja i porównanie
- Framing i synteza
- Stosowanie metodologii/frameworków
- Techniczne zadania (formatowanie, kod, obliczenia)

> "Agent to twój wykonawca, nie twój doradca. Ty wiesz CO, on wie JAK."

---

## Część II: Dwa Tryby, Dwie Pętle

### Chat Mode vs Agent Mode

| Chat Mode | Agent Mode |
|-----------|------------|
| AI jako rozmówca | AI jako wykonawca |
| Wiedza "w głowie AI" | Wiedza w plikach |
| Konwersacja | Zadania |
| Output ginie w historii | Output żyje w artefaktach |
| Każda sesja od zera | Praca się kumuluje |

Ale to nie jest binarny wybór. To spectrum:

```
Pure chat → Chat z checkpointami → Agent ze sterowaniem → Pełna delegacja
```

Każdy punkt na spectrum ma swoje miejsce. Problem pojawia się gdy **zostajemy** w trybie który nie służy celowi.

### Editing Loop vs Steering Loop

Dwie pętle pracy:

| Editing Loop | Steering Loop |
|--------------|---------------|
| Prompt → Czytasz → Poprawiasz → Prompt again | Definiujesz task → Review planu → Redirect → Akceptujesz artefakt |
| Ty poprawiasz output | Ty kierujesz procesem |
| Cognitive load: HIGH | Cognitive load: LOW |
| Wartość: w edytowaniu | Wartość: w definiowaniu |

**Shift:** Praca poznawcza nadal jest twoja, ale dzieje się na początku (steering), nie na końcu (editing).

W editing loop jesteś redaktorem - poprawiasz co agent napisał.
W steering loop jesteś kierownikiem - mówisz co ma powstać i weryfikujesz czy powstało.

> "The cognitive work is on you, but it happens at the top. It's the steering work - articulating what you want. Not downstream cleaning up what you got."

---

## Część III: Rola Czatu

### Czat nie jest wrogiem

Łatwo wpaść w myślenie binarne: czat = zły, artefakt = dobry. To uproszczenie.

Czat ma swoją funkcję w systemie. To **interfejs kontroli** - medium przez które człowiek steruje agentem.

### Czat PRZED wykonaniem

Nie zawsze wiesz czego chcesz. Intencje są:
- Zinternalizowane (w głowie, nie wyartykułowane)
- Niejasne (mgliście wiesz, nie precyzyjnie)
- Ewoluujące (zmieniają się gdy widzisz opcje)

Czat pozwala na **eksternalizację intencji**:

```
Intencja zinternalizowana/niejasna
            ↓
    [CZAT: dialog, iteracja]
            ↓
Intencja skrystalizowana, wyartykułowana
            ↓
    [CHECKPOINT: zapisz jako task/brief]
```

Czat to przestrzeń krystalizacji. Miejsce gdzie "wiem co chcę ale nie umiem powiedzieć" zamienia się w precyzyjne wymagania.

### Czat PO wykonaniu

Agent wykonał zadanie. Masz output. Czat służy teraz do:

- **Course correction:** "Nie to miałem na myśli, zmień X"
- **Dalsze odkrywanie:** "A może jednak podejdźmy inaczej..."
- **Quality control:** "Sprawdź źródła dla punktu 3"
- **Dopytywanie:** "Czemu wybrałeś to podejście?"

```
            [AGENT WYKONUJE]
                   ↓
              [OUTPUT]
                   ↓
    [CZAT: review, korekta, dopytywanie]
                   ↓
         [LEPSZY OUTPUT / NOWY TASK]
```

### Czat jako warstwa kontroli

**Gdyby nie czat, agent byłby w pełni autonomiczny:**
- Dostaje task → wykonuje → output
- Zero steering, zero feedback
- Człowiek nie ma gdzie interweniować

**Czat daje ci kontrolę:**
- Przed: precyzujesz co chcesz
- W trakcie: redirectujesz jeśli trzeba
- Po: koregujesz i iterujesz

> "Czat to kokpit. Bez niego agent leci na autopilocie. Z nim - ty sterujesz."

### Model: Stan i Sygnał

```
ARTEFAKT = Stan (noun)
    - Co jest teraz
    - Persystuje
    - Widoczny, weryfikowalny

CZAT = Sygnał (verb)
    - Co zmienić
    - Efemeryczny
    - Intencja, korekta

AGENT = Transformacja (function)
    - Stan + Sygnał → Nowy Stan
```

**Formuła:** `nowy_artefakt = agent(obecny_artefakt, sygnał_z_czatu)`

Czat i artefakt nie konkurują. Czat mówi CO ZMIENIĆ, artefakt jest CZYM SIĘ ZMIENIA.

---

## Część IV: Dlaczego Artefakty

### 5 Funkcji Artefaktu

Artefakt to nie tylko "plik zamiast tekstu w chacie". To mechanizm który rozwiązuje pięć problemów jednocześnie.

---

#### 1. FILTR (Signal vs Noise)

**Problem:** Czat gromadzi wszystko.

Kiedy pracujesz w chacie, agent widzi:
- Twoje błędy ("nie, jednak inaczej")
- Twoje wahania ("a może...")
- Ślepe uliczki ("zapomnij o tym")
- Literówki i pomyłki

To "zanieczyszcza" kontekst. Agent jest "zbiasowany" twoim procesem dochodzenia do rozwiązania.

**Artefakt rozwiązuje:** Zapisujesz tylko to co warte zachowania.

Kiedy zapisujesz do pliku, robisz selekcję. Filtr. Zostawiasz signal, odrzucasz noise.

| Czat | Artefakt |
|------|----------|
| Historia bólu | Tylko efekt końcowy |
| Noise + signal wymieszane | Przefiltrowany signal |
| Agent widzi twoje męczenie się | Agent widzi czysty stan |

> "Chat pamięta twoje błędy. Artefakt pamięta twój sukces."

> "Artefakt to garbage collection dla kontekstu."

**Praktyczny przykład:** Wywiad z klientem trwa 40 minut. Miotasz się, zmieniasz zdanie, wracasz do poprzednich pomysłów. Na końcu: plik `REQUIREMENTS.md`. Agent który będzie budował nie widzi 40 minut wahań. Widzi czysty brief.

---

#### 2. KOTWICA (Przeciw Context Drift)

**Problem:** W długim czacie kontekst degraduje.

Im dłuższa rozmowa, tym bardziej agent "zapomina" początek. Instrukcje z pierwszych wiadomości tracą wagę. Styl się zmienia. Powtarzasz te same korekty.

To jest **context drift** - naturalna degradacja jakości w miarę wydłużania się kontekstu.

**Artefakt rozwiązuje:** Checkpoint. Reset. Nowa sesja zaczyna od czystego stanu.

```
Długi czat z driftem
        ↓
[CHECKPOINT: zapisz artefakt]
        ↓
Nowa sesja z czystym kontekstem
Agent czyta artefakt (czysty stan)
Nie czyta historii chatu (drift)
```

| Czat | Artefakt |
|------|----------|
| Context drift | Świeży start |
| Instrukcje tracą wagę | Instrukcje w pliku zawsze obecne |
| Kumulacja szumu | Reset do czystego stanu |

> "Artefakt to kotwica. Nie dryfujesz."

**Checkpointing rozwiązuje jednocześnie:**
- Drift - świeży kontekst
- Slop - mniejszy output do weryfikacji
- Utratę pracy - artefakt persystuje

---

#### 3. INTERFEJS NADZORU (Epistemic Transparency)

**Problem:** W chacie z "wbudowaną wiedzą" nie wiesz co agent wie.

Kiedy agent korzysta z RAG, embeddings, "pamięci" - to jest black box. Nie możesz zweryfikować na jakiej podstawie coś twierdzi. Możesz tylko kłócić się z outputem.

**Artefakt rozwiązuje:** Widzisz dokładnie te same pliki co agent.

W systemie plikowym masz **epistemic transparency** - pełną widoczność tego co agent wie. Bo "wie" tylko to co jest w plikach. A pliki możesz otworzyć i przeczytać.

| Czat z RAG | System plikowy |
|------------|----------------|
| "Skąd to wiesz?" - nie wiadomo | Otwierasz plik, widzisz |
| Zgadywanie | Weryfikacja |
| Kłócisz się z outputem | Poprawiasz input |

> "Nadzór wymaga widoczności. Widzisz te same pliki co agent. Możesz go nadzorować."

**Inverse supervision:** Agent produkuje szybko i dużo. Bottleneck to TWOJA zdolność weryfikacji. Dlatego projektujesz system pod łatwość weryfikacji, nie pod łatwość wykonania.

Artefakty + pliki źródłowe = weryfikacja jest możliwa.

---

#### 4. IZOLATOR (Multi-threading)

**Problem:** W czacie nie możesz robić dwóch rzeczy naraz.

Jeden czat = jeden wątek myślowy. Chcesz żeby agent spojrzał na coś z dwóch perspektyw? "Zapomnij co powiedziałem wcześniej i teraz pomyśl jako X". To nie działa - kontekst się miesza.

**Artefakt rozwiązuje:** Wielu agentów pracuje na tym samym pliku, izolowani od siebie.

```
                    [PLIK: cv.md]
                    /            \
        [Agent A: Rekruter]    [Agent B: Manager]
        Ocenia z perspektywy   Ocenia z perspektywy
        rekrutacji             zespołu
                    \            /
                    [Dwie niezależne oceny]
```

Każdy agent widzi tylko plik. Nie widzi co drugi agent powiedział. Nie sugeruje się. Czyste, izolowane wątki.

| Czat | System plikowy |
|------|----------------|
| Jeden wątek | Wiele równoległych |
| "Zapomnij o tamtym" | Każdy agent widzi tylko plik |
| Zanieczyszczenie między wątkami | Pełna izolacja |

> "Plik to punkt styku bez zanieczyszczenia."

---

#### 5. AKUMULATOR (Compounding Knowledge)

**Problem:** Czat jest transakcyjny.

Zamykasz okno, wiedza znika. Zaczynasz nową sesję od zera. Każdy projekt od początku. Żadnej kumulacji.

**Artefakt rozwiązuje:** Wiedza persystuje. Projekty budują na sobie.

```
Projekt 1 → Artefakty → [zachowane]
                              ↓
Projekt 2 → buduje na artefaktach z Projektu 1
                              ↓
Projekt 3 → buduje na wszystkim powyżej
                              ↓
            [COMPOUND KNOWLEDGE]
```

| Czat | Artefakt |
|------|----------|
| Sesja | Lata |
| Od zera | Na fundamencie |
| Wiedza znika | Wiedza procentuje |

> "Chat is session. Artifact is institution."

**Praktyczny przykład:** Nowy manager "dziedziczy" chaos po poprzedniku. Zamiast pytać chata "jak naprawić program lojalnościowy" (generic advice), agent czyta folder `old-campaigns/` i `company-context/`. Uczy się historii firmy w 30 sekund. Proponuje rozwiązania osadzone w kontekście.

Tej historii nie dałoby się wklejać do chata za każdym razem.

---

### Podsumowanie: 5 Funkcji

| Funkcja | Problem (czat) | Rozwiązanie (artefakt) | Metafora |
|---------|---------------|------------------------|----------|
| **FILTR** | Gromadzi noise | Zachowuje signal | Garbage collection |
| **KOTWICA** | Context drift | Checkpoint, świeży start | Punkt odniesienia |
| **INTERFEJS** | Black box | Epistemic transparency | Otwarta książka |
| **IZOLATOR** | Mieszanie wątków | Równoległość | Firewall |
| **AKUMULATOR** | Sesyjność | Persystencja | Compound interest |

> **Artefakt FILTRUJE noise, KOTWICZE kontekst, ODSŁANIA stan, IZOLUJE wątki, KUMULUJE wiedzę.**

---

## Część V: Praktyka

### Trójkąt Jakości

Agent wykonuje dobrze gdy trzy warunki są spełnione:

```
        KONTEKST
           △
          / \
         /   \
        /     \
    ZADANIE ─── WERYFIKACJA
```

- **Kontekst** jest wystarczający (źródła, wiedza domenowa)
- **Zadanie** jest precyzyjne (intencja, kroki, wymagania)
- **Weryfikacja** jest możliwa (checkpointy, źródła do sprawdzenia)

Brakuje jednego - jakość spada.

### Framework WIRE (definiowanie zadań)

Dobre zadanie ma strukturę:

**W - What** (Co ma powstać)
- Konkretny artefakt
- Format, długość, struktura
- Gdzie ma trafić

**I - Input** (Z czego)
- Jakie pliki/dane
- Jaki kontekst
- Jakie źródła

**R - Rules** (Jakie zasady)
- Styl, ton
- Ograniczenia
- Must-have / nice-to-have

**E - Examples** (Jak ma wyglądać)
- Reference outputs
- Anti-examples (czego unikać)
- Quality bar

**Przykład:**

❌ Słaby prompt: "Przeanalizuj dane sprzedażowe"

✅ Dobry task (WIRE):
- **W:** PowerPoint z wykresami trendów, 10 slajdów, zapisz w /reports
- **I:** Pliki CSV w folderze /sales-q4
- **R:** Top 10 produktów po revenue, wykres trend per produkt
- **E:** Zobacz raport z Q3 jako reference

### Mechanizmy Anti-Slop

**Slop** = output który wygląda OK ale nie jest zweryfikowany.

Dlaczego wypuszczasz slop:
- Sprawdzenie wielkiego raportu jest żmudne
- Lenistwo + presja czasu
- "Wygląda profesjonalnie"

5 mechanizmów przeciw:

1. **Artifact-first output** - output = gotowy deliverable, nie blob tekstu
2. **Visible planning** - widzisz plan przed wykonaniem, możesz redirect
3. **Specificity through files** - wskazujesz realne pliki, nie opisujesz abstrakcyjnie
4. **Checkpointing** - mniejsza płaszczyzna do sprawdzenia
5. **Źródła inline** - agent podaje skąd wie, możesz zweryfikować

### Inverse Supervision

Klasycznie: Manager → zadanie → pracownik → output → manager sprawdza

Z agentem:
- Agent produkuje szybko i dużo
- Bottleneck to TWOJA zdolność weryfikacji
- Projektujesz system pod łatwość weryfikacji

Praktycznie:
- Małe kroki (łatwiej sprawdzić plan niż 50-stronicowy raport)
- Źródła inline (nie musisz szukać skąd to wie)
- Checkpointy (nie tracisz pracy przez drift)
- Proś o cytaty, referencje

---

## Część VI: Pełny Model

### Warstwy Systemu

```
┌─────────────────────────────────────────┐
│  WARSTWA INTENCJI                       │
│  - Cel, wartości, "po co to robimy"     │
│  - Żyje w głowie → eksternalizuje się   │
│    przez czat do briefów/CLAUDE.md      │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  WARSTWA KONTROLI (CZAT)                │
│  - Interfejs sterowania agentem         │
│  - PRZED: eksternalizacja intencji      │
│  - PO: course correction, QA            │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  WARSTWA WYKONANIA (AGENT)              │
│  - Transformuje stan według sygnału     │
│  - Procesor, nie źródło                 │
│  - Wykonuje zadania na plikach          │
└─────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────┐
│  WARSTWA STANU (ARTEFAKTY)              │
│  - Aktualny stan pracy                  │
│  - Persystuje między sesjami            │
│  - Filtr, Kotwica, Interfejs,           │
│    Izolator, Akumulator                 │
└─────────────────────────────────────────┘
```

### Przepływ Pracy

```
[1. INTENCJA NIEJASNA]
         │
         ▼
[2. CZAT: krystalizacja intencji]
    - "Co właściwie chcę?"
    - Dialog, iteracja
    - Eksternalizacja
         │
         ▼
[3. CHECKPOINT: task/brief]
    - Skrystalizowana intencja
    - WIRE framework
         │
         ▼
[4. AGENT WYKONUJE]
    - Na plikach źródłowych
    - Według task/brief
         │
         ▼
[5. ARTEFAKT: output]
    - Zapisany stan
    - Weryfikowalny
         │
         ▼
[6. CZAT: review]
    - Course correction
    - Quality control
    - Dopytywanie
         │
         ├──► [OK] → Kontynuacja na artefakcie
         │
         └──► [KOREKTA] → Powrót do 4 lub 3
```

### Formuła

```
nowy_artefakt = agent(obecny_artefakt, sygnał_z_czatu, kontekst_z_plików)
```

- **Artefakt** = stan (co jest)
- **Czat** = sygnał (co zmienić)
- **Pliki źródłowe** = kontekst (na podstawie czego)
- **Agent** = transformacja

---

## Część VII: Narracja na Szkolenie

### Arc

1. **Status quo:** Używacie AI jak wyroczni. Pytacie "co wiesz". Halucynuje. Nie ufacie.

2. **Reframe:** To nie wina AI. To zły tryb użycia. AI nie jest źródłem wiedzy - jest procesorem.

3. **Shift:** Agent mode. Dajesz materiały, mówisz co zrobić. Agent przetwarza, nie wymyśla.

4. **Klucz 1 - Kontekst:** Daj mu materiały. Pliki, źródła, dane. Nie pytaj "co wiesz" - powiedz "przeanalizuj to".

5. **Klucz 2 - Precyzja:** WIRE framework. What, Input, Rules, Examples. Precyzyjne zadanie = precyzyjny output.

6. **Klucz 3 - Checkpointing:** Zapisuj artefakty. Nie pracuj w nieskończonym chacie. Checkpoint = filtr, kotwica, reset.

7. **Rola czatu:** Czat nie jest wrogiem. To interfejs kontroli. Przed: krystalizacja intencji. Po: course correction.

8. **Artefakty - 5 funkcji:** Filtr (signal vs noise), Kotwica (przeciw drift), Interfejs (transparency), Izolator (multi-threading), Akumulator (compound knowledge).

9. **Twoja rola:** Nie pisarz - kierownik. Steering loop, nie editing loop. Definiujesz, weryfikujesz, decydujesz. Agent wykonuje.

### Jedno zdanie

> "Przestań pytać AI co wie. Zacznij mówić co ma zrobić z tym co mu dasz."

---

*Pełna narracja v1.0 - Styczeń 2026*
*Synteza: frameworki, 5 funkcji artefaktu, rola czatu, model warstw*
