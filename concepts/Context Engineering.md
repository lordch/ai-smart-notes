type:: [[Permanent Note]]
status:: Working
date-created:: 2025-12-09
sources:: [[YouTube - Chatting agents, context engineering and more with Dex Horthy (@dexhorthy)]]

- # Context Engineering
- **The discipline of designing systems that provide language models with maximally useful information at minimal token cost.**
- ---
- ## Definition
	- From Dex Horthy:
		- "How do you get the most out of today's models?"
		- "Getting the right information in, but also keeping it as small as possible"
		- "Not token dense, but **information per token density**"
	- Context engineering optimizes for **signal density**, not token count.
- ---
- ## Two Dimensions
	- ### Context Density Engineering
		- Maximizing signal-to-noise in a given context window
		- Techniques: pruning, compaction, progressive disclosure, retrieval strategies
		- Focus: the single interaction
	- ### Context Continuity Engineering
		- How context persists, accumulates, and transfers across time
		- Systems: memory architectures, workspace organization, handoff protocols
		- Focus: learning over time
	- See [[Context Continuity Engineering]] for the continuity dimension (this framework's focus).
- ---
- ## Why It's Permanent
	- From Dex:
		- > "As long as we're dealing with quadratic transformer attention, you're always going to benefit from doing the deterministic engineering that allows you to keep the context window as small as possible for a given task."
	- Context engineering isn't a temporary workaround—it's a **permanent discipline**.
- ---
- ## Techniques Catalog
	- ### Selection & Retrieval
		- What to include, what to exclude
		- RAG, semantic search, literal lookup
		- Progressive disclosure (show metadata, load on demand)
	- ### Formatting & Density
		- [[Markdown as LLM-Native Format]]
		- Front matter for deterministic filtering
		- Information density per token
	- ### Architecture
		- Fast orchestrator + slow oracle pattern
		- Sub-agents for context isolation
		- Deterministic layers for context stuffing
	- ### Failure Prevention
		- [[Brevity Bias and Context Collapse]]
		- Instruction following limits (~100-200 instructions)
		- Instruction severity inflation (all-caps competition)
- ---
- ## Relation to This Framework
	- This framework focuses on **Context Continuity Engineering**—the systems that feed the context window over time.
	- Context density techniques make that infrastructure more efficient when it hits the model.
	- | Framework Focus | Context Engineering Focus |
	  |-----------------|---------------------------|
	  | Where context lives | How context is optimized |
	  | Who curates it | What goes in |
	  | Why it persists | How dense it is |
- ---
- ## Related
	- [[Context Continuity Engineering]]
	- [[Manual context curation is the work]]
	- [[Brevity Bias and Context Collapse]]
	- [[The Filesystem as Agentic Ba]]



