type:: [[Permanent Note]]
status:: Settled
date-created:: 2025-12-08
sources:: [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]], [[Literature - Governance for AI Agent Deployment (MLOps Community)]]

- # The Supervision Split
  
  **Who supervises determines the pattern: developer-supervised autonomous agents vs. user-supervised collaborative agents.**
  
  ---
- ## The Two Patterns
- ### Developer-Supervised Autonomous Agents
	- **Developer** builds, tests, supervises during development
	- **User** just uses the finished agent
	- Agent runs autonomously once deployed
	- Supervision happens pre-deployment
	- Changes require developer intervention
- ### User-Supervised Collaborative Agents
	- **User** supervises the agent during actual work
	- Agent and user collaborate on tasks together
	- Supervision happens during execution
	- User builds autonomy gradually through use
	- [[The Autonomy Slider]] moves right over time as trust increases
	  
	  ---
- ## Why This Distinction Matters
- ### Different Value Propositions
  
  **Autonomous agents** promise:
- "Set it and forget it"
- No ongoing human time required
- Scale through deployment
  
  **Collaborative agents** promise:
- Better outcomes on complex tasks
- User retains control and judgment
- Learning compounds over time
- ### Different Bottlenecks
  
  **Autonomous agents** bottlenecked by:
- Developer expertise in the domain
- Comprehensive testing/evaluation
- Edge case handling
- Trust requirements for unattended operation
  
  **Collaborative agents** bottlenecked by:
- User willingness to supervise
- Quality of supervision interface ([[Agentic UX]])
- Context curation infrastructure ([[The Filesystem as Agentic Ba]])
  
  ---
- ## The Skills Framework Bridges Both
  
  From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
  
  **The breakthrough**: Non-technical users can create skills (procedural knowledge) that make agents more autonomous.
  
  The progression:
  1. User does task manually (tacit knowledge)
  2. User supervises agent doing task (externalization begins)
  3. User captures patterns as skills/AGENTS.md (procedural context)
  4. Agent does task more autonomously (slider moves right)
  5. **Another user inherits that autonomy** (skills transfer)
  
  **The insight**: The user who supervises daily IS the person who should encode the skills, not a separate developer.
  
  This creates a third category:
- **User-developed autonomous agents** - Users build autonomy incrementally through supervision, then that autonomy becomes reusable
  
  ---
- ## Practical Implications
- ### For Product Design
  
  **If building autonomous agents**:
- Need comprehensive evals ([[Trust model determines formalization requirements]])
- Must handle edge cases without human
- Target simple, predictable workflows
- Example: Email draft generation (from governance podcast)
  
  **If building collaborative agents**:
- Need excellent supervision UX ([[Agentic UX — The Dual Interface Requirement]])
- Focus on [[Middle artifacts as collaboration checkpoints]]
- Target complex, judgment-heavy work
- Example: Research workflows, legal analysis
  
  **If enabling user-developed autonomy**:
- Provide skill/context authoring tools
- Make supervision → externalization easy
- Support incremental formalization
- Example: Claude Skills, AGENTS.md patterns
- ### For Use Case Selection
  
  | Task Characteristics | Pattern |
  |---------------------|---------|
  | Simple, repetitive, predictable | Developer-supervised autonomous |
  | Complex, requires judgment, high-stakes | User-supervised collaborative |
  | Domain expertise lives with user | User-develops autonomy via skills |
  
  ---
- ## The Supervision Progression Model
  
  **Phase 1: High Supervision**
- User watches every action
- Frequent intervention
- [[Manual context curation is the work]]
  
  **Phase 2: Checkpoint Supervision**
- User reviews intermediate artifacts
- [[Supervision is context curation, not action approval]]
- Agent has autonomy between checkpoints
  
  **Phase 3: Outcome Supervision**
- User reviews final results
- Agent handles full workflow
- Intervention only on failure
  
  **Phase 4: Autonomous (with monitoring)**
- Agent runs unattended
- User checks periodically
- May serve other users
  
  **Key insight**: Phases 1-3 are user-supervised collaboration. Phase 4 is when it becomes truly autonomous. Most valuable work lives in Phases 2-3.
  
  ---
- ## Connection to Trust Models
  
  From [[Trust model determines formalization requirements]]:
- **Embedded trust** (user supervises their own agent) = collaborative pattern
- **Transferable trust** (others use the agent) = autonomous pattern
  
  The supervision split maps directly to trust requirements:
- User-supervised = embedded trust is sufficient
- Autonomous = transferable trust required (formal evals, docs, error handling)
  
  **The opportunity**: Most current value is in embedded trust / collaborative agents, which has lower barriers to deployment than fully autonomous agents.
  
  ---
- ## Quotes from Sources
  
  **On autonomous agents** (Governance podcast):
- "Email for instance... an AI that just looks through your inbox and then puts a draft reply... you didn't go to a chat... it's right there."
- Simple, predictable task → autonomous pattern works
  
  **On collaborative agents** (Governance podcast):
- "You got to be on top of them. Once an hour, every couple of hours, you got to check in... until you get a level of trust."
- Complex work → supervision required
  
  **On user-developed autonomy** (Agent Skills):
- "Non-technical skill builders... people in functions like finance, recruiting, accounting, legal"
- Domain experts encoding their supervision as reusable skills
  
  ---
- ## Related
- [[The Autonomy Slider]]
- [[Trust model determines formalization requirements]]
- [[Knowledge Externalization as Agentic Interface]]
- [[The human works through the agent's hands]]
- [[In-Context Skill Development]]
- [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]