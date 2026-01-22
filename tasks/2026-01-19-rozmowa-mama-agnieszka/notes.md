# Rozmowa z mamą i Agnieszką — 2026-01-19

## Kontekst

Rozmowa o tym jak pracują z AI. Obie knowledge workers, obie używają AI, różne konteksty.

---

## Agnieszka — NGO, Copilot

**Profil:** współzarządza organizacją pozarządową, intensywnie używa AI.

**Jak pracuje:**
- Microsoft Copilot z dostępem do Sharepointa organizacji
- Pracuje na swoich dokumentach — nie polega na AI jako źródle wiedzy
- Wrzuca dokument → streść / wyciągnij konkretną rzecz

**Use cases:**
- Generowanie rekomendacji (wzory + kontekst współpracy z osobą)
- Wnioski grantowe — odpowiedzi na pojedyncze pytania
- Wyciąganie wniosków z raportu ewaluacyjnego w kontekście konkretnego pytania

**Bariery:**
- Ograniczone zaufanie — anonimizuje dokumenty, nie wie czy dane nie stają się "publiczne"
- Nie chce generować całego wniosku — boi się antyplagiatowych i generyczności ("wszyscy będą mieli taki sam")

**Potencjalny case:**
> Wniosek grantowy jako iteracyjny workflow z wieloma artefaktami i źródłami kontekstu.

---

## Mama — freelance, projekty 3-sektor

**Profil:** wcześniej zarządzała NGO, teraz freelance — projekty, szkolenia, różnorodność.

**Ostatni projekt:** Program szkoleniowy "Psychologiczne aspekty prowadzenia mediacji"

**Jak pracowała:**
1. ChatGPT: "zrób mi program" → bezwartościowy output
2. Gemini iteracyjnie z checkpointami:
   - "hej muszę zrobić program, robimy krok po kroku"
   - najpierw paradygmaty mediacji
   - potem psychologiczne aspekty bezstronności
   - potem propozycje ćwiczeń
   - co ją ciekawiło — pogłębiała

**Rezultat:**
- Bardzo dobra jakość
- "Znalazł ciekawsze treści niż myślimy z Konradem wymyślimy"

**Nadchodzący projekt:** Oferta kulturalna dla migranckich dzieci

**Obserwacja:**
> Realizuje Human-Agent Collaboration ręcznie — iteracja, checkpointy, człowiek steruje. Pytanie: ile zyska z workspace'u i czy będą bariery wejścia?

---

## Wnioski strategiczne

### Copilot vs Agentic Workspace — gdzie moja przewaga?

**Copilot ma:**
- Integrację z Sharepointem — kontekst organizacji "out of the box"
- Niski próg wejścia dla M365 users

**Copilot nie ma:**
- Edycji dokumentów (?) — tylko chat
- Przejrzystości — przeglądarka plików + edytor + chat w jednym oknie
- Izolacji kontekstu — nie da się zrobić systematycznego researchu gdzie:
  - masz plan
  - zbierasz źródła
  - analizujesz każde źródło w oddzielnym kontekście (żeby się nie gromadził)
  - długie zadanie z dużym kontekstem

**Moja przewaga:**
- Złożone, długie zadania z wieloma źródłami
- Kontrola i przejrzystość
- Izolacja kontekstu między subtaskami
- Artefakty jako medium (nie chat)

### Pytania do zbadania

1. **Jakie zadania wymagają tego co daje agentic workspace a nie daje copilot?**
   - Wnioski grantowe (wiele źródeł, iteracja, checkpointy)
   - Literature review
   - Strategia (wiele perspektyw, synteza)
   - Co jeszcze?

2. **Czy dla kogoś takiego jak mama wystarczy "usystematyzowanie pracy z chatem"?**
   - Ona już robi iterację z checkpointami
   - Ile zyska z workspace'u vs ile kosztuje wdrożenie?

3. **Czy copilot + dedykowani agenci M365 mogliby dać podobną wartość?**
   - Trzeba zbadać co copilot agents potrafią

---

## Potencjalne oferty / case'y

| Osoba | Potencjalny case | Typ oferty |
|-------|------------------|------------|
| Agnieszka | Wniosek grantowy jako workflow | Workflow Sprint |
| Mama | Program szkoleniowy workflow | Workspace Build (freelancer) |

---

## Linki

- [[Vision - AI Native Knowledge Work]] — trzy podejścia do AI
- [[AI Workspace Build]] — oferta workspace'u
- [[Workflow Implementation Sprints]] — oferta workflow'owa
