type:: [[Index Note]]
status:: Working
date-created:: 2025-12-04
sources:: [[Standard Beagle]], [[Microsoft Design]], [[Nielsen Norman Group]]

- # Agentic UX
- **User Experience design for systems where the user manages autonomous agents rather than manipulating direct interfaces.**
- ---
- ## Core Concepts
	- **The Dual Interface**: Users need both a "Chat" (to direct) and a "Dashboard" (to inspect/correct). See [[Agentic UX — The Dual Interface Requirement]].
	- **The Autonomy Slider**: Users control how much autonomy to grant based on task and context quality. See [[The Autonomy Slider]].
	- **Visibility of Thought**: The system must expose *how* it is thinking, not just the final output.
	- **Steerability**: The ability to intervene mid-flight (stopping, redirecting, clarifying) without restarting.
	- **Context Awareness**: The interface must show what context the agent is currently "holding" (files, memories, instructions).
	- **Integrated Environment**: Minimize context switching - see [[Integrated Environment Principle]].

- ## The Paradigm Shift
	- | Traditional UX | Agentic UX |
	  |---|---|
	  | User clicks buttons | User defines goals |
	  | Deterministic paths | Probabilistic outcomes |
	  | Immediate feedback | Asynchronous execution |
	  | State is hidden | State (context) is the interface |

- ## Key Challenges
	- **Trust**: How do we know the agent did what we asked? (Answer: [[Supervision is context curation, not action approval]])
	- **Handoff**: How does the agent pass control back to the user when stuck?
	- **Latency**: How to manage expectations when "thinking" takes time?
	- **Knowledge Externalization**: How to make "teaching the agent" feel like work, not a chore? ([[Knowledge Externalization as Agentic Interface]])

- ## Insights & Patterns
	- **"Show Your Work"**: Agents should produce intermediate artifacts (plans, outlines) before final deliverables.
	- **"Diff Views"**: Interfaces should highlight *what changed* rather than just showing the new state.
	- **"Memory Management"**: Users need tools to see and edit what the agent "remembers" about them.
	- **"Meet Users Where They Are"**: Agent outputs should appear in tools users already use, not force users to visit separate AI interface. See [[Meeting Users Where They Are]].
	- **"Beyond Text I/O"**: Output in native formats (charts not descriptions), input via buttons/sliders for frequent actions (not just chat).

- ## Related Notes
	- [[Human-Agent Collaboration Framework]]
	- [[The human works through the agent's hands]]
	- [[Knowledge Externalization as Agentic Interface]]
	- [[Manual context curation is the work]]
	- [[Meeting Users Where They Are]]
	- [[Integrated Environment Principle]]
	- [[The Supervision Split]]

