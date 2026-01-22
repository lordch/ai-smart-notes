# Frameworki: Praca z Agentami AI

Synteza myśli o zmianie paradygmatu z chat na agent.

---

## 1. Dwa tryby pracy z AI

| Chat Mode | Agent Mode |
|-----------|------------|
| AI jako rozmówca | AI jako wykonawca |
| Wiedza "w głowie AI" | Wiedza w plikach |
| Konwersacja | Zadania |
| Output ginie w historii | Output żyje w artefaktach |
| Każda sesja od zera | Praca się kumuluje |

**Kluczowy insight:** To nie jest binarne. Jest spectrum:

```
Pure chat → Chat z checkpointami → Agent ze sterowaniem → Pełna delegacja
```

Czat nie jest "zły" - służy do krystalizacji intencji. Problem pojawia się gdy zostajemy w czacie zamiast przejść do artefaktów.

---

## 2. Dwie pętle (z curriculum)

| Editing Loop | Steering Loop |
|--------------|---------------|
| Prompt → Czytasz → Poprawiasz → Prompt again | Definiujesz task → Review planu → Redirect → Akceptujesz artefakt |
| Ty poprawiasz output | Ty kierujesz procesem |
| Cognitive load: HIGH | Cognitive load: LOW |
| Wartość: w edytowaniu | Wartość: w definiowaniu |

**Shift:** Praca poznawcza nadal jest twoja, ale dzieje się na początku (steering), nie na końcu (editing).

---

## 3. Fundamentalny insight: Agent nie jest źródłem wiedzy

**Dlaczego ludzie nie ufają AI:**
- Traktują ChatGPT jako encyklopedię
- Pytają "co wiesz o X"
- AI halucynuje → utrata zaufania

**Zmiana paradygmatu:**
- Agent pracuje NA źródłach, nie JEST źródłem
- Ty dostarczasz materiały, on przetwarza
- Halucynacje dramatycznie maleją gdy agent ma konkret

**Zadania agenta (to robi dobrze):**
- Ekstrakcja informacji ze źródeł
- Interpretacja i porównanie
- Framing i synteza
- Stosowanie metodologii/frameworków
- Techniczne zadania

**Twoje zadania:**
- Zapewnienie kontekstu (źródła, wiedza domenowa)
- Zapewnienie intencji (co chcesz osiągnąć)
- Dekompozycja na kroki
- Weryfikacja jakości i źródeł
- Decyzje kierunkowe

---

## 4. Trójkąt jakości agenta

```
        KONTEKST
           △
          / \
         /   \
        /     \
    ZADANIE ─── WERYFIKACJA
```

Agent wykonuje dobrze gdy:
- **Kontekst** jest wystarczający (źródła, wiedza domenowa)
- **Zadanie** jest precyzyjne (intencja, kroki, wymagania)
- **Weryfikacja** jest możliwa (checkpointy, źródła do sprawdzenia)

---

## 5. Definiowanie zadań: Framework WIRE (z curriculum)

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

---

## 6. Problemy → Rozwiązania

| Problem | Przyczyna | Rozwiązanie |
|---------|-----------|-------------|
| **Halucynacje** | AI jako źródło wiedzy | AI pracuje NA źródłach |
| **Slop** | Brak precyzyjnych wymagań | WIRE framework upfront |
| **Context drift** | Długi kontekst, brak kotwicy | Checkpointing |
| **Utrata kontekstu** | Ograniczenia window | Context offloading do plików |
| **Trudna weryfikacja** | Duży output na raz | Małe kroki, weryfikacja przyrostowa |

---

## 7. Checkpointing: dlaczego jest kluczowy

**Co to rozwiązuje:**
- **Slop** - mniejsza płaszczyzna do sprawdzenia
- **Drift** - kotwica do której wracamy
- **Utrata kontekstu** - offloading do plików
- **Zmarnowana praca** - łapiemy błędy wcześniej

**Mechanizm:**
```
Praca w czacie → Checkpoint (zapisz artefakt) → Kontynuacja na artefakcie
```

**Dlaczego wypuszczamy slop:**
- Sprawdzenie wielkiego raportu jest żmudne
- Lenistwo + presja czasu
- "Wygląda profesjonalnie"

Checkpointing sprawia, że weryfikacja staje się tractable.

---

## 8. Rola czatu w systemie pracy

**Czat służy do:**
- Odkrywania/precyzowania intencji
- Iteracji na wymaganiach
- Poprawiania jakości w trakcie

**Problem z czatem:**
- Zajmuje kontekst
- Powoduje drift
- Output ginie

**Rozwiązanie:**
```
Intencja niejasna → [CZAT: dialog, iteracja] → Intencja skrystalizowana
                                                        ↓
                                              [CHECKPOINT: zapisz]
                                                        ↓
                                              [Dalsze zadania na artefakcie]
```

**Optymalnie:** Guidance z czatu kondensuje się do instrukcji na przyszłość.

Nie zawsze możemy mieć wszystkie instrukcje upfront:
- Nie znamy intencji od początku
- Intencje ewoluują
- Oceniamy w trakcie

Dlatego czat jest częścią systemu, nie wrogiem.

---

## 9. Inverse Supervision

**Klasycznie:** Manager → zadanie → pracownik → output → manager sprawdza

**Z agentem:**
- Agent produkuje szybko i dużo
- Bottleneck to TWOJA zdolność weryfikacji
- Więc projektujesz system pod łatwość weryfikacji

**Praktycznie:**
- Małe kroki (łatwiej sprawdzić plan niż raport)
- Źródła inline (nie musisz szukać skąd to wie)
- Checkpointy (nie tracisz pracy przez drift)
- Proś o cytaty, referencje

---

## 10. Against Slop: 5 mechanizmów (z curriculum)

1. **Artifact-first output** - output = gotowy deliverable, nie blob tekstu
2. **Visible planning** - widzisz plan przed wykonaniem
3. **Specificity through files** - wskazujesz realne pliki
4. **Async execution** - task queue wymusza przemyślenie
5. **Quality from origin** - standard z kodowania dla knowledge work

---

## 11. Narracja na szkolenie

**Arc:**

1. **Status quo:** Używacie AI jak wyroczni → halucynacje, brak zaufania
2. **Reframe:** To nie wina AI - to zły tryb pracy
3. **Shift:** Agent mode - AI jako wykonawca, nie źródło
4. **Klucz 1:** Kontekst - daj mu materiały, nie pytaj "co wiesz"
5. **Klucz 2:** Precyzja - WIRE framework
6. **Klucz 3:** Checkpointing - zapisuj, weryfikuj, kontynuuj
7. **Rola czatu:** Krystalizacja intencji → checkpoint → artefakt
8. **Twoja rola:** Nie pisarz - kierownik. Steering loop, nie editing loop.

---

## 12. Podsumowanie: dwie tabelki

### Podział odpowiedzialności

| Człowiek | Agent |
|----------|-------|
| Intencja (co chcemy) | Wykonanie (ekstrakcja, synteza) |
| Kontekst (jakie źródła) | Stosowanie metodologii |
| Dekompozycja (jak podzielić) | Generowanie wariantów |
| Weryfikacja (czy dobre) | Techniczne zadania |
| Decyzje (kierunek) | - |

### Problemy → Rozwiązania

| Problem | Rozwiązanie |
|---------|-------------|
| Halucynacje | Agent na źródłach, nie jako źródło |
| Slop | WIRE framework + checkpointing |
| Drift | Checkpointing |
| Trudna weryfikacja | Małe kroki, źródła inline |
| Niejasna intencja | Czat jako krystalizacja → checkpoint |

---

*Synteza notatek + curriculum v1.0 - Styczeń 2026*
