# Propozycja: Agentic Workspace dla metodologii GrowGo

*Dokument roboczy — propozycja współpracy*

---

## Koncepcja

### Co budujemy

**Agentic Workspace** — gotowe środowisko pracy z AI, w które wbudowana jest metodologia Rudego (proces dywersyfikacji strategicznej).

Klient Rudego dostaje:
- Repozytorium/folder z całą strukturą
- Agenta który "zna" metodologię i prowadzi przez proces
- Miejsce gdzie powstają wszystkie artefakty projektu

### Jak to działa

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENTIC WORKSPACE                        │
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │  CLAUDE.md  │    │   proces/   │    │  kontekst/  │     │
│  │ (instrukcje │    │ (metodologia│    │  (wiedza    │     │
│  │  dla agenta)│    │  Rudego)    │    │  o kliencie)│     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│         │                  │                  │             │
│         └──────────────────┼──────────────────┘             │
│                            ▼                                │
│                    ┌─────────────┐                          │
│                    │    AGENT    │                          │
│                    │  (Claude /  │                          │
│                    │   Cursor)   │                          │
│                    └─────────────┘                          │
│                            │                                │
│                            ▼                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                      praca/                          │   │
│  │  faza-1/          faza-2/          faza-3/          │   │
│  │  ├─ vrio.md       ├─ trendy.md     ├─ scenariusz-a  │   │
│  │  ├─ kompetencje   ├─ tam-sam/      ├─ scenariusz-b  │   │
│  │  └─ DELIVERABLE   ├─ porter/       └─ business-case │   │
│  │                   └─ DELIVERABLE                     │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Przepływ pracy klienta

1. **Start:** Klient klonuje/kopiuje workspace
2. **Kickoff:** Agent pyta o firmę, zapisuje do `kontekst/firma.md`
3. **Faza po fazie:** Agent prowadzi przez proces, tworzy artefakty
4. **Checkpoint:** Po każdej fazie — deliverable do akceptacji
5. **Koniec:** Klient ma folder z całą dokumentacją projektu

---

## Przewagi nad Gemami

### 1. Pamięć między sesjami i krokami

| Gems | Agentic Workspace |
|------|-------------------|
| Każdy Gem zaczyna od zera | Agent czyta poprzednie artefakty |
| Kopiuj-wklej kontekstu między Gemami | Kontekst w plikach, zawsze dostępny |
| Po tygodniu — "gdzie to było?" | Wszystko w jednym folderze |

**Przykład:**
W Fazie 3 (Scenariusze) agent automatycznie czyta wyniki VRIO z Fazy 1. Klient nie musi nic wklejać.

### 2. Drobne artefakty zamiast jednego outputu

| Gems | Agentic Workspace |
|------|-------------------|
| Gem generuje jeden wielki dokument | Każdy krok = osobny plik |
| Trudno wrócić do fragmentu | Łatwo edytować konkretny artefakt |
| "Wygeneruj od nowa" | "Popraw tylko ten plik" |

**Przykład:**
Analiza VRIO to osobny plik. Analiza Portera dla branży A to osobny plik. Klient może wrócić i poprawić jeden element bez regenerowania całości.

### 3. Reużywalność źródeł i artefaktów

| Gems | Agentic Workspace |
|------|-------------------|
| Źródła "gdzieś w historii czatu" | Źródła w folderze `kontekst/dokumentacja/` |
| Trzeba wklejać te same dane wielokrotnie | Agent czyta z pliku gdy potrzebuje |
| Brak cross-reference | Artefakt z Fazy 1 używany w Fazie 2 i 3 |

**Przykład:**
Raport branżowy wrzucony raz do `kontekst/dokumentacja/` jest dostępny w każdej fazie. Agent cytuje konkretne fragmenty.

### 4. Agent robi robotę (nie tylko radzi)

| Gems | Agentic Workspace |
|------|-------------------|
| Gem daje porady, user wykonuje | Agent wykonuje zadania |
| "Powinieneś sprawdzić trendy w..." | Agent robi web research i zapisuje wyniki |
| "Policz TAM według wzoru..." | Agent liczy i generuje tabelę |

**Co agent może robić:**
- Web research (trendy, konkurencja, raporty)
- Obliczenia (TAM/SAM/SOM, finansowe)
- Generowanie tabel i wykresów
- Tworzenie prezentacji
- Ekstrakcja z dokumentów klienta

### 5. Iteratywna praca (Anchor vs Stream)

| Gems (Stream) | Agentic Workspace (Anchor) |
|---------------|----------------------------|
| Cały kontekst w historii czatu | Kontekst w plikach (czysty stan) |
| "Context rot" — jakość spada z długością rozmowy | Każda sesja zaczyna od czystego stanu |
| "Zmień punkt 3" → regeneruje całość | Chirurgiczna edycja (diff) |
| Nie wiadomo co się zmieniło | Git diff pokazuje dokładnie zmiany |

**Przykład:**
Klient: "Dodaj do scenariusza A ryzyko regulacyjne"
- Gem: generuje cały scenariusz od nowa (może zmienić coś innego)
- Workspace: agent dodaje sekcję do pliku, reszta nienaruszona

### 6. Audytowalność i historia

| Gems | Agentic Workspace |
|------|-------------------|
| "Co było inputem?" — nie wiadomo | Wszystko w plikach, wersjonowane |
| Brak historii zmian | Git log pokazuje kto, co, kiedy |
| Trudno odtworzyć proces | Cały proces udokumentowany w artefaktach |

**Dla klienta korporacyjnego:** Może pokazać zarządowi dokładnie jak powstały rekomendacje.

### 7. Skalowalność wiedzy

| Gems | Agentic Workspace |
|------|-------------------|
| Każdy projekt od zera | Wiedza kumuluje się |
| Learnings "w głowie" | Learnings w plikach (patterns, templates) |
| Trudno porównać projekty | Standaryzowana struktura |

**Dla Rudego:** Po 10 projektach ma bibliotekę wzorców, case studies, ulepszonych promptów.

---

## Obiekcje i odpowiedzi

### Obiekcje Rudego (jako twórcy narzędzia)

#### "Gems są prostsze do zbudowania"

**Odpowiedź:**
Tak, pojedynczy Gem jest prostszy. Ale:
- Zestaw 5-7 Gemów które muszą współpracować = kompleksowość porównywalna
- Utrzymanie Gemów (aktualizacje metodologii) = edycja wielu miejsc
- W workspace: zmiana w jednym pliku propaguje się wszędzie

**Propozycja:** Buduję infrastrukturę raz, Rudy wkłada metodologię. Potem Rudy może sam aktualizować.

#### "Moi klienci nie są techniczni"

**Odpowiedź:**
- Klient nie musi rozumieć struktury — agent prowadzi
- Interface: rozmowa z agentem, nie edycja plików
- Klient mówi: "Zaczynamy Fazę 2" — agent wie co robić
- Pliki są "pod spodem", klient widzi głównie czat

**Ale:** Jeśli klient CHCE zajrzeć głębiej — może. Transparency jako feature.

#### "Gems działają w Google, moi klienci tam są"

**Odpowiedź:**
- To jest realne ograniczenie
- Ale: Cursor/Claude Code działają lokalnie lub w cloud
- Alternatywa: workspace jako folder Google Drive + Gemini z dostępem do plików
- Lub: hybrid — Gems jako interface, workspace jako backend

**Do zbadania:** Czy da się zrobić workspace w ekosystemie Google?

#### "Trudniej sprzedać coś czego klient nie zna"

**Odpowiedź:**
- Sprzedajesz WYNIK (przeprowadzony proces dywersyfikacji), nie narzędzie
- Demo: "Popatrz jak to wygląda w praktyce" (pokazujesz sesję)
- Klient nie musi rozumieć technologii — ma rozumieć wartość

**Pitch:** "Dostajesz AI-owego konsultanta strategicznego który zna moją metodologię i prowadzi Cię przez cały proces. Na końcu masz folder z kompletną dokumentacją."

### Obiekcje klienta końcowego

#### "To wygląda skomplikowanie"

**Odpowiedź:**
- Klient widzi: czat z agentem
- Agent mówi: "Zaczynamy od analizy Twoich kompetencji. Opowiedz mi o..."
- Pliki powstają "w tle"
- Klient może ignorować strukturę — lub zajrzeć gdy chce

**Kluczowe:** UX musi być prosty. Kompleksowość jest dla agenta, nie dla klienta.

#### "Wolę po prostu rozmawiać z ChatGPT"

**Odpowiedź:**
- Możesz — ale po tygodniu nie znajdziesz swoich ustaleń
- Możesz — ale będziesz wklejać te same informacje wielokrotnie
- Możesz — ale nie będziesz mieć dokumentacji procesu

**Pitch:** "To JEST rozmowa z AI. Tylko że ta rozmowa zostawia ślad — uporządkowaną dokumentację którą możesz pokazać zarządowi."

#### "Nie chcę instalować nowych narzędzi"

**Odpowiedź:**
- Zależy od implementacji
- Opcja 1: Cursor (wymaga instalacji, ale prosty)
- Opcja 2: Claude.ai z Projects (zero instalacji)
- Opcja 3: Google Drive + Gemini (jeśli klient jest w Google)

**Do przemyślenia:** Jaki jest "minimal viable interface" dla klienta?

#### "Co jeśli AI się pomyli?"

**Odpowiedź:**
- Dlatego są checkpointy — klient akceptuje deliverable przed przejściem dalej
- Dlatego artefakty — widać co agent "myśli", można skorygować
- To samo ryzyko jest w Gemach — tu przynajmniej jest transparentność

---

## Model współpracy

### Co robi kto

| Rudy | Ja |
|------|-----|
| Metodologia (proces, kryteria, pytania) | Infrastruktura (struktura, CLAUDE.md, prompty) |
| Wiedza strategiczna | Wiedza o context engineering |
| Relacja z klientem, sprzedaż | Budowa i utrzymanie workspace'u |
| Feedback z projektów | Iteracje na podstawie feedbacku |

### Faza 1: Budowa (razem)

**Czas:** 2-3 tygodnie

1. **Kick-off (2h):** Rudy opowiada proces, ja pytam o szczegóły
2. **Ja buduję v1:** Struktura, CLAUDE.md, instrukcje kroków
3. **Review (2h):** Rudy testuje, daje feedback
4. **Iteracja:** Poprawki, dopracowanie
5. **Pilot:** Rudy przeprowadza jeden projekt (ze mną w tle)
6. **Finalizacja:** Gotowy workspace

**Output:** Działający workspace który Rudy może dawać klientom.

### Faza 2: Sprzedaż (Rudy)

Rudy sprzedaje klientom:
- "AI-Powered Strategy Toolkit"
- "Narzędzie do samodzielnego przeprowadzenia procesu dywersyfikacji"
- Opcjonalnie: z konsultacjami Rudego (wsparcie przy kluczowych decyzjach)

### Faza 3: Utrzymanie i rozwój

| Rudy | Ja |
|------|-----|
| Zbiera feedback od klientów | Implementuję poprawki |
| Rozwija metodologię | Aktualizuję workspace |
| Identyfikuje nowe use cases | Buduję nowe moduły |

### Model finansowy (opcje)

**Opcja A: Jednorazowa budowa**
- Ja buduję workspace, Rudy płaci za projekt
- Rudy jest właścicielem, sprzedaje jak chce
- Maintenance: osobne zlecenia

**Opcja B: Revenue share**
- Buduję za mniejszą opłatę (lub free)
- Procent od każdej sprzedaży klientowi
- Motywacja do rozwoju produktu

**Opcja C: Licencja**
- Ja utrzymuję "silnik" (infrastrukturę)
- Rudy płaci miesięczną licencję
- Aktualizacje wliczone

---

## Strategia sprzedaży: Show, don't tell

### Insight

Ludziom (w tym Rudemu) trudno wyobrazić sobie wartość pracy z agentem. Dokumenty i argumenty nie wystarczą — trzeba **pokazać na żywym przykładzie**.

### Plan

```
1. Buduję prototyp workspace'u (proces dywersyfikacji)
2. Buduję porównawczego Gema (ten sam proces, porządnie zrobiony)
3. Pokazuję Rudemu oba — niech sam doświadczy różnicy
4. Rudy "kupuje" bo zobaczył, nie bo przeczytał
```

### Moja przewaga

- Z agentem mogę szybko vibe-codować prototyp
- Mogę szybko wchłonąć metodologię dywersyfikacji (agent pomaga)
- Koszt stworzenia demo = kilka godzin pracy
- Ryzyko = niskie, potencjał = wysoki

### Co pokazać w demo workspace'u

- Agent prowadzi przez Fazę 1 (VRIO)
- Artefakty powstają w folderze w czasie rzeczywistym
- Powrót do sesji po przerwie — agent pamięta kontekst
- Iteracja na artefakcie (chirurgiczna edycja, nie "od nowa")
- Agent robi research / generuje tabelę / wizualizację

### Co pokazać w demo Gema (dla kontrastu)

- Ten sam proces, porządnie zrobiony (fair comparison)
- Ale: kopiuj-wklej między krokami
- Ale: "wygeneruj od nowa" zamiast edycji fragmentu
- Ale: brak pamięci między sesjami
- Ale: trudność w znalezieniu wcześniejszych ustaleń

### Cel demo

Rudy sam mówi: "O, tu widzę różnicę. Tu muszę wklejać, a tu nie. Tu tracę kontekst, a tu agent pamięta."

---

## Następne kroki

1. **Zbudować prototyp workspace'u** — Faza 1 procesu dywersyfikacji
2. **Zbudować porównawczego Gema** — ten sam zakres
3. **Demo dla Rudego** — pokazać oba, zebrać reakcje
4. **Decyzja:** Czy idziemy dalej?
5. **Jeśli tak:** Pełna budowa + model współpracy

---

## Pytania otwarte

- [ ] Jaki interface dla klienta? (Cursor? Claude Projects? Google?)
- [ ] Ile Rudy chce być zaangażowany w onboarding klienta?
- [ ] Czy klient ma mieć dostęp do "bebechów" czy tylko do czatu?
- [ ] Jak wycenić dla klienta końcowego?
- [ ] Czy to jest "produkt" czy "usługa z narzędziem"?
