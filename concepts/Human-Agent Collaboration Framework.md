type:: [[Index Note]]
status:: Working
date-created:: 2025-12-02
sources:: [[Michał (own)]], [[Boundaryml]], [[Tool Use (Artem)]], [[AI and I (Noah)]], [[Darren]], [[Karpathy]], [[Vanishing Gradients]], [[Filesystems for Context Engineering (Gupta)]], [[AGENTS.md Best Practices (Sewell)]], [[LLM-Friendly Content in Markdown (Mukherjee)]], [[Agentic Context Engineering ACE (Zhang et al.)]]

- # Human-Agent Collaboration Framework
- A framework for working with AI agents that challenges the "AI as automation" narrative. The core insight: **the human works through the agent's hands** — delegated execution with retained responsibility, not replacement.
- ---
- ## The Core Thesis
	- The common framing of AI transformation imagines automation: a tool that takes tasks from human hands entirely. This misses what actually works.
	- What works: the human remains in the loop, but **what the human does changes**. Instead of doing the task directly, the human:
		- Curates context (what the agent sees)
		- Reviews intermediate artifacts (research, plans)
		- Maintains the infrastructure that makes collaboration possible
		- Moves up abstraction levels as patterns become reliable
	- The agent has hands; the human has judgment about where to point them.
- ---
- ## Core Principles
	- ### [[Supervision is context curation, not action approval]]
		- The high-leverage work isn't clicking "approve" — it's shaping what the agent sees before it acts. Context curation *is* supervision.
		- **Leverage hierarchy**: Research wrong → 1000s of bad lines. Plan wrong → 100s. Code wrong → 1.
	- ### [[The human works through the agent's hands]]
		- Delegated execution with retained responsibility. Not alongside, not replaced — *through*.
		- The collaboration loop: problem → agent researches → agent performs under supervision → human refines → knowledge updates → move up abstraction level → repeat.
	- ### [[Specs are contracts, not commands]]
		- Specs aren't input to a translator. They're shared artifacts of understanding — evidence that human and agent reached agreement.
		- Context curation is the layer *above* specs: factual (what agent knows), procedural (how to act), organizational (continuity).
	- ### [[Trust model determines formalization requirements]]
		- **Embedded trust**: You built it, supervise by feel, fix when it breaks. Formal evals optional.
		- **Transferable trust**: Others use it without you. Needs formal evals, documented behaviors.
		- Current high-value opportunity is in embedded regime.
	- ### [[Scripts for reliability, LLM for flexibility]]
		- Don't waste tokens on deterministic tasks. Scripts lock in patterns LLMs discover.
		- The ratchet: LLM explores → human identifies pattern → script captures → LLM explores at next level.
	- ### [[Resist premature artifact production]]
		- Models trained to produce. For complex work, producing too early short-circuits thinking.
		- Sequence: gather → organize → think → *then* produce.
	- ### [[The Autonomy Slider]]
		- Amount of autonomy granted should vary by task complexity and context quality.
		- As knowledge base improves, autonomy can safely increase.
		- "Decade of agents, not year" — gradual progression with verification.
- ---
- ## The Workspace Model
	- ### [[The workspace is the collaboration surface]]
		- Effective collaboration needs shared, persistent, inspectable space.
		- Properties that matter: persistent, navigable, editable by both, diffable, interoperable, inspectable.
		- The filesystem is a mature implementation. The properties matter more than the specific technology.
	- ### [[The Filesystem as Agentic Ba]]
		- The filesystem implements what Nonaka called "ba" (場) — a shared space for knowledge creation.
		- Unlike human-to-human ba, the filesystem **requires externalization** — tacit knowledge must become explicit to enter.
		- This constraint is a feature: forces articulation, creates audit trails, enables handoffs.
		- Directory structure maps to cognitive functions:
		- ```
		  project/
		    data/     → Factual context (raw inputs)
		    memory/   → Organizational context (cross-session)
		    task/     → Working context (current reasoning)
		    logs/     → Audit context (execution traces)
		  ```
		- Research shows structured hierarchical retrieval improves accuracy 40–60% vs. semantic search alone.
		- The "limitation" of literal retrieval is an advantage: keeps human in curation loop.
	- ### [[Tight feedback loops through artifact visibility]]
		- Gap between "agent acts" and "human observes" should be zero.
		- Spatial (same view), temporal (immediate), structural (artifact not chat message).
		- **You supervise by watching, not by interrogating.**
	- ### [[Middle artifacts as collaboration checkpoints]]
		- Every step produces inspectable artifact: research.md → plan.md → processed data → analysis.
		- These are contracts (shared understanding), inspection points (verify before proceeding), recovery points (trace back if wrong).
		- Artifacts enable handoff across agent amnesia boundaries.
		- Externalized chain-of-thought improves agent self-consistency (not just human review).
	- ### [[Markdown as LLM-Native Format]]
		- Markdown is not just convenient — it's the optimal format for LLM consumption.
		- Why: aligned with natural language, minimal syntax overhead, hierarchical headers, token efficient.
		- JSON/XML require LLMs to "navigate through layers of tags and attributes" — adds processing overhead and error potential.
		- This creates **double hierarchy**: filesystem structure + markdown headers within files.
		- Practical implication: knowledge base, AGENTS.md, research artifacts, plans — all should be markdown.
- ---
- ## Context Curation Taxonomy
	- 🚧 *Working model — important but not fully settled*
	- Three (possibly four) types of context the human curates:
	- | Type | Question | Examples | Directory | Canonical File |
	  |------|----------|----------|-----------|----------------|
	  | **Factual** | What does agent know? | Knowledge base, docs, research files | `data/` | — |
	  | **Procedural** | How should agent act here? | Dos/don'ts, commands, safety rules | `task/` | `AGENTS.md` |
	  | **Organizational** | How maintain continuity? | Compaction rituals, handoffs, folder structures | `memory/` | — |
	  | **Audit** *(candidate)* | What happened? | Execution traces, error logs, decision history | `logs/` | — |
	- Missing any one breaks differently:
		- Missing factual → agent hallucinates or searches forever
		- Missing procedural → agent does wrong thing confidently
		- Missing organizational → every session starts from scratch
		- Missing audit → can't debug failures or trace reasoning
	- **Implementation note**: `AGENTS.md` is an emerging standard for procedural context — a single file at project root containing dos/don'ts, commands, and safety rules.
	- See also: [[Context curation taxonomy]]
- ---
- ## Practical Implementation
	- ### What the human does
		- Curates knowledge base (factual context)
		- Defines workflows and commands (procedural context)
		- Establishes rituals for continuity (organizational context)
		- Reviews research and plans (high-leverage checkpoints)
		- Maintains the workspace infrastructure
	- ### What the agent does
		- Researches (searches, reads, synthesizes)
		- Plans (proposes approaches, identifies files to change)
		- Executes (writes code, produces artifacts)
		- Self-verifies (runs tests, checks against criteria)
	- ### The collaboration loop
		- 1. Human identifies problem/goal
		  2. Agent researches, produces research artifact
		  3. Human reviews research, steers if needed
		  4. Agent produces plan artifact
		  5. Human reviews plan, edits if needed
		  6. Agent implements against plan
		  7. Tests verify (automated trust)
		  8. Human updates knowledge base with learnings
		  9. If pattern reliable, human moves up one abstraction level
	- ### Procedural Context Files (AGENTS.md Pattern)
		- Every project should have procedural context at root (AGENTS.md, .cursorrules, etc.)
		- This is **procedural context** — telling agents how to act in this specific project
		- Recommended sections:
			- **Dos and Don'ts**: Library versions, patterns, conventions
			- **Commands**: File-scoped lint/test/typecheck (fast feedback)
			- **Safety**: What agent can do without asking vs. must ask first
			- **Structure hints**: Where routes, components, tokens live
			- **Examples**: Good files to emulate, legacy files to avoid
		- Build iteratively: "Add a rule the second time you see the same mistake"
		- See [[In-Context Skill Development]] for how these emerge during work
- ---
- ## Key Framings from Sources
	- ### From [[Boundaryml]]
		- Three-phase workflow: research → plan → implement
		- Sub-agents for context control (not anthropomorphizing)
		- "If I'm shouting at Claude, the plan was bad"
		- "Specs are source code, generated code is compiled artifact"
	- ### From [[Karpathy]]
		- LLMs are operating systems, circa 1960s
		- Generation/verification loop — speed it up, keep AI on leash
		- "Iron Man suits, not Iron Man robots"
		- Autonomy slider that moves right over time
		- "This is the *decade* of agents, not the year"
	- ### From [[Tool Use (Artem)]]
		- Slash commands as packaged workflows
		- "Don't waste tokens" — scripts for reliability
		- "80% with grep is good enough for personal use"
	- ### From [[AI and I (Noah)]]
		- Explicit "do not produce" instructions
		- Thinking partner mode (questions, not artifacts)
		- "Reading > writing"
	- ### From [[Vanishing Gradients]]
		- "Vibes first, then formalize"
		- Evals as competitive moat (for productized trust)
		- Destruction-rebuild cycle (harnesses rebuilt 3-5x/year)
- ---
- ## What This Is Not
	- **Not automation**: Human stays in loop, responsibility retained
	- **Not replacement**: Human's role changes, doesn't disappear
	- **Not "AI alongside human"**: Human works *through* agent, not next to it
	- **Not fully autonomous agents**: Autonomy earned incrementally, with human oversight
	- **Not one-shot solutions**: Infrastructure that compounds over time
- ---
- ## Academic Validation
	- ### ACE: Agentic Context Engineering (Zhang et al. 2025)
		- [arXiv:2510.04618](https://arxiv.org/abs/2510.04618) formalizes many concepts in this framework.
		- **Key alignment**:
			- "Contexts as evolving playbooks" = our knowledge base approach
			- "Generation → Reflection → Curation" = our collaboration loop
			- "Offline contexts" = AGENTS.md / system prompts
			- "Online contexts" = task/ artifacts / working memory
			- "Natural execution feedback" = learning from doing, not labels
		- **Results**: +10.6% on agent benchmarks, matched top production agent on AppWorld with smaller model.
		- **Critical insight**: Identified [[Brevity Bias and Context Collapse]] as failure modes that manual curation prevents.
		- See: [[Literature - Agentic Context Engineering ACE (Zhang et al.)]]
- ---
- ## The Business Opportunity
	- Implementing human-agent collaboration systems for specific knowledge work roles.
	- **What this involves:**
		- Organizing knowledge (factual curation)
		- Defining workflows and intermediate steps (procedural curation)
		- Designing mechanisms for continuity (organizational curation)
		- Setting up the workspace infrastructure
	- **What you're selling:**
		- Not an agent, not a tool, not automation
		- The implementation of working relationship infrastructure
	- **Target**: Work that's "too expensive to do well" currently. Roles with high context-switching costs. Industries: legal, consulting, technical writing, financial analysis, recruiting.
- ---
- ## Open Questions
	- What determines "reliable enough" to move up an abstraction level?
	- Is knowledge organization automatable, or is manual curation the moat? → ACE research suggests curation is essential to prevent [[Brevity Bias and Context Collapse]].
	- How do you transfer embedded trust to transferable trust without losing what works?
	- Is there a fourth type of context curation? → **Candidate: Audit** (execution traces, error logs, decision history). See [[The Filesystem as Agentic Ba]].
	- What would productized "collaboration infrastructure implementation" look like?
	- What are the right compaction/cleanup policies? → ACE suggests "structured incremental updates" — append and organize, don't rewrite and compress. See [[Brevity Bias and Context Collapse]].
- ---
- ## Related Notes
	- ### Permanent Notes
		- [[Supervision is context curation, not action approval]]
		- [[The human works through the agent's hands]]
		- [[Scripts for reliability, LLM for flexibility]]
		- [[Trust model determines formalization requirements]]
		- [[Resist premature artifact production]]
		- [[Specs are contracts, not commands]]
		- [[The workspace is the collaboration surface]]
		- [[The Filesystem as Agentic Ba]]
		- [[Markdown as LLM-Native Format]]
		- [[Tight feedback loops through artifact visibility]]
		- [[Middle artifacts as collaboration checkpoints]]
		- [[The Autonomy Slider]]
		- [[Agentic UX]]
		- [[Brevity Bias and Context Collapse]]
	- ### Working Notes
		- [[Context curation taxonomy]]
		- [[Knowledge Externalization as Agentic Interface]]
	- ### Reference Notes
		- [[Knowledge Management]]
		- [[Literature Review - Knowledge Management Field (2020-2025)]]
	- ### Literature Notes
		- [[Literature - Boundaryml]]
		- [[Literature - Karpathy]]
		- [[Literature - Vanishing Gradients]]
		- [[Literature - Tool Use (Artem)]]
		- [[Literature - AI and I (Noah)]]
		- [[Literature - Darren]]
		- [[Literature - Filesystems for Context Engineering (Gupta)]]
		- [[Literature - AGENTS.md Best Practices (Sewell)]]
		- [[Literature - LLM-Friendly Content in Markdown (Mukherjee)]]
		- [[Literature - Agentic Context Engineering ACE (Zhang et al.)]]