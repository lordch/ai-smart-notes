# Koncepcja: Uniwersalny Agent do Procesu Dywersyfikacji

*Odpowiedź na pytanie Rudy'ego: "Czy da się zrobić uniwersalnego agenta działającego dobrze z taką logiką?"*

---

## Wizja

Jedno repozytorium, które:
1. **Zawiera instrukcje** — jak prowadzić cały proces i każdy jego etap
2. **Gromadzi artefakty** — outputy każdego kroku zostają jako pliki, dostępne w kolejnych krokach
3. **Pamięta kontekst** — agent w każdej sesji "wie" co już ustaliliśmy, bez konieczności wklejania

Klient (lub konsultant) klonuje repozytorium, odpala agenta, i jest prowadzony przez proces krok po kroku.

---

## Struktura repozytorium

```
dywersyfikacja-projekt/
│
├── CLAUDE.md                          # Główne instrukcje dla agenta
│
├── proces/                            # Instrukcje procesu (read-only, nie edytowane podczas projektu)
│   ├── 00-overview.md                 # Przegląd całego procesu, mapa zależności
│   ├── 01-ewaluacja-zasobow.md        # Instrukcja Kroku 1
│   ├── 02-analiza-eksploracyjna.md    # Instrukcja Kroku 2
│   ├── 03-wycena-selekcja.md          # Instrukcja Kroku 3
│   ├── 04-budowa-scenariuszy.md       # Instrukcja Kroku 4
│   ├── 05-business-case.md            # Instrukcja Kroku 5
│   ├── 06-wybor-plan.md               # Instrukcja Kroku 6-7
│   └── templates/                     # Szablony deliverables
│       ├── raport-core-competencies.md
│       ├── short-list-rynkow.md
│       ├── teczka-projektowa.md
│       └── roadmap.md
│
├── kontekst/                          # Wiedza o kliencie (wypełniana na starcie)
│   ├── firma.md                       # Podstawowe info o firmie
│   ├── branza.md                      # Kontekst branżowy
│   └── dokumentacja/                  # Materiały źródłowe od klienta
│       └── (pliki od klienta)
│
├── praca/                             # Tu powstają artefakty projektu
│   ├── faza-1-diagnoza/
│   │   ├── notatki-warsztaty.md
│   │   ├── kompetencje-twarde.md
│   │   ├── kompetencje-miekkie.md
│   │   ├── analiza-vrio.md
│   │   └── DELIVERABLE-core-competencies.md
│   │
│   ├── faza-2-eksploracja/
│   │   ├── adjacency-produktowa.md
│   │   ├── adjacency-kliencka.md
│   │   ├── trendy-research.md
│   │   ├── long-list.md
│   │   ├── tam-sam-som/
│   │   │   ├── branza-a.md
│   │   │   ├── branza-b.md
│   │   │   └── ...
│   │   ├── analiza-porter/
│   │   │   └── ...
│   │   └── DELIVERABLE-short-list.md
│   │
│   ├── faza-3-strategia/
│   │   ├── scenariusz-a.md
│   │   ├── scenariusz-b.md
│   │   ├── scenariusz-c.md
│   │   ├── pre-mortem.md
│   │   ├── financials.md
│   │   └── DELIVERABLE-teczki-projektowe.md
│   │
│   └── faza-4-egzekucja/
│       ├── decyzja.md
│       └── DELIVERABLE-roadmap.md
│
└── log/                               # Historia sesji (opcjonalne)
    ├── 2026-01-20-kickoff.md
    ├── 2026-01-27-warsztat-inzynieria.md
    └── ...
```

---

## CLAUDE.md — instrukcje dla agenta

```markdown
# Agent Dywersyfikacji Strategicznej

## Twoja rola

Jesteś agentem prowadzącym proces dywersyfikacji strategicznej. 
Pomagasz firmie zidentyfikować nowe rynki i zbudować plan wejścia.

## Jak pracujesz

1. **Zawsze zaczynaj od orientacji:**
   - Przeczytaj `kontekst/firma.md` i `kontekst/branza.md`
   - Sprawdź stan projektu w `praca/` — co już zostało zrobione?
   - Określ który krok jest aktualny

2. **Przed każdym krokiem:**
   - Przeczytaj instrukcję kroku z `proces/0X-nazwa.md`
   - Przeczytaj deliverables z poprzednich kroków (pliki DELIVERABLE-*.md)
   - Upewnij się że masz potrzebny kontekst

3. **Podczas pracy:**
   - Zapisuj ustalenia do odpowiednich plików w `praca/`
   - Nie trzymaj wiedzy "w głowie" — wszystko co ważne idzie do pliku
   - Gdy kończysz etap → stwórz DELIVERABLE

4. **Checkpointy:**
   - Po każdym kroku zatrzymaj się i zapytaj o akceptację
   - Nie przechodź dalej bez potwierdzenia

## Komendy

- `/status` — pokaż gdzie jesteśmy w procesie
- `/krok [N]` — rozpocznij/kontynuuj krok N
- `/podsumuj` — podsumuj dotychczasowe ustalenia
- `/deliverable [nazwa]` — wygeneruj deliverable na podstawie dotychczasowej pracy

## Ważne

- NIE generuj analiz "z głowy" — bazuj na danych od klienta
- Gdy brakuje informacji — PYTAJ, nie zgaduj
- Zapisuj wszystko do plików — następna sesja może być za tydzień
```

---

## Przykładowa instrukcja kroku (proces/01-ewaluacja-zasobow.md)

```markdown
# Krok 1: Ewaluacja Zasobów (Audyt Strategiczny)

## Cel

Oddzielenie tego, co nam się wydaje, od tego, w czym obiektywnie jesteśmy wybitni.

## Wymagane inputy

- `kontekst/firma.md` — podstawowe info
- `kontekst/dokumentacja/` — materiały od klienta (jeśli są)
- Rozmowa z klientem / notatki z warsztatów

## Zadania

### 1. Katalogowanie kompetencji twardych

Zapisz do `praca/faza-1-diagnoza/kompetencje-twarde.md`:
- Technologie (spawanie, hydraulika, elektronika...)
- Certyfikaty i uprawnienia
- Unikalne procesy produkcyjne
- Patenty, know-how

**Pytania pomocnicze:**
- Co potrafimy zrobić, czego konkurencja nie zrobi taniej i lepiej?
- Za co klienci nas chwalą?
- Co robiliśmy w projektach które "wyszły ponad normę"?

### 2. Katalogowanie kompetencji miękkich/procesowych

Zapisz do `praca/faza-1-diagnoza/kompetencje-miekkie.md`:
- Serwis (czas reakcji, zasięg geograficzny)
- Logistyka (wielkogabaryty, trudny teren)
- Relacje (z kim mamy unikalne kontakty)
- Elastyczność (customizacja, małe serie)

### 3. Analiza VRIO

Dla każdej kompetencji przeprowadź test VRIO.
Zapisz do `praca/faza-1-diagnoza/analiza-vrio.md`:

| Kompetencja | Valuable? | Rare? | Inimitable? | Organized? | Wynik |
|-------------|-----------|-------|-------------|------------|-------|
| ...         | ...       | ...   | ...         | ...        | ...   |

**Kryteria:**
- **Valuable:** Czy klienci za to płacą? Czy daje przewagę?
- **Rare:** Czy konkurenci też to mają?
- **Inimitable:** Czy łatwo to skopiować?
- **Organized:** Czy potrafimy to wykorzystywać systematycznie?

Kompetencje które mają 4x TAK → to są nasze "supermoce".

## Deliverable

Stwórz `praca/faza-1-diagnoza/DELIVERABLE-core-competencies.md`:
- Lista 3-5 unikalnych "supermocy" firmy
- Dla każdej: krótki opis, dowody, potencjał transferu do innych branż

## Checkpoint

Przed przejściem do Kroku 2:
- [ ] Klient zaakceptował listę kompetencji
- [ ] Mamy konkretne przykłady/dowody dla każdej supermocy
- [ ] Wiemy które kompetencje są "transferowalne" do innych kontekstów
```

---

## Jak to działa w praktyce — przykładowa sesja

**Sesja 1: Kickoff**

```
Użytkownik: Zaczynamy projekt dywersyfikacji dla firmy MIFAMA (sprzęt górniczy).

Agent: Rozumiem. Zaczynam od orientacji.
       
       Widzę że `kontekst/firma.md` jest pusty. Potrzebuję podstawowych informacji:
       - Czym dokładnie zajmuje się MIFAMA?
       - Jakie produkty/usługi oferujecie?
       - Jaka jest skala działalności (obroty, zatrudnienie)?
       - Kim są główni klienci?
       
       Możesz mi to opowiedzieć lub wrzucić dokumenty do `kontekst/dokumentacja/`.

Użytkownik: [opowiada o firmie]

Agent: Zapisuję do `kontekst/firma.md`. 
       
       Według procesu, zaczynamy od Kroku 1: Ewaluacja Zasobów.
       Przeczytałem instrukcję w `proces/01-ewaluacja-zasobow.md`.
       
       Mamy dwie opcje:
       A) Przeprowadzam "wywiad" z tobą teraz — pytam o kompetencje
       B) Organizujecie warsztat z inżynierami, a ja pomogę uporządkować notatki
       
       Co wolisz?
```

**Sesja 2: Kontynuacja (tydzień później)**

```
Użytkownik: Wracamy do projektu MIFAMA.

Agent: Sprawdzam stan projektu...
       
       📍 Status:
       - Faza 1 (Diagnoza): W TRAKCIE
         - ✅ kontekst/firma.md — wypełnione
         - ✅ kompetencje-twarde.md — draft jest
         - ⏳ kompetencje-miekkie.md — pusty
         - ⏳ analiza-vrio.md — nie zaczęte
         - ⏳ DELIVERABLE — nie zaczęte
       
       Wygląda na to, że mamy draft kompetencji twardych. 
       Chcesz go przejrzeć/uzupełnić, czy idziemy do kompetencji miękkich?
```

**Sesja 5: Przejście między fazami**

```
Agent: Deliverable Fazy 1 jest gotowy: `DELIVERABLE-core-competencies.md`
       
       Zidentyfikowaliśmy 4 supermoce MIFAMA:
       1. Spawanie stali trudnościeralnych (Hardox, XAR)
       2. Systemy ATEX (certyfikacja przeciwwybuchowa)
       3. Serwis 24h w trudnym terenie
       4. Projektowanie "pod klienta" (małe serie)
       
       Przed przejściem do Fazy 2 (Eksploracja) potrzebuję potwierdzenia:
       - Czy ta lista jest kompletna?
       - Czy zgadzasz się z priorytetyzacją?
       
       Dopiero po akceptacji przechodzimy dalej.
```

---

## Różnica vs Gems

| Aspekt | Model Gems | Model Agent + Artefakty |
|--------|------------|-------------------------|
| **Pamięć między krokami** | Brak — człowiek przenosi kontekst | Automatyczna — agent czyta poprzednie pliki |
| **Pamięć między sesjami** | Brak — zaczynasz od zera | Pełna — pliki zostają |
| **Deliverables** | Gdzieś w Google Docs | W repozytorium, wersjonowane |
| **Powrót do wcześniejszych kroków** | Ręczne wklejanie kontekstu | Agent sam czyta co potrzebuje |
| **Audytowalność** | Trudna (co było inputem Gema?) | Pełna (git history) |
| **Reużywalność dla innego klienta** | Kopiuj-wklej promptów | Sklonuj repo, zacznij od nowa |

---

## Warianty użycia

### Wariant A: Konsultant jako operator

Rudy prowadzi proces, używa agenta jako "asystenta analitycznego". Klient uczestniczy w warsztatach, ale nie dotyka repozytorium.

**Zalety:** Kontrola jakości, nie wymaga szkolenia klienta
**Wady:** Skalowanie = więcej czasu Rudy'ego

### Wariant B: Klient jako operator (z wsparciem)

Klient dostaje repozytorium i instrukcję. Rudy jest dostępny na konsultacje gdy utknął.

**Zalety:** Skalowalność, klient buduje własne kompetencje
**Wady:** Wymaga minimalnej technicznej biegłości klienta

### Wariant C: Hybrid

- Faza 1 (Diagnoza): Warsztaty z Rudym, agent jako narzędzie
- Faza 2-3 (Eksploracja, Strategia): Klient pracuje sam z agentem, Rudy review'uje deliverables
- Faza 4 (Egzekucja): Wspólna sesja podsumowująca

---

## Co trzeba zbudować

1. **Instrukcje procesu** (`proces/*.md`) — już masz draft w mailu, trzeba rozpisać szczegółowo
2. **Szablony deliverables** — jak ma wyglądać "Raport Core Competencies"
3. **CLAUDE.md** — instrukcje dla agenta
4. **Przykładowy projekt** — jeden przejechany case jako demo

**Estimate:** 2-3 dni pracy na MVP, które można testować z pierwszym klientem.

---

## Pytania otwarte

1. **Kto jest target user?** Czy zakładamy że klient umie obsłużyć Claude Code / Cursor? Czy potrzebny jest prostszy interfejs?

2. **Jak dostarczamy kontekst branżowy?** Czy agent ma szukać w internecie, czy klient musi dostarczyć raporty?

3. **Jak wygląda pricing?** Czy to jest "produkt" (klient kupuje dostęp do repo) czy "usługa" (Rudy prowadzi proces używając tego narzędzia)?

4. **Czy to jest open source / template?** Czy każdy może wziąć i użyć, czy to jest proprietary metodologia GrowGo?
