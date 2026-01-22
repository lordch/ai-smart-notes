# AI Workspace Build

type:: [[Offer]]
status:: Draft
date-created:: 2026-01-19
related:: [[Context Engineering Skill Development Program]], [[Workflow Implementation Sprints]], [[Strategy - AI Consultancy for Polish SME Knowledge Work]]

---

## Esencja

**Przychodzę do firmy (lub osoby) i buduję im kompletne środowisko do pracy z AI.**

Nie uczę zasad (to szkolenia). Nie wdrażam jednego workflow'u (to sprint). **Buduję całą infrastrukturę kontekstową** — od organizacji wiedzy, przez template'y artefaktów, po gotowe skille i komendy.

Klient wychodzi z wdrożenia z:
- Zorganizowanym workspace'em
- Udokumentowaną wiedzą domenową
- Gotowymi template'ami do codziennej pracy
- Działającymi agentami którzy "rozumieją" ich kontekst
- Umiejętnością utrzymania i rozwijania tego systemu

---

## Pozycjonowanie

| Szkolenia | Workflow Sprints | **Workspace Build** |
|-----------|------------------|---------------------|
| Uczą zasad | Wdrażają jeden proces | Budują całe środowisko |
| Abstrakcyjne | Konkretne ale wąskie | Konkretne i szerokie |
| Wiedza w głowach | Jeden workflow działa | System który skaluje się |
| "Wiem jak" | "Mam jeden działający flow" | "Mam infrastrukturę" |

**Szkolenia** → uczestnik wie CO robić, ale musi sam zbudować
**Workflow Sprint** → ma jeden działający kawałek
**Workspace Build** → ma fundament na którym buduje dalej

---

## Kto jest klientem

### Profil idealny

**Solo knowledge worker / mały zespół (1-10 osób)** który:
- Robi złożoną pracę intelektualną (badania, analizy, tworzenie dokumentów)
- Ma powtarzalne typy zadań i artefaktów
- Gromadzi specjalistyczną wiedzę domenową
- Chce używać AI, ale nie wie jak zorganizować
- Ma czas na współpracę przy wdrożeniu (to nie "zrobimy za was")

### Przykłady klientów

| Klient | Domena | Typowe artefakty |
|--------|--------|------------------|
| Lekarz-badacz | Badania kliniczne | Literature review, Table 1, wykresy statystyczne, drafty paperów |
| Prawnik | Prawo korporacyjne | Opinie prawne, due diligence, umowy, pisma procesowe |
| Konsultant strategiczny | Strategia biznesowa | Analizy rynku, rekomendacje, prezentacje |
| Analityk finansowy | M&A / wyceny | Modele finansowe, raporty, memoranda |
| Researcher UX | Product discovery | Interview notes, synthesis, persony, journey maps |

### Antyprofil (kiedy NIE)

- Potrzebują "zrobienia za nich" (chcą outsource, nie capability building)
- Brak czasu na współpracę (3-5 godzin/tydzień przez wdrożenie)
- Oczekują magii ("AI wszystko zrobi samo")
- Zbyt duża organizacja (>50 osób = inne wyzwania)

---

## Co dostarczamy

### 1. Struktura workspace'u

```
client-workspace/
├── CLAUDE.md                    # Główny context file
├── context/
│   ├── domain/                  # Wiedza domenowa
│   │   ├── glossary.md          # Terminologia specjalistyczna
│   │   ├── concepts.md          # Kluczowe koncepcje
│   │   └── references.md        # Ważne źródła/linki
│   ├── workflows/               # Opisy procesów
│   │   └── workflow-X.md
│   └── examples/                # Przykłady dobrej pracy
│       └── good-artifact-1.md
├── templates/                   # Szablony artefaktów
│   ├── artifact-type-A.md
│   └── artifact-type-B.md
├── skills/                      # Zdefiniowane skille agenta
│   ├── skill-research.md
│   └── skill-analysis.md
├── projects/                    # Aktywne projekty
│   └── [nazwa-projektu]/
└── archive/                     # Zakończone projekty
```

### 2. CLAUDE.md (Context File)

Główny plik kontekstowy dla agenta:
- **Kim jestem / co robię** — profil użytkownika
- **Terminologia** — glosariusz domenowy
- **Preferencje pracy** — język, styl, formatowanie
- **Workflow'y** — co robić gdy użytkownik mówi "X"
- **Artefakty** — linki do template'ów

### 3. Glosariusz domenowy

Plik z terminologią specjalistyczną. Agent nie pyta o podstawowe pojęcia z domeny klienta.

### 4. Template'y artefaktów

Szablony dla każdego typu dokumentu który klient regularnie tworzy:
- Struktura
- Cel
- Instrukcje dla agenta
- Przykład

### 5. Skille (Reusable Workflows)

Zdefiniowane, powtarzalne przepływy pracy:
- Trigger (kiedy uruchamiać)
- Input (czego potrzebuje)
- Kroki
- Output

### 6. Slash Commands

Skróty do częstych operacji:
```
/research [temat]     → uruchom skill research
/draft [sekcja]       → napisz draft sekcji
/review [plik]        → przejrzyj i zasugeruj poprawki
```

### 7. Przykłady (Examples Library)

Wzorcowe artefakty jako reference dla agenta.

### 8. Dokumentacja utrzymania

Maintenance Guide + Troubleshooting — klient wie jak utrzymywać i rozwijać system.

### 9. Sesja handoff

Walkthrough + test + Q&A + plan na start.

---

## Metodologia

```
Week 0          Week 1-2        Week 3-4        Week 5-6
[Discovery] → [Build Core] → [Build Details] → [Handoff]
   ↓              ↓               ↓               ↓
Zrozumienie    CLAUDE.md      Templates      Transfer
kontekstu      Struktura      Skille         Maintenance
               Glosariusz     Commands       Support
```

### Faza 0: Discovery (Tydzień 0)
- Spotkanie kickoff (2h)
- Zbieranie materiałów od klienta
- Analiza, mapowanie, plan wdrożenia

**Output:** Brief Discovery, Mapa artefaktów, Mapa workflow'ów, Plan

### Faza 1: Build Core (Tygodnie 1-2)
- Sesja 1: Struktura folderów (2h)
- Async: CLAUDE.md v1
- Sesja 2: Review + Glosariusz (2h)

**Output:** Workspace ze strukturą, CLAUDE.md v1, Glosariusz v1

### Faza 2: Build Details (Tygodnie 3-4)
- Sesja 3: Templates (2h)
- Async: Dopracowanie template'ów
- Sesja 4: Skille + Commands (2h)

**Output:** 3-5 template'ów, 3-5 skilli, Slash commands, Przykłady

### Faza 3: Handoff (Tygodnie 5-6)
- Sesja 5: Full walkthrough (2h)
- Async: Dokumentacja
- Sesja 6: Q&A + Zamknięcie (1h)
- Follow-up check-iny (opcjonalne)

**Output:** Kompletny workspace, Maintenance Guide, Transfer wiedzy

### Podsumowanie czasu

| Faza | Klient | Ja | 
|------|--------|-----|
| Discovery | 3-4h | 6-8h |
| Build Core | 4-5h | 10-12h |
| Build Details | 4-5h | 12-15h |
| Handoff | 3-4h | 6-8h |
| **RAZEM** | **15-18h** | **35-43h** |

---

## Pricing

### Pakiet SOLO

**Dla:** Pojedynczy knowledge worker

**Zakres:** Discovery + Build Core + Build Details + Handoff
- Struktura + CLAUDE.md + glosariusz
- 3 template'y + 3 skille + commands
- Maintenance guide

**Czas:** 4-5 tygodni | **Klient:** ~15h | **Ja:** ~35h

**Cena:** 6,000 - 9,000 PLN

---

### Pakiet TEAM

**Dla:** Mały zespół (2-5 osób)

**Zakres:** Wszystko z SOLO +
- Więcej template'ów (5-7) i skilli (5-7)
- Shared context files
- 2h training session
- 2 follow-up check-iny

**Czas:** 6-8 tygodni | **Zespół:** ~25h | **Ja:** ~55h

**Cena:** 12,000 - 18,000 PLN

---

### Pakiet FOUNDATION (Light)

**Dla:** Techniczni użytkownicy którzy chcą tylko fundament

**Zakres:** Discovery + Build Core only
- Struktura + CLAUDE.md + glosariusz
- 1h handoff

**Czas:** 2-3 tygodnie | **Klient:** ~8h | **Ja:** ~18h

**Cena:** 3,500 - 5,000 PLN

---

### Dodatki (à la carte)

| Dodatek | Cena |
|---------|------|
| Dodatkowy template | 500-800 PLN |
| Dodatkowy skill | 600-900 PLN |
| Training session (2h) | 1,500 PLN |
| Monthly check-in (3 mies.) | 1,200 PLN |
| Custom connector | Wycena indywidualna |

---

## Value proposition

> "Za 4-6 tygodni będziesz miał workspace, w którym AI rozumie Twój kontekst, zna Twoje artefakty i potrafi Ci efektywnie pomagać. Nie będziesz zaczynał każdej sesji od zera."

| Problem teraz | Po wdrożeniu |
|---------------|--------------|
| Każda sesja z AI od zera | Agent zna kontekst projektu/firmy |
| Wiedza w głowie | Wiedza w plikach, dostępna dla agenta |
| "Jak to zrobić?" przy każdym zadaniu | Template'y + instrukcje gotowe |
| Rozproszone notatki i dokumenty | Zorganizowany workspace |
| AI nie rozumie mojej domeny | CLAUDE.md z terminologią i kontekstem |
| Powtarzam te same prompty | Slash commands i skille |

---

## Przykład: Lekarz-badacz (Dagny)

### Profil
- Doktor nauk medycznych, specjalizacja HIV/AIDS
- Robi badania retrospektywne na danych szpitalnych
- Główne bóle: lit review (20h), statystyka outsourcowana, brak iteracji

### Co by dostała

**Struktura:**
```
dagny-research/
├── CLAUDE.md
├── context/domain/glossary.md    # HIV, CD4, ART, choroby oportunistyczne
├── templates/
│   ├── paper-extraction-form.md
│   ├── table1-template.md
│   └── statistical-report.md
├── skills/
│   ├── literature-search.md
│   ├── generate-table1.md
│   └── statistical-analysis.md
└── projects/
```

**Skille:**
- `/search [temat]` → search strategy do PubMed
- `/extract [pdf]` → ekstrakcja z paperu
- `/table1 [excel]` → Table 1 z danych
- `/km [excel]` → Kaplan-Meier

**ROI:**
- Oszczędność: ~120h/rok
- Wartość: ~24,000 PLN/rok
- Cena wdrożenia: 6,000-9,000 PLN
- Zwrot: 3-5 miesięcy

---

## Powiązania z innymi ofertami

```
[Audit] → identyfikujemy gdzie jest wartość
    ↓
[Workspace Build] → budujemy infrastrukturę  ← TO
    ↓
[Workflow Sprints] → wdrażamy konkretne workflow'y na infrastrukturze
    ↓
[Training] → skalujemy umiejętności na zespół
    ↓
[Advisory] → ongoing support i rozwój
```

---

## Dlaczego my?

1. **Praktyka, nie teoria** — sami pracujemy w ten sposób, codziennie
2. **Framework, nie narzędzie** — metodologia działa z Cursor, Claude Code, Windsurf...
3. **Hands-on** — nie piszemy raportu i odchodzimy; budujemy razem z klientem
4. **Transfer wiedzy** — klient wychodzi umiejąc utrzymywać i rozwijać system

---

## Gwarancje

1. **Działający workspace** — testuję na realnych zadaniach klienta
2. **Dokumentacja** — wszystko opisane, klient może kontynuować sam
3. **Follow-up support** — 2 check-iny wliczone w SOLO/TEAM

---

## Kiedy Workspace Build vs inne oferty

| Sytuacja | Rekomendacja |
|----------|--------------|
| "Chcę zorganizować całą moją pracę z AI" | **Workspace Build** ✓ |
| "Chcę zoptymalizować jeden konkretny proces" | Workflow Sprint |
| "Chcę przeszkolić zespół w zasadach" | Szkolenia |
| "Nie wiem od czego zacząć" | Audit → potem Build |

---

## Szczegółowa dokumentacja

Rozszerzone materiały w:
- [[tasks/2026-01-19-ai-workspace-offer/deliverables.md]] — pełna lista deliverables
- [[tasks/2026-01-19-ai-workspace-offer/methodology.md]] — szczegóły metodologii
- [[tasks/2026-01-19-ai-workspace-offer/dagny-case-study.md]] — pełny case study
- [[tasks/2026-01-19-ai-workspace-offer/pricing.md]] — rozbudowany pricing
