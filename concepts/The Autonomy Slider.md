type:: [[Permanent Note]]
status:: Settled
date-created:: 2025-12-04
sources:: [[Karpathy]]

- # The Autonomy Slider
- **The amount of autonomous control you grant an agent should vary by task complexity and the quality of context available.**
- "It's less Iron Man robots and more Iron Man suits." — Karpathy
- ---
- ## The Concept
	- Different tasks warrant different levels of agent autonomy:
		- **Low autonomy**: Tab completion, single-line suggestions
		- **Medium autonomy**: File-level edits with approval
		- **High autonomy**: Multi-file changes, full repo access
	- Examples from Cursor (Karpathy):
		- Tab completion (you're mostly in charge)
		- Command K (change selected chunk)
		- Command L (change entire file)
		- Command I ("let it rip" - full autonomy)
	- Examples from Perplexity:
		- Quick search (fast, narrow)
		- Research mode (medium depth)
		- Deep research (come back in 10 minutes)

- ## The Key Insight: Context Enables Autonomy
	- **The autonomy slider moves right as context quality improves.**
	- The more you invest in [[Knowledge Externalization as Agentic Interface]], the more you can safely delegate:
		- **Better factual context** → Agent knows what's true, hallucinates less
		- **Better procedural context** → Agent knows how to act, makes fewer mistakes
		- **Better organizational context** → Agent maintains continuity across sessions
	- This creates a positive feedback loop:
		- 1. Build knowledge base (manual curation)
		- 2. Increase autonomy slider (delegate more)
		- 3. Agent produces better artifacts (less supervision needed)
		- 4. Update knowledge base with learnings (context improves)
		- 5. Increase autonomy further

- ## The Timeline: Decade, Not Year
	- From Karpathy: **"This is the decade of agents, not the year."**
	- Autonomy increases gradually, not overnight.
	- Lessons from Tesla Autopilot:
		- Perfect demo in 2013
		- Still working on full autonomy 12 years later
		- Humans remain in the loop
	- The slider moves right over time, but carefully, with verification at each stage.

- ## Design Implications for Agentic UX
	- Products should expose the autonomy slider to users.
	- Users should control how much they delegate based on:
		- Task complexity
		- Risk tolerance
		- Quality of available context
	- The generation-verification loop must stay fast:
		- **Speed up verification**: Better GUIs, diffs, visual feedback
		- **Keep AI on leash**: Prevent 10,000-line diffs you can't review

- ## Related
	- [[Knowledge Externalization as Agentic Interface]]
	- [[Agentic UX]]
	- [[Supervision is context curation, not action approval]]
	- [[The human works through the agent's hands]]







