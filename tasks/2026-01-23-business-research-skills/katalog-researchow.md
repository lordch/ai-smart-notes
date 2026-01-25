# Katalog Business Research Skills

## Cel
Zbudować reużywalne Claude skille dla typowych researchów biznesowych — z podziałem na etapy, checkpointy, i gotowymi promptami.

## Lista researchów do rozwinięcia

### 1. Market Analysis
- **Trigger:** "Chcemy wejść w nowy segment/rynek"
- **Deliverable:** Market sizing, key players, barriers to entry, go-to-market implications
- **Źródła:** Industry reports, competitor websites, news, expert interviews

### 2. Competitive Intelligence
- **Trigger:** "Co robi konkurencja? Jak się pozycjonują?"
- **Deliverable:** Competitive matrix, positioning map, SWOT, feature comparison
- **Źródła:** Websites, pricing pages, case studies, reviews, job postings, news

### 3. Customer Discovery / ICP Research
- **Trigger:** "Kim jest nasz idealny klient? Jakie ma problemy?"
- **Deliverable:** Persona, Jobs-to-be-Done, pain points, buying triggers
- **Źródła:** Interviews, surveys, reviews, forum discussions, support tickets

### 4. Due Diligence
- **Trigger:** "Rozważamy akwizycję/inwestycję/partnera"
- **Deliverable:** Risk assessment, red flags, valuation inputs, integration considerations
- **Źródła:** Financial statements, contracts, news, references, public records

### 5. Trend Analysis / Technology Scout
- **Trigger:** "Co zmienia naszą branżę? Jakie technologie obserwować?"
- **Deliverable:** Trend radar, maturity assessment, implications for strategy
- **Źródła:** Research papers, VC investments, patent filings, conference talks, expert blogs

### 6. Pricing Research
- **Trigger:** "Jak nas pozycjonować cenowo? Ile klienci zapłacą?"
- **Deliverable:** Price benchmarks, packaging options, willingness-to-pay analysis
- **Źródła:** Competitor pricing, customer interviews, value analysis

### 7. Partnership / Vendor Evaluation
- **Trigger:** "Który vendor/partner wybrać?"
- **Deliverable:** Evaluation matrix, pros/cons, recommendation
- **Źródła:** Demos, references, reviews, case studies, contract terms

### 8. Regulatory / Compliance Scan
- **Trigger:** "Jakie regulacje nas dotyczą? Co się zmienia?"
- **Deliverable:** Compliance checklist, risk areas, timeline of changes
- **Źródła:** Legal texts, regulatory announcements, industry associations, legal opinions

### 9. Talent / Skills Gap Analysis
- **Trigger:** "Jakich kompetencji potrzebujemy? Jak wygląda rynek?"
- **Deliverable:** Skills matrix, market rates, sourcing strategy
- **Źródła:** Job postings, salary surveys, LinkedIn data, training programs

### 10. Content / Messaging Research
- **Trigger:** "Jak mówi nasza branża? Jakie tematy rezonują?"
- **Deliverable:** Messaging audit, content gaps, topic clusters, voice guidelines
- **Źródła:** Competitor content, social media, search trends, customer language

---

## Wspólna struktura (template)

### Fazy + Checkpointy

| Faza | Checkpoint | Artifact |
|------|------------|----------|
| 1. Briefing | Research questions defined | `brief.md` |
| 2. Source mapping | Sources identified + prioritized | `sources.md` |
| 3. Data gathering | Raw data collected | `raw-notes.md` |
| 4. Analysis | Patterns + insights identified | `analysis.md` |
| 5. Synthesis | Draft recommendations | `draft.md` |
| 6. Delivery | Final artifact ready | `deliverable.md` |

### Elementy każdego skilla
- Trigger (kiedy używać)
- Input requirements (co potrzebne na start)
- Fazy z checkpointami
- Przykładowe prompty per faza
- Output template
- Quality criteria (jak ocenić czy dobrze)
- Failure modes (na co uważać)

---

## Następne kroki
1. [ ] Wybrać 2-3 researchery do pełnego rozwinięcia jako pierwsze
2. [ ] Stworzyć template skilla
3. [ ] Rozwinąć pierwszy skill jako wzorcowy przykład
4. [ ] Przetestować na realnym case'ie

## Pytania do rozstrzygnięcia
- Czy skille mają być w `use-cases/research/` czy osobny folder `skills/`?
- Jak integrować z Claude Code (jako komendy `/research-market`)?
- Jaki format: markdown czy coś bardziej executable?

---

## Uznane metodologie (z dokumentacją)

### Jobs-to-be-Done (JTBD) → Customer Discovery
**Twórca:** Tony Ulwick (1990), spopularyzowane przez Claytona Christensena

**Universal Job Map — 8 kroków:**
1. Define & plan — klient tworzy plan podejścia
2. Locate input — identyfikacja potrzebnych informacji
3. Prepare — organizacja, filtrowanie, kwalifikacja
4. Confirm & validate — podejmowanie decyzji i walidacja
5. Execute — wykonanie akcji
6. Monitor — monitorowanie efektów
7. Modify — dostosowanie na podstawie nowych informacji
8. Conclude — zakończenie, wnioski

**JTBD Statement Formula:**
> "When [Circumstance], I want to [job], so I can [need/outcome] without [pain point]."

**Desired Outcomes:** 50-150 mierzalnych statements opisujących jak klient mierzy sukces

**Źródła:**
- [Strategyn - JTBD Comprehensive Guide](https://strategyn.com/jobs-to-be-done/)
- [Tony Ulwick - JTBD Framework](https://jobs-to-be-done.com/jobs-to-be-done-a-framework-for-customer-needs-c883cbf61c90)
- [thrv - Building JTBD Templates Step-by-Step](https://www.thrv.com/blog/building-effective-jobs-to-be-done-templates-a-step-by-step-deep-dive)

---

### Steve Blank's Customer Discovery → Customer/ICP Research
**Twórca:** Steve Blank (lata 90.)

**4-Step Process:**
1. **Build contact list** — 50 nazwisk z sieci kontaktów
2. **Problem presentation** — prezentacja hipotez, zbieranie feedbacku (NIE sprzedaż!)
3. **Solution presentation** — sprawdzenie czy klienci wykazują zainteresowanie zakupem
4. **Iterate** — aktualizacja hipotez na podstawie feedbacku

**Kluczowe zasady:**
- Founderzy muszą robić to osobiście (nie delegować)
- Wywiady > ankiety (więcej swobody eksploracji)
- "Breaking assumptions" zamiast potwierdzania
- Low burn rate dopóki nie ma walidacji

**Źródła:**
- [Steve Blank - Customer Discovery](https://steveblank.com/tag/customer-discovery/)
- [MaRS - Blank's Customer Discovery Method](https://learn.marsdd.com/article/blanks-customer-discovery-method-part-2-the-customer-development-model-in-value-proposition/)
- [Future Founders - 4-Step Guide](https://www.futurefounders.com/news-article/what-is-customer-discovery-4-step-guide-to-building-the-right-product-for-the-right-customers/)

---

### TAM/SAM/SOM → Market Analysis
**Definicje:**
- **TAM** (Total Addressable Market) — cały rynek, 100% share
- **SAM** (Serviceable Available Market) — segment który możesz obsłużyć
- **SOM** (Serviceable Obtainable Market) — realistyczny share do zdobycia

**6-Step Process:**
1. **Define market** — kategoria produktu/usługi
2. **Define ICP** — firmographics, behavioral, technographics
3. **Calculate TAM** — (liczba klientów) × (średni roczny przychód)
4. **Calculate SAM** — filtry: geografia, wielkość, product fit
5. **Calculate SOM** — uwzględnienie zasobów, konkurencji, sales capacity
6. **Develop strategies** — jak zwiększyć share

**Dwa podejścia:**
- **Top-down:** raporty branżowe → zawężanie
- **Bottom-up:** dane własne, CRM, surveys (bardziej wiarygodne dla inwestorów)

**Źródła:**
- [Antler - TAM SAM SOM Guide](https://www.antler.co/blog/tam-sam-som)
- [HG Insights - Complete Guide to Market Sizing](https://hginsights.com/2025/03/07/tam-sam-som-the-complete-guide-to-market-sizing/)
- [Data-Mania - Top-Down Market Sizing Step-by-Step](https://www.data-mania.com/blog/top-down-market-sizing-tam-sam-som-guide/)

---

### Porter's Five Forces → Market/Competitive Analysis
**Twórca:** Michael Porter (1979, Harvard)

**5 sił:**
1. Competitive Rivalry
2. Threat of New Entrants
3. Bargaining Power of Suppliers
4. Bargaining Power of Customers
5. Threat of Substitutes

**7-Step Process:**
1. **Identify key players** — struktura branży, gracze, dostawcy, kupujący
2. **Brainstorm & research** — listy dla każdej kategorii
3. **Gather industry data** — raporty (IBISWorld, S&P), trade journals
4. **Evaluate each force** — bariery wejścia, koncentracja dostawców/kupujących
5. **Rate the forces** — "++" / "+" / "o" / "-" / "--"
6. **Compile & summarize** — kluczowe insighty i patterns
7. **Develop strategic responses** — jak konkurować

**Źródła:**
- [Cascade - Porter's Five Forces Complete Guide](https://www.cascade.app/blog/porters-5-forces)
- [Quantive - Porter's 5 Forces Framework](https://quantive.com/resources/articles/porters-5-forces)
- [MindTools - Porter's Five Forces](https://www.mindtools.com/at7k8my/porter-s-five-forces/)

---

### SCIP Intelligence Cycle → Competitive Intelligence
**Organizacja:** Strategic Consortium of Intelligence Professionals

**4-Phase Intelligence Cycle:**
1. **Obtain requests** — zdefiniowanie potrzeb intelligence
2. **Collect information** — gathering z różnych źródeł
3. **Analyze & synthesize** — analiza, łączenie, wnioski
4. **Communicate findings** — rekomendacje dla decydentów

**Kluczowa zasada:** "Intelligence is more than information" — wystarczająco dużo czasu na analizę

**Źródła:**
- [SCIP - Foundational Tools and Practices](https://www.scip.org/page/Competitive-Intelligence-Foundational-Tools-and-Practices)
- [SCIP - How to Deliver Insights](https://www.scip.org/page/How_to_Deliver_Insights)
- [Wikipedia - Competitive Intelligence](https://en.wikipedia.org/wiki/Competitive_intelligence)

---

### Van Westendorp Price Sensitivity Meter → Pricing Research
**Twórca:** Peter Van Westendorp (1976)

**6-Step Process:**
1. **Ask 4 questions:**
   - Za jaką cenę produkt byłby zbyt drogi? (too expensive)
   - Za jaką cenę drogi, ale rozważyłbyś? (expensive but acceptable)
   - Za jaką cenę to okazja? (bargain)
   - Za jaką cenę podejrzanie tani? (too cheap)
2. **Collect & organize data** — lista unikalnych price points
3. **Calculate cumulative frequencies** — dla każdej kategorii
4. **Plot price sensitivity graph** — X=cena, Y=% respondentów
5. **Identify intersections:**
   - PMC (Point of Marginal Cheapness) — dolna granica
   - PME (Point of Marginal Expensiveness) — górna granica
   - OPP (Optimal Price Point) — przecięcie "too cheap" i "too expensive"
   - IPP (Indifference Price Point) — "normalna" cena
6. **Determine acceptable price range** — PMC do PME

**Źródła:**
- [SurveyMonkey - Van Westendorp Guide](https://www.surveymonkey.com/market-research/resources/van-westendorp-price-sensitivity-meter/)
- [Conjointly - Van Westendorp PSM](https://conjointly.com/products/van-westendorp/)
- [Conjointly - Manual Calculation](https://conjointly.com/guides/manual-calculation-of-van-westendorp/)

---

### M&A Due Diligence → Due Diligence
**Timeline:** 30-90 dni (może dłużej przy regulatory review)

**5-Step Process:**
1. **Define scope & objectives** — risk areas, zespół cross-functional
2. **Request & organize documents** — data request list, virtual data room
3. **Build DD team** — legal, real estate, IP, environmental, HR specialists
4. **Review key information:**
   - Financials (income statements, balance sheets, tax)
   - Legal (contracts, litigation, IP, corporate structure)
   - HR (employment agreements, benefits, org chart)
   - Interviews z key personnel
5. **Compile reports** — valuation, risks, compliance requirements

**Zespół:** 6-8 wyspecjalizowanych teamów równolegle

**Źródła:**
- [DFIN - Complete M&A Due Diligence Checklist](https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/m-a-due-diligence-checklist)
- [Diligent - 20-Point Checklist](https://www.diligent.com/resources/blog/mergers-acquisitions-due-diligence-checklist)
- [Dealroom - 7 Vital Steps](https://dealroom.net/faq/due-diligence-process)
- [Intralinks - 5 Steps of DD Process](https://www.intralinks.com/guides/due-diligence-process)

---

## Metodologie zbierania i oceny źródeł

### Problem
Kluczowe pytania w każdym researchu:
1. **Completeness** — czy szukałem pod wystarczająco wieloma kątami?
2. **Saturation** — skąd wiem że mam "dość"?
3. **Quality** — czy źródła są wartościowe?
4. **Verification** — czy informacje są prawdziwe?
5. **Transparency** — jak udokumentować proces?

---

### 1. Saturation (kiedy przestać szukać)
**Pochodzenie:** Glaser & Strauss (1967), badania jakościowe

**Definicja:** Punkt w którym nowe źródła nie wnoszą nowych tematów/informacji.

**Praktyczne wytyczne:**
- Pierwsze 5-6 źródeł daje większość nowych informacji
- Po ~12 źródłach w homogenicznej grupie osiągamy wysoką saturację
- **"Stopping criterion"**: minimum N źródeł, potem kontynuuj aż 3 kolejne nie wnoszą nic nowego

**Typy saturacji:**
- **Thematic saturation** — tematy zaczynają się powtarzać
- **Data saturation** — te same fakty z różnych źródeł
- **Theoretical saturation** — model/teoria się stabilizuje

**Dla agenta AI:**
> Jeśli ostatnie 3 wyszukiwania nie wniosły nowych tematów → można zakończyć gathering

**Źródła:**
- [PMC - Saturation in Qualitative Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC5993836/)
- [PLOS One - Simple Method to Assess Thematic Saturation](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0232076)

---

### 2. CRAAP Test (ocena jakości źródła)
**Twórca:** Sarah Blakeslee, California State University Chico (2004)

**5 kryteriów:**

| Kryterium | Pytania |
|-----------|---------|
| **Currency** | Kiedy opublikowane? Czy temat wymaga aktualności? Czy były update'y? |
| **Relevance** | Czy odpowiada na moje pytanie? Głębokość vs potrzeby? |
| **Authority** | Kim jest autor? Credentials? Afiliacja? Ekspert w temacie? |
| **Accuracy** | Czy claims są udokumentowane? Cytowane źródła? Można zweryfikować? |
| **Purpose** | Po co powstało? Inform/persuade/sell? Bias? Konflikt interesów? |

**Dla agenta AI:**
> Przed włączeniem źródła do analizy — quick CRAAP check każdego

**Źródła:**
- [CSU Chico - CRAAP Test](https://library.nwacc.edu/sourceevaluation/craap)
- [Wikipedia - CRAAP Test](https://en.wikipedia.org/wiki/CRAAP_test)

---

### 3. Lateral Reading (weryfikacja przez zewnętrzne źródła)
**Pochodzenie:** Stanford History Education Group, metoda fact-checkerów

**Vertical vs Lateral:**
- **Vertical reading** — czytasz źródło od góry do dołu, ufasz temu co mówi o sobie
- **Lateral reading** — otwierasz nowe taby, sprawdzasz co INNE źródła mówią o tym źródle

**4 Moves and a Habit:**
1. **Check for previous work** — czy ktoś już to zweryfikował? (Wikipedia, Snopes, Politifact)
2. **Go upstream to source** — dotrzeć do oryginalnego źródła informacji
3. **Read laterally** — co inne strony mówią o tym autorze/organizacji?
4. **Circle back** — jeśli ślepy zaułek, zmień podejście

**Dla agenta AI:**
> Nie ufaj temu co strona mówi o sobie. Zawsze sprawdź zewnętrznie.

**Źródła:**
- [Civic Online Reasoning - Lateral vs Vertical Reading](https://cor.inquirygroup.org/curriculum/lessons/lateral-vs-vertical-reading/)
- [TeachHUB - Lateral Reading vs Vertical Reading](https://www.teachhub.com/professional-development/2020/10/lateral-reading-vs-vertical-reading-differences-and-benefits/)

---

### 4. Triangulation (wielokrotna weryfikacja)
**Pochodzenie:** Campbell & Fiske (1959), nawigacja → nauki społeczne

**Definicja:** Używanie wielu źródeł/metod/perspektyw do weryfikacji tych samych wniosków.

**4 typy triangulacji (Denzin):**

| Typ | Opis | Przykład |
|-----|------|----------|
| **Data triangulation** | Wiele źródeł danych | Raporty + wywiady + dane publiczne |
| **Methodological** | Różne metody zbierania | Desk research + surveys + interviews |
| **Investigator** | Wielu badaczy niezależnie | Dwóch analityków osobno, porównanie |
| **Theory** | Różne frameworki interpretacyjne | SWOT + Porter + PESTEL na te same dane |

**Dla agenta AI:**
> Kluczowe wnioski muszą być potwierdzone przez ≥2 niezależne źródła

**Źródła:**
- [Scribbr - Triangulation in Research](https://www.scribbr.com/methodology/triangulation/)
- [NN/g - Triangulation Better Research Results](https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/)

---

### 5. Systematic Search Strategy (exhaustive searching)
**Pochodzenie:** Evidence-based medicine, systematic literature reviews

**Kluczowe zasady:**
- **Sensitivity > Precision** — lepiej mieć za dużo niż pominąć coś ważnego
- **Minimum 3 bazy/źródła** — nie polegać na jednym
- **Keywords + controlled vocabulary** — różne sposoby opisu tego samego
- **Grey literature** — nie tylko publikacje, też raporty, prezentacje, blogi ekspertów

**Dokumentacja (PRISMA standard):**
- Pełna search strategy (dokładnie jak uruchomiona)
- Liczba wyników per źródło
- Kryteria włączenia/wykluczenia
- Flow diagram (ile znaleziono → ile przeszło screening → ile włączono)

**Dla agenta AI:**
> Dokumentuj: jakie queries, w jakich źródłach, ile wyników, ile użytecznych

**Źródła:**
- [PMC - Systematic Approach to Searching](https://pmc.ncbi.nlm.nih.gov/articles/PMC6148622/)
- [PRISMA-S - Search Reporting Extension](https://link.springer.com/article/10.1186/s13643-020-01542-z)
- [Covidence - How to Write Search Strategy](https://www.covidence.org/blog/how-to-write-search-strategy-for-your-systematic-review/)

---

### 6. Iteracyjne zbieranie źródeł

#### Problem
Research nie jest liniowy. Wnioski z analizy prowadzą do:
- Nowych pytań których nie przewidziałem
- Nowych terminów/keywords których nie znałem
- Nowych źródeł na które trafiłem przez cytowania
- Luk w wiedzy które trzeba uzupełnić

#### Grounded Theory / Constant Comparative Method
**Twórcy:** Glaser & Strauss (1960s)

**Kluczowa idea:** Zbieranie i analiza dzieją się **równocześnie**, nie sekwencyjnie.

**Proces:**
```
collect → analyze → discover gaps → collect more → analyze → ...
```

**Zasady:**
- Nie czekaj z analizą aż zbierzesz wszystko
- Każda analiza może ujawnić nowe pytania
- Porównuj nowe dane z już zebranymi (constant comparison)
- Kontynuuj aż **theoretical saturation** — nowe dane nie zmieniają wniosków

**Dla agenta AI:**
> Po każdej partii źródeł — mini-analiza. Czy pojawiły się nowe pytania/terminy? Jeśli tak → nowa runda szukania.

**Źródła:**
- [Simply Psychology - Constant Comparative Method](https://www.simplypsychology.org/constant-comparative-method.html)
- [ATLAS.ti - Constant Comparison](https://atlasti.com/research-hub/constant-comparative-method)
- [PMC - Grounded Theory Framework for Novice Researchers](https://pmc.ncbi.nlm.nih.gov/articles/PMC6318722/)

---

#### Snowballing / Pearl Growing / Citation Chaining
**Metafora:** Mała perła rośnie warstwa po warstwie. Śnieżka toczy się i zbiera więcej śniegu.

**Kluczowa idea:** Jedno dobre źródło prowadzi do następnych.

**Dwa kierunki:**

| Kierunek | Pytanie | Narzędzie |
|----------|---------|-----------|
| **Backward chaining** | "Kogo cytuje to źródło?" | Bibliografia artykułu |
| **Forward chaining** | "Kto cytuje to źródło?" | Google Scholar "Cited by", Scopus |

**Statystyka:** Do 51% źródeł w systematic reviews pochodzi z snowballingu, nie z pierwotnego searchu.

**Hybrid strategy:**
1. Database search → initial set
2. Snowballing na najlepszych źródłach → extended set
3. Repeat aż saturation

**Dla agenta AI:**
> Dla każdego high-quality źródła: sprawdź bibliografię (backward) i "cited by" (forward)

**Źródła:**
- [MediWrite - Pearl Growing in Systematic Searching](https://www.mediwrite.com.au/medical-writing/pearl-growing/)
- [Oxbridge Essays - Snowballing Guide](https://www.oxbridgeessays.com/blog/snowballing-in-research-a-complete-guide-to-citation-chaining/)
- [ScienceDirect - Hybrid Search Strategy](https://www.sciencedirect.com/science/article/pii/S0950584922000659)

---

## Framework dla agentowego researchu (iteracyjny)

Na podstawie powyższych metodologii — propozycja struktury dla AI research skills.

**Kluczowa zmiana:** To NIE jest wodospad. Fazy się przeplatają i powtarzają.

```
    ┌─────────────────────────────────────────────┐
    │                                             │
    ▼                                             │
┌───────────┐    ┌───────────┐    ┌───────────┐  │
│  Search   │───▶│  Gather   │───▶│  Analyze  │──┤
│  Strategy │    │  + Eval   │    │  (mini)   │  │
└───────────┘    └───────────┘    └───────────┘  │
    ▲                                   │        │
    │              new questions?       │        │
    │              new keywords?        │        │
    │              knowledge gaps?      │        │
    └───────────────────────────────────┘        │
                                                 │
                    saturation? ─────────────────┘
                        │
                        ▼
                ┌───────────────┐
                │   Synthesis   │
                │   (final)     │
                └───────────────┘
```

---

### Faza 1: Initial Search Strategy
- [ ] Zdefiniuj pytania badawcze (wstępne, będą ewoluować)
- [ ] Określ keywords + synonimy + related terms
- [ ] Lista źródeł do przeszukania (min. 3 różne typy)
- [ ] Kryteria włączenia/wykluczenia

**Output:** `search-strategy-v1.md`

---

### Faza 2: Gather + Evaluate (iteracyjnie)

**Dla każdej rundy:**

1. **Search** — wykonaj queries, zapisz wyniki
```
| Runda | Query | Źródło | Wyników | Przydatnych | Nowe tematy? |
|-------|-------|--------|---------|-------------|--------------|
| 1     | ...   | ...    | ...     | ...         | tak/nie      |
```

2. **Evaluate** — per źródło:
   - [ ] CRAAP quick check
   - [ ] Lateral reading (dla kluczowych)
   - [ ] Decyzja: include / exclude / flag

3. **Snowball** — dla high-quality źródeł:
   - [ ] Backward: sprawdź bibliografię
   - [ ] Forward: "cited by" w Google Scholar
   - [ ] Dodaj do kolejnej rundy

**Output:** `sources-log.md`, `source-evaluations.md`

---

### Faza 3: Mini-Analysis (po każdej rundzie)

**Constant comparison — nie czekaj na wszystkie źródła:**

- [ ] Co nowego się pojawiło w tej rundzie?
- [ ] Jakie **nowe pytania** wyłoniły się z analizy?
- [ ] Jakie **nowe keywords/terminy** odkryłem?
- [ ] Jakie **luki** widzę w zebranym materiale?
- [ ] Czy są **sprzeczności** między źródłami?

**Jeśli nowe pytania/keywords → wróć do Fazy 1 (update strategy)**
**Jeśli luki → wróć do Fazy 2 (targeted search)**

**Output:** `analysis-notes-round-N.md`

---

### Faza 4: Saturation Check

**Kryteria zakończenia gatheringu:**

| Kryterium | Check |
|-----------|-------|
| **Thematic saturation** | Ostatnie 3 źródła nie wniosły nowych tematów |
| **Triangulation** | Kluczowe wnioski potwierdzone przez ≥2 niezależne źródła |
| **Coverage** | Przeszukano ≥3 różne typy źródeł |
| **Snowball exhaustion** | Forward/backward chaining nie daje nowych trafień |

**Jeśli nie spełnione → kolejna runda**
**Jeśli spełnione → można przejść do synthesis**

---

### Faza 5: Final Synthesis

**Tylko gdy saturation osiągnięta:**

- [ ] **Methodology statement**: "Przeszukano X źródeł w Y rundach, używając queries Z..."
- [ ] **Source summary**: N źródeł włączonych, M wykluczonych (z powodami)
- [ ] **Confidence levels**: per wniosek (high/medium/low + uzasadnienie)
- [ ] **Knowledge gaps**: czego NIE udało się ustalić
- [ ] **Limitations**: gdzie źródła były słabe/stare/stronnicze

**Output:** `final-report.md`

---

## Checkpointy dla użytkownika

Agent powinien zatrzymać się i poprosić o feedback w kluczowych momentach:

| Checkpoint | Pytanie do użytkownika |
|------------|------------------------|
| Po Fazie 1 | "Czy search strategy wygląda kompletna? Brakuje jakichś kątów?" |
| Po rundzie z niską yield | "Znalazłem mało — zmienić podejście czy kontynuować?" |
| Przy sprzecznościach | "Źródła mówią różne rzeczy o X — jak rozstrzygnąć?" |
| Przed synthesis | "Czy mogę zakończyć zbieranie? Oto co mam..." |
| Po synthesis | "Oto raport — czy są luki które powinienem uzupełnić?" |
