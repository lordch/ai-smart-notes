type:: [[Permanent Note]]
status:: Settled
sources:: [[Michał (own)]], [[Boundaryml]], [[Tool Use (Artem)]], [[AI and I (Noah)]], [[Darren]]
date-created:: 2025-11-29
core-claim:: The high-leverage work is shaping what the agent sees, not approving what it does. Human attention should be proportional to leverage (research > plan > code).

- The valuable work in human-agent collaboration isn't clicking "approve" on agent actions. It's shaping what the agent sees before it acts.
- This reframes what supervision means. The naive model: agent proposes, human approves or rejects. The actual high-leverage move: human curates the context window — what files to read, what constraints matter, what "good" looks like — so the agent's proposals are already aligned.
- ## The leverage hierarchy
	- Boundaryml quantifies this:
		- Core prompts/setup wrong → 100,000 bad lines of code
		- Research wrong → 1,000 bad lines
		- Implementation plan wrong → 10-100 bad lines
		- Individual code line wrong → 1 bad line
	- Human attention should be proportional to leverage. Review the research and plan closely. The code itself? Less scrutiny if tests pass. The bottleneck isn't the final action — it's the context that shaped it.
- ## Why "automate the approval step" misses the point
	- Even if you could perfectly verify every agent action, you'd still need a human curating what goes into the context. The context *is* the supervision.
- ## Practical implications
	- Invest in knowledge base organization (what the agent can see)
	- Write implementation plans before letting agents code
	- Treat "what files should it read?" as a first-class decision
	- Review outputs at the research/planning layer, not just the execution layer
- ## Sources
	- **Boundaryml (Dexter & Vaibhav)** — Explicit leverage hierarchy. "A bad line of research can lead to a thousand bad lines of code." Three-phase workflow with human review gates at each transition.
	- **Artem Zhutov (Tool Use)** — Context management through parsers that extract only last 3 logs. The curation infrastructure *is* the work.
	- **Noah Brier (AI and I)** — "Catch me up on last three days" pattern. Human maintains the organization that makes context recoverable.
	- **Darren** — Strategic alignment layer that everything checks against. Human defines the knowledge base; system enforces alignment.
	- **Michał (own practice)** — Manual workflow with close curation for compact context. "Like my worker" — responsible for what it does, which means responsible for what it knows.
- ## Related
	- [[The human works through the agent's hands]]
	- [[Leverage hierarchy — attention follows impact]]
	- [[Trust model determines formalization requirements]]
