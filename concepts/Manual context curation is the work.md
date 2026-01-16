type:: [[Permanent Note]]
status:: Settled
date-created:: 2025-12-04
sources:: [[Michał (own)]], [[Tool Use (Artem)]], [[AI and I (Noah)]], [[Boundaryml]]

- # Manual Context Curation is the Work
- Managing both **remembering** (what gets saved) and **recall** (what gets retrieved) manually is currently what works best.
- **This is not a limitation to overcome. It's a practice to embrace.**
- ---
- ## The postulate
	- Instead of trying to implement automated, universal context management systems, do it manually:
		- Curate what goes into the knowledge base
		- Tag relevant files into prompts by hand
		- Decide what to compact and what to preserve
		- Organize folder structures intentionally
	- This works better than automation because:
		- You know what's relevant to *this* task
		- You can apply judgment about what level of detail matters
		- You learn your system by maintaining it
		- No schema maintenance, no retrieval tuning, no RAG failures
- ---
- ## Evidence from practitioners
	- Everyone doing effective human-agent collaboration does manual curation:
	- **Artem Zhutov** — Tried to build automated context-preparation system. Abandoned it for simpler manual approach.
	- **Noah Brier** — Folder organization maintained by hand.
	- **Boundaryml** — "Slash compact is trash." Manual compaction beats auto-summarization.
	- **Michał** — Close curation of markdown knowledge base. Tag relevant .md files into prompts. Update after each task.
- ---
- ## Why automation fails (for now)
	- Automated systems try to solve:
		- What to remember? (everything? summaries? key facts?)
		- How to retrieve? (semantic search? keyword? recency?)
		- What's relevant now? (depends on task, context, intent)
	- These require judgment. The human has it. The system doesn't.
	- Automation adds:
		- Schema to maintain
		- Retrieval to tune
		- Failure modes to debug
		- Abstraction between you and your knowledge
	- Manual curation removes all of this. Files in folders. You know where things are.
- ---
- ## The agent-managed memory alternative
	- There is an emerging middle ground: **agents that manage their own memory** (e.g., mem-agent, MemGPT)
	- ### How it works
		- Agent has file operation tools (create, read, update, delete)
		- Agent autonomously decides what to store, where, and when
		- Structured format (markdown + links) keeps it human-readable
		- Agent trained specifically for memory management tasks
	- ### The trade-off
		- **Gained**: Zero manual effort from human
		- **Lost**: Human editorial control over what's remembered
		- **Reality**: Current performance ~77% on benchmarks (promising but imperfect)
	- ### When each approach works best
		- | Context Type | Best Approach | Why |
		  |--------------|---------------|-----|
		  | **Procedural knowledge** (workflows, best practices) | Human curation | High stakes, requires domain judgment, team knowledge transfer |
		  | **Personal context** (preferences, history) | Agent-managed | Low stakes, user-specific, high volume |
		  | **Organizational memory** (weird unique ways we do things) | Human curation | Tacit knowledge that can't be automatically captured |
		  | **Conversational continuity** (session handoffs) | Agent-managed or hybrid | Automatic capture useful, human reviews important patterns |
	- See [[Agent Amnesia and the Continuity Problem]] for detailed comparison of approaches.
- ---
- ## The practice
	- 1. **After each task**: Update knowledge base with what you learned
	  2. **Before each task**: Pull relevant files into context manually
	  3. **Regularly**: Reorganize, consolidate, prune
	  4. **When context fills**: Compact intentionally to progress file
	- This is work. It's also the *right* work — high-leverage curation that makes everything downstream better.
- ---
- ## Curation at scale: Progressive disclosure
	- From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
		- Manual curation doesn't mean you can only manage a few files
		- With progressive disclosure, you can curate **hundreds of skills**
		- How: Show only metadata initially, load full content when needed
	- ### The pattern
		- Skill library: 100+ skills available
		- Runtime: Agent sees list of skill names + brief descriptions
		- When needed: Agent loads full skill.md with detailed instructions
		- Result: "Hundreds of skills" curated manually, accessed efficiently
	- ### Why this works
		- Initial context cost: ~1 line per skill (name + description)
		- Full context cost: Only when skill is actually used
		- Human curates each skill carefully (quality stays high)
		- Agent benefits from entire library without context overload
	- This is manual curation that scales through **organization**, not automation.
	- See [[Brevity Bias and Context Collapse]] for why progressive disclosure beats compression.
- ---
- ## Related
	- [[Supervision is context curation, not action approval]]
	- [[Context curation taxonomy]]
	- [[The workspace is the collaboration surface]]
	- [[Agentic UX — The Dual Interface Requirement]]
