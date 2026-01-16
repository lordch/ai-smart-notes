# Alternatywne Łuki Narracyjne Kursu

Brainstorm dla persony: **pracownik umysłowy, który czasem używa ChatGPT, ale do końca mu nie ufa.**

---

## Persona: Co wie, co czuje

**Doświadczenia:**
- Używał ChatGPT do maili, streszczeń, draftów
- Widział halucynacje, zmyślone fakty, "confident bullshit"
- Czasem AI pomogło, czasem zmarnowało czas
- Nie wie DLACZEGO czasem działa, a czasem nie

**Przekonania:**
- "AI to loteria — czasem trafi, czasem nie"
- "Trzeba wszystko po nim sprawdzać"
- "Może być pomocne, ale nie można na nim polegać"
- "Nie wiem kiedy mogę mu zaufać"

**Potrzeby:**
- Model mentalny: DLACZEGO tak się dzieje
- Poczucie kontroli nad wynikiem
- Przewidywalność zamiast losowości
- Pewność KIEDY można zaufać, a kiedy nie

---

## Łuk 1: "Od Loterii do Systemu"

### Core insight
*"AI nie jest nieprzewidywalne. Nieprzewidywalny jest kontekst, który mu dajesz. Gdy kontrolujesz kontekst, kontrolujesz wynik."*

### Story arc

**Akt 1: Walidacja** — "Masz rację że nie ufasz"
- Tak, AI halucynuje. Tak, daje confident bullshit.
- To nie jest twoja wina, że ci nie wyszło.
- ALE: To nie jest też "wina AI" ani "losowość".

**Akt 2: Demistyfikacja** — "Oto dlaczego tak się dzieje"
- AI nie "wie" — widzi tylko to, co mu dasz.
- Gdy dajesz mało kontekstu, zgaduje (i często źle).
- Gdy dajesz zły kontekst, produkuje śmieci.
- **Garbage in, garbage out** — ale dla wiedzy, nie danych.

**Akt 3: Kontrola** — "Możesz to kontrolować"
- Każdy element wyniku zależy od jakiegoś elementu inputu.
- Uczysz się które dźwignie pociągać.
- Context engineering = systematyczne kontrolowanie zmiennych.

**Akt 4: System** — "Od przypadku do procesu"
- Budujesz powtarzalne środowisko pracy.
- Wyniki stają się przewidywalne.
- "Loteria" zamienia się w "system".

### Kluczowa wizualizacja

```
        PRZED                           PO

    ┌─────────────┐                ┌─────────────┐
    │   INPUT     │                │   INPUT     │
    │  (losowy)   │                │(kontrolowany)│
    └──────┬──────┘                └──────┬──────┘
           │                              │
           ▼                              ▼
    ┌─────────────┐                ┌─────────────┐
    │    AI       │                │    AI       │
    │  (czarna    │                │  (ta sama   │
    │  skrzynka)  │                │  mechanika) │
    └──────┬──────┘                └──────┬──────┘
           │                              │
           ▼                              ▼
    ┌─────────────┐                ┌─────────────┐
    │   OUTPUT    │                │   OUTPUT    │
    │  (losowy?)  │                │(przewidywal.)│
    └─────────────┘                └─────────────┘

    "AI to loteria"            "AI to funkcja inputu"
```

### Reframe
❌ "AI jest nieprzewidywalne"
✅ "Mój kontekst był nieprzewidywalny"

---

## Łuk 2: "Pilot i Autopilot"

### Core insight
*"Nie chodzi o to czy ufać AI. Chodzi o to, żebyś wiedział kiedy włączyć autopilot, a kiedy przejąć stery."*

### Metafora przewodnia

Pilot samolotu nie "ufa" ani "nie ufa" autopilotowi. Ma procedury:
- **Włączam** gdy: warunki są stabilne, trasa znana, cel jasny
- **Wyłączam** gdy: turbulencje, nietypowa sytuacja, zbliżam się do lądowania
- **Monitoruję** zawsze: przyrządy, otoczenie, postęp

### Story arc

**Akt 1: "Nie jesteś pasażerem"**
- W ChatGPT czujesz się jak pasażer — wpisujesz i czekasz co wyjdzie
- Problem: nie masz kontroli, nie widzisz co się dzieje
- Agent z plikami = przesiadka do kokpitu

**Akt 2: "Poznaj przyrządy"**
- Co agent widzi (context window)
- Co agent pamięta (pliki, CLAUDE.md)
- Gdzie agent może się mylić (halucynacje, context rot)

**Akt 3: "Procedury pilota"**
- Kiedy delegować (autopilot ON)
- Kiedy kontrolować (manual)
- Jak monitorować (checkpointy)

**Akt 4: "Budowanie godzin nalotu"**
- Im więcej latasz, tym lepiej wyczuwasz
- Twoje procedury ewoluują
- Autonomy slider przesuwa się naturalnie

### Kluczowa wizualizacja

```
         PILOT MINDSET
         ═════════════

    ┌──────────────────────────────────────┐
    │            COCKPIT VIEW               │
    │                                        │
    │   ┌────────┐  ┌────────┐  ┌────────┐  │
    │   │CONTEXT │  │PROGRESS│  │ TRUST  │  │
    │   │ WINDOW │  │        │  │ LEVEL  │  │
    │   │ ████░░ │  │ Step 3 │  │ ██░░░░ │  │
    │   │ 67%    │  │ of 5   │  │ 40%    │  │
    │   └────────┘  └────────┘  └────────┘  │
    │                                        │
    │        [AUTOPILOT: ON/OFF]             │
    │                                        │
    │   Ty decydujesz. Ty monitorujesz.     │
    │   Ty odpowiadasz za lot.              │
    └──────────────────────────────────────┘
```

### Mapowanie na poziomy kursu

| Faza lotu | Tryb | Poziom kursu |
|-----------|------|--------------|
| Kołowanie | Manual | L0 — podstawowa interakcja |
| Start | Manual | L0-1 — uczysz się przyrządów |
| Wznoszenie | Semi-auto | L2 — checkpointy |
| Lot | Autopilot OK | L3-5 — system działa |
| Turbulencje | Manual | L6-7 — diagnoza, naprawa |
| Lądowanie | Manual | Finalizacja, weryfikacja |

### Reframe
❌ "Czy mogę zaufać AI?"
✅ "Kiedy włączyć autopilot, a kiedy trzymać stery?"

---

## Łuk 3: "Budowanie Zaufania przez Kontrolę"

### Core insight
*"Zaufanie to nie cecha AI. Zaufanie to funkcja twojej kontroli. Im więcej kontrolujesz, tym więcej możesz zaufać."*

### Psychologia zaufania

Dlaczego nie ufamy AI:
1. **Brak przewidywalności** — nie wiemy co dostaniemy
2. **Brak zrozumienia** — nie wiemy dlaczego coś wyszło
3. **Brak kontroli** — nie wiemy jak wpłynąć na wynik
4. **Negatywne doświadczenia** — pamiętamy wpadki

Rozwiązanie: Budować kontrolę → kontrola daje przewidywalność → przewidywalność buduje zaufanie.

### Story arc

**Akt 1: "Zaufanie zero" — Gdzie jesteś teraz**
- Wpisujesz → dostajesz coś → sprawdzasz WSZYSTKO
- Koszt weryfikacji często > koszt zrobienia samemu
- Frustracja: "po co mi to AI"

**Akt 2: "Zaufanie warunkowe" — Pierwsze success stories**
- Uczysz się: "przy TAKIM kontekście, działa DOBRZE"
- Zaczynasz rozumieć warunki sukcesu
- Checkpoint: "tutaj sprawdzam, tu ufam"

**Akt 3: "Zaufanie kalibrowane" — Wiesz kiedy i ile**
- Masz mentalny model: gdzie AI jest dobre, gdzie słabe
- Świadomie decydujesz co delegować
- Weryfikujesz proporcjonalnie do ryzyka

**Akt 4: "Zaufanie systematyczne" — System zamiast intuicji**
- CLAUDE.md, reference files, skills = system
- Powtarzalne warunki = powtarzalne wyniki
- Zaufanie wynika z systemu, nie z nadziei

### Kluczowa wizualizacja

```
    TRUST = f(CONTROL)

    Zaufanie
        ▲
        │                              ●
        │                          ●
        │                      ●
        │                  ●
        │              ●
        │          ●
        │      ●
        │  ●
        └────────────────────────────────► Kontrola

        Mniej kontroli = mniej zaufania (słusznie!)
        Więcej kontroli = więcej zaufania (zasłużenie!)
```

### Poziomy zaufania → Poziomy kursu

| Poziom zaufania | Charakterystyka | Co umiesz |
|-----------------|-----------------|-----------|
| **Zero** | Sprawdzam wszystko | — |
| **Warunkowe** | Sprawdzam gdy ryzyko | L0-1: wiesz co agent widzi |
| **Kalibrowane** | Wiem gdzie ufać | L2-3: masz checkpointy |
| **Systematyczne** | System generuje zaufanie | L4-5: reference files, skills |
| **Delegowane** | Subagenci, minimal check | L6-7: orchestration |

### Reframe
❌ "Czy AI jest godne zaufania?"
✅ "Czy mój system daje mi podstawy do zaufania?"

---

## Łuk 4: "Od Rozmówcy do Narzędzia"

### Core insight
*"Przestań rozmawiać z AI jak z człowiekiem. Zacznij je obsługiwać jak profesjonalne narzędzie."*

### Problem: Błędny model mentalny

ChatGPT interfejs sugeruje: "rozmawiasz z kimś mądrym"
- Piszesz jak do człowieka
- Oczekujesz że "zrozumie" kontekst
- Zakładasz że "pamięta" co mówiłeś
- Dziwisz się gdy "nie rozumie" czegoś oczywistego

Rzeczywistość: To przetwarzanie tekstu, nie rozmowa
- Nie "rozumie" — pattern-matchuje
- Nie "pamięta" — widzi tylko to co w oknie
- Nie "wie" — generuje prawdopodobne ciągi znaków

### Story arc

**Akt 1: "Dlaczego rozmowa nie działa"**
- Demo: to samo zadanie, różne wyniki
- Pokazanie: AI nie ma "intencji", "pamięci", "rozumienia"
- Przesunięcie: od "z kim rozmawiam" do "jakie narzędzie obsługuję"

**Akt 2: "Poznaj swoje narzędzie"**
- Context window = pamięć robocza narzędzia
- System prompt = konfiguracja narzędzia
- Tools = capabilities narzędzia
- Jak każde narzędzie: ma specyfikację, limity, best practices

**Akt 3: "Naucz się obsługi"**
- CLAUDE.md = instrukcja obsługi dla TEGO projektu
- Reference files = materiały referencyjne
- Skills = procedury operacyjne

**Akt 4: "Professional workflow"**
- Traktujesz jak profesjonalne oprogramowanie
- Masz workflow, procedury, checkpoints
- Wyniki są przewidywalne bo obsługa jest systematyczna

### Kluczowa wizualizacja

```
    MENTAL MODEL SHIFT
    ══════════════════

    PRZED                          PO

    ┌─────────────┐            ┌─────────────┐
    │  "Rozmawiam │            │  "Obsługuję │
    │  z mądrym   │            │  profesjo-  │
    │  asystentem"│            │  nalne      │
    │             │            │  narzędzie" │
    └─────────────┘            └─────────────┘
          │                          │
          ▼                          ▼
    • Piszę jak do człowieka    • Konfiguruję środowisko
    • Oczekuję zrozumienia      • Dostarczam specyfikację
    • Liczę na pamięć           • Zarządzam kontekstem
    • Jestem zaskoczony         • Wyniki przewidywalne
      wynikami
```

### Reframe
❌ "Jak sprawić żeby AI mnie rozumiało?"
✅ "Jak skonfigurować narzędzie do mojego zadania?"

---

## Łuk 5: "Inspection Points"

### Core insight
*"Problem nie w tym że AI robi błędy. Problem w tym że nie wiesz GDZIE sprawdzać."*

### Dla persony która "wszystko sprawdza"

Ta persona ma dobry instynkt (sprawdzać!) ale zły proces (sprawdzać wszystko).

Rezultat:
- Zmęczenie (checking fatigue)
- Nieefektywność (tyle samo pracy co bez AI)
- Frustration ("po co mi to")

### Story arc

**Akt 1: "Twój instynkt jest dobry"**
- Tak, AI robi błędy. Tak, trzeba sprawdzać.
- ALE: Nie wszystko. Nie wszędzie. Nie tak samo.
- Są punkty HIGH RISK i punkty LOW RISK.

**Akt 2: "Gdzie AI zawodzi"**
- Fakty (halucynacje) — HIGH RISK
- Logika wielokrokowa — MEDIUM RISK
- Format, struktura — LOW RISK
- Stylistyka, fluency — VERY LOW RISK

**Akt 3: "Inspection points"**
- Zamiast sprawdzać output → sprawdzaj w KEY POINTS
- Checkpoint PRZED kontynuacją, nie po zakończeniu
- Weryfikuj proporcjonalnie do ryzyka

**Akt 4: "Trust but verify (strategically)"**
- System checkpointów wbudowany w workflow
- Wiesz gdzie AI jest reliable, gdzie nie
- Sprawdzasz mądrze, nie wszędzie

### Kluczowa wizualizacja

```
    INSPECTION STRATEGY
    ═══════════════════

    PRZED (sprawdzam wszystko):

    Input → [AI] → Output → CHECK EVERYTHING → Done
                              (exhausting)

    PO (inspection points):

    Input → [AI] → Checkpoint 1 → [AI] → Checkpoint 2 → Done
                   (verify plan)         (verify facts)

    ┌────────────────────────────────────────────────┐
    │  INSPECTION PRIORITY                           │
    │                                                │
    │  ████████████  Fakty, dane    → ZAWSZE        │
    │  ████████      Logika, plan   → CHECKPOINTY   │
    │  ████          Struktura      → SAMPLING      │
    │  ██            Styl, format   → RZADKO        │
    └────────────────────────────────────────────────┘
```

### Reframe
❌ "Muszę sprawdzać wszystko po AI"
✅ "Muszę wiedzieć GDZIE sprawdzać"

---

## Łuk 6: "Praca PRZEZ agenta, nie Z agentem"

### Core insight
*"To nie jest współpraca dwóch partnerów. To ty pracujesz, używając agenta jako narzędzia wykonawczego."*

### Problem: "Współpraca" jako model

Gdy myślisz "współpracuję z AI":
- Dzielisz odpowiedzialność (ale AI nie ma odpowiedzialności)
- Oczekujesz inicjatywy (ale AI reaguje, nie inicjuje)
- Liczysz na judgment (ale AI nie ma judgment)

### Właściwy model: Delegated Execution

**Ty:**
- Decydujesz CO zrobić
- Dostarczasz WIEDZĘ
- Weryfikujesz WYNIK
- Ponosisz ODPOWIEDZIALNOŚĆ

**Agent:**
- Wykonuje MECHANICZNIE
- Przetwarza KONTEKST
- Produkuje OUTPUT
- Nie ma opinii ani judgment

### Story arc

**Akt 1: "Redefiniowanie relacji"**
- To nie partner, to narzędzie wykonawcze
- Bardzo zdolne narzędzie, ale narzędzie
- Ty jesteś właścicielem wyniku

**Akt 2: "Twoja robota = context curation"**
- Zbierasz wiedzę, organizujesz, dostarczasz
- Agent przetwarza to co dasz
- Output zależy od twojego inputu

**Akt 3: "Delegated execution w praktyce"**
- Jasne zadania, jasny kontekst
- Checkpointy gdzie weryfikujesz
- Iteracja gdy wynik nie taki jak chcesz

**Akt 4: "Przesuwanie granicy"**
- Im lepszy system kontekstu, tym więcej możesz delegować
- Autonomy slider jako funkcja dojrzałości systemu
- Ale odpowiedzialność zawsze twoja

### Kluczowa wizualizacja

```
    WORK THROUGH, NOT WITH
    ══════════════════════

         ┌───────────────────────────────────┐
         │              TY                    │
         │   • Decyzje    • Wiedza           │
         │   • Weryfikacja • Odpowiedzialność│
         └───────────────┬───────────────────┘
                         │
                    DELEGACJA
                         │
                         ▼
         ┌───────────────────────────────────┐
         │            AGENT                   │
         │   • Wykonanie  • Przetwarzanie    │
         │   (mechaniczne, nie autonomiczne) │
         └───────────────┬───────────────────┘
                         │
                      OUTPUT
                         │
                         ▼
         ┌───────────────────────────────────┐
         │          WYNIK                     │
         │   (twój wynik, twoja odpow.)      │
         └───────────────────────────────────┘
```

### Reframe
❌ "Współpracuję z AI"
✅ "Pracuję, używając AI jako narzędzia wykonawczego"

---

## Porównanie Łuków

| Łuk | Główny problem który adresuje | Główny reframe | Dla kogo najlepszy |
|-----|------------------------------|----------------|-------------------|
| **Loteria→System** | "Nie wiem czego się spodziewać" | Kontroluj input, kontrolujesz output | Sfrustrowani nieprzewidywalnością |
| **Pilot/Autopilot** | "Nie wiem kiedy ufać" | Ty decydujesz o trybie | Chcący zachować kontrolę |
| **Zaufanie przez kontrolę** | "Nie ufam AI" | Zaufanie = f(kontroli) | Sceptyczni, ostrożni |
| **Rozmówca→Narzędzie** | "AI mnie nie rozumie" | To narzędzie, nie rozmówca | Antropomorfizujący AI |
| **Inspection Points** | "Muszę wszystko sprawdzać" | Sprawdzaj mądrze, nie wszędzie | Perfekcjoniści, QA-minded |
| **Przez agenta** | "Nie wiem kto odpowiada" | Ty odpowiadasz, zawsze | Managerowie, właściciele |

---

## Rekomendacja: Łuk Hybrydowy

Dla persony "pracownik który nie ufa" proponuję kombinację:

**Primary frame: "Od Loterii do Systemu"**
- Bezpośrednio adresuje główną frustrację
- Daje jasny model mentalny
- Obiecuje konkretny wynik (przewidywalność)

**Supporting frame: "Inspection Points"**
- Waliduje instynkt sprawdzania
- Daje praktyczne narzędzie (gdzie sprawdzać)
- Redukuje fatigue

**Background frame: "Przez agenta, nie z agentem"**
- Klaruje odpowiedzialność
- Zapobiega rozczarowaniu "współpracą"
- Buduje właściwy model relacji

### Propozycja zmodyfikowanej struktury kursu

```
MODUŁ 0: "Dlaczego dotąd nie działało"
  - Walidacja doświadczeń
  - Model: AI nie jest loteria, kontekst jest
  - Demo: ten sam agent, różne wyniki przy różnym kontekście

MODUŁ 1: "Co agent widzi"
  - Context window jako klucz do przewidywalności
  - Practical: jak kontrolować co agent widzi

MODUŁ 2: "Gdzie sprawdzać"
  - Inspection points zamiast checking everything
  - Checkpointy jako narzędzie kontroli

MODUŁ 3: "Pamięć projektu"
  - CLAUDE.md jako stabilizator
  - System zamiast każdorazowej konfiguracji

MODUŁ 4: "Skalowanie kontroli"
  - Reference files, skills
  - Więcej systemu = więcej przewidywalności

MODUŁ 5: "Delegowanie z kontrolą"
  - Subagenci
  - Kontrolowane rozszerzanie autonomii

MODUŁ 6: "Feedback loop"
  - Ciągłe ulepszanie systemu
  - Od "loterii" do "procesu"
```

---

## Potencjalne Nazwy Kursu (dla tej persony)

- "Od ChatGPT do systemu: AI które działa przewidywalnie"
- "Context Engineering: Jak sprawić, żeby AI było wiarygodne"
- "Kontrolowana automatyzacja: AI bez niespodzianek"
- "Zaufać AI? Najpierw zbuduj system"
- "Przewidywalne AI: Od chatu do workflow"
