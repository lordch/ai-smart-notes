type:: [[Permanent Note]]
status:: Working
date-created:: 2025-12-13
sources:: [[Human-Agent Collaboration Framework]], [[Integrated Environment Principle]], [[The Supervision Split]], [[Working Memory vs Long-Term Memory]], [[Agentic UX — The Dual Interface Requirement]], [[Meeting Users Where They Are]], [[Literature - NEW ChatGPT 5.2 Complete Breakdown (Nate B Jones)]]

- # Middle artifacts as collaboration checkpoints
- ---
- ## Core idea
	- **Artifacts are the supervision interface and the collaboration interface.**
	- Chat is the steering channel; artifacts are the shared state.
	- The practical loop: produce an inspectable artifact → review/adjust → proceed with bounded autonomy until the next checkpoint.
- ---
- ## Why “middle” artifacts matter
	- **They externalize progress** so it doesn’t live only in tokens or human memory. See [[Working Memory vs Long-Term Memory]].
	- **They create recovery points**: when something goes wrong, you can trace back to the last good artifact.
	- **They enable handoff** across session boundaries (and across agents) without losing the task state.
	- **They make supervision cheap**: you supervise by inspecting, not by interrogating.
- ---
- ## Artifact types (useful taxonomy)
	- **Research artifact**: what was found and what sources were used (e.g., `research.md`, `sources/*`).
	- **Plan artifact**: the intended steps, constraints, and acceptance criteria (e.g., `plan.md`, TODO list).
	- **Intermediate work artifacts**: partial outputs that let you validate direction early (draft slide outline, preliminary table, partial analysis).
	- **Final artifacts**: the deliverable in the native medium (PowerPoint, spreadsheet, doc, code change set).
- ---
- ## Checkpoint supervision (the pattern)
	- From [[The Supervision Split]]: most high-value work happens when the agent has autonomy **between checkpoints**, not fully unattended.
	- A checkpoint is where the human verifies:
		- **Scope**: are we solving the right problem?
		- **Inputs**: did the agent interpret the bundle correctly?
		- **Output contract**: is the artifact trending toward the right shape/audience?
		- **Risk**: what could silently fail if we continue?
- ---
- ## UX requirement: artifacts must be easy to see and edit
	- Checkpoints only work when the environment is integrated:
		- Immediate visibility + dual editability + navigation. See [[Integrated Environment Principle]].
		- “Diff-first” supervision for text; analogous inspection affordances for non-text artifacts. See [[Agentic UX — The Dual Interface Requirement]].
- ---
- ## Why native artifacts matter (beyond “nice outputs”)
	- Native artifacts reduce context switching and supervision cost. See [[Meeting Users Where They Are]].
	- They’re also how long-running delegation stays safe: the longer the run, the more expensive a misframe, so the more valuable checkpoints become.
	- This is the key connection to [[Literature - NEW ChatGPT 5.2 Complete Breakdown (Nate B Jones)]]: long-running, agentic work increases leverage of artifact-based checkpointing.
- ---
- ## Guardrail: resist premature artifacts
	- The failure mode: producing a polished deliverable too early can lock in the wrong frame.
	- Sequence that tends to work:
		- gather → organize → think → **intermediate artifact** → verify → **final artifact**
	- See [[Resist premature artifact production]].
- ---
- ## Practical “delegation packet” (checkpoint-friendly)
	- **Scope**: what problem, what’s out of scope.
	- **Output spec**: format, structure, audience, “done” criteria.
	- **Input description**: what’s in the bundle and how to interpret it.
	- **Validation**: what to spot-check (numbers, claims, formatting, assumptions).




