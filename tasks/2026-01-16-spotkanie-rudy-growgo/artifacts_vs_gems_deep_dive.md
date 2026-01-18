# Artefakty vs Gems: Dlaczego Praca na Plikach Zmienia Grę

*Dokument dla Rudego - GrowGo*

---

## Wstęp: O czym właściwie mówimy?

Rudy, Twój model z Gemsami działa. Firmy dostają narzędzia, które "robią robotę". Ale chcę Ci pokazać, dlaczego praca na artefaktach (plikach) otwiera drzwi, których Gems nie są w stanie nawet zobaczyć.

Nie chodzi o to, że Gems są złe. Chodzi o to, że są **ograniczone do pewnej klasy problemów**. I ta klasa jest mniejsza, niż się wydaje.

---

## Część I: Anatomia Problemu

### Scenariusz 1: "Napisz mi procedurę obsługi reklamacji"

**W Gemie:**
- Użytkownik: "Napisz procedurę obsługi reklamacji dla naszej firmy."
- Gem generuje 2-stronicowy dokument.
- Użytkownik: "Dodaj punkt o eskalacji do managera po 48h."
- Gem generuje... ponownie cały dokument. Z nowym punktem.
- Użytkownik: "Czekaj, w punkcie 3 było 'w ciągu 24h', a teraz jest '48h'. Nie zmieniaj tego!"
- Gem: "Przepraszam, oto poprawiona wersja..." (znowu cały dokument)

**Co się stało?** Model nie ma pamięci "co było ustalone". Każda iteracja to rzut kośćmi. W korporacji, gdzie jeden przecinek w procedurze może mieć konsekwencje prawne, to jest **niedopuszczalne**.

**W systemie artefaktów:**
- Agent zapisuje `procedura_reklamacji.md` w folderze projektu.
- Użytkownik: "Dodaj punkt o eskalacji."
- Agent robi **chirurgiczną edycję**: dodaje linijki 45-52, reszta dokumentu jest nienaruszona.
- Każda zmiana jest widoczna w historii (git diff). Można ją cofnąć. Można ją audytować.

**Wniosek:** Artefakty dają **stabilność** i **przewidywalność**. Gems dają **lotność**.

---

### Scenariusz 2: "Przygotuj raport kwartalny dla zarządu"

**W Gemie:**
- Użytkownik wkleja dane z Excela, notatki ze spotkań, maile.
- Po 30 wymianach czat ma 50 000 tokenów.
- Model zaczyna "gubić wątek" - zapomina o ustaleniach z początku rozmowy.
- Użytkownik: "Przecież mówiłem, że dział sprzedaży to priorytet!"
- Model: "Przepraszam, oto zaktualizowana wersja..."

**Co się stało?** To jest **Context Rot** - degradacja jakości w miarę zapełniania kontekstu. Model zaczyna halucynować, bo "widzi" za dużo informacji i traci zdolność rozróżniania tego, co ważne.

**W systemie artefaktów:**
- Masz folder `raporty/Q3/`.
- W środku: `dane.md`, `wnioski.md`, `draft_v1.md`, `draft_v2.md`.
- Każda sesja z AI zaczyna się od **czystego kontekstu**: "Przeczytaj `wnioski.md` i napisz executive summary."
- AI nie widzi "bólu rodzenia" poprzednich wersji. Widzi tylko to, co **zaakceptowałeś**.

**Wniosek:** Artefakty działają jak **garbage collection dla kontekstu**. Każda sesja to świeży start z czystym stanem.

---

### Scenariusz 3: "Mamy 5 działów, każdy potrzebuje swoich procedur"

**W Gemach:**
- Tworzysz 5 Gemsów, każdy z instrukcją: "Jesteś asystentem działu X, mów w tonie Y..."
- CEO decyduje: "Od teraz firma mówi per 'Wy', nie per 'Pan/Pani'."
- Musisz edytować 5 Gemsów. Ręcznie. W konfiguratorze.
- Przy 50 Gemsach to jest dzień pracy. I błędy gwarantowane.

**W systemie artefaktów:**
- Masz jeden plik `context/brand_voice.md`:
  ```markdown
  # Głos marki
  - Forma: "Wy" (nie "Pan/Pani")
  - Ton: profesjonalny, ale ciepły
  - Unikaj: żargonu prawniczego
  ```
- Wszystkie agenty/workflow'y czytają ten plik.
- CEO zmienia zdanie? Edytujesz **jeden plik**. Gotowe.

**Wniosek:** To jest **DRY (Don't Repeat Yourself)** dla procesów biznesowych. Gems tworzą silosy. Artefakty tworzą **Single Source of Truth**.

---

## Część II: Sytuacje, Których Gems Nie Ogarnął

### Scenariusz 4: Praca zespołowa

Anna z marketingu pisze artykuł. Bartek z prawnego ma go sprawdzić. Celina z SEO ma dodać słowa kluczowe.

**W Gemach:**
- Anna kończy w swoim Gemie.
- Kopiuje tekst do maila.
- Bartek wkleja do swojego Gema ("Sprawdź pod kątem prawnym").
- Kopiuje poprawki do maila.
- Anna wkleja do swojego Gema ("Wprowadź te poprawki").
- ...i tak w kółko.

**W systemie artefaktów:**
- Plik `content/artykul_produkt_x.md` leży w folderze współdzielonym.
- Anna: "Napisz artykuł według briefu" → Agent zapisuje plik.
- Bartek otwiera **nowy czat**: "Sprawdź plik `artykul_produkt_x.md` pod kątem prawnym, zaproponuj zmiany."
- Agent dodaje komentarze lub robi PR (Pull Request) z sugestiami.
- Celina otwiera **kolejny nowy czat**: "Zoptymalizuj pod SEO."

**Kluczowe:** Każdy pracuje w **izolowanym kontekście**. Bartek nie widzi burzy mózgów Anny nad nagłówkami. Anna nie widzi prawniczego żargonu Bartka. Ale wszyscy operują na **tym samym pliku** (Single Source of Truth).

---

### Scenariusz 5: Długotrwałe projekty (tygodnie, miesiące)

Firma pisze specyfikację nowego produktu. Prace trwają 3 miesiące.

**W Gemach:**
- Po każdym spotkaniu ktoś wkleja notatki do Gema i prosi o aktualizację specyfikacji.
- Po miesiącu nikt nie pamięta, co było w pierwszej wersji.
- Historia zmian? Nie ma. "Gdzieś w czacie było..."

**W systemie artefaktów:**
- Folder `specs/produkt_2026/`.
- Pliki: `wymagania_biznesowe.md`, `architektura.md`, `user_stories.md`.
- Każda sesja: "Zaktualizuj `user_stories.md` na podstawie dzisiejszego spotkania (notatki w załączniku)."
- Historia? `git log specs/produkt_2026/user_stories.md`.
- "Co się zmieniło od wersji z 15 stycznia?" → `git diff v1.2..v1.5`.

**Wniosek:** Artefakty umożliwiają **procesy długotrwałe**. Gems są ograniczone do **sesji**.

---

### Scenariusz 6: Onboarding nowego pracownika

Nowy junior dołącza do zespołu.

**W modelu Gems:**
- "Tu masz Gema do pisania maili, tu do raportów, tu do..."
- Junior nie rozumie, dlaczego Gem mówi "per Wy". Nie wie, gdzie to zmienić.
- Jak Gem się zepsuje (bo ktoś zmienił instrukcję), nikt nie wie dlaczego.

**W systemie artefaktów:**
- Junior dostaje dostęp do repozytorium z folderem `context/`.
- Może **przeczytać** pliki: `brand_voice.md`, `procedury/onboarding.md`, `products/produkt_x.md`.
- Rozumie, skąd biorą się instrukcje. Może zaproponować poprawki (Pull Request).
- Wiedza jest **jawna i edytowalna**, nie ukryta w konfiguracji Gema.

---

### Scenariusz 7: Audyt i Compliance

Audytor pyta: "Skąd AI wiedziało, że ma odrzucić tę umowę?"

**W Gemach:**
- "No... bo tak było w instrukcji Gema."
- "Pokaż mi tę instrukcję."
- "Eeee... to jest w konfiguracji... sekundę..."
- (nerwowe szukanie w panelu Google)

**W systemie artefaktów:**
- "Proszę, oto plik `context/compliance_rules.md`, wersja z 12 marca 2026."
- `git blame`: "Tę regułę dodał Kowalski 5.03.2026, commit message: 'Dodanie zasady XYZ zgodnie z ISO 12345'."
- Pełna **traceability**. Audytor jest szczęśliwy.

---

## Część III: Kiedy Gems Wystarczą (Serio)

Nie wszystko wymaga artefaktów. Gems są OK dla:

1. **Jednorazowych strzałów:** "Napisz życzenia urodzinowe dla Kasi."
2. **Proste transformacje:** "Przetłumacz ten akapit na angielski."
3. **Brainstorming bez konsekwencji:** "Wymyśl 10 nazw dla nowego produktu."
4. **Szybkie pytania:** "Co to jest EBITDA?"

**Reguła kciuka:** Jeśli output możesz **wyrzucić** i nic się nie stanie, Gem wystarczy.

Ale jeśli output ma **żyć dłużej niż sesja**, jeśli ktoś inny ma na nim pracować, jeśli ma być **wersjonowany, audytowany, utrzymywany** — wtedy potrzebujesz artefaktów.

---

## Część IV: Model Mentalny dla Rudego

Pomyśl o tym tak:

| Aspekt | Gems | Artefakty (Filesystem) |
|--------|------|------------------------|
| **Metafora** | Rozmowa telefoniczna | Dokument w segregatorze |
| **Trwałość** | Ulotna (po zamknięciu okna znika) | Trwała (plik zostaje) |
| **Współpraca** | Trudna (kopiuj-wklej) | Naturalna (współdzielony plik) |
| **Wersjonowanie** | Brak | Pełne (git) |
| **Audytowalność** | Minimalna | Pełna |
| **Skalowalność** | Liniowa (więcej Gemsów = więcej pracy) | Sublinearna (DRY, shared context) |
| **Idealne dla** | Jednorazowe zadania, Q&A | Procesy, projekty, wiedza organizacyjna |

---

## Część V: Propozycja dla Klientów Rudego

Nie mówimy im: "Wyrzućcie Gems."
Mówimy: "Zbudujmy **backend** dla Waszych Gemsów."

1. **Warstwa 1: Context Repository**
   - Pliki `.md` z wiedzą firmy: procedury, brand voice, zasady, produkty.
   - Wersjonowane w Git. Przeglądane przez seniorów.

2. **Warstwa 2: Agent Workflows**
   - Agenty (Antigravity, Cursor, Claude Code) czytają pliki i wykonują zadania.
   - Pisze raporty, aktualizuje dokumentację, przetwarza dane.

3. **Warstwa 3: Simple Interfaces (Gems, Custom GPTs)**
   - Dla juniorów: proste UI, "wrzuć plik, dostań wynik".
   - Ale **prompt Gema** jest generowany z plików w Context Repository.
   - Zmiana brand voice? Zmień plik → wszystkie Gems mają nowy prompt.

**Hasło sprzedażowe:** "Gems to frontend. My budujemy backend wiedzy Waszej firmy."

---

## Zakończenie: Co Zyskuje Klient?

1. **Kontrola:** Wiedza jest w plikach, nie w "magii" Gema.
2. **Skalowalność:** Jeden plik rządzi wieloma procesami.
3. **Ciągłość:** Projekty trwają miesiącami, wiedza się kumuluje.
4. **Audytowalność:** Każda zmiana ma autora, datę, powód.
5. **Współpraca:** Zespoły pracują na tych samych artefaktach, nie na kopiach w czatach.

Gems dają firmie **asystenta**. Artefakty dają firmie **pamięć instytucjonalną**.
