# Context Engineering jako Nić Przewodnia Kursu

Ćwiczenie intelektualne: jak ustrukturyzować kurs wokół jednego spójnego modelu mentalnego.

---

## Główna Teza

**Context engineering to nie "prompt engineering 2.0" — to architektura środowiska pracy agenta.**

Prompt engineering = co powiedzieć agentowi
Context engineering = co agent wie, widzi, pamięta, do czego ma dostęp

Uczestnik kursu powinien wyjść z myśleniem: *"Projektuję system informacyjny, nie piszę prompty."*

---

## Centralny Model: The Context Stack

Jeden diagram który wyjaśnia całą strukturę kursu:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│              CONTEXT WINDOW AGENTA                      │
│            (ograniczone "biurko")                       │
│                                                         │
│  ┌───────────────────────────────────────────────────┐  │
│  │  5. EXTERNAL        MCP, web, tools, bazy         │  │  ← Level 1
│  │     (dynamiczne)    Agent sięga gdy potrzebuje    │  │
│  ├───────────────────────────────────────────────────┤  │
│  │  4. REFERENCE       context/, examples/           │  │  ← Level 4
│  │     (on-demand)     Ładowane na żądanie           │  │
│  ├───────────────────────────────────────────────────┤  │
│  │  3. PROJECT         CLAUDE.md, struktura          │  │  ← Level 3
│  │     (persistent)    Ładowane NA STARCIE sesji     │  │
│  ├───────────────────────────────────────────────────┤  │
│  │  2. SESSION         Historia tej rozmowy          │  │  ← Level 2
│  │     (temporary)     Znika po zamknięciu           │  │
│  ├───────────────────────────────────────────────────┤  │
│  │  1. IMMEDIATE       Ta wiadomość, ten plik        │  │  ← Level 0
│  │     (now)           Co właśnie pokazujesz         │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
                         ↑
              "Context window" = wszystko
              co agent "widzi" w tej chwili

              Ma ograniczoną pojemność!
              (context rot, attention dilution)
```

**Kluczowy insight:** Każdy poziom kursu uczy zarządzać inną warstwą tego stacka.

---

## Cztery Akty Narracji

### Akt I: Zrozumienie Ograniczeń
**Poziomy 0-1 | "Agent nie jest magiczny"**

Uczestnik uczy się:
- Agent ma ograniczone "biurko" (context window)
- Nie "wie" — widzi tylko to, co mu pokażesz
- Więcej ≠ lepiej (context rot, pollution)

**Metafora:** Agent to bardzo zdolny pracownik z ADHD. Ma świetne umiejętności, ale ograniczoną pamięć roboczą. Nie pamiętka co mówiłeś 2h temu. Jeśli zaśmiecisz mu biurko, zgubi się.

**Problemy z researchu które tu adresujemy:**
- Context rot → dlatego sesje mają granice
- Attention dilution → dlatego nie ładujemy wszystkiego na raz
- Lost in the middle → dlatego ważne rzeczy na początku/końcu

---

### Akt II: Organizacja w Czasie
**Poziomy 2-3 | "Pamięć która przetrwa sesję"**

Uczestnik uczy się:
- Sesje się kończą, kontekst znika
- Ale możesz stworzyć persistent layer
- CLAUDE.md = instrukcja obsługi projektu
- Checkpointy = punkty synchronizacji z agentem

**Metafora:** Wyobraź sobie że pracujesz z asystentem który każdego ranka zapomina wszystko. Możesz:
1. Codziennie tłumaczyć od nowa (męczące)
2. Napisać mu "instrukcję obsługi siebie" którą czyta na starcie

CLAUDE.md to ta instrukcja. Checkpointy to notatki które asystent robi dla siebie na jutro.

**Strategie z researchu które tu stosujemy:**
- Context offloading → zapisuj do plików, nie trzymaj w głowie
- Scratchpad pattern → todo.md jako external attention anchor
- Compaction → CLAUDE.md krótki, esencja, nie wszystko

**Wizualizacja: Przepływ między sesjami**

```
    Sesja 1              Sesja 2              Sesja 3
    ┌─────┐              ┌─────┐              ┌─────┐
    │     │              │     │              │     │
    │ ... │              │ ... │              │ ... │
    │     │              │     │              │     │
    └──┬──┘              └──┬──┘              └──┬──┘
       │                    │                    │
       ▼                    ▼                    ▼
    ┌─────────────────────────────────────────────────┐
    │                  CLAUDE.md                       │
    │            (persistent context)                  │
    │                                                  │
    │  + artefakty (pliki, notatki, checkpointy)      │
    └─────────────────────────────────────────────────┘

    Agent "zapomina" rozmowę, ale "pamięta" projekt.
```

---

### Akt III: Skalowanie Systemu
**Poziomy 4-5 | "Właściwe informacje we właściwym momencie"**

Uczestnik uczy się:
- Nie wszystko musi być w CLAUDE.md (byłby za duży)
- Reference files = kontekst ładowany on-demand
- Skills = powtarzalne workflows jako "funkcje"

**Metafora:** CLAUDE.md to "co asystent musi wiedzieć zawsze". Reference files to "szuflady z dokumentami do których sięga gdy potrzebuje". Skills to "procedury które asystent zna i może uruchomić na żądanie".

```
                    CLAUDE.md
                   (zawsze w głowie)
                        │
         ┌──────────────┼──────────────┐
         │              │              │
         ▼              ▼              ▼
    ┌─────────┐   ┌─────────┐   ┌─────────┐
    │context/ │   │examples/│   │ skills/ │
    │         │   │         │   │         │
    │ brand   │   │ good/   │   │/research│
    │ voice   │   │ bad/    │   │/draft   │
    │ ...     │   │ ...     │   │/review  │
    └─────────┘   └─────────┘   └─────────┘
    (on-demand)   (on-demand)   (on-demand)
```

**Strategie z researchu:**
- Context retrieval → just-in-time loading
- Hierarchical memory → tiers of context (always-on vs on-demand)
- RAG patterns → agent sam decyduje co pobrać

---

### Akt IV: Delegowanie i Iteracja
**Poziomy 6-7 | "System który się uczy"**

Uczestnik uczy się:
- Subagenci = fresh context windows dla specjalistycznych zadań
- Feedback loop = systematyczne usprawnianie
- Autonomy slider przesuwa się w miarę budowania systemu

**Metafora:** Zamiast jednego asystenta który robi wszystko, masz zespół specjalistów. Każdy dostaje tylko to, co potrzebuje do swojego zadania. Główny asystent koordynuje, specjaliści wykonują.

```
                    ┌─────────────────┐
                    │   GŁÓWNY AGENT  │
                    │  (orchestrator) │
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
       ┌─────────┐      ┌─────────┐      ┌─────────┐
       │RESEARCH │      │ DRAFT   │      │ REVIEW  │
       │ AGENT   │      │ AGENT   │      │ AGENT   │
       │         │      │         │      │         │
       │ fresh   │      │ fresh   │      │ fresh   │
       │ context │      │ context │      │ context │
       └────┬────┘      └────┬────┘      └────┬────┘
            │                │                │
            └────────────────┼────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    WYNIK        │
                    │ (condensed      │
                    │  summary)       │
                    └─────────────────┘
```

**Strategie z researchu:**
- Context isolation → każdy subagent ma czysty kontekst
- Orchestrator-worker pattern → koordynacja przez głównego agenta
- Agent-as-tool → subagent jako funkcja, nie rozmówca

---

## Mapowanie: Problemy → Rozwiązania

| Problem (z researchu) | Gdzie się objawia | Rozwiązanie w kursie |
|-----------------------|-------------------|---------------------|
| **Context rot** | Długie sesje, degradacja jakości | Checkpointy, artefakty pośrednie (L2) |
| **Context pollution** | Za dużo irrelevantnych info | Minimalistyczny CLAUDE.md, on-demand files (L3-4) |
| **Context confusion** | Agent nie wie co jest instrukcją, co danymi | Jasna struktura, XML tags, sekcje (L3) |
| **Attention dilution** | Ważne info ginie w masie | Position-aware placement, reference files (L4) |
| **Lost in the middle** | Agent gubi środek długich kontekstów | Krótkie sesje, pliki jako pamięć (L2-3) |
| **Tool overload** | 100+ narzędzi → halucynacje | Hierarchical action space, skills (L5) |

---

## Kluczowe Reframes dla Uczestników

### Reframe 1: Od "prompt" do "system"
❌ "Jak napisać lepszy prompt?"
✅ "Jak zaprojektować środowisko w którym agent działa niezawodnie?"

### Reframe 2: Od "sesja" do "projekt"
❌ "Każda rozmowa zaczyna się od zera"
✅ "Projekt ma pamięć, sesje to tylko punkty interakcji"

### Reframe 3: Od "wszystko na raz" do "on-demand"
❌ "Załaduję agentowi wszystko co może być przydatne"
✅ "Dam mu dostęp do tego, co potrzebuje, gdy tego potrzebuje"

### Reframe 4: Od "jeden agent" do "zespół"
❌ "Agent ma wszystko zrozumieć i zrobić"
✅ "Główny agent koordynuje, specjaliści wykonują z czystym kontekstem"

### Reframe 5: Od "gotowe" do "iteracyjne"
❌ "Raz ustawię i działa"
✅ "Feedback loop: obserwuję, diagnozuję, naprawiam, testuję"

---

## Wizualna Synteza: The Journey

```
TWOJA PODRÓŻ PRZEZ KURS
═══════════════════════════════════════════════════════════════

Level 0-1                Level 2-3                Level 4-5                Level 6-7
ZROZUMIENIE              ORGANIZACJA              SKALOWANIE               DELEGOWANIE
    │                        │                        │                        │
    │                        │                        │                        │
    ▼                        ▼                        ▼                        ▼
┌─────────┐              ┌─────────┐              ┌─────────┐              ┌─────────┐
│   CO    │              │   JAK   │              │   KIEDY │              │   KTO   │
│  agent  │     ───►     │ pamięć  │     ───►     │  co     │     ───►     │  robi   │
│  widzi  │              │ między  │              │ ładować │              │   co    │
│         │              │ sesjami │              │         │              │         │
└─────────┘              └─────────┘              └─────────┘              └─────────┘
                                                                                │
                                                                                ▼
                                                                    ┌─────────────────┐
                                                                    │  FEEDBACK LOOP  │
                                                                    │  Obserwuj →     │
                                                                    │  Diagnozuj →    │
                                                                    │  Napraw →       │
                                                                    │  Testuj         │
                                                                    └─────────────────┘

═══════════════════════════════════════════════════════════════
        Autonomy Slider: ◀━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━▶
                         mniej                          więcej
                         kontroli                       delegacji
```

---

## Storytelling Arc

**Hook (Level 0):**
"LLM-y halucynują. Ale to nie ich wina — to twoja. Bo nie dałeś im właściwego kontekstu."

**Rising Action (Level 1-3):**
"Twoja praca to context engineering — organizowanie wiedzy tak, żeby agent działał niezawodnie. Zaczynasz od rozumienia co agent widzi, potem budujesz pamięć projektu."

**Midpoint Revelation (Level 4):**
"Odkrywasz że nie wszystko musi być w głowie agenta zawsze. Projektujesz system gdzie właściwe informacje pojawiają się we właściwym momencie."

**Climax (Level 5-6):**
"Gdy system działa, możesz delegować więcej. Skills jako powtarzalne workflows. Subagenci jako specjaliści z czystym kontekstem."

**Resolution (Level 7):**
"To nie jest jednorazowa konfiguracja. To feedback loop — ciągłe obserwowanie, diagnozowanie i usprawnianie. Twój system się uczy razem z tobą."

---

## Takeaways dla Uczestnika

Po kursie uczestnik powinien umieć odpowiedzieć na pytania:

1. **Co agent widzi w tej chwili?** (Context Stack)
2. **Co będzie pamiętał jutro?** (CLAUDE.md, artefakty)
3. **Jak skalować gdy projekty rosną?** (Reference files, on-demand)
4. **Kiedy delegować do subagenta?** (Context isolation)
5. **Jak systematycznie usprawniać?** (Feedback loop)

I powinien myśleć w kategoriach:

*"Projektuję architekturę informacyjną, nie piszę prompty."*

---

## Meta: Dlaczego Ta Narracja Działa

1. **Jeden centralny model** (Context Stack) który można wizualizować i do którego można wracać

2. **Progresja od prostego do złożonego** — każdy level buduje na poprzednim

3. **Praktyczne metafory** — "biurko agenta", "instrukcja obsługi", "zespół specjalistów"

4. **Połączenie z badaniami** — terminologia z researchu (context rot, isolation, offloading) jako uzasadnienie praktyk

5. **Clear reframes** — konkretne przesunięcia mentalne do zapamiętania

6. **Story arc** — hook, rising action, climax, resolution
