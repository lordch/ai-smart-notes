# Research Raw - Jobs to Be Done

## Data zebrania
2026-01-22

---

## Zrodla z workspace

### tasks/2026-01-16-spotkanie-rudy-growgo/dwa-modele-consulting.md

**Dwa modele dostarczania wartosci:**

**Model Rudego: "Productized Consulting"**
- Wiedza plynie od konsultanta do klienta przez narzedzie (Gem)
- Klient nie musi rozumiec *dlaczego* - wystarczy ze odpowie na pytania
- Wartosc = "kupiles dostep do mojej metodologii w formie self-service"
- Klient = operator, nie ekspert
- Po projekcie: klient zalezny od narzedzia

**Moj model: "Knowledge Empowerment"**
- Wiedza jest juz u klienta - trzeba ja wydobyc i uporzadkowac
- Klient jest specjalista w swojej dziedzinie
- Narzedzie jest infrastruktura dla wiedzy klienta, nie kontenerem mojej wiedzy
- Wartosc = "nauczyles sie pracowac z AI, wiedza zostaje u ciebie"
- Po projekcie: klient ma kompetencje

**Kluczowy cytat:**
> "To nie sa konkurencyjne podejscia - to rozne segmenty rynku. Rudy celuje w klientow, ktorzy nie chca sie uczyc - chca wynik. Ja celuje w klientow, ktorzy chca budowac wlasne kompetencje."

---

### tasks/2026-01-16-spotkanie-rudy-growgo/artifacts_vs_gems_deep_dive.md

**Scenariusze gdzie Gems nie wystarcza:**

1. **Stabilnosc dokumentow** - "W korporacji, gdzie jeden przecinek w procedurze moze miec konsekwencje prawne, to jest niedopuszczalne" (model nie pamieta co bylo ustalone)

2. **Context Rot** - "Degradacja jakosci w miare zapelniania kontekstu. Model zaczyna halucynowac, bo widzi za duzo informacji"

3. **Skalowalnosc zmian** - "CEO zmienia zdanie? Edytujesz jeden plik. Gotowe." (vs edycja 50 Gemsow)

4. **Praca zespolowa** - "Kazdy pracuje w izolowanym kontekscie. Ale wszyscy operuja na tym samym pliku (Single Source of Truth)"

5. **Dlugotrawle projekty** - "Historia zmian? git log. Co sie zmienilo od wersji z 15 stycznia? git diff"

6. **Onboarding** - "Junior moze przeczytac pliki, rozumie skad biora sie instrukcje, moze zaproponowac poprawki"

7. **Audyt i Compliance** - "Pelna traceability. Audytor jest szczesliwy."

**Kiedy Gems wystarczy:**
- Jednorazowe strzaly: "Napisz zyczenia urodzinowe dla Kasi"
- Proste transformacje: "Przetlumacz ten akapit"
- Brainstorming bez konsekwencji
- Szybkie pytania

**Regula kciuka:**
> "Jesli output mozesz wyrzucic i nic sie nie stanie, Gem wystarczy. Ale jesli output ma zyc dluzej niz sesja, jesli ktos inny ma na nim pracowac, jesli ma byc wersjonowany, audytowany, utrzymywany - wtedy potrzebujesz artefaktow."

**Haslo sprzedazowe:**
> "Gems to frontend. My budujemy backend wiedzy Waszej firmy."

---

### tasks/2026-01-19-rozmowa-mama-agnieszka/notes.md

**Agnieszka (NGO, Copilot):**
- Microsoft Copilot z dostepem do Sharepointa organizacji
- Pracuje na swoich dokumentach - nie polega na AI jako zrodle wiedzy
- Use cases: rekomendacje, wnioski grantowe (pojedyncze pytania), wyciaganie wnioskow z raportow

**Bariery:**
- "Ograniczone zaufanie - anonimizuje dokumenty, nie wie czy dane nie staja sie publiczne"
- "Nie chce generowac calego wniosku - boi sie antyplagiatowych i generycznosci (wszyscy beda mieli taki sam)"

**Mama (freelance):**
- ChatGPT: "zrob mi program" -> bezwartosciowy output
- Gemini iteracyjnie z checkpointami - "bardzo dobra jakosc"
- "Znalazl ciekawsze tresci niz myslismy z Konradem wymyslimy"

**Obserwacja:**
> "Realizuje Human-Agent Collaboration recznie - iteracja, checkpointy, czlowiek steruje. Pytanie: ile zyska z workspace'u i czy beda bariery wejscia?"

**Moja przewaga vs Copilot:**
- Zlozone, dlugie zadania z wieloma zrodlami
- Kontrola i przejrzystosc
- Izolacja kontekstu miedzy subtaskami
- Artefakty jako medium (nie chat)

**Copilot nie ma:**
- Edycji dokumentow (?) - tylko chat
- Przejrzystosci - przegladarka plikow + edytor + chat w jednym oknie
- Izolacji kontekstu - nie da sie zrobic systematycznego researchu

**Pytania do zbadania:**
1. Jakie zadania wymagaja tego co daje agentic workspace a nie daje copilot?
2. Czy dla kogos takiego jak mama wystarczy "usystematyzowanie pracy z chatem"?
3. Czy copilot + dedykowani agenci M365 mogliby dac podobna wartosc?

---

### concepts/Human-Agent Collaboration Framework.md

**Core Thesis:**
> "The common framing of AI transformation imagines automation: a tool that takes tasks from human hands entirely. This misses what actually works."

**Zasady:**
1. Supervision is context curation, not action approval
2. The human works through the agent's hands
3. Specs are contracts, not commands
4. Trust model determines formalization requirements
5. Scripts for reliability, LLM for flexibility
6. Resist premature artifact production
7. The Autonomy Slider

**Leverage hierarchy:**
> "Research wrong -> 1000s of bad lines. Plan wrong -> 100s. Code wrong -> 1."

**Collaboration loop:**
1. Human identifies problem/goal
2. Agent researches, produces research artifact
3. Human reviews research, steers if needed
4. Agent produces plan artifact
5. Human reviews plan, edits if needed
6. Agent implements against plan
7. Tests verify (automated trust)
8. Human updates knowledge base with learnings
9. If pattern reliable, human moves up one abstraction level

**Context Curation Taxonomy:**
| Typ | Pytanie | Przyklady |
|-----|---------|-----------|
| Factual | What does agent know? | Knowledge base, docs, research files |
| Procedural | How should agent act here? | Dos/don'ts, commands, safety rules |
| Organizational | How maintain continuity? | Compaction rituals, handoffs, folder structures |

**Target markets:**
> "Work that's 'too expensive to do well' currently. Roles with high context-switching costs. Industries: legal, consulting, technical writing, financial analysis, recruiting."

---

### strategy/offers/AI Workspace Build.md

**Esencja:**
> "Przychodzę do firmy (lub osoby) i buduję im kompletne środowisko do pracy z AI. Buduję całą infrastrukturę kontekstową."

**Profil idealny:**
- Solo knowledge worker / mały zespół (1-10 osób)
- Robi złożoną pracę intelektualną
- Ma powtarzalne typy zadań i artefaktów
- Gromadzi specjalistyczną wiedzę domenową
- Ma czas na współpracę przy wdrożeniu

**Przykłady klientów:**
- Lekarz-badacz: literature review, Table 1, drafty paperow
- Prawnik: opinie prawne, due diligence, umowy
- Konsultant strategiczny: analizy rynku, rekomendacje
- Analityk finansowy: modele, raporty, memoranda
- Researcher UX: interview notes, synthesis, persony

**Antyprofil:**
- Potrzebują "zrobienia za nich"
- Brak czasu na współpracę (3-5 godzin/tydzień)
- Oczekują magii ("AI wszystko zrobi samo")
- Zbyt duża organizacja (>50 osób)

**Pricing:**
- Pakiet SOLO: 6,000 - 9,000 PLN (4-5 tygodni)
- Pakiet TEAM: 12,000 - 18,000 PLN (6-8 tygodni)
- Pakiet FOUNDATION (Light): 3,500 - 5,000 PLN (2-3 tygodnie)

**Value proposition:**
> "Za 4-6 tygodni będziesz miał workspace, w którym AI rozumie Twój kontekst, zna Twoje artefakty i potrafi Ci efektywnie pomagać. Nie będziesz zaczynał każdej sesji od zera."

**ROI (Dagny case):**
- Oszczędność: ~120h/rok
- Wartość: ~24,000 PLN/rok
- Cena wdrożenia: 6,000-9,000 PLN
- Zwrot: 3-5 miesięcy

---

### strategy/offers/Workflow Implementation Sprints.md

**Esencja:**
> "Wdrażam jeden konkretny workflow z AI w 2-4 tygodnie. Biorę jeden powtarzalny proces i sprawiam, że działa z AI."

**Przykłady workflow'ów:**
| Branża | Workflow | Input -> Output |
|--------|----------|-----------------|
| Prawo | Case research | Pytanie prawne -> Opinia z precedensami |
| Consulting | Client discovery | Wywiady -> Problem statement + rekomendacje |
| Finance | Document review | Umowy/sprawozdania -> Ekstrakcja danych + analiza |
| Marketing | Content production | Brief -> Research -> Draft -> Final |
| Research | Literature review | Pytanie -> Search strategy -> Extraction -> Synthesis |

**Pricing:**
- Standard Sprint: 25,000 - 35,000 PLN (3-4 tygodnie)
- Complex Sprint: 40,000 - 50,000 PLN (4-6 tygodni)
- Light Sprint: 15,000 - 20,000 PLN (2 tygodnie)

**Value calculation (Legal Case Research):**
- Przed: 6h x 400 PLN/h = 2,400 PLN/case
- Po: 3h x 400 PLN/h = 1,200 PLN/case
- Oszczędność: 60,000 PLN/rok (50 cases)
- ROI: 6 miesięcy

---

### strategy/offers/Context Engineering Skill Development Program.md

**Poziomy kompetencji:**

| Level | Czas | Dla kogo | Rezultat |
|-------|------|----------|----------|
| 0 | 2-3h | Każdy | Efektywna pojedyncza sesja |
| 1 | 4-6h | Knowledge workers | Złożone zadania w wielu sesjach |
| 2 | 6-8h | Power users, founders | Personal knowledge system |
| 3 | 4-6h | Teams, leaders | Organizational capability |

**Full program:** 16-20h (4-5 warsztatów)

**Cytat:**
> "Context is the new moat. Same model, different results. The team that can externalize what they know and feed it to agents in a structured way will build things competitors can't copy."

---

### strategy/plans/Strategy - AI Consultancy for Polish SME Knowledge Work.md

**The Opportunity:**
> "Polish SMEs are hearing the AI narrative: autonomous agents, automation, replacement of human work. Enterprise reports show 70%+ failure rates on agent deployments. ROI takes 2-4 years."

**What's missing:**
> "Guidance on *how to work with AI effectively* — not as automation, but as amplification."

**Target: Polish SME knowledge work (10-200 employees)**
- Law firms
- Consulting firms
- Financial advisory
- Marketing agencies
- Research organizations
- Technical documentation / translation
- Architecture and design studios

**Why this segment:**
- Large enough to have workflow complexity
- Small enough they can't afford failed AI experiments
- Polish language adds friction to "just use the tools"
- SME decision-making faster than enterprise

**Competitive Landscape:**

| Konkurent | Ich podejście | Moja przewaga |
|-----------|---------------|---------------|
| Large consultancies (Deloitte etc) | Enterprise scale/price | Accessible, practical, SME-focused |
| IT integrators | Building custom solutions | Faster time to value, lower cost |
| Individual AI trainers | Generic "how to use ChatGPT" | Deeper methodology, implementation support |

**Key Messages:**

**For skeptics (burned by AI hype):**
> "Zapomniej o 'autonomicznych agentach'. Pokażemy ci, jak naprawdę pracować z AI — jako narzędzie wzmacniające twoje kompetencje, nie zastępujące."

**For enthusiasts (excited but unfocused):**
> "AI to nie magia. To umiejętność. Nauczymy cię systematycznego podejścia, które przynosi powtarzalne rezultaty."

**For pragmatists (want results, not hype):**
> "Konkretne wdrożenia, mierzalne efekty, wsparcie przy implementacji. Bez budowania skomplikowanych systemów."

---

### strategy/plans/Strategy - Mapa Terenu (Consulting Practice).md

**Narracje (kąty sprzedażowe):**

**Poziom strategiczny (C-level):**
- "Amplification, not Automation"
- "Externalized Expertise as Competitive Moat"
- "Learning Organization 2.0"

**Poziom operacyjny (menedżerowie):**
- "Dlaczego agenty AI nie dowożą" (hook: kontra-hype)
- "ChatGPT nie pamięta Twojego kontekstu" (hook: konkretny pain point)
- "Od promptu do systemu" (hook: dla ludzi którzy już używają AI)

**Poziom praktyczny (individual contributors):**
- "Twórz z AI, nie bądź zastąpiony przez AI"
- "Przestrzeń współpracy z AI"

**Narzędzia - stopniowanie:**
| Level | Narzędzie | Dla kogo |
|-------|-----------|----------|
| 0-1 | Claude.ai + Projects | Każdy |
| 2 | Claude Desktop + MCP | Power users |
| 3 | Cursor / Claude Code | Techniczni, devs |

**Pricing logic (warsztaty):**
- Open enrollment: 500-1500 PLN/osoba
- In-house: 10,000-25,000 PLN/warsztat

**Pricing logic (wdrożenia):**
- 8,000-50,000 PLN zależnie od scope

---

### concepts/Externalized Expertise as Competitive Moat.md

**Core insight:**
> "Models are commoditizing. Everyone has access to GPT-4, Claude, and Gemini. The new competitive advantage is externalized organizational expertise."

**Why externalization wasn't prioritized before:**
- Cost: High (takes time away from "real work")
- Benefit: Low (rarely read, quickly outdated)

**What changed:**
> "Externalized knowledge = executable capability. Documentation for humans: Maybe someone reads it someday. Externalized knowledge for agents: Agent executes it immediately."

**The bottleneck shifted:**
- Was: "Can agents even do this?"
- Now: "Do agents know HOW WE do this?"

**What to sell:**
- "We help you externalize your organizational expertise"
- "Your domain knowledge becomes executable capability"
- "Build competitive moat through knowledge accumulation"

---

### concepts/Context Engineering.md

**Definition:**
> "The discipline of designing systems that provide language models with maximally useful information at minimal token cost."

**Why it's permanent:**
> "As long as we're dealing with quadratic transformer attention, you're always going to benefit from doing the deterministic engineering that allows you to keep the context window as small as possible for a given task."

---

### tasks/2026-01-20-claude-cowork-research/SUMMARY.md

**YouTube Research - 95 videos scored:**
- 73% scored 4-5/5 (high-quality content)
- Top creators: Brock Mesarich (AI for Non Techies), No Code MBA, Matt Maher

**Top use cases for Claude Cowork:**
- Comprehensive tutorials (15-30 min)
- Real use case demonstrations
- Business value propositions ("7 Days of Work in 15 Minutes")
- Niche professional applications (accounting, RevOps, HR analytics)

**Pattern:**
> "Non-techie comprehensive" tutorials are among top-rated content - indicating market demand for accessible AI tools.

---

## Zrodla z web

### Stan wdrozen AI w polskich firmach (EY, BCG, Gartner)

**Statystyki:**
- Wzrost odsetka firm z udanymi wdrożeniami AI: z 20% do 25%
- 89% firm deklaruje gotowość do kolejnych wdrożeń (wzrost z 78%)
- 59% traktuje AI jako jeden z ważniejszych priorytetów (wzrost z 53%)
- Ponad połowa organizacji planuje znacznie zwiększyć wydatki na AI w ciągu 18 miesięcy

**Ale:**
- Tylko 22% firm wykracza poza etap proof of concept (BCG)
- Zaledwie 4% osiąga istotne korzyści z AI
- Opóźnione wdrożenia uszczuplają wartość firmy średnio o 8,6%

**Prognozy 2026:**
> "W 2026 roku nie wystarczy wykazać, że AI działa - musi działać lepiej, szybciej lub taniej niż wcześniejsze procesy."

**Trend:**
> "Firmy przesuwają środki z efektownych eksperymentów w stronę infrastruktury, integracji danych i automatyzacji."

**Gartner:**
> "Do 2026 roku ponad 75% przedsiębiorstw będzie wykorzystywać AI jako integralną część swoich procesów biznesowych."

Zrodla:
- [ITwiz - 2026 rok przyniesie biznesowi chłodne spojrzenie na inwestycje w AI](https://itwiz.pl/2026-rok-przyniesie-biznesowi-chlodne-spojrzenie-na-inwestycje-w-sztuczna-inteligencje/)
- [Raport EY: Jak polskie firmy wdrażają AI](https://www.ey.com/pl_pl/insights/raporty-analizy/jak-polskie-firmy-wdrazaja-ai-raport--ai-fy25-gc-fy25)
- [eGospodarka - Człowiek i sztuczna inteligencja](https://www.egospodarka.pl/195875,Czlowiek-i-sztuczna-inteligencja-jak-firmy-beda-korzystac-z-AI-w-2026-roku,1,39,1.html)

---

### Microsoft Copilot - sytuacja rynkowa

**Udziały rynkowe:**
- Styczeń 2025: ~1,5% rynku
- Styczeń 2026: spadek do 1,1%
- W tym czasie ChatGPT: spadek z 87% do 64,5%
- Gemini: wzrost z 5,7% do 21,5%

**Problem Copilota:**
> "Dla wielu użytkowników jest 'doklejką' do systemu, a nie czymś naturalnym, koniecznym i przydatnym."

**Nowa funkcja 2026:**
- Lokalne przetwarzanie danych w Polsce od 2026
- Dla klientów z sektora publicznego i branż regulowanych

**Zalety Copilota:**
- Integracja z M365
- Niski próg wejścia dla użytkowników Microsoft

**Wady:**
- Konieczność dostosowania do infrastruktury Microsoft 365
- Krzywa uczenia się
- Potencjalne problemy z prywatnością
- Niektóre funkcje niedostępne w języku polskim

Zrodla:
- [Antyweb - Microsoft jest największym przegranym](https://antyweb.pl/microsoft-copilot-porazka)
- [ITwiz - Microsoft 365 Copilot z lokalnym przetwarzaniem w Polsce](https://itwiz.pl/microsoft-365-copilot-z-lokalnym-przetwarzaniem-danych-w-polsce-od-2026-roku/)
- [Cognity - Microsoft Copilot zalety i wady](https://www.cognity.pl/microsoft-copilot-czy-warto-zalety-wady-narzedzia-ai)

---

### Bariery adopcji AI w polskich firmach

**Główne bariery:**

1. **Luka kompetencyjna** (45% firm)
   - 58% uważa że hamuje innowacje
   > "Widzimy lukę kompetencyjną dotyczącą rozpoznania potencjału sztucznej inteligencji na poziomie motywacji i chęci spróbowania nowych technologii."

2. **Koszty wdrożenia** (36,7% firm)
   - Główna przeszkoda: wysokie wydatki na wdrożenie i utrzymanie

3. **Niepewność regulacyjna - EU AI Act** (67% firm)
   - Nie rozumieją swoich obowiązków
   - 22% firm - bariera we wdrożeniach
   - 80% startupów musiało opóźnić lub zmodyfikować strategie AI
   - Koszty zgodności: średnio 38% wydatków technologicznych

4. **Obawy o bezpieczeństwo danych**
   > "Modele LLM-owe są z reguły deponowane w chmurze. Uruchomienie ich wymaga zbudowania polityk bezpieczeństwa."

5. **Problemy z danymi**
   > "Firmy często nie mają przygotowanych danych. Nie potrafią jeszcze analizować danych w spółkach."

6. **Inercja organizacyjna**
   > "Wiele firm unika zmian, jeśli dotychczasowe procesy działają poprawnie."

**Polska vs Europa:**
- Polska: 5,9% firm korzysta z AI (przedostatnie miejsce w UE)
- Ale: wzrost 56% r/r - najwyższa dynamika w UE
- 34% wszystkich przedsiębiorstw korzysta z AI

**Gotowość strategiczna:**
- Polska: 8% dużych firm gotowych do strategicznego wdrożenia AI
- Niemcy: 41%

Zrodla:
- [PwC - Polskie firmy nie wykorzystują w pełni potencjału AI](https://www.pwc.pl/pl/publikacje/polskie-firmy-nie-wykorzystuja-w-pelni-potencjalu-ai.html)
- [MIT SMR Polska - Adopcja AI w Polsce](https://mitsmr.pl/sztuczna-inteligencja-i-uczenie-maszynowe/pedzacy-pociag-rewolucji-sztucznej-inteligencji-adopcja-ai-w-polsce/)
- [Kariera.net - AI w polskich firmach: wielkie obietnice, realne bariery](https://kariera.net.pl/ai-w-polskich-firmach-wielkie-obietnice-realne-bariery-29150589.html)
- [PurePC - Raport IFS Polska 2025](https://www.purepc.pl/raport-ifs-polska-2025-ai-w-najwiekszych-firmach-wdrozenie-strategia-statystyki)

---

### Cennik szkoleń AI w Polsce 2025-2026

**Kursy online:**
- Business Programme AI (BPAI) 2026: od 2999 zł (12 miesięcy dostępu)
- AI_devs 4: program 5-tygodniowy (cena nieujawniona publicznie)

**Szkolenia otwarte (eventis.pl):**
- Agenci AI dla działu Zakupów: od 3 771 zł
- Agenci AI dla Biura Zarządu: od 3 201 zł
- AI w pracy biurowej: od 790 zł
- Polityka AI dla działów prawnych: od 2 536 zł
- AI w pracy i nauce (na zamówienie): od 5 335 zł
- Narzędzia AI - organizacja pracy: od 9 990 zł

**Bezpłatne szkolenia:**
- Portal Gov.pl - webinary
- Akademia PARP - "AI w biznesie - kurs I stopnia"

**Dofinansowania:**
- DAGMA Szkolenia IT: 70-90% dofinansowania możliwe

Zrodla:
- [AI o AI - Ranking kursów AI 2026](https://aioai.pl/ranking-5-kursow-ai-na-2026-rok/)
- [Eventis.pl - Szkolenia AI](https://eventis.pl/szkolenia-kursy/ai-sztuczna-inteligencja)
- [DAGMA Szkolenia IT](https://szkolenia.dagma.eu/pl/training,catalog,98056/sztuczna-inteligencja-ai-w-pracy-i-biznesie-poziom-1)

---

### Problemy knowledge workers z AI

**Wpływ na myślenie krytyczne:**
- Badanie 319 knowledge workers (pracownicy socjalni, programiści, etc.)
- Negatywna zależność między częstym korzystaniem z AI a zdolnością do krytycznego myślenia
- "GenSI zwiększa subiektywnie deklarowaną efektywność, ale jednocześnie obniża poziom krytycznego myślenia"

**Obawy o projektowanie narzędzi:**
> "Generatywną sztuczną inteligencję należy traktować jako narzędzie wspierające, a nie zastępujące własne myślenie. Problem polega na tym, że same te narzędzia są wręcz tak zaprojektowane, by zachęcać do nadmiernego korzystania z nich."

**Frustracje programistów:**
- "ChatGPT w wersji 4 odpowiada zdecydowanie bardziej ogólnie niż przed 2 miesiącami"
- "Kodowanie w ChatGPT 4.0 staje się coraz trudniejsze z każdym tygodniem"
- "Model nie pamięta już historii konwersacji"
- "Kod zawierający błędy jest nagle obcinany lub całkowicie zmieniany"

**Problemy z jakością:**
- Informacje nieprawdziwe lub nieaktualne
- Odpowiedzi zbyt ogólne, niekompletne
- "Gubienie wątku" w dłuższej rozmowie

**Uzależnienie od technologii:**
> "Awaria ChatGPT pokazuje, jak bardzo zależni jesteśmy od technologii AI w codziennym życiu."

Zrodla:
- [OKO.press - Czy korzystanie z ChataGPT ogłupia ludzi?](https://oko.press/czy-korzystanie-z-chatagpt-nas-oglupia)
- [MagicTM - Problemy z ChatGPT](https://magictm.com/blog/problemy-z-chatem-gpt-i-jak-je-rozwiazac)

---

### Rynek konsultingu AI w Polsce

**Główni gracze (Clutch.co, Sortlist, GoodFirms):**
- Addepto (Warszawa) - AI, ML, data-driven solutions
- NobleProg - szkolenia i konsultacje AI, prompt engineering
- Silk Data (Warszawa) - AI, ML, data science, PhD-level experts
- Zfort Group - AI consulting, product development
- Future Prompters (Wrocław) - AI consultancy
- Develtio - service productization, AI development

**Charakterystyka rynku:**
> "Poland, with its growing ecosystem of startups and experienced engineering teams, stands out as a leader in AI development in Europe."

**Wartość rynku IT w Polsce:**
- Projected revenue 2025: $10.44 billion
- CAGR through 2029: 5.91%

**Usługi:**
- AI consulting
- Big data engineering
- Machine learning solutions
- Generative AI
- Computer vision
- Prompt engineering consulting

**Uwaga:**
> Nie znaleziono firm oferujących "context engineering" jako wyodrębnioną usługę. Rynek skupia się na: machine learning, data science, generative AI, prompt engineering.

Zrodla:
- [Clutch.co - Top AI Consultants in Poland](https://clutch.co/pl/consulting/ai)
- [Sortlist - AI Agencies in Poland](https://www.sortlist.com/s/artificial-intelligence/poland-pl)
- [NobleProg - Prompt Engineering Consulting](https://www.nobleprog.pl/en/consulting/prompt-engineering)

---

### Vibe Coding - trend 2025/2026

**Co to jest:**
> "AI-assisted software development technique. Chatbot-based approach where the developer describes a project to an LLM, which generates source code. The developer does not review or edit the code, but solely uses tools and execution results to evaluate it."

**Kto wprowadził:**
- Andrej Karpathy, luty 2025
- Collins English Dictionary - Słowo Roku 2025

**Statystyki adopcji 2025:**
- 92% deweloperów US używa AI coding tools codziennie
- 82% globalnie - przynajmniej raz w tygodniu
- 41% kodu globalnie jest generowane przez AI
- 87% Fortune 500 przyjęło przynajmniej jedną platformę vibe coding
- Y Combinator Winter 2025: 25% startupów ma codebase w 95% generowany przez AI

**Wzrost wyszukiwań:**
> "Searches for 'vibe coding' jumped 6,700% in spring 2025"

**Wpływ na non-technical users:**
> "Vibe Coding makes software development more accessible to non-technical teams like product managers, designers, and even business stakeholders, who can now contribute to the development process by describing features and functionality in everyday language."

**Prognozy 2026:**
> "In 2026, the industry will gain greater access to mainstream quick-start app development functionalities. Next-generation UI's will bring new business opportunities for non-coders to create and even market attractive application options."

**Popularne narzędzia:**
- Beginners: ChatGPT, Claude, Lovable, Zapier Agents
- Developers: Bolt, Cursor, Windsurf

**Ryzyka:**
- 40%+ junior developers deploys AI-generated code they don't fully understand
- Brak accountability, maintainability
- Increased security vulnerabilities
- Technical debt

Zrodla:
- [The New Stack - AI Engineering Trends 2025](https://thenewstack.io/ai-engineering-trends-in-2025-agents-mcp-and-vibe-coding/)
- [Tech Monitor - Vibe coding goes mainstream in 2026](https://www.techmonitor.ai/analysis/vibe-coding-will-become-mainstream-in-2026)
- [Wikipedia - Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding)
- [Second Talent - Vibe Coding Statistics 2026](https://www.secondtalent.com/resources/vibe-coding-statistics/)

---

### Wsparcie rządowe dla AI w Polsce

**Budżet 2025:**
- Ministerstwo Cyfryzacji: ponad 4,5 mld zł na rozwój cyfryzacji
- Program Ścieżka SMART: 1,3 mld zł na projekty B+R
- Program Infostrateg: ponad 500 mln zł na rozwój polskiego potencjału AI

Zrodla:
- [BGK - Polska potęgą AI?](https://www.bgk.pl/dla-klienta/strefa-wiedzy-bgk/artykul/polska-potega-ai-jak-gigainwestycje-i-nowe-fundusze-otwieraja-rynek-dla-twojej-firmy/)

---

## Kluczowe obserwacje

### O rynku polskim:
1. **Dynamiczny wzrost, niska baza** - 56% wzrost r/r ale tylko 5,9% firm używa AI (przedostatnie miejsce w UE)
2. **Luka kompetencyjna** jako główna bariera (45% firm) - rynek na szkolenia i wdrożenia
3. **Rozjazd między aspiracjami a gotowością** - 89% chce wdrażać, tylko 8% jest gotowych strategicznie
4. **EU AI Act** jako czynnik niepewności - 67% nie rozumie obowiązków
5. **Copilot nie zdobył rynku** - spadek z 1,5% do 1,1% mimo integracji z M365

### O knowledge workers:
1. **Context rot i "gubienie wątku"** - powtarzający się problem w długich sesjach
2. **Frustracja z brakiem pamięci** - "każda sesja od zera"
3. **Obawy o bezpieczeństwo danych** - anonimizacja, polityki
4. **Strach przed generycznością** - "wszyscy będą mieli taki sam wniosek"
5. **Spadek krytycznego myślenia** przy nadmiernym poleganiu na AI

### O mojej przewadze:
1. **Nisza "context engineering"** - brak konkurencji w Polsce (nikt nie oferuje)
2. **Gap między prostymi narzędziami a pełną automatyzacją** - moje miejsce
3. **Knowledge workers którzy chcą budować kompetencje** vs ci co chcą gotowe rozwiązania
4. **Złożone, długie zadania z wieloma źródłami** - to czego Copilot/Gems nie dają

### O zagrożeniach:
1. **Vibe coding** - 92% devs używa AI daily, bariera wejścia spada dramatycznie
2. **Claude Cowork** - "Master 99% in 26 Minutes (No Code)" - dostępność rośnie
3. **Tool vendors** będą dodawać więcej funkcji "context management"
4. **Ceny szkoleń** - rynek 790 - 10,000 PLN, ale dużo bezpłatnych opcji (PARP, Gov.pl)

### Jobs to be done (wstępnie):
1. **"Chcę żeby AI pamiętało mój kontekst między sesjami"**
2. **"Chcę systematyczny workflow, nie chaos w chatach"**
3. **"Chcę mieć kontrolę nad tym co AI wie o mojej firmie"**
4. **"Chcę żeby mój zespół mógł współpracować na tych samych artefaktach"**
5. **"Chcę auditowalne, wersjonowane outputy"**
6. **"Chcę wyłączyć moją ekspertyzę z głowy do systemu"**

---

*Koniec fazy research. Następny krok: analiza Jobs to Be Done.*
