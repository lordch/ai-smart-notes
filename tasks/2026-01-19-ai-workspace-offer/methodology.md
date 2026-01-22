# AI Workspace Build — Metodologia wdrożenia

Jak przeprowadzamy wdrożenie krok po kroku.

---

## Przegląd procesu

```
Week 0          Week 1-2        Week 3-4        Week 5-6
[Discovery] → [Build Core] → [Build Details] → [Handoff]
   ↓              ↓               ↓               ↓
Zrozumienie    CLAUDE.md      Templates      Transfer
kontekstu      Struktura      Skille         Maintenance
               Glosariusz     Commands       Support
```

**Całkowity czas:** 4-6 tygodni
**Zaangażowanie klienta:** 3-5 godzin/tydzień

---

## Faza 0: Discovery (Tydzień 0)

### Cel
Zrozumieć świat klienta: domenę, procesy, artefakty, narzędzia.

### Działania

**Spotkanie kickoff (2h)**
- Kim jest klient, co robi
- Jakie są główne typy pracy
- Jak wygląda typowy tydzień/projekt
- Jakich narzędzi używa (gdzie trzyma pliki, jak komunikuje się z AI)
- Co nie działa / co frustruje

**Zbieranie materiałów**
Klient dostarcza:
- Przykładowe dokumenty które tworzy (5-10 sztuk)
- Opis 2-3 typowych projektów/zadań
- Lista terminów specjalistycznych (draft)
- Dostęp do obecnego workspace'u (jeśli istnieje)

**Moja analiza (async)**
- Przegląd dostarczonych materiałów
- Identyfikacja wzorców (typy artefaktów, powtarzalne struktury)
- Mapowanie procesów
- Draft planu wdrożenia

### Output fazy
- **Brief Discovery** — dokument podsumowujący zrozumienie kontekstu
- **Mapa artefaktów** — lista typów dokumentów które klient tworzy
- **Mapa workflow'ów** — główne procesy do wsparcia
- **Plan wdrożenia** — co zrobimy w fazach 1-3

### Czas
- Klient: 3-4h
- Ja: 6-8h

---

## Faza 1: Build Core (Tygodnie 1-2)

### Cel
Zbudować fundament: strukturę workspace'u, główny context file, podstawową terminologię.

### Działania

**Sesja 1: Struktura (2h)**
- Wspólnie definiujemy strukturę folderów
- Ustalam naming conventions
- Tworzę szkielet workspace'u
- Klient widzi jak to wygląda, daje feedback

**Praca async: CLAUDE.md v1**
- Piszę pierwszy draft CLAUDE.md na podstawie Discovery
- Sekcje: Kim jestem, Terminologia (podstawowa), Preferencje

**Sesja 2: Review + Glosariusz (2h)**
- Przegląd CLAUDE.md z klientem
- Wspólnie uzupełniamy terminologię
- Definiujemy preferencje pracy z AI
- Testujemy: czy agent rozumie kontekst?

**Praca async: Iteracja**
- Poprawiam CLAUDE.md na podstawie feedbacku
- Rozbudowuję glosariusz

### Output fazy
- Workspace z pełną strukturą folderów
- CLAUDE.md v1 (działający, ale jeszcze bez skills)
- Glosariusz v1 (20-50 kluczowych terminów)

### Czas
- Klient: 4-5h
- Ja: 10-12h

---

## Faza 2: Build Details (Tygodnie 3-4)

### Cel
Zbudować template'y artefaktów, skille, komendy — konkretne narzędzia do codziennej pracy.

### Działania

**Sesja 3: Templates (2h)**
- Wybieramy 3-5 najważniejszych typów artefaktów
- Dla każdego definiujemy: struktura, cel, instrukcje
- Piszę draft template'ów podczas sesji

**Praca async: Template'y**
- Dopracowuję template'y
- Tworzę przykłady (z materiałów klienta lub nowe)
- Linkuję w CLAUDE.md

**Sesja 4: Skille + Commands (2h)**
- Definiujemy 3-5 głównych workflow'ów jako skille
- Tworzymy slash commands
- Testujemy na żywo: czy działa?

**Praca async: Iteracja**
- Poprawiam na podstawie testów
- Dodaję edge cases do instrukcji

### Output fazy
- 3-5 template'ów artefaktów
- 3-5 zdefiniowanych skilli
- Slash commands skonfigurowane
- Biblioteka przykładów (2-3 per typ)

### Czas
- Klient: 4-5h
- Ja: 12-15h

---

## Faza 3: Handoff (Tygodnie 5-6)

### Cel
Przekazać workspace klientowi, upewnić się że umie go używać i rozwijać.

### Działania

**Sesja 5: Full walkthrough (2h)**
- Przechodzimy przez cały workspace
- Klient wykonuje typowe zadanie od początku do końca
- Rozwiązujemy problemy na żywo

**Praca async: Dokumentacja**
- Piszę Maintenance Guide
- Troubleshooting FAQ
- "Co dalej" — sugestie rozwoju

**Sesja 6: Q&A + Zamknięcie (1h)**
- Ostatnie pytania
- Plan na pierwsze 2 tygodnie samodzielnej pracy
- Ustalenia dot. follow-up support

**Follow-up (opcjonalny, tydzień 7-8)**
- 2 krótkie check-iny (30 min każdy)
- Odpowiedzi na pytania które się pojawiły
- Drobne korekty

### Output fazy
- Kompletny, działający workspace
- Maintenance Guide
- Klient umie używać i rozwijać system
- (Opcjonalnie) nagranie walkthrough

### Czas
- Klient: 3-4h
- Ja: 6-8h

---

## Podsumowanie czasu

| Faza | Klient | Ja | Razem |
|------|--------|-----|-------|
| Discovery | 3-4h | 6-8h | ~12h |
| Build Core | 4-5h | 10-12h | ~16h |
| Build Details | 4-5h | 12-15h | ~18h |
| Handoff | 3-4h | 6-8h | ~12h |
| **RAZEM** | **15-18h** | **35-43h** | **~55h** |

Rozłożone na 4-6 tygodni = ok. 3-5h/tydzień dla klienta.

---

## Format pracy

### Sesje synchroniczne
- Video call (Zoom/Meet/Teams)
- Screen sharing — pracujemy razem na workspace'ie
- Nagrywanie (za zgodą) dla późniejszego reference

### Praca asynchroniczna
- Ja pracuję na workspace'ie między sesjami
- Klient dostarcza materiały i feedback przez shared folder / email
- Krótkie async updates przez chat (Slack/email)

### Narzędzia
- Workspace: lokalne pliki klienta lub shared repo (GitHub/Dropbox)
- Komunikacja: email + opcjonalnie Slack/chat
- Sesje: Zoom/Meet

---

## Co jeśli klient potrzebuje więcej/mniej?

### Wersja Light (2-3 tygodnie)
- Discovery + Build Core only
- Klient dostaje: strukturę, CLAUDE.md, glosariusz
- Sam buduje template'y i skille (z moim wsparciem async)
- Dla: klientów technicznych, którzy chcą tylko fundament

### Wersja Extended (6-8 tygodni)
- Pełne wdrożenie + głębsze skille
- Więcej template'ów (8-10)
- Connectors / automatyzacje
- Training dla zespołu (jeśli >1 osoba)
- Dla: zespołów, złożonych domen

---

## Kryteria sukcesu wdrożenia

### Po zakończeniu klient powinien:

**Umieć:**
- [ ] Rozpocząć nową sesję z AI bez powtarzania kontekstu
- [ ] Użyć template'u do stworzenia artefaktu
- [ ] Wywołać skill/command do typowego zadania
- [ ] Dodać nowy termin do glosariusza
- [ ] Zaktualizować CLAUDE.md gdy coś się zmieni

**Mieć:**
- [ ] Workspace z pełną strukturą
- [ ] CLAUDE.md który agent rozumie
- [ ] Minimum 3 działające template'y
- [ ] Minimum 3 działające skille
- [ ] Dokumentację utrzymania

**Doświadczyć:**
- [ ] "Agent rozumie mój kontekst bez wyjaśniania"
- [ ] "Mam gdzie zapisać to co się nauczyłem"
- [ ] "Wiem jak rozwijać system dalej"

---

## Ryzyko i mitigation

| Ryzyko | Mitigation |
|--------|------------|
| Klient nie ma czasu na sesje | Jasne ustalenie na początku; reschedule policy |
| Domena zbyt złożona | Scope do 1-2 głównych workflow'ów; reszta jako follow-up |
| Klient oczekuje magii | Honest conversation w Discovery; clear expectations |
| Narzędzia się zmienią | Framework jest tool-agnostic; dokumentujemy zasady, nie buttony |
| Klient nie używa po wdrożeniu | Handoff z planem; follow-up check-iny; opcjonalny advisory |
