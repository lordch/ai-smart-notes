# Analiza Strategiczna - Jobs to Be Done

## Executive Summary

Twoja najsilniejsza pozycja to **jobs wymagajace trwalosci, audytowalnosci i wspolpracy zespolowej** - obszary gdzie proste narzedzia (Gems, Cowork, Copilot) maja fundamentalne ograniczenia architektoniczne, ktorych nie zamkna w perspektywie 12-18 miesiecy. Kluczowy segment to **branze regulowane i firmy budujace wiedze jako aktywo** - tu "good enough" nie wystarcza, bo konsekwencje bledow sa zbyt wysokie. Timeline risk jest realny dla jobs zwiazanych z jakoscia outputow i prostymi workflow'ami - Cowork moze byc "good enough" w ciagu roku. Rekomendacja: skoncentruj marketing na compliance/audyt i eksternalizacji wiedzy, entry point to Workflow Implementation Sprint dla branzy regulowanej.

---

## 1. Jobs ktore wygrywam

### WYGRYWAM ZDECYDOWANIE (przewaga strukturalna, nie do nadrobienia)

**JOB 4: Wersjonowanie i audytowalnosc**
- **Dlaczego wygrywam**: Git jako fundament to architektura, nie feature. Zadna platforma chatowa nie da pelnej traceability. "git log", "git diff", "git blame" - to standard przemyslowy, nie wlasne rozwiazanie.
- **Trwalosc przewagi**: Permanentna. Platformy moga dodac "historia wersji", ale nie pelny git z branchami, merge'ami, PR-ami.
- **Kluczowy segment**: Branze regulowane (prawo, finanse, audyt, sektor publiczny), firmy z wymaganiami compliance (EU AI Act).

**JOB 5: Skalowalne zarzadzanie zmianami**
- **Dlaczego wygrywam**: "CEO zmienia zdanie? Edytujesz jeden plik." vs "Edytujesz 50 Gemsow/Projects". Single Source of Truth to architektura, nie feature.
- **Trwalosc przewagi**: Wysoka. Platformy by design izoluja uzytkownikow/projekty. Centralizacja wymaga fundamentalnej przebudowy.
- **Kluczowy segment**: Zespoly 5-20 osob z dynamicznymi wytycznymi, firmy w fazie transformacji.

**JOB 6: Wspolpraca zespolowa na wspolnym kontekscie**
- **Dlaczego wygrywam**: Cowork Projects sa prywatne. Gems sa per-user. Copilot daje dostep do dokumentow, ale nie "wspolny kontekst AI". Wspolne repozytorium = kazdy widzi to samo.
- **Trwalosc przewagi**: Wysoka (12-18 mies). Anthropic moze dodac team features, ale to wymaga przebudowy modelu licencjonowania i infrastruktury.
- **Kluczowy segment**: Male zespoly knowledge workers (konsulting, prawo, research).

**JOB 10: Eksternalizacja ekspertyzy do systemu**
- **Dlaczego wygrywam**: "Domain knowledge becomes executable capability". To nie feature - to metodologia (Context Engineering). Trzeba wiedziec CO eksternalizowac, JAK strukturyzowac, GDZIE przechowywac.
- **Trwalosc przewagi**: Permanentna. Narzedzia moga ulatwiac, ale metodologia pozostaje roznicnikiem.
- **Kluczowy segment**: Firmy budujace wiedze jako aktywo, konsultanci z unikalna metodologia, eksperci domenowi.

### WYGRYWAM MOCNO (przewaga wyrazna, ale konkurencja moze sie przyblizyc)

**JOB 1: Ciaglosc kontekstu miedzy sesjami**
- **Dlaczego wygrywam**: Filesystem jako "pamiec zewnetrzna" - pliki persystentne, zawsze dostepne. Nie ma limitu tokenow w "pamieci" (jest limit w sesji).
- **Ryzyko konkurencji**: SREDNIE. Cowork Projects daja pewna ciaglosc. Anthropic moze dodac "project memory" w 6-12 mies. Ale filesystem pozostaje bardziej elastyczny.
- **Kluczowy segment**: Power users z zlozony projektami, anyone doing multi-week projects.

**JOB 8: Systematyczny workflow dla zlozonych zadan**
- **Dlaczego wygrywam**: Foldery per task = izolacja kontekstu. tasks/ jako przestrzen robocza. Checkpointy w plikach. Gems/Cowork mieszaja wszystko w jednym watku.
- **Ryzyko konkurencji**: SREDNIE. Cowork Artifacts to checkpointy "light". Ale brak struktury folderow, brak izolacji miedzy subtaskami.
- **Kluczowy segment**: Researchers, analitycy, konsultanci z multi-step deliverables.

---

## 2. Jobs ktorych nie wygrywam

### PRZEGRYWAM LUB TIE (nie warto konkurowac)

**JOB 9: Budowanie kompetencji (nie uzaleznienie)**
- **Problem**: DIY robi to "za darmo". Entuzjasta z czasem nauczy sie sam.
- **Rekomendacja**: Nie sprzedawac na tym jobie. To jest "nice to have" w moich ofertach, nie core value prop. Podkreslac jako bonus, nie glowny argument.

**JOB 7: Onboarding nowych osob**
- **Problem**: Niska czestotliwosc, srednia intensywnosc. Copilot + dokumentacja firmowa moze wystarczyc.
- **Rekomendacja**: Nie budowac marketingu na tym. Wspominac tylko w kontekscie JOB 6 (wspolpraca zespolowa).

**JOB 11: Przejscie od PoC do wartosci**
- **Problem**: Contestable. Copilot/Cowork moga byc "good enough" dla prostszych use cases. Rynek sie uczy - wiecej firm przejdzie PoC samodzielnie.
- **Rekomendacja**: Workflow Sprints adresuja to, ale nie pozycjonowac jako "pomagamy przejsc PoC". Lepiej: "budujemy infrastructure-grade rozwiazania".

### JOBS GDZIE ALTERNATYWY WYSTARCZAJA

**JOB 3: Unikalnosc outputow**
- Cowork + dobre prompty + pelny kontekst w Project = "good enough" dla wielu.
- Nie wygrywam architektura - wygrywam metodologia. Slabsza pozycja.

**JOB 12: Stabilnosc wynikow**
- Cowork Artifacts + iteracja = akceptowalne dla wielu.
- Moja przewaga (pelna kontrola kontekstu) jest realna, ale trudna do zademonstrowania w krotkim demo.

**JOB 2: Bezpieczenstwo danych**
- Copilot z lokalnym przetwarzaniem (od 2026 dla sektora publicznego) zamyka luke.
- Nadal wygrywam dla firm spoza M365, ale to mniejszy segment.

---

## 3. Messaging i komunikacja

### Kluczowe przekazy

**Glowny przekaz (umbrella):**
> "Gems to frontend. My budujemy backend wiedzy Twojej firmy."

**Dla branzy regulowanej (compliance):**
> "Pelna traceability. Audytor widzi kazda zmiane, kazda decyzje. Git log to Twoj dziennik compliance."

**Dla zespolow:**
> "Kazdy pracuje w swoim kontekscie, ale wszyscy operuja na tym samym zrodle prawdy. Koniec z 'ja mialem inna wersje instrukcji'."

**Dla ekspertow domenowych:**
> "Twoja wiedza w glowie to koszt utraconych mozliwosci. Wyeksternalizowana - to executable capability, ktora pracuje 24/7."

**Anty-przekazy (czego unikac):**
- NIE: "Pomagamy przejsc od PoC do wartosci" (zbyt generyczne)
- NIE: "AI pamięta Twój kontekst" (Cowork tez to mowi)
- NIE: "Ucz sie pracowac z AI" (DIY robi to za darmo)

### Dowody do zbudowania

**Must-have case studies:**

1. **Kancelaria prawna** - due diligence workflow
   - Metryki: czas na case, liczba zrodel, compliance audits passed
   - Story: "Audytor pytal o historię zmian. Pokazalismy git log. Koniec rozmowy."

2. **Firma consultingowa** - zespol 5-10 osob, wspolny knowledge base
   - Metryki: czas onboardingu nowego consultanta, consistency dokumentow
   - Story: "Nowy konsultant produktywny w 3 dni, nie 3 tygodnie."

3. **Ekspert domenowy** (lekarze-badacze, analitycy)
   - Metryki: czas na literature review, jakosc ekstrakcji
   - Story: "Moja metodologia teraz pracuje nawet gdy spie."

**Format case study:**
- Problem (cytaty klienta)
- Rozwiazanie (co zbudowalismy)
- Rezultat (metryki, ROI)
- "Dlaczego nie Copilot/Gems" (explicit porownanie)

### "Aha moment" dla klienta

**Dla compliance:**
> "Pokaz `git diff` miedzy wersja z 15 stycznia a dzisiejsza. Audytor widzi dokladnie co sie zmienilo, kiedy, przez kogo (lub przez AI pod czyja kontrola)."

**Dla zespolow:**
> "Otworz ten sam plik z dwoch komputerow. Edytuj. git pull. Wszyscy maja ta sama wersje. Zero Slacka, zero 'wyslij mi najnowsza wersje'."

**Dla ekspertow:**
> "Twoja instrukcja 'jak robimy due diligence' = plik. AI czyta plik. AI robi due diligence wg Twojej metodologii. Metodologia pracuje za Ciebie."

**Demo flow (15 min):**
1. (2 min) Pokaz chaos: "nowa sesja, AI nie wie nic"
2. (3 min) Pokaz pamiec: "otwieram folder, AI widzi caly kontekst"
3. (5 min) Pokaz workflow: "task folder -> research -> draft -> final, wszystko wersjonowane"
4. (3 min) Pokaz git: "historia zmian, diff, compliance-ready"
5. (2 min) "A teraz Twoj kolega otwiera ten sam folder..."

---

## 4. Idealny klient (ICP)

### Profil

**Stanowisko:**
- Partner/Senior Associate w kancelarii prawnej
- Manager/Senior w firmie consultingowej
- Head of Research/Analityk senior
- Founder/CEO malej firmy knowledge-intensive (5-20 osob)
- Chief Knowledge Officer / Chief Learning Officer

**Branża (priorytet):**
1. **Prawo** - compliance-driven, wysoka wartosc dokumentow
2. **Consulting** - zespolowa praca na artefaktach, powtarzalne deliverables
3. **Finanse** (doradztwo, analiza) - audytowalnosc, precision
4. **Research** (akademia, think-tanki) - dlugie projekty, wiele zrodel

**Charakterystyka firmy:**
- 5-50 osob (sweet spot: 10-25)
- Knowledge-intensive work (>60% czasu to praca intelektualna)
- Powtarzalne typy deliverables (raporty, opinie, analizy)
- Unikalna metodologia lub wiedza domenowa
- Regulacje lub klienci wymagajacy audytowalnosci

**Anty-profil (kogo NIE targetowac):**
- "Chce zeby zrobili za mnie" -> to segment Rudego (productized consulting)
- Brak czasu na wspolprace (0h/tydzien) -> Copilot
- Jednorazowe, proste use cases -> Gems/GPTs
- Duze korporacje (>200 osob) -> inne procesy zakupowe, inne potrzeby
- "Checkbox AI" ("musimy miec AI, bo wszyscy maja") -> Copilot

### Sygnaly dojrzalosci

**Sygnaly "gotowy do kupienia":**

1. **Juz uzywa AI, ale jest sfrustrowany:**
   - "ChatGPT nie pamieta co ustalilismy"
   - "Mam 47 Gemsow i nie wiem gdzie co jest"
   - "Kazdy w zespole ma inne instrukcje"

2. **Ma problem z compliance/audytem:**
   - "Audytor pyta o historie zmian"
   - "Nie moge udowodnic jak powstal ten dokument"
   - "EU AI Act - nie wiem co musimy robic"

3. **Ma wiedze w glowach ludzi:**
   - "Tylko Marek wie jak to robic"
   - "Jak odejdzie senior, tracimy metodologie"
   - "Onboarding trwa 3 miesiace"

4. **Probował DIY i utknął:**
   - "Zaczalem cos budowac, ale nie wiem jak dalej"
   - "Mam dokumenty, ale AI ich nie rozumie"
   - "Brakuje mi struktury"

**Czerwone flagi (nie kupować):**
- "Pokaz mi gotowe rozwiazanie, ja tylko klikam"
- "Nie mam czasu na spotkania w trakcie wdrozenia"
- "Nasz IT musi zatwierdzic wszystko" (korporacyjne procesy)
- "Potrzebujemy tego na wczoraj" (brak cierpliwosci na wdrozenie)

### Gdzie ich szukac

**Kanaly dotarcia:**

1. **Content marketing (organiczny):**
   - LinkedIn: posty o "context engineering", "dlaczego Gems nie wystarczaja"
   - Blog: case studies, porownania z alternatywami
   - Webinary: "Compliance w erze AI", "Zespolowa praca z AI"

2. **Partnerstwa:**
   - Izby branżowe (NRA, KIDP, izby konsultingow)
   - Firmy szkoleniowe (cross-selling po szkoleniach AI)
   - Software houses (oni budują custom, Ty budujesz metodologie)

3. **Eventy:**
   - Konferencje branzowe (prawnicze, consultingowe, finansowe)
   - AI meetupy (jako speaker, nie sponsor)

4. **Referrale:**
   - Zadowoleni klienci w tej samej branzy
   - "Marek z kancelarii X polecil"

**Wiadomosc cold outreach (przyklad dla kancelarii):**
> "Widzialem [artykul/post] o [temat]. Pracuje z kancelariami nad systematyzacja pracy z AI - tak zeby kazdy dokument mial pelna historie zmian i audytor nie zadawal pytan. Czy macie juz rozwiazanie tego typu, czy to jest na radarze?"

---

## 5. Risk Assessment

### Co moze sie zmienic (12-18 miesiecy)

**Claude Cowork - prawdopodobne zmiany:**
- **Lepsza pamiec projektowa** - "Project Memory" ktora trwa miedzy sesjami (WYSOKIE prawdopodobienstwo, 6-12 mies)
- **Team features** - wspoldzielenie projektow, role (SREDNIE, 12-18 mies, wymaga zmian licencjonowania)
- **Lepsza historia Artifacts** - wersjonowanie wewnatrz sesji (WYSOKIE, juz jest czesciowo)
- **Integracje z zewnetrznymi storage** - Google Drive, Dropbox (SREDNIE, 12 mies)

**Microsoft Copilot - prawdopodobne zmiany:**
- **Lokalne przetwarzanie** - juz zapowiedziane na 2026 dla sektora publicznego
- **Lepszy kontekst M365** - glebsza integracja z SharePoint, Teams
- **Agents/Skills** - customizowalne "mini-agenty" (juz w beta)
- **NIE zmieni**: fundamentalna architektura chat-first, brak git-like wersjonowania

**Gems/GPTs - prawdopodobne zmiany:**
- **Memory miedzy sesjami** - ChatGPT juz ma "Memory", bedzie lepsza
- **Team sharing** - ChatGPT Team juz pozwala dzielic GPTs
- **NIE zmieni**: fundamentalna izolacja, brak filesystem-based approach

### Trwale przewagi (2+ lata)

1. **Git jako fundament** - Nikt nie zbuduje lepszego VCS. Platformy moga nawiazywac, ale nie odtworza pelnego ekosystemu (branching, merging, PR, CI/CD).

2. **Przenoszalnosc** - Folder z plikami mozna przenosic miedzy narzedzami. Gems/Projects = vendor lock-in.

3. **Metodologia Context Engineering** - To umiejetnosc, nie feature. Nawet jesli narzedzia sie zmienia, metodologia pozostaje.

4. **Human-Agent Collaboration model** - To sposob myslenia o pracy, nie funkcjonalnosc. Konkurencja moze kopiowac features, nie framework mentalny.

5. **Enterprise-grade audytowalnosc** - Prawdziwy compliance wymaga standardow przemyslowych (git), nie "versioned artifacts".

### Timeline summary

| Obszar | Jak szybko konkurencja zamknie luke? | Co robic? |
|--------|--------------------------------------|-----------|
| Pamiec miedzy sesjami | 6-12 mies (Cowork) | Przesun messaging na "pelna kontrola", nie tylko "pamiec" |
| Team collaboration | 12-18 mies (Cowork Team) | Bulduj case studies zespolowe TERAZ |
| Wersjonowanie | 2+ lata (nikt nie odtworzy git) | To jest core differentiator - eksploatuj |
| Compliance/audyt | 2+ lata | Sweet spot - tu fokus marketingowy |
| Eksternalizacja wiedzy | Permanentna (metodologia) | Buduj content o Context Engineering |

---

## 6. Rekomendacje taktyczne

### Quick wins (teraz - najblizsze 4 tygodnie)

1. **Stworz one-pager dla branzy regulowanej**
   - Tytul: "AI Compliance dla kancelarii prawnych"
   - Zawiera: git = traceability, case study (jesli masz), EU AI Act implications
   - Uzyj do cold outreach

2. **Napisz 3 posty LinkedIn:**
   - "Dlaczego Gems nie wystarczaja dla pracy zespolowej"
   - "Historia zmian w dokumentach AI - jak to robic dobrze"
   - "CEO zmienil zdanie - ile kosztuje aktualizacja 50 Gemsow?"

3. **Przeprowadz 1-2 discovery calls z kancelariami prawnymi**
   - Cel: walidacja jobs, zebranie jezykamisow "jak mowia o problemie"
   - Nie sprzedawaj - sluchaj

4. **Przygotuj 15-min demo**
   - Flow opisany w sekcji 3
   - Nagrany jako video do wysylania

### Medium-term (3-6 miesiecy)

1. **Zbuduj pierwszy case study w branzy regulowanej**
   - Idealnie: kancelaria prawna lub doradztwo finansowe
   - Metryki: czas, compliance, ROI
   - Format: PDF + strona na blogu + video testimonial

2. **Uruchom webinar cykliczny**
   - Temat: "Compliance w erze AI" lub "Zespolowa praca z AI"
   - Czestotliwosc: miesiecznie
   - Cel: lead generation, pozycjonowanie jako ekspert

3. **Nawiaz partnerstwo z 1-2 izbami branzowymi**
   - NRA (Naczelna Rada Adwokacka) - dostep do kancelarii
   - KIDP (Krajowa Izba Doradcow Podatkowych) - dostep do doradcow

4. **Rozbuduj oferte Workflow Sprint dla legal/compliance**
   - Workflow: "Due Diligence z AI"
   - Pricing: 25,000-35,000 PLN
   - Deliverable: dzialajacy workflow + pelna dokumentacja + szkolenie zespolu

5. **Content hub o Context Engineering**
   - Seria artykulow: "Context Engineering 101", "102", "103"
   - Cel: pozycjonowanie jako inventor/owner terminu w Polsce

### Czego unikac

1. **Nie konkuruj cenowo ze szkoleniami**
   - Rynek szkolen AI: 790 - 10,000 PLN, duzo darmowych opcji (PARP, Gov.pl)
   - Twoja wartosc to wdrozenie, nie edukacja

2. **Nie targetuj "wszystkich knowledge workers"**
   - Zbyt szerokie = brak przekazu
   - Zacznij od 1 branzy (prawo), rozszerzaj po walidacji

3. **Nie walcz z Cowork na "prostych" jobsach**
   - Solo power user z prostymi projektami = Cowork wystarczy
   - Nie tracwsil na przekonywanie

4. **Nie ignoruj timeline risk**
   - Cowork bedzie lepszy za rok
   - Buduj case studies i pozycje TERAZ, zanim okno sie zamknie

5. **Nie obiecuj "magii"**
   - "AI zrobi wszystko samo" = antyprofil
   - Bądź jasny: "wymaga 3-5h/tydzien Twojego czasu przez 4-6 tygodni"

---

## Appendix: Zrodla analizy

### Pliki z workspace:
- `/home/user/ai-smart-notes/tasks/2026-01-22-porter/jobs-map.md` - mapa 12 jobs z priorytetyzacja
- `/home/user/ai-smart-notes/tasks/2026-01-22-porter/alternatives.md` - analiza 5 alternatyw vs jobs
- `/home/user/ai-smart-notes/tasks/2026-01-22-porter/research-raw.md` - surowy research (EY, BCG, Gartner, raporty polskie)

### Materialy zrodlowe (cytowane w research):
- Notatki ze spotkan: Rudy (GrowGo), mama, Agnieszka
- Dokumenty strategiczne: AI Workspace Build, Workflow Implementation Sprints
- Koncepty: Human-Agent Collaboration Framework, Context Engineering, Externalized Expertise
- Raporty zewnetrzne: EY AI adoption, BCG AI implementation, Gartner predictions

### Metodologia:
1. Jobs extraction - na podstawie workspace materials + web research
2. Alternatives mapping - ocena 5 alternatyw vs 12 jobs
3. Pattern analysis - identyfikacja wzorcow w jobsach
4. Competitive positioning - gdzie wygrywam vs gdzie nie warto
5. Timeline risk assessment - prognoza zmian w alternatywach
6. Tactical recommendations - actionable next steps

---

*Dokument stworzony: 2026-01-22*
*Autor: Analiza strategiczna JTBD*
*Status: Finalny*
