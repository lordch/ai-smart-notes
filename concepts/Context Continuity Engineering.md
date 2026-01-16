type:: [[Permanent Note]]
status:: Working
date-created:: 2025-12-09
sources:: [[YouTube - Chatting agents, context engineering and more with Dex Horthy (@dexhorthy)]]

- # Context Continuity Engineering
- **How context persists, accumulates, and transfers across time, sessions, and agents—enabling in-context long-term learning.**
- This is a subset of [[Context Engineering]] focused on building systems for just-in-time, tailored context curation.
- ---
- ## The Problem Space
	- Models are stateless
	- Context windows are finite and ephemeral
	- Without intervention, every session starts from zero
	- See [[Agent Amnesia and the Continuity Problem]]
- ---
- ## Two Memory Types
	- ### Long-Term Memory (Learning Memory)
		- **Purpose**: Agent gets better over time
		- **Scope**: Cross-session, cross-task
		- **Examples**: Skills, AGENTS.md, knowledge base
		- **Who curates**: Human (or agent with human oversight)
		- **Question answered**: "How do we do things here?"
		- **Failure mode**: Agent amnesia
	- ### Working Memory (Task Memory)
		- **Purpose**: Task gets completed coherently
		- **Scope**: Within-task, potentially multi-session
		- **Examples**: Task lists, research reports, progress files
		- **Who curates**: Agent (with human checkpoints)
		- **Question answered**: "What's the state of this task?"
		- **Failure mode**: Context overflow, handoff failures
	- See [[Working Memory vs Long-Term Memory]] for detailed comparison.
- ---
- ## Context Layers Model
	- | Layer | Scope | Purpose | Durability |
	  |-------|-------|---------|------------|
	  | **Weights** | Universal | What models know from training | Permanent |
	  | **System context** | Session | Who agent is, how to behave | Session-bound |
	  | **Long-term context** | Cross-session | Organizational/domain expertise | Persistent |
	  | **Working context** | Within-task | Task state, progress, decisions | Task-bound |
	  | **Immediate context** | Current turn | What's being discussed now | Turn-bound |
	- This framework focuses on **long-term** and **working** layers—the two requiring explicit infrastructure.
- ---
- ## Domain Dependency
	- **Hypothesis**: The importance of external procedural memory varies by domain characteristics.
	- ### Why SWE Agents Need Less Procedural Memory
		- **Knowledge in weights**: Massive programming knowledge in training data
		- **Code-native actions**: Most actions (git, databases, servers, docker) executable via code/commands
		- The domain's "action space" is already the model's native interface
	- ### Why Other Domains Need More
		- **Knowledge gap**: Less domain expertise in weights (legal, finance, recruiting, niche processes)
		- **Integration-heavy actions**: Require browser use, external systems, complex APIs, human-facing interfaces
		- The domain's action space requires translation and orchestration
	- ### Implication
		- SWE agents: Factual + task context most critical
		- Other domains: Procedural memory becomes essential infrastructure
		- See [[General Agents with Domain Skills]] for the architectural implications.
- ---
- ## Related
	- [[Context Engineering]]
	- [[Agent Amnesia and the Continuity Problem]]
	- [[Working Memory vs Long-Term Memory]]
	- [[Manual context curation is the work]]
	- [[Middle artifacts as collaboration checkpoints]]



