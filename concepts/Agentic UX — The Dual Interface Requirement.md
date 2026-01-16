type:: [[Working Note]]
status:: Working
date-created:: 2025-12-04
sources:: [[Michał (own)]]
related:: [[The workspace is the collaboration surface]], [[Tight feedback loops through artifact visibility]]

- # Agentic UX — The Dual Interface Requirement
- 🚧 *This is a moat observation — the UX layer is undersolved and critical*
- ---
- ## The Core Requirement: Dual Interface
	- A workspace where:
		- **Agent can make changes** — write files, edit content, produce artifacts
		- **Human quickly sees changes** — diffs visible, navigation easy
		- **Human can make changes too** — same surface, editable by both
	- This is not just "agent has tools." It's **shared editability on visible artifacts**.
- ---
- ## Why Cursor Works (and Claude Desktop Doesn't)
	- After a week with Claude Desktop/Claude Code for non-coding agentic work, returned to Cursor with .md files.
	- ### What Cursor gets right
		- **Chat and file in one view** — tight feedback loop, no context switch
		- **Diff visibility** — see exactly what agent changed, accept/reject granularly
		- **File tree navigation** — hierarchical, not flat; visibility into system structure
		- **Cmd+P quick open** — fast navigation to any file
		- **Seamless file search and editing** — agent writes, human edits, same interface
		- **Can update the system itself** — cursor commands, cursor rules editable in-place
		- **No schema maintenance** — just files, no database to manage
	- ### What Claude Desktop gets wrong
		- **Filesystem use is hard** — agent's results not easily visible
		- **Artifacts can't be edited by humans** — read-only, breaks dual interface
		- **Artifact list is flat** — no hierarchy, no tree, can't see structure
		- **No navigation** — can't quickly jump to specific artifact or file
		- **Separation between chat and workspace** — context switch required
- ---
- ## The Dual Interface Properties
	- | Property | What it means | Cursor | Claude Desktop |
	  |----------|---------------|--------|----------------|
	  | **Shared surface** | Both agent and human write to same place | ✓ files | ✗ artifacts read-only |
	  | **Visible diffs** | See what changed, not just new state | ✓ git-style | ✗ no diff view |
	  | **Hierarchical navigation** | Tree structure, not flat list | ✓ file tree | ✗ flat artifact list |
	  | **Quick access** | Keyboard shortcuts to any location | ✓ Cmd+P | ✗ scroll through list |
	  | **In-view editing** | Change without leaving context | ✓ inline | ✗ separate mode |
	  | **System self-modification** | Agent/human can update the rules | ✓ cursor rules | ✗ no equivalent |
- ---
- ## Why This Matters
	- The UX layer determines whether supervision is effortful or natural.
	- If seeing agent's work requires context switch → supervision degrades → trust degrades → collaboration fails.
	- **The workspace UX is load-bearing infrastructure, not nice-to-have.**
- ---
- ## The Moat Observation
	- Everyone's building agents. Few are building the collaboration surface well.
	- Cursor succeeded partly because they solved dual interface for code.
	- **Who solves it for non-code knowledge work?**
	- This is undersolved and critical. The agent capabilities are commoditizing; the UX for human-agent collaboration is not.
- ---
- ## Design Principles for Agentic UX
	- 1. **Dual editability** — both parties can modify the same artifacts
	  2. **Spatial proximity** — chat and workspace visible together
	  3. **Diff-first** — show changes, not just new state
	  4. **Hierarchical navigation** — tree structure, not flat list
	  5. **Keyboard-driven** — quick access without mouse hunting
	  6. **Self-modifying** — the system's rules live in the workspace too
	  7. **No schema** — files over databases where possible
- ---
- ## Implications for Product
	- If building agentic tools for knowledge workers:
		- Don't just add "AI features" to existing UI
		- Redesign for dual interface from ground up
		- The artifact surface is the product, not the chat
	- If implementing collaboration systems for clients:
		- Tool choice matters — Cursor-like UX vs Claude-like UX is night and day
		- May need to build custom workspace layer
		- File-based systems currently win on inspectability
- ---
- ## Open Questions
	- Can Claude Desktop evolve to have these properties? Or is it architecturally limited?
	- What's the equivalent of "file tree" for non-file artifacts (e.g., database records, API state)?
	- Is there a general-purpose agentic workspace waiting to be built?
	- How do you get diff visibility for non-text artifacts (images, structured data)?
- ---
- ## Related
	- [[The workspace is the collaboration surface]]
	- [[Tight feedback loops through artifact visibility]]
	- [[Middle artifacts as collaboration checkpoints]]
	- [[Manual context curation is the work]]
	- [[In-Context Skill Development]]