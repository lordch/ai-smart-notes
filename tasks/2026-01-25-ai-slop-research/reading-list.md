# AI Slop Research - Reading List

date-created:: 2026-01-26
status:: Active

---

## Top 5 do przeczytania

### 1. Benedict Evans — "The Deep Research Problem"
- **Typ:** Expert blog | Luty 2025
- **Link:** https://www.ben-evans.com/benedictevans/2025/2/17/the-deep-research-problem
- **Status:** [ ] Do przeczytania

Tech analyst z a16z testuje OpenAI Deep Research na *własnej domenie ekspertyzy* — smartphone data. Rezultat? AI cytuje Statista (SEO aggregator), podaje liczby *odwrotne* niż w swoich własnych źródłach, i robi błędy faktyczne które Evans łapie w 5 minut.

**Relevance:** Konkretny case study płytkiego researchu. Pokazuje jak AI wybiera "łatwe" źródła zamiast primary sources. Actionable — wiesz co sprawdzać.

---

### 2. Ethan Mollick — "The Cybernetic Teammate"
- **Typ:** Wharton/One Useful Thing | 2025
- **Link:** https://www.oneusefulthing.org/p/the-cybernetic-teammate
- **Status:** [ ] Do przeczytania

Definiuje trzy tryby pracy z AI: Centaur (jasny podział), Cyborg (fused), Self-Automator (deleguj wszystko). Dwa pierwsze działają. Trzeci produkuje workslop. BCG study: 40% quality improvement *ale tylko w trybie Centaur/Cyborg*.

**Relevance:** Bezpośrednie empiryczne wsparcie dla Human-Agent Collaboration. Mollick to najbardziej cytowany głos w temacie AI w pracy. Framing który można użyć.

---

### 3. Georgetown/Stanford — "Homogenization Effects on Creative Ideation"
- **Typ:** C&C 2024 Conference | Peer-reviewed
- **Link:** https://mkremins.github.io/publications/Homogenization_C&C2024.pdf
- **Status:** [ ] Do przeczytania

2,200+ college admission essays. Kluczowy finding: homogenizacja wynika z *group-level* suggestion podobnych idei różnym użytkownikom — nie z individual fixation. **Prompt modifications i parameter adjustments nie mitigują diversity gap.**

**Relevance:** Wyjaśnia *mechanizm* płytkości. To nie jest "użytkownik robi źle" — to architektura. Implikacja: sama instrukcja "bądź kreatywny" nie działa.

---

### 4. Apple ML Research — "The Illusion of Thinking"
- **Typ:** Corporate research | 2025
- **Link:** https://machinelearning.apple.com/research/illusion-of-thinking
- **Status:** [ ] Do przeczytania

Large Reasoning Models (o1, etc.) doświadczają "complete accuracy collapse" przy wysokiej złożoności. Paradoks: modele *redukują* wysiłek rozumowania gdy problemy stają się trudniejsze.

**Relevance:** Podważa narrację że "reasoning models" rozwiążą problem słabej analizy. Nawet najnowsze architektury mają fundamentalne limity. To nie kwestia czasu — to kwestia designu.

---

### 5. Simon Willison — Blog o LLM
- **Typ:** Django co-creator, Datasette | Ongoing
- **Link:** https://simonw.substack.com/p/how-i-use-llms-to-help-me-write-code
- **Status:** [ ] Do przeczytania

Power-user LLM który publicznie dokumentuje swoje praktyki. Kluczowy cytat o Deep Research: *"Some of its summaries were just pleasant to read, they felt so information-dense and intelligent! Not like typical AI slop at all! But then it turned out most of it was just AI slop underneath anyway, and now my slop-recognition function has adjusted."*

**Relevance:** Praktyk z najwyższej półki opisuje jak jego "taste" ewoluuje. Pokazuje że rozpoznawanie slop to *nabywana umiejętność*. Relevant dla "taste as the new skill".

---

## Kolejne 10 rekomendacji

### 6. David Cropley — "Mathematical Ceiling on AI Creativity"
- **Typ:** Journal of Creative Behavior (Wiley) | 2025 | Peer-reviewed
- **Link:** https://www.psypost.org/a-mathematical-ceiling-limits-generative-ai-to-amateur-level-creativity/
- **Status:** [ ] Do przeczytania

Formalizuje matematycznie dlaczego LLM mają ceiling na kreatywność = 0.25 (skala 0-1). Trade-off: novelty vs. effectiveness są odwrotnie skorelowane w systemach probabilistycznych.

**Relevance:** Teoretyczna podstawa argumentu o strukturalnych ograniczeniach. Nie "AI jeszcze nie umie" — "AI *nie może* z definicji".

---

### 7. Stanford HAI — "AI on Trial: Legal Models Hallucinate"
- **Typ:** Stanford Research | 2024
- **Link:** https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries
- **Status:** [ ] Do przeczytania

Benchmark hallucination rates: Lexis+ AI 17%+, Westlaw AI 34%+, general chatbots 58-82%. Nawet *specjalistyczne* narzędzia prawne halucynują.

**Relevance:** Domain-specific failure rates. Argument: "specjalizowane AI" nie rozwiązuje problemu.

---

### 8. CNBC — "AI-Generated Workslop Is Destroying Productivity"
- **Typ:** Business journalism | Wrzesień 2025
- **Link:** https://www.cnbc.com/2025/09/23/ai-generated-workslop-is-destroying-productivity-and-teams-researchers-say.html
- **Status:** [ ] Do przeczytania

Raportuje Stanford/HBR research: 40% pracowników otrzymuje workslop miesięcznie. Koszt: $186/pracownika. Definiuje termin dla mainstream.

**Relevance:** Źródło definicji "workslop". Dobre do cytowania w contencie.

---

### 9. Deloitte Australia/Canada — Case Studies
- **Typ:** Business journalism | 2025
- **Linki:**
  - https://fortune.com/2025/10/07/deloitte-ai-australia-government-report-hallucinations-technology-290000-refund/
  - https://fortune.com/2025/11/25/deloitte-caught-fabricated-ai-generated-research-million-dollar-report-canada-government/
- **Status:** [ ] Do przeczytania

Australia: $290K raport z fabricated citations. Kanada: $1M+ raport z nieistniejącymi artykułami. Senator Pocock: "things a first-year university student would be in deep trouble for."

**Relevance:** Real-world consulting failures. Case studies do używania w argumentacji.

---

### 10. UW — "RLHF User Values Research"
- **Typ:** University of Washington | Grudzień 2024
- **Link:** https://www.washington.edu/news/2024/12/18/ai-user-values-preferences-rlhf/
- **Status:** [ ] Do przeczytania

Wyjaśnia mechanizm RLHF jako averaging: "the model can basically try to average all preferences together, and this can be incorrect for all users." Maze example: jeśli jedni chcą top-right, drudzy bottom-right → model idzie na środek = źle dla wszystkich.

**Relevance:** Mechanizm "averaging of perspectives". Dlaczego AI produkuje bezpieczne, nijakie odpowiedzi.

---

### 11. "Creative Scar" Longitudinal Study
- **Typ:** Technology in Society (ScienceDirect) | 2025 | Peer-reviewed
- **Link:** https://www.sciencedirect.com/science/article/abs/pii/S0160791X25002775
- **Status:** [ ] Do przeczytania

61 studentów przez kilka miesięcy. Homogenizacja "keeps climbing even months later" — efekt utrzymuje się po zakończeniu używania AI.

**Relevance:** Długoterminowe skutki. Argument: to nie jest "jednorazowy błąd" — to trwała zmiana w myśleniu.

---

### 12. Microsoft Research — "Impact of GenAI on Critical Thinking"
- **Typ:** Microsoft Research + CMU | Luty 2025
- **Link:** https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
- **Status:** [ ] Do przeczytania

319 knowledge workers, 936 real-world use cases. Inverse correlation: wyższa confidence in AI = mniej critical thinking. Definiuje shift "from problem-solving to AI response integration."

**Relevance:** Enterprise perspective. "Response integration" jako nowa praca.

---

### 13. Peng et al. — "Limitations of Transformer Architecture"
- **Typ:** arXiv preprint | Luty 2024
- **Link:** https://arxiv.org/html/2402.08164v1
- **Status:** [ ] Do przeczytania

Matematyczny dowód że Transformery są "fundamentalnie niekompatybilne" z function composition. Przykład: "What is the birthday of Chopin's father?" — model zna oba fakty osobno, ale nie potrafi ich połączyć.

**Relevance:** Architectural explanation. Dlaczego "więcej danych" nie rozwiąże problemu.

---

### 14. "LLM Cannot Discover Causality"
- **Typ:** arXiv | Czerwiec 2025
- **Link:** https://arxiv.org/abs/2506.00844
- **Status:** [ ] Do przeczytania

Autoregresyjne modelowanie LLM "inherently lacks theoretical grounding for causal reasoning." Nawet gdy causal relationships są explicite stated, LLM failują.

**Relevance:** Fundamentalne ograniczenie dla analizy. LLM mogą opisać korelację, nie causation.

---

### 15. Philosophical Salon — "The Idea of AI Slop Is Slop"
- **Typ:** Philosophy essay | 2025
- **Link:** https://www.thephilosophicalsalon.com/the-idea-of-ai-slop-is-slop/
- **Status:** [ ] Do przeczytania

Counterargument: "humanity has never produced one masterpiece after another. Mediocrity is the baseline of culture." Sturgeon's Law: 90% wszystkiego to crap — AI tylko to skaluje.

**Relevance:** Steelman przeciwnej pozycji. Ważne żeby znać kontrargumenty.

---

## Snowballing: BCG/Harvard "Jagged Frontier" Study

Źródła które cytują lub rozwijają oryginalne badanie Dell'Acqua et al. (2023).

### 16. HBS — "Cyborgs, Centaurs and Self-Automators"
- **Typ:** Harvard Business School Working Paper | Grudzień 2025
- **Autorzy:** Randazzo, Lifshitz-Assaf, Dell'Acqua, Mollick et al.
- **Link:** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4921696
- **PDF:** https://www.hbs.edu/ris/Publication%20Files/26-036_e7d0e59a-904c-49f1-b610-56eb2bdfe6f9.pdf
- **Status:** [ ] Do przeczytania

**Bezpośredni follow-up** oryginalnego BCG study. Ten sam zespół wraca do 244 konsultantów. Kluczowa nowość: formalizują **Self-Automator** jako trzeci tryb (obok Centaur/Cyborg). Finding: Self-Automators delegują całe taski i *nie rozwijają umiejętności* — produkują workslop. Central tension: automation vs. augmentation.

**Relevance:** Najważniejsze źródło dla "tryby współpracy". Empirycznie definiuje tryb który najbardziej pasuje do slop production. 63 strony, peer-reviewed jakość.

---

### 17. Doshi & Hauser — "Generative AI Enhances Individual Creativity but Reduces Collective Diversity"
- **Typ:** Science Advances | Lipiec 2024 | Peer-reviewed
- **Autorzy:** Anil R. Doshi (UCL), Oliver P. Hauser (Exeter)
- **Link:** https://www.science.org/doi/10.1126/sciadv.adn5290
- **Status:** [ ] Do przeczytania

300 uczestników piszących opowiadania. Finding: AI podnosi indywidualną kreatywność (+8-10% novelty), ale obniża zbiorową różnorodność. Less creative writers zyskują najwięcej — AI "equalizuje" do średniej. Cytuje Jagged Frontier jako kontekst.

**Relevance:** Mechanizm homogenizacji na poziomie grupy. Komplementarne do BCG study — pokazuje *dlaczego* AI produkuje podobne outputy.

---

### 18. Dell'Acqua — "Falling Asleep at the Wheel"
- **Typ:** Field experiment | HR/Recruiting
- **Autor:** Fabrizio Dell'Acqua (ten sam co Jagged Frontier)
- **PDF:** https://www.almendron.com/tribuna/wp-content/uploads/2023/09/falling-asleep-at-the-whee.pdf
- **Status:** [ ] Do przeczytania

181 rekruterów ocenia 44 CV. Paradoks: rekruterzy z **85% accurate AI** performowali *gorzej* niż ci z **75% accurate AI**. High-quality AI → "rubber-stamping", mniej czasu per CV, brak improvement. Lower-quality AI → krytyczne myślenie, 10 sekund więcej per CV, skill development.

**Relevance:** Empiryczny dowód że *zbyt dobra AI może być szkodliwa*. "Goldilocks level" of AI accuracy. Argument za human-in-the-loop który wymusza engagement.

---

## Honorable mentions

- **Wikipedia "Signs of AI Writing"** — crowdsourced detection heuristics
  - Link: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
  - Praktyczne, konkretne, aktualizowane na bieżąco

- **MDPI/SBS Critical Thinking Study (n=666)** — największe dane empiryczne
  - Link: https://www.mdpi.com/2075-4698/15/1/6
  - r=-0.68 między AI usage a critical thinking

---

## Pełna lista źródeł

Zobacz: [ai_slop_sources_annotated.md](reports/ai_slop_sources_annotated.md)
