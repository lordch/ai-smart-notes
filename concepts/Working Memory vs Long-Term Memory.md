type:: [[Permanent Note]]
status:: Working
date-created:: 2025-12-09
sources:: [[Conversation with Claude (2025-12-09)]]

- # Working Memory vs Long-Term Memory
- **Two distinct memory systems serve different purposes in human-agent collaboration.**
- ---
- ## Comparison
	- | Dimension | Long-Term Memory | Working Memory |
	  |-----------|------------------|----------------|
	  | **Purpose** | Agent gets better over time | Task gets completed coherently |
	  | **Scope** | Cross-session, cross-task | Within-task, multi-session possible |
	  | **Examples** | Skills, AGENTS.md, knowledge base | Task lists, research reports, progress files |
	  | **Who curates** | Human (or agent with oversight) | Agent (with human checkpoints) |
	  | **Question** | "How do we do things here?" | "What's the state of this task?" |
	  | **Persists after task?** | Yes | Archive only |
	  | **Failure mode** | Agent amnesia | Context overflow, handoff failures |
- ---
- ## Long-Term Memory (Learning Memory)
	- Enables **in-context long-term learning**
	- Accumulates organizational/domain expertise
	- Multiple agents access it (organizational asset)
	- Human edits frequently
	- Primary value: expertise accumulation
	- See [[Agent Amnesia and the Continuity Problem]] for implementation approaches.
- ---
- ## Working Memory (Task Memory)
	- Enables **execution continuity**
	- Allows multiple agents to work on same task
	- Enables handoff when context window fills
	- Agent writes, human reviews at checkpoints
	- Primary value: coherent task completion
- ---
- ## Mid-Work Artifacts
	- Working memory materializes as **mid-work artifacts**:
	- ### Functions
		- **Context offloading**: Move information out of context window, retrieve when needed
		- **Handoff enablement**: Another agent (or future session) can continue
		- **Human-agent alignment**: Inspect intermediate state, verify we're on same page
		- **Crystallization**: Producing artifact forces commitment to structure, creates stable foundation for subsequent work
	- ### The Compounding Effect
		- > "Artifacts externalize progress so it doesn't live only in tokens."
		- Without artifacts: progress exists only in conversation (fills window), human memory (unreliable), or weights (can't update mid-task)
		- With artifacts: progress exists in persistent files, shareable structures, inspectable states
		- Each artifact creates a **new baseline** from which subsequent work builds
		- **Artifacts are how you ratchet progress forward.**
	- See [[Middle artifacts as collaboration checkpoints]]
- ---
- ## The Interaction
	- Working memory can **graduate** to long-term memory:
		- Pattern emerges during task execution
		- Human recognizes it as reusable
		- Captures in skills/AGENTS.md/knowledge base
	- Long-term memory **informs** working memory:
		- Procedures loaded at task start
		- Working artifacts follow established patterns
		- New task benefits from accumulated expertise
- ---
- ## Related
	- [[Context Continuity Engineering]]
	- [[Agent Amnesia and the Continuity Problem]]
	- [[Middle artifacts as collaboration checkpoints]]
	- [[The Filesystem as Agentic Ba]]
	- [[Manual context curation is the work]]



