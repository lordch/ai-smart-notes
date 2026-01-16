type:: [[Reference Note]]
status:: Working
date-created:: 2025-12-05
sources:: [[Nonaka & Takeuchi]], [[Michael Polanyi]], [[Etienne Wenger]], [[Dave Snowden]]

- # Knowledge Management
- **Knowledge Management (KM) is the interdisciplinary field concerned with how organizations create, capture, share, and effectively use knowledge as a strategic asset.** It emerged in the early 1990s at the intersection of management consulting, information science, organizational learning, and epistemology.
- ---
- ## Historical Origins
	- KM coalesced from multiple intellectual streams in the late 1980s–early 1990s:
	- **Management consulting** — Firms like McKinsey and Accenture began treating knowledge as competitive differentiator
	- **Organizational learning** — Peter Senge's *The Fifth Discipline* (1990), Argyris & Schön's [[Double-Loop Learning]]
	- **Philosophy of knowledge** — Polanyi's [[Tacit vs. Explicit Knowledge]] distinction from *The Tacit Dimension* (1966)
	- **Economics** — Recognition of the "knowledge economy" and intellectual capital as organizational value
	- The field gained momentum with Nonaka's 1991 *Harvard Business Review* article and Skandia's appointment of the first "Chief Knowledge Officer" in 1994.
- ---
- ## Two Schools of Thought
	- ### Technology-centric (First Generation)
		- Focus: databases, intranets, document management systems
		- Framing: knowledge as an **object** to be captured and stored
		- Associated with IT vendors selling "knowledge management systems"
		- Criticism: reduces knowledge to information, ignores tacit dimension
	- ### People-centric (Second Generation)
		- Focus: communities of practice, social networks, organizational culture
		- Framing: knowledge as a **process** enacted by people
		- Associated with Wenger (communities of practice), Snowden (Cynefin), Nonaka
		- Insight: knowledge "sticks" to people and context — can't be fully extracted
- ---
- ## Core Theoretical Frameworks
	- | Framework | Contributors | Central Idea |
	  |-----------|--------------|--------------|
	  | [[The SECI Model]] | Nonaka & Takeuchi | Knowledge spirals through tacit↔explicit conversions |
	  | Communities of Practice | Wenger, Lave | Learning happens through participation in social groups |
	  | Ba (場) | Nonaka & Konno | Shared spaces (physical, virtual, mental) enable knowledge creation |
	  | Cynefin | Dave Snowden | Context (simple, complicated, complex, chaotic) determines knowledge approach |
	  | Intellectual Capital | Sveiby, Stewart | Knowledge as measurable organizational asset |
	  | [[Double-Loop Learning]] | Argyris & Schön | Learning that updates rules, not just solves problems |
- ---
- ## Institutional Home
	- KM doesn't have a single disciplinary home — it lives at the intersection of:
	- **Business schools** — strategy, organizational behavior
	- **Information schools** — information science, library science
	- **Computer science** — knowledge representation, AI, semantic web
	- **Philosophy** — epistemology
	- **Sociology** — organizational sociology, science & technology studies
	- Key journals: *Journal of Knowledge Management*, *Knowledge Management Research & Practice*, *VINE Journal of Information and Knowledge Management Systems*
- ---
- ## The Field's Arc
	- **1990s**: Emergence and hype — knowledge as the new competitive advantage
	- **Early 2000s**: Trough of disillusionment — technology-focused initiatives fail
	- **2010s**: Maturation — focus shifts to social, cultural, and practice-based approaches
	- **2020s**: AI integration — generative AI reopens questions about knowledge capture and creation
- ---
- # Relation to My Interests
- ## KM as Foundation for Human-Agent Collaboration
	- The [[Human-Agent Collaboration Framework]] is, in many ways, an applied KM project for the age of AI agents.
	- **The core KM problem**: How do you get knowledge out of people's heads and into organizational systems?
	- **The core HAC problem**: How do you get knowledge out of people's heads and into agent context?
	- Same problem, new substrate. KM gives theoretical grounding for what I'm building.
- ---
- ## Context Curation is Knowledge Management
	- [[Manual context curation is the work]] is essentially manual KM:
	- | KM Term | HAC Equivalent |
	  |---------|----------------|
	  | Knowledge capture | Writing to knowledge base |
	  | Knowledge organization | Folder structure, tagging |
	  | Knowledge retrieval | Pulling files into context |
	  | Knowledge transfer | Agent reading context |
	- The second-generation KM insight — that knowledge sticks to people and context — explains why [[Manual context curation is the work|manual curation works better]] than automated RAG systems.
- ---
- ## Externalization as the Critical Bridge
	- [[Externalization]] is the KM process most central to agentic workflows.
	- **Why externalization specifically?**
		- Agents can only work with explicit knowledge
		- Tacit knowledge must be externalized before delegation is possible
		- The "distraction" of explaining to an agent IS the externalization process
	- This is the insight behind [[Knowledge Externalization as Agentic Interface]]: interacting with an agent forces the tacit → explicit conversion that KM has always sought.
	- The recent HAC-SECI (2025) and GRAI (2025) frameworks formalize this — AI as externalization accelerator, but human remains essential for internalization.
- ---
- ## The Autonomy Connection
	- KM traditionally aimed to make organizational knowledge **persistent** (survives employee turnover) and **accessible** (findable when needed).
	- In HAC, externalized knowledge enables **autonomy**:
	- > Better context = Higher safe autonomy
	- [[The Autonomy Slider]] moves right as knowledge becomes more explicit and accessible to agents.
	- This reframes KM's value proposition: not just "knowledge stays when people leave" but "knowledge enables delegation while people stay."
- ---
- ## Where I Extend Beyond Classical KM
	- | Classical KM | My Framework |
	  |--------------|--------------|
	  | Knowledge for organizational memory | Knowledge for agent context |
	  | Transfer between humans | Transfer from human to agent |
	  | Codification vs. personalization debate | Manual curation as synthesis |
	  | Communities of practice as social | Workspace as collaboration surface |
	  | Ba as shared space | IDE/filesystem as ba |
	- The key extension: **the agent as a knowledge consumer with different properties than human consumers**
		- Agents don't "internalize" — they only process explicit context
		- Agents have no persistent memory across sessions (yet)
		- Agents can process more explicit knowledge faster, but lack tacit judgment
	- This asymmetry is why [[The human works through the agent's hands]] — the human provides the tacit remainder.
- ---
- ## Open Questions
	- Is there a "third generation" of KM emerging around human-AI knowledge systems?
	- Does the HAC-SECI model's finding (AI helps externalization, hurts internalization) suggest a fundamental limit?
	- How do communities of practice work when some members are agents?
	- What happens to "ba" when the shared space is an IDE and one participant is an LLM?
- ---
- ## Related
	- [[Externalization]]
	- [[Tacit vs. Explicit Knowledge]]
	- [[Knowledge Externalization as Agentic Interface]]
	- [[Human-Agent Collaboration Framework]]
	- [[Manual context curation is the work]]
	- [[The SECI Model]]






