# AI Workspace Build — Deliverables

Co konkretnie dostarczamy klientowi po zakończeniu wdrożenia.

---

## 1. Struktura workspace'u

### Zorganizowany filesystem

```
client-workspace/
├── CLAUDE.md                    # Główny context file
├── context/
│   ├── domain/                  # Wiedza domenowa
│   │   ├── glossary.md          # Terminologia specjalistyczna
│   │   ├── concepts.md          # Kluczowe koncepcje
│   │   └── references.md        # Ważne źródła/linki
│   ├── workflows/               # Opisy procesów
│   │   ├── workflow-X.md
│   │   └── workflow-Y.md
│   └── examples/                # Przykłady dobrej pracy
│       ├── good-artifact-1.md
│       └── good-artifact-2.md
├── templates/                   # Szablony artefaktów
│   ├── artifact-type-A.md
│   ├── artifact-type-B.md
│   └── ...
├── skills/                      # Zdefiniowane skille agenta
│   ├── skill-research.md
│   ├── skill-analysis.md
│   └── ...
├── projects/                    # Aktywne projekty
│   └── [nazwa-projektu]/
│       ├── brief.md
│       ├── notes.md
│       └── artifacts/
└── archive/                     # Zakończone projekty
```

### Naming conventions

Dokument definiujący jak nazywać pliki i foldery dla spójności i łatwego znajdowania.

---

## 2. CLAUDE.md (Context File)

Główny plik kontekstowy dla agenta. Zawiera:

### Sekcja: Kim jestem / co robię
```markdown
## O mnie
- Kim jest użytkownik
- W jakiej domenie pracuje
- Jakie są główne typy zadań
```

### Sekcja: Terminologia
```markdown
## Terminologia
Agent rozumie bez wyjaśniania:
- [Termin 1] — definicja
- [Termin 2] — definicja
- ...
```

### Sekcja: Preferencje pracy
```markdown
## Jak pracujemy
- Preferowany język (PL/EN)
- Styl komunikacji
- Formatowanie outputów
- Co agent powinien/nie powinien robić
```

### Sekcja: Workflow'y
```markdown
## Typowe workflow'y
Kiedy użytkownik mówi "zrób X", wykonaj kroki:
1. ...
2. ...
```

### Sekcja: Artefakty
```markdown
## Artefakty
Tworzymy następujące typy dokumentów:
- [Typ A] — zobacz template: templates/artifact-A.md
- [Typ B] — zobacz template: templates/artifact-B.md
```

---

## 3. Glosariusz domenowy

Plik `context/domain/glossary.md` z terminologią specjalistyczną.

| Termin | Definicja | Kontekst użycia |
|--------|-----------|-----------------|
| [Term] | [Co znaczy] | [Kiedy/jak używamy] |

Cel: Agent nie pyta o podstawowe pojęcia z domeny klienta.

---

## 4. Template'y artefaktów

Dla każdego typu dokumentu który klient regularnie tworzy:

### Struktura template'a
```markdown
# [Nazwa typu artefaktu]

## Cel
Co ten dokument ma osiągnąć.

## Struktura
### Sekcja 1: [Nazwa]
[Opis co tu idzie]

### Sekcja 2: [Nazwa]
[Opis co tu idzie]

## Instrukcje dla agenta
- Jak wypełniać poszczególne sekcje
- Jakie źródła wykorzystać
- Na co uważać
- Czego unikać

## Przykład
[Link do example/good-artifact-X.md]
```

### Typowe template'y (zależne od domeny)

**Lekarz-badacz:**
- Literature extraction form
- Table 1 (demographic characteristics)
- Statistical analysis report
- Paper draft (Introduction, Methods, Results, Discussion)

**Prawnik:**
- Opinia prawna
- Due diligence checklist
- Umowa (różne typy)
- Pismo procesowe

**Konsultant:**
- Brief projektu
- Analiza rynku
- Rekomendacje
- Prezentacja dla klienta

---

## 5. Skille (Reusable Workflows)

Zdefiniowane, powtarzalne przepływy pracy. Format:

```markdown
# Skill: [Nazwa]

## Trigger
Kiedy użytkownik mówi: "..."

## Input
Czego skill potrzebuje:
- [Input 1]
- [Input 2]

## Kroki
1. [Krok 1]
2. [Krok 2]
3. [Krok 3]

## Output
Co skill produkuje:
- [Artefakt]
- [Format]

## Przykład użycia
[Konkretny przykład]
```

### Typowe skille

| Skill | Opis |
|-------|------|
| `/literature-search` | Zbuduj search strategy dla [temat] |
| `/extract-paper` | Wyciągnij kluczowe info z PDF |
| `/draft-section` | Napisz draft sekcji [nazwa] |
| `/table1` | Wygeneruj Table 1 z danych |
| `/analyze` | Przeprowadź analizę [typ] |

---

## 6. Slash Commands

Skróty do częstych operacji. Zdefiniowane w sposób natywny dla narzędzia (Cursor, Claude Code).

```
/research [temat]     → uruchom skill research
/draft [sekcja]       → napisz draft sekcji
/review [plik]        → przejrzyj i zasugeruj poprawki
/format [standard]    → sformatuj według standardu
/summarize            → podsumuj bieżący kontekst
```

---

## 7. Przykłady (Examples Library)

Folder `context/examples/` z przykładami dobrej pracy:
- Wzorcowe artefakty
- Dobre outputy z poprzednich sesji
- Reference implementations

Agent może się do nich odwoływać jako do wzorców.

---

## 8. Dokumentacja utrzymania

### Maintenance Guide
```markdown
# Jak utrzymywać workspace

## Codziennie
- [Co robić po każdej sesji]

## Tygodniowo
- [Przegląd i aktualizacja]

## Miesięcznie
- [Głębszy przegląd]

## Kiedy dodajesz nowy typ pracy
- [Jak rozszerzyć system]
```

### Troubleshooting
- Co robić gdy agent "zapomina" kontekst
- Jak debugować problemy
- Kiedy aktualizować CLAUDE.md

---

## 9. Sesja handoff

Na zakończenie wdrożenia:
- Walkthrough całego workspace'u z klientem
- Test kilku typowych zadań
- Q&A
- Plan na pierwsze 2 tygodnie samodzielnej pracy

---

## Podsumowanie deliverables

| Deliverable | Format | Cel |
|-------------|--------|-----|
| Struktura workspace'u | Foldery + pliki | Organizacja |
| CLAUDE.md | Markdown | Główny kontekst |
| Glosariusz | Markdown table | Terminologia |
| Template'y artefaktów | Markdown | Standaryzacja |
| Skille | Markdown | Reusable workflows |
| Slash commands | Native do narzędzia | Szybki dostęp |
| Przykłady | Markdown/PDF | Wzorce jakości |
| Maintenance guide | Markdown | Samodzielność |
| Sesja handoff | Spotkanie | Transfer wiedzy |
