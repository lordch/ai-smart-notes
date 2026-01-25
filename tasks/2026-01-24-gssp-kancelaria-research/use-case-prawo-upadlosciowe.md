# Use Case: Human-Agent Collaboration w Prawie Upadłościowym

**Kontekst:** Kancelaria GSSP (Anna Sobańska - Kierownik Działu Postępowań Upadłościowych)
**Data:** 2026-01-24

---

## Kluczowa koncepcja

**Nie budujemy autonomicznych botów ani automatyzacji.**

Budujemy **workspace**, w którym adwokat pracuje z agentem AI (Claude Code lub podobnym) - interaktywnie, w czasie rzeczywistym. Agent zna kontekst kancelarii, terminologię, workflow'y i template'y. Adwokat steruje, agent wykonuje.

---

## Dlaczego prawo upadłościowe to dobry case?

| Cecha praktyki upadłościowej | Implikacja dla workspace'u |
|------------------------------|---------------------------|
| **Wysoki wolumen** (100+ spraw) | Dużo powtarzalnych artefaktów - warto mieć template'y |
| **Ustandaryzowany proces** | Workflow'y można precyzyjnie opisać |
| **Document-heavy** | Agent może pomagać w tworzeniu i ekstrakcji dokumentów |
| **Specjalistyczna terminologia** | Glosariusz eliminuje wyjaśnianie podstaw |
| **Duża precyzja formalna** | Template'y zapewniają spójność |

### Problem właściciela praktyki (Anna Sobańska)
- Każda sesja z AI zaczyna od zera - trzeba tłumaczyć co to upadłość konsumencka
- Dokumenty tworzone "na piechotę" - brak spójnych szablonów
- Wiedza o procedurach w głowach prawników, nie w plikach
- Brak systematycznego sposobu pracy z AI

---

## Co by dostali: Workspace dla praktyki upadłościowej

### Struktura

```
gssp-upadlosci/
├── CLAUDE.md                          # Główny plik kontekstowy
├── context/
│   ├── domain/
│   │   ├── glossary.md                # Terminologia: syndyk, masa upadłości, plan spłaty...
│   │   ├── procedury.md               # Etapy postępowania upadłościowego
│   │   └── orzecznictwo.md            # Kluczowe orzeczenia, precedensy
│   ├── workflows/
│   │   ├── intake-klienta.md          # Jak przyjmujemy nową sprawę
│   │   ├── przygotowanie-wniosku.md   # Jak przygotowujemy wniosek
│   │   └── postepowanie-syndyk.md     # Jak współpracujemy z syndykiem
│   └── examples/
│       ├── dobry-wniosek.md           # Wzorcowy wniosek
│       └── dobra-lista-wierzycieli.md # Wzorcowa lista
├── templates/
│   ├── wniosek-upadlosciowy.md        # Szablon wniosku
│   ├── lista-wierzycieli.md           # Szablon listy
│   ├── intake-form.md                 # Formularz przyjęcia sprawy
│   └── raport-dla-klienta.md          # Szablon aktualizacji statusu
├── skills/
│   ├── extract-debt.md                # Ekstrakcja zadłużenia z dokumentów
│   ├── draft-wniosek.md               # Drafting wniosku
│   └── analyze-umowa.md               # Analiza umowy kredytowej
└── projects/
    └── [YYYYMM-nazwisko-klienta]/     # Folder per sprawa
```

### CLAUDE.md - serce workspace'u

```markdown
# GSSP - Praktyka Upadłościowa

## Kim jestem
Adwokat/prawnik w kancelarii GSSP specjalizującej się w upadłości
konsumenckiej i restrukturyzacji.

## Co robię
Pomagam klientom wyjść z długów poprzez postępowania upadłościowe.
Prowadzę sprawy od intake'u przez wniosek, postępowanie z syndykiem,
do planu spłaty lub umorzenia.

## Kontekst domenowy
- `context/domain/glossary.md` - terminologia upadłościowa
- `context/domain/procedury.md` - etapy postępowania

## Workflow'y
Gdy mówię:
- "nowy klient" → użyj `workflows/intake-klienta.md`
- "przygotuj wniosek" → użyj `workflows/przygotowanie-wniosku.md`
- "ekstrakcja" → użyj `skills/extract-debt.md`

## Templates
- Wniosek: `templates/wniosek-upadlosciowy.md`
- Lista wierzycieli: `templates/lista-wierzycieli.md`

## Preferencje
- Język: polski
- Styl: formalny, prawniczy
- Cytaty: pełne sygnatury, numery artykułów
```

### Glosariusz (fragment)

```markdown
# Terminologia Prawa Upadłościowego

## Podstawowe pojęcia

**Upadłość konsumencka** - postępowanie sądowe pozwalające osobie fizycznej
nieprowadzącej działalności gospodarczej na oddłużenie. Podstawa: art. 491¹
i nast. Prawa upadłościowego.

**Syndyk** - osoba wyznaczona przez sąd do prowadzenia postępowania
upadłościowego. Zarządza masą upadłości, likwiduje majątek, przygotowuje
plan spłaty.

**Masa upadłości** - majątek upadłego, który służy zaspokojeniu wierzycieli.

**Plan spłaty wierzycieli** - harmonogram spłat ustalony przez sąd,
trwający od 3 do 7 lat w zależności od okoliczności.

**Lista wierzycieli** - zestawienie wszystkich wierzytelności upadłego
z podaniem wierzyciela, kwoty, podstawy i dokumentacji.

...
```

---

## Jak wygląda praca adwokata w tym workspace'u

### Scenariusz 1: Nowy klient na upadłość

**Dziś (bez workspace'u):**
1. Spotkanie z klientem
2. Notatki na kartce / w Wordzie
3. Otwiera Claude, wyjaśnia co to upadłość konsumencka
4. Prosi o pomoc z listą dokumentów
5. Agent pyta o podstawowe rzeczy
6. Frustracja - "muszę to tłumaczyć od zera"

**Z workspace'em:**
1. Adwokat otwiera Claude Code w folderze `gssp-upadlosci/`
2. Claude automatycznie czyta CLAUDE.md - zna kontekst
3. Adwokat: "Nowy klient, Kowalski, dług 120k PLN, 3 wierzycieli bankowych"
4. Claude: używa `workflows/intake-klienta.md`, wie co pytać
5. Tworzy `projects/202601-kowalski/intake.md` z zebranym stanem faktycznym
6. Sugeruje listę dokumentów do zebrania (zna procedurę)

**Różnica:** Agent rozumie kontekst od pierwszej sekundy. Nie pyta "co to syndyk?".

---

### Scenariusz 2: Przygotowanie wniosku upadłościowego

**Dziś:**
1. Adwokat ma dokumenty klienta
2. Ręcznie wypełnia formularz wniosku
3. Osobno liczy sumę zadłużenia
4. Sprawdza czy nic nie pominął

**Z workspace'em:**
1. Adwokat: "Przygotuj wniosek dla Kowalskiego"
2. Claude: czyta `projects/202601-kowalski/` (intake, dokumenty)
3. Używa `templates/wniosek-upadlosciowy.md`
4. Generuje draft wniosku z wypełnionymi danymi
5. Tworzy `lista-wierzycieli.md` z podsumowaniami
6. Adwokat: przegląda, koryguje, zatwierdza

**Różnica:** Agent zna szablon, wypełnia według standardu kancelarii. Adwokat weryfikuje, nie pisze od zera.

---

### Scenariusz 3: Ekstrakcja danych z dokumentów

**Dziś:**
1. Klient przynosi 15 umów kredytowych i wezwań do zapłaty
2. Prawnik ręcznie wyciąga: wierzyciel, kwota, data, podstawa
3. Przepisuje do Excela

**Z workspace'em:**
1. Adwokat: "Ekstrahuj dane z tych dokumentów" + załącza PDFy
2. Claude: używa `skills/extract-debt.md`
3. Dla każdego dokumentu wyciąga strukturyzowane dane
4. Kompiluje do `lista-wierzycieli.md` według template'u
5. Adwokat: weryfikuje, koryguje kwoty, dodaje brakujące

**Różnica:** Agent robi ciężką robotę ekstrakcji. Adwokat kontroluje jakość.

---

## Konkretne skills do zbudowania

### 1. `/extract-debt` - Ekstrakcja zadłużenia

```markdown
# Skill: Ekstrakcja zadłużenia z dokumentów

## Trigger
Użytkownik dostarcza dokumenty (umowy, wezwania, BIK) i chce wyciągnąć dane.

## Input
- Dokumenty (PDF/skan/tekst)

## Output
Strukturyzowane dane:
- Wierzyciel (nazwa, adres, KRS)
- Kwota główna
- Odsetki (jeśli wskazane)
- Data powstania zobowiązania
- Podstawa (umowa nr, z dnia)
- Status (wypowiedziana/windykowana/cesja)

## Instrukcje
1. Przeanalizuj dokument
2. Zidentyfikuj typ (umowa/wypowiedzenie/wezwanie/BIK)
3. Wyekstrahuj dane według struktury powyżej
4. Oznacz niepewności [?]
5. Podsumuj w formie tabeli
```

### 2. `/draft-wniosek` - Draft wniosku

```markdown
# Skill: Przygotowanie wniosku upadłościowego

## Trigger
Użytkownik prosi o przygotowanie wniosku, ma komplet danych.

## Input
- Dane osobowe dłużnika (z intake)
- Lista wierzycieli (z ekstrakcji)
- Dokumentacja dochodowa

## Output
Draft wniosku według `templates/wniosek-upadlosciowy.md`

## Instrukcje
1. Wczytaj dane z projektu klienta
2. Wypełnij szablon wniosku
3. Oblicz sumy (zadłużenie całkowite, liczba wierzycieli)
4. Wygeneruj uzasadnienie (standard dla upadłości konsumenckiej)
5. Oznacz miejsca wymagające weryfikacji [DO SPRAWDZENIA]
```

### 3. `/status-report` - Raport dla klienta

```markdown
# Skill: Przygotowanie aktualizacji dla klienta

## Trigger
Trzeba poinformować klienta o postępach w sprawie.

## Input
- Folder projektu (zawiera historię działań)

## Output
Zwięzły raport według `templates/raport-dla-klienta.md`

## Instrukcje
1. Przejrzyj ostatnie działania w projekcie
2. Zidentyfikuj: co się wydarzyło, co jest następne
3. Napisz prostym językiem (klient nie jest prawnikiem)
4. Zaproponuj kanał wysyłki (email/telefon)
```

---

## Propozycja współpracy

### Opcja A: Workspace Build (TEAM)
**Budujemy kompletne środowisko dla działu upadłościowego**

- Discovery: mapowanie procesów, terminologii, artefaktów
- Build: CLAUDE.md, glosariusz, 5 template'ów, 5 skilli
- Training: 2h sesja z zespołem
- Support: 2 follow-up check-iny

**Timeline:** 6-8 tygodni
**Zaangażowanie zespołu:** ~25h
**Cena:** 12-18k PLN

---

### Opcja B: Workflow Sprint - Przygotowanie wniosku
**Wdrażamy jeden workflow: od intake'u do gotowego wniosku**

- Discovery: jak dziś wygląda proces
- Build: template wniosku, skill ekstrakcji, workflow
- Pilot: testowanie na 2-3 realnych sprawach
- Handoff: dokumentacja, training

**Timeline:** 3-4 tygodnie
**Zaangażowanie:** ~15h
**Cena:** 25-35k PLN

---

### Opcja C: Foundation (Light)
**Budujemy tylko fundamenty - CLAUDE.md i strukturę**

- Discovery: szybkie mapowanie
- Build: CLAUDE.md, glosariusz, struktura folderów
- Handoff: 1h walkthrough

**Timeline:** 2-3 tygodnie
**Zaangażowanie:** ~8h
**Cena:** 3.5-5k PLN

---

## Wartość dla kancelarii

### Bez workspace'u (teraz)
- Każda sesja z AI od zera
- Agent nie zna terminologii, pyta o podstawy
- Dokumenty tworzone ad hoc, różna jakość
- Wiedza w głowach prawników

### Z workspace'em
- Agent zna kontekst od pierwszej sekundy
- Spójne template'y = spójna jakość dokumentów
- Workflow'y udokumentowane = łatwiejszy onboarding
- Skille = powtarzalne operacje zdefiniowane raz

### ROI (szacunkowo)
- Oszczędność: 1-2h na sprawie (setup context + tworzenie dokumentów)
- 50 spraw/rok × 1.5h × 300 PLN/h = **22,500 PLN/rok**
- Workspace Build (12k) = zwrot w 6-7 miesięcy

---

## Pytania do rozmowy z Anną Sobańską

1. **Jak dziś pracujecie z AI?** Czy używacie Claude/ChatGPT? Do czego?

2. **Jak wygląda typowa sprawa upadłościowa?** Od pierwszego kontaktu do zakończenia - co jest powtarzalne?

3. **Co zajmuje najwięcej czasu?** Dokumentacja? Komunikacja z klientem? Korespondencja z syndykiem?

4. **Jakie dokumenty tworzycie najczęściej?** Wnioski, pisma, raporty - co można by standaryzować?

5. **Czy macie już jakieś template'y/checklisty?** Używane w praktyce?

6. **Ile osób pracuje na upadłościach?** Kto by używał workspace'u?

7. **Czy widzisz siebie pracującą w narzędziu typu Claude Code?** Pisanie poleceń, praca z plikami?
