# Jobs Map v2 - Perspektywa Metodologii

## Zmiana Framingu

**Poprzednia wersja** traktowala oferte jako produkt:
- Jobs = potrzeby funkcjonalne (ciaglosc kontekstu, wersjonowanie, bezpieczenstwo)
- Alternatywy = inne produkty (Copilot, Gems, Cowork)
- Wartosc = features

**Ta wersja** traktuje oferte jako metodologie:
- Jobs = potrzeby kompetencyjne i strategiczne
- Alternatywy = scenariusze rozwoju rynku
- Wartosc = sposob myslenia, framework, umiejetnosc

---

## Core Insight

**Oferta nie jest narzedziem** - jest metodologia pracy z AI.

Co sprzedajemy:
1. **Framework myslenia**: Human steruje, agent wykonuje (trzecia droga miedzy chatem a autonomia)
2. **Insight strategiczny**: Autonomia jest droga i trudna; human-agent collaboration daje swietne wyniki niskim kosztem
3. **Praktyczne wytyczne**: Context engineering - jak organizowac wiedze, zeby agent mogl jej uzyc
4. **Strategia biznesowa**: Eksternalizacja wiedzy jako przewaga konkurencyjna firmy

Tool-agnostic: dziala z Claude, ChatGPT, Cursor, Copilot - narzedzie jest drugorzedne.

---

## Jobs to Be Done - Perspektywa Metodologii

### KATEGORIA 1: JAK PRACOWAC Z AI

#### JOB M1: Zrozumienie modelu mentalnego
> "Kiedy probuje uzywac AI w zlozonej pracy, chce zrozumiec JAK o tym myslec, zebym mogl swiadomie decydowac co delegowac, a co robic sam"

**Kontekst sytuacyjny:**
- Uzytkownik juz probowal ChatGPT/Copilot, czasem dziala, czasem nie
- Nie rozumie DLACZEGO czasem swietne wyniki, czasem smieci
- Frustracja: "AI jest jak losowa maszyna"
- Brak modelu mentalnego = brak kontroli

**Cytaty z researchu:**
- "Rozjazd miedzy aspiracjami a gotowoscia - 89% chce wdrazac, tylko 8% jest gotowych strategicznie"
- "Luka kompetencyjna dotyczaca rozpoznania potencjalu AI"
- "Generatywna AI nalezy traktowac jako narzedzie wspierajace, a nie zastepujace wlasne myslenie"

**Co metodologia daje:**
- Framework: "Human steruje, agent wykonuje" - jasny podzial rol
- Leverage hierarchy: "Research zle -> 1000 zlych linii. Plan zle -> 100. Kod zle -> 1"
- Autonomy slider: kiedy dac wiecej swobody, kiedy mniej

---

#### JOB M2: Praktyczna umiejetnosc context engineering
> "Kiedy mam zlozone zadanie wymagajace wielu krokow i zrodel, chce wiedziec JAK zorganizowac informacje dla AI, zeby agent naprawde mi pomogl zamiast halucynowac"

**Kontekst sytuacyjny:**
- Uzytkownik wie ze AI moze wiecej, ale nie wie jak to "odblokowac"
- Doswiadczyl context rot ("model gubi watek")
- Probowal dlugich promptow - nie dziala
- Szuka "wlasciwego sposobu" karmienia AI kontekstem

**Cytaty z researchu:**
- "Context Rot - Degradacja jakosci w miare zapelniania kontekstu"
- "Model nie pamieta co bylo ustalone"
- "Firmy czesto nie maja przygotowanych danych. Nie potrafia jeszcze analizowac danych"
- "The bottleneck shifted: Was 'Can agents even do this?' Now: 'Do agents know HOW WE do this?'"

**Co metodologia daje:**
- Context Curation Taxonomy: factual / procedural / organizational
- Praktyki: "Middle artifacts as collaboration checkpoints"
- Zasada: "Resist premature artifact production" - gather -> organize -> think -> produce
- Workflow: research -> plan -> implement (z checkpointami)

---

#### JOB M3: Powtarzalnosc wynikow
> "Kiedy raz udalo mi sie zrobic cos dobrze z AI, chce moc to powtorzyc, zeby nie zaczynac od zera przy kazdym podobnym zadaniu"

**Kontekst sytuacyjny:**
- "Raz mi wyszlo swietnie, a potem nie moglem powtorzyc"
- Brak systematycznosci = kazda sesja jak loteria
- Frustracja z brakiem kontroli nad jakoscia

**Cytaty z researchu:**
- "Gemini iteracyjnie z checkpointami - bardzo dobra jakosc" (mama - realizuje recznie, bez systemu)
- "Scripts for reliability, LLM for flexibility"
- "The ratchet: LLM explores -> human identifies pattern -> script captures -> LLM explores at next level"

**Co metodologia daje:**
- Collaboration loop: problem -> research artifact -> review -> plan artifact -> implement -> tests -> update knowledge -> repeat
- "Build iteratively: Add a rule the second time you see the same mistake"
- Procedural context (AGENTS.md pattern) = captured patterns

---

### KATEGORIA 2: BUDOWANIE KOMPETENCJI

#### JOB M4: Rozwoj bez uzaleznienia
> "Kiedy korzystam z AI w pracy, chce budowac wlasne umiejetnosci i rozumienie, zeby nie stac sie zalezny od narzedzia i nie stracic krytycznego myslenia"

**Kontekst sytuacyjny:**
- Swiadomosc ryzyka "atrofii umiejetnosci"
- Obawa przed "black box" - nie wiem co AI robi
- Chce kontroli i zrozumienia, nie magii

**Cytaty z researchu:**
- "Negatywna zaleznosc miedzy czestym korzystaniem z AI a zdolnoscia do krytycznego myslenia"
- "40%+ junior developers deploys AI-generated code they don't fully understand"
- "GenSI zwieksza subiektywnie deklarowana efektywnosc, ale jednoczesnie obniza poziom krytycznego myslenia"
- "Wartosc = nauczyles sie pracowac z AI, wiedza zostaje u ciebie" (moj model vs Rudy)

**Co metodologia daje:**
- "Knowledge Empowerment" vs "Productized Consulting" - swiadomy wybor modelu
- Transparency: "Supervision is context curation" - wiesz co AI widzi
- Budowanie: context engineering jako transferowalna umiejetnosc (nie vendor lock-in)

---

#### JOB M5: Przejscie od eksperymentu do systemu
> "Kiedy juz wiem ze AI moze mi pomoc w pojedynczych zadaniach, chce zbudowac systematyczne podejscie, zeby wartosc sie kumulowala zamiast zaczynac od zera"

**Kontekst sytuacyjny:**
- "Probowalem, dziala, ale to wciaz chaos"
- Rosnace rozczarowanie: pojedyncze sukcesy, brak systemu
- Poczucie ze "musi byc lepszy sposob"

**Cytaty z researchu:**
- "Tylko 22% firm wykracza poza etap proof of concept"
- "Zaledwie 4% osiaga istotne korzysci z AI"
- "W 2026 roku nie wystarczy wykazac, ze AI dziala - musi dzialac lepiej, szybciej lub taniej"
- "Od promptu do systemu" (hook dla ludzi ktorzy juz uzywaja AI)

**Co metodologia daje:**
- Workspace model: filesystem jako collaboration surface
- Kumulacja: "Every session builds on previous" vs "every session from scratch"
- "If pattern reliable, human moves up one abstraction level"

---

### KATEGORIA 3: STRATEGIA ORGANIZACYJNA

#### JOB M6: Eksternalizacja wiedzy jako przewaga
> "Kiedy buduje firme oparta na wiedzy eksperckiej, chce wyciagnac te wiedze z glow ludzi do systemu, zeby stala sie trwala przewaga konkurencyjna"

**Kontekst sytuacyjny:**
- "Wiedza jest w glowach, jak ktos odejdzie - tracimy"
- Dokumentacja "niby jest" ale nikt jej nie czyta
- Potrzeba: wiedza musi byc "zywa", nie martwa

**Cytaty z researchu:**
- "Models are commoditizing. Everyone has access to GPT-4, Claude, Gemini. The new competitive advantage is externalized organizational expertise"
- "Documentation for humans: Maybe someone reads it someday. Externalized knowledge for agents: Agent executes it immediately"
- "Context is the new moat. Same model, different results"
- "The team that can externalize what they know and feed it to agents in a structured way will build things competitors can't copy"

**Co metodologia daje:**
- Framework: "Your domain knowledge becomes executable capability"
- Zmiana ROI dokumentacji: nie "moze ktos przeczyta" ale "agent uzyje natychmiast"
- Strategic narrative: "Gems to frontend. My budujemy backend wiedzy Waszej firmy"

---

#### JOB M7: Madre decyzje o inwestycjach w AI
> "Kiedy slysze hype o AI i autonomicznych agentach, chce rozumiec co naprawde dziala, zebym mogl podejmowac racjonalne decyzje inwestycyjne"

**Kontekst sytuacyjny:**
- Bombardowany narracja "AI wszystko zautomatyzuje"
- Widzi 70% failure rate w enterprise
- Nie chce wydac pieniedzy na "AI theater"
- Szuka "rzeczywistej wiedzy" vs marketing

**Cytaty z researchu:**
- "Polish SMEs are hearing the AI narrative: autonomous agents, automation, replacement of human work. Enterprise reports show 70%+ failure rates on agent deployments"
- "Opoznione wdrozenia uszczuplaja wartosc firmy srednio o 8,6%"
- "Firmy przesuwaja srodki z efektownych eksperymentow w strone infrastruktury, integracji danych i automatyzacji"
- "Zapomniej o 'autonomicznych agentach'. Pokazemy ci, jak naprawde pracowac z AI"

**Co metodologia daje:**
- Trzecia droga: miedzy chatem a autonomia
- ROI calculation: konkretne oszczednosci (np. case Dagny: ~120h/rok)
- Realistyczne oczekiwania: "This is the decade of agents, not the year" (Karpathy)

---

#### JOB M8: Skalowalnosc kompetencji w zespole
> "Kiedy jeden czlowiek w zespole 'umie AI', chce zeby ta umiejetnosc rozprzestrzennila sie na reszte, zeby cala organizacja byla bardziej efektywna"

**Kontekst sytuacyjny:**
- "Mamy jednego power usera, reszta ledwo uzywa"
- Brak standardow = kazdy robi po swojemu
- Transfer wiedzy nie dziala

**Cytaty z researchu:**
- "Luka kompetencyjna jako glowna bariera (45% firm)"
- "Junior moze przeczytac pliki, rozumie skad biora sie instrukcje, moze zaproponowac poprawki"
- "Kazdy pracuje w izolowanym kontekscie. Ale wszyscy operuja na tym samym pliku (Single Source of Truth)"

**Co metodologia daje:**
- Externalized knowledge = teachable system
- Context Engineering Skill Development Program (levels 0-3)
- Team-level capability: "Learning Organization 2.0"

---

## Priorytetyzacja Jobs

### Kryterium: Czy job wymaga metodologii?

| Job | Wymaga metodologii? | Alternatywy? | Priorytet |
|-----|:-------------------:|:------------:|:---------:|
| M1: Model mentalny | TAK - core value | DIY mozliwe ale wolne | **KRYTYCZNY** |
| M2: Context engineering | TAK - praktyczna umiejetnosc | DIY mozliwe ale trudne | **KRYTYCZNY** |
| M6: Eksternalizacja wiedzy | TAK - strategiczny insight | Nikt inny nie mowi | **KRYTYCZNY** |
| M7: Madre decyzje AI | TAK - kontra-narracja | Troche w mediach | **WYSOKI** |
| M3: Powtarzalnosc | TAK ale tools tez pomagaja | Narzedzia sie poprawiaja | SREDNI |
| M4: Bez uzaleznienia | TAK ale mniej pilne | Swiadomosc rosnie organicznie | SREDNI |
| M5: Od eksperymentu do systemu | TAK | Tools + DIY moga wystarczyc | SREDNI |
| M8: Skalowalnosc w zespole | TAK ale enterprise-focused | Szkolenia korporacyjne | NISKI (dla SME) |

### Top 3 Jobs dla komunikacji:

1. **M1 + M2**: "JAK pracowac z AI" - praktyczna metodologia, nie teoria
2. **M6**: "Wiedza jako moat" - strategiczny insight dla decision makers
3. **M7**: "Trzecia droga" - kontra-narracja vs hype

---

## Wzorce

### Wzorzec A: "Brak modelu mentalnego"
Jobs M1, M2, M3 lacza sie: **ludzie nie wiedza JAK myslec o pracy z AI**.

Symptomy:
- Losowe wyniki ("czasem dziala, czasem nie")
- Frustracja z narzedziami
- Proby "lepszych promptow" zamiast lepszego systemu

Rozwiazanie metodologii: Framework + praktyki + feedback loop

### Wzorzec B: "Gap kompetencyjny"
Jobs M4, M5, M8 lacza sie: **od eksperymentu do kompetencji jest przepasc**.

Symptomy:
- PoC dziala, production nie
- Power user, reszta nie uzywa
- "Wiemy ze powinnismy, ale nie wiemy jak"

Rozwiazanie metodologii: Skill development + team capability building

### Wzorzec C: "Strategic blindness"
Jobs M6, M7 lacza sie: **brak strategicznego rozumienia AI w biznesie**.

Symptomy:
- Decyzje na podstawie hype'u
- Brak ROI z inwestycji w AI
- "Autonomiczne agenty" jako cel

Rozwiazanie metodologii: Strategic narrative + realistic expectations + competitive moat framing

---

## Mapowanie na oferty

| Job | AI Workspace Build | Workflow Sprints | Skill Development |
|-----|:------------------:|:----------------:|:-----------------:|
| M1: Model mentalny | implicitly | implicitly | **CORE** |
| M2: Context engineering | **CORE** | TAK | **CORE** |
| M3: Powtarzalnosc | **CORE** | **CORE** | TAK |
| M4: Bez uzaleznienia | TAK | TAK | **CORE** |
| M5: Eksperyment->system | **CORE** | TAK | TAK |
| M6: Eksternalizacja | **CORE** | NIE | TAK (strategic) |
| M7: Madre decyzje | strategic | strategic | strategic |
| M8: Team capability | team package | NIE | **CORE** (Level 3) |

---

## Kluczowe Wnioski

### 1. Jobs sa o ROZUMIENIU, nie o FUNKCJACH
Poprzednia wersja: "chce ciaglosc kontekstu" (feature)
Ta wersja: "chce wiedziec JAK pracowac z AI" (competence)

### 2. Metodologia jest defensible
Narzedzia mozna skopiowac. Metodologia wymaga:
- Glebokiego zrozumienia problemu
- Doswiadczenia we wdrozeniach
- Aktualizacji wraz z ewolucja technologii

### 3. Tool-agnostic = strategiczna przewaga
Klient nie jest locked-in do konkretnego narzedzia.
Metodologia dziala z Claude, ChatGPT, Cursor, cokolwiek.

### 4. Dwa poziomy wartosci
- **Poziom taktyczny**: "Naucz mnie context engineering"
- **Poziom strategiczny**: "Pomoz mi zbudowac przewage konkurencyjna z eksternalizowanej wiedzy"

---

*Nastepny krok: alternatives-v2.md - konkurencja jako scenariusze, nie produkty.*
