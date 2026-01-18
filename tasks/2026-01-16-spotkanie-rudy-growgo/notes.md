# Spotkanie z Rudym (GrowGo) - 2026-01-16

## Kontekst
Rudy prowadzi growgo.tech - consulting AI dla dużych firm (Carlsberg, Kruk S.A., Fundacja Batorego).

## Model pracy GrowGo
- Pomagają firmom tworzyć "custom GPTs" (konkretnie Google Gems)
- Jeden Gem = jedno zadanie
- Cel: usystematyzować, uczynić przewidywalną pracę mniej kompetentnej osoby
- Google jako "godniejszy zaufania partner" dla korporacji niż Anthropic

## Perspektywa Rudego (klienci korporacyjni)
- Szukają **przewidywalności i systematyzacji**
- Chcą, żeby mniej kompetentna osoba mogła wykonać proces
- Pracownik nie ma motywacji usprawniać pracy (bo go zwolnią)
- Zatrudniają konsultanta, który wypracuje Gemsy

## Moje kontrargumenty
- In-context learning jest kluczowy
- Lepiej rozwijać możliwości oddolnie, w praktyce (bo taski ewoluują szybciej niż soft)
- Nie przez zewnętrznego konsultanta tworzącego gotowe rozwiązania (bo konsultant nie zna dziedziny tak głęboko jak pracownik)

## Moje przemyślenia
- Moja oferta → bardziej abstrakcyjna praca, trudna do zamknięcia w custom GPTs
- Ale: praca typu "Gems" też mieści się w moim systemie
- Mój system daje więcej: elastyczność, toole, reużywalność, in-context rozwój
- **Pytanie:** jak to sprzedać klientom typu klienci Rudego?

## Do zbadania
- Jak pozycjonować Context Engineering dla korporacji szukających przewidywalności?
- Gdzie jest granica między "custom GPT per task" a "agent-native workflow"?
- Argument "pracownik się nie zmotywuje" - jak na to odpowiedzieć?

---

# Brainstorming: Corporate Context Ops (Budowa Aktywów)

## 1. Zmiana ramy: Z "Umiejętności" na "Zarządzanie Wiedzą (Knowledge Ops)"

Korporacje nie chcą "uczyć ludzi myśleć" (niestety), chcą "działających procesów".
**Context Engineering** w skali B2B to nie "kurs pisania promptów", to **budowa "Systemu Operacyjnego Wiedzy"**.

- **Stary model (Baza wiedzy/Wiki):** Pasywna, nikt nie czyta, trudna w utrzymaniu.
- **Model Rudego (Gems):** "Zamrożone" procedury. Szybko się dezaktualizują. Black box.
- **Twój model (Context Files):** "Żywa" wiedza, którą AI *aktywnie wykorzystuje* do pracy.
    - To jest **"Executable Knowledge"**.

**Sprzedaż:**
"Nie sprzedajemy szkolenia dla pracowników. Sprzedajemy wdrożenie systemu 'Context Ops', gdzie Wasza wiedza ekspercka (domena, procedury) jest **externalizowana do plików**, które AI rozumie i wykonuje. To budowa 'Corporate Brain'."

## 2. Rozwiązanie konfliktu "Niezmotywowany Pracownik" (Architekt vs Operator)

Rudy ma rację: przeciętny pracownik nie chce "inżynierować".
Rozwiązanie: **Podział ról (Tiered System)**.

Nie uczymy wszystkich Level 3 (Architektura Systemu).
- **Context Architects (1-5%):** Seniorzy/Liderzy. Oni tworzą `CLAUDE.md`, `context/rules.md`, `specs/`. Oni "kodują" proces biznesowy w języku naturalnym.
- **Context Operators (95%):** Juniorzy. Oni tylko "uruchamiają" kontekst. "Weź plik `[context/procedura_fakturowania.md]` i przetwórz te PDFy".
    - Dla nich to jest równie proste jak Gem, ale **bardziej audytowalne i elastyczne**.
    - Gdy proces się zmienia, Architekt zmienia plik `.md`. W modelu Gems trzeba przeklikać konfigurację bota (trudne w version control).

**Wniosek:** "Context Files" to kod źródłowy procesu biznesowego. Gems to skompilowana binarka. Wolisz mieć dostęp do kodu źródłowego (łatwe zmiany, audyt) czy binarki (czarna skrzynka)?

## 3. "Process as Code" dla Korporacji (Audyt i Kontrola)

Korporacje kochają kontrolę (Compliance, ISO).
- Custom GPT (Gem) = Magia. Dlaczego zadziałał tak a nie inaczej? Trudno sprawdzić system prompt ukryty w konfiguracji.
- Context Engineering = Pliki.
    - Możesz zrobić `git diff` na procesie sprzedaży.
    - "W zeszłym kwartale zmieniliśmy wytyczne w `context/compliance.md` i AI zaczęło odrzucać te ryzykowne umowy."
    - To jest **zarządzalność** na poziomie IT, ale dla procesów biznesowych.

**Hasło:** "Przynosimy standardy DevOps do pracy z wiedzą (Knowledge Work)."
- Versioning procesów.
- Review zmian w procesach (Pull Request do `context/standards.md`).

## 4. Wyższość nad Custom GPTs (Why Gems fail at scale)

- **Silosy:** Każdy Gem ma swoje instrukcje. Jak zmienia się brand voice, musisz edytować 50 Gemów.
- **Shared Context (Twój system):** Masz jeden plik `brand_voice.md` i 50 agentów go zasysa. Zmieniasz w jednym miejscu, działa wszędzie. (DRY - Don't Repeat Yourself).
    - To jest argument **ekonomiczny** (koszt utrzymania).
    - Gems to "dług technologiczny" w momencie powstania.

## 5. Strategia "Trojan Horse"

Nie walcz z Gems. Gems są świetne jako interfejs końcowy (Frontend).
Ale: **Co karmi Gema?**
Jeśli wpiszesz prompt Gema "z palca" w konfiguratorze - to jest legacy.
System Context Engineering służy do **generowania i utrzymywania promptów dla Gemsów**.

- "Używajmy Google Gems dla pracowników liniowych, świetny pomysł."
- "Ale RZĄDZIĆ tymi Gemsami będziemy z repozytorium kontekstu (Markdown Files), żeby zachować spójność."

## Podsumowanie dla Rudego

1.  **Gems są OK jako "Runtime"**, ale fatalne jako "Source Code" procesów (trudne w utrzymaniu, brak versioningu, silosy).
2.  **Context Engineering to "Backend"** dla AI w firmie. To tam żyje wiedza.
3.  **Role:** Architekci (tworzą Context Files) vs Operatorzy (używają Gemsów zasilanych Context Files).
4.  **Value Prop:** Skalowalność, Utrzymywalność (Maintenance), Audytowalność.
