type:: [[Permanent Note]]
status:: Working
date-created:: 2025-12-08
sources:: [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]], [[Literature - Filesystems for Context Engineering (Gupta)]], [[The Supervision Split]]

- # Agent Amnesia and the Continuity Problem
  
  **Agents lack persistent memory across sessions. Without remediation, every interaction starts from zero. The solution requires externalized, persistent knowledge that accumulates over time — whether through human-supervised curation or automatic memory systems.**
  
  ---
- ## The Problem: Session Boundaries Reset Everything
  
  Agents don't retain experience:
- No memory of what worked last time
- No accumulated expertise from previous tasks
- No internalized patterns or procedures
- Each session requires re-teaching context
  
  From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
  > "Agents today are a lot like Mahesh. They're brilliant, but they lack expertise. They can't really absorb your expertise super well, and they don't learn over time."
  
  This is **agent amnesia** — the computational equivalent of organizational knowledge loss when employees leave.
  
  ---
- ## Why This Matters
- ### Every Session Starts From Scratch
  Without persistent procedural memory:
- You repeat the same instructions every time
- The agent rediscovers patterns it found before
- Context curation becomes repetitive manual labor
- No compounding returns on supervision effort
  
  From [[Human-Agent Collaboration Framework]]:
  > "Missing organizational → every session starts from scratch"
- ### Expertise Doesn't Accumulate
  The "300 IQ genius vs. experienced professional" problem:
- Raw intelligence without domain knowledge = ineffective
- Brilliance alone can't replace accumulated expertise
- The agent has capability but lacks procedural wisdom
  
  This is why [[The Autonomy Slider]] stays stuck at low autonomy — without accumulated knowledge, you can't safely delegate more.
  
  ---
- ## Solution Requirements: What Properties Matter
  
  To solve agent amnesia, the memory system must have certain properties:
- ### 1. Persistence
- Survives session boundaries
- Durable across restarts, crashes, agent switches
- Not ephemeral (chat history fails this)
- ### 2. Structure
- Organized by type (factual, procedural, organizational)
- Retrievable when needed
- Not just undifferentiated accumulation
- ### 3. Editability
- Human can inspect and correct
- Agent can read and write
- Collaborative curation possible
- ### 4. Explicitness
  From [[The Filesystem as Agentic Ba]]:
  > "The filesystem doesn't support Nonaka's 'Socialization' phase — only externalized knowledge can enter."
  
  Tacit knowledge must become explicit to persist. This forces articulation.
- ### 5. Accumulation Over Replacement
  From [[Brevity Bias and Context Collapse]]:
- Iterative compression loses fidelity
- Better to accumulate and organize than compress and replace
- Structured incremental updates preserve detail
  
  ---
- ## Implementation Approaches
  
  Different systems address continuity with different trade-offs:
- ### Approach 1: Human-Curated Filesystem Knowledge
  
  **Examples**: Anthropic Skills, AGENTS.md, knowledge bases
  
  **Mechanism**:
- Filesystem provides persistent, structured space
- Humans externalize procedural knowledge into files
- Agent reads from curated context
  
  **Directory structure** (from [[The Filesystem as Agentic Ba]]):
  ```
  project/
  data/     → Factual context (what's true)
  memory/   → Organizational context (cross-session artifacts)
  task/     → Working context (current session)
  logs/     → Audit context (what happened)
  ```
  
  **Specific implementations**:
  
  **Anthropic Skills**:
  > "Organized collections of files that package composable procedural knowledge for agents. In other words, they're folders."
  
  **AGENTS.md**:
- Dos and don'ts (learned patterns)
- Commands (codified workflows)
- Safety rules (boundary conditions)
- Structure hints (organizational knowledge)
  
  **Strengths**:
- Human maintains full control and visibility
- Explicit, inspectable, editable
- Literal retrieval (no "black box" ranking)
- [[Manual context curation is the work]] — intentional selection
  
  **Weaknesses**:
- Requires manual curation effort
- No automatic relevance ranking
- Human must decide what to include each session
- Doesn't scale without discipline
- ### Approach 2: Agent-Managed Memory Systems
  
  **Examples**: mem-agent (Dria), MemGPT, agent-managed knowledge graphs
  
  **Mechanism**:
- Agent autonomously manages its own memory using tools
- Decides what to store, update, retrieve, and delete
- Uses structured formats (markdown files, links) or knowledge graphs
- Trained specifically to handle memory operations
  
  **Case Study: mem-agent** ([Dria, 2025](https://huggingface.co/blog/driaforall/mem-agent))
  
  Architecture:
- Obsidian-like markdown memory system (`user.md`, `entities/` directory)
- Agent has file operation tools (create, read, update, delete)
- Links between files in format `[[entities/entity_name.md]]`
- Agent trained with online RL to handle three subtasks:
	- **Retrieval**: Finding and filtering relevant information
	- **Updating**: Adding new information to memory
	- **Clarification**: Asking when information is missing/unclear
	  
	  Key insight: **The agent IS the curator**, not the human.
	  
	  **Strengths**:
- No manual curation required from human
- Agent learns memory management through training
- Structured, human-readable format (markdown + links)
- Agent can clarify when memory is insufficient
- Scales automatically with usage
  
  **Weaknesses**:
- Requires specialized model training (4B model trained with GSPO)
- Agent decides what's important (human loses direct editorial control)
- Retrieval quality depends on model capability
- Potential for agent errors in memory management
- Still developing (76.8% overall score on benchmark)
  
  Comparison table:
  
  | Approach | Curator | Structure | Transparency | Effort | Maturity |
  |----------|---------|-----------|--------------|--------|----------|
  | **Human-curated filesystem** | Human | Explicit (dirs, files) | High | Manual | Proven |
  | **Agent-managed memory** | Agent | Explicit (markdown, links) | Medium | None | Emerging |
  | **Semantic/vector DB** | Automatic | Implicit (embeddings) | Low | None | Proven |
  | **Hybrid** | Human + Agent | Both | Medium | Moderate | Experimental |
- ### Approach 3: Automatic Semantic Memory
  
  **Examples**: Vector databases with RAG, semantic memory systems
  
  **Mechanism**:
- System automatically captures interactions
- Builds embedding space for semantic search
- Retrieves "relevant" memories without explicit structure
  
  **Strengths**:
- Zero human effort
- Semantic relevance vs. literal matching
- Can surface unexpected connections
  
  **Weaknesses**:
- Opaque retrieval (black box ranking)
- No organization by knowledge type
- Human can't inspect or correct easily
- Retrieval quality unpredictable
- Risk of noise accumulation
- ### Approach 4: Hybrid Systems
  
  **Mechanism**:
- Curated filesystem structure for procedural knowledge
- Agent-managed or automatic memory for factual/conversational context
- Human decides what moves from automatic → curated
  
  **Example pattern**:
- Agent manages day-to-day memory (like mem-agent)
- Human reviews and promotes important patterns to AGENTS.md
- Filesystem for "known good" procedures, agent memory for exploratory context
  
  **Trade-off**: Complexity of maintaining both systems
  
  ---
- ## The Human-Supervised Approach in Detail
  
  Our framework emphasizes the first approach (human-curated filesystem) because it aligns with several core principles.
  
  ---
- ## The Mechanism: Supervised Knowledge Transfer
  
  When using human-curated filesystem approach, the progression from amnesia to autonomy follows this pattern:
- ### Phase 1: Manual Supervision
- Human does task, agent watches (or vice versa)
- Tacit knowledge lives only in human's head
- Agent has zero persistent memory
- High supervision burden
- ### Phase 2: Externalization Begins
- Human supervises agent doing task
- Patterns emerge through repetition
- Human captures patterns in persistent files (skills, AGENTS.md, knowledge base)
- [[Knowledge Externalization as Agentic Interface]] — interaction becomes documentation
- ### Phase 3: Procedural Memory Accumulates
- Persistent knowledge files grow with each task
- Agent references accumulated context
- Supervision shifts from "how to do this" to "is this correct"
- [[Supervision is context curation, not action approval]]
- ### Phase 4: Trust Enables Autonomy
- Sufficient procedural knowledge accumulated
- Agent performs reliably without step-by-step guidance
- [[The Autonomy Slider]] moves right
- Human monitors outcomes, not actions
- ### Phase 5: Knowledge Transfers
  From [[The Supervision Split]]:
  > "Another user inherits that autonomy (skills transfer)"
  
  The procedural memory becomes organizational asset:
- New team members inherit expertise
- Knowledge works across agents (not tied to one session)
- Organizational memory compounds
  
  ---
- ## The Payoff: Continuous Learning Over Time
  
  Regardless of implementation approach, solving continuity enables continuous learning.
  
  From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]], describing their Skills implementation:
- ### Day 1: Standardized Format
  > "Anything that cloud writes down can be used efficiently by a future version of itself."
  
  Externalization format (markdown, files, folders) enables knowledge transfer across sessions.
- ### Day 10: Tangible Memory
  > "Skills makes the concept of memory more tangible."
  
  Procedural knowledge accumulates. The agent becomes noticeably more effective.
- ### Day 30: Dynamic Evolution
  > "Cloud can acquire new capabilities instantly, evolve them as needed, and then drop the ones that become obsolete."
  
  The goal:
  > "Claude on day 30 of working with you is going to be a lot better than cloud on day one."
  
  **This is continuous learning** — not through model weights, but through **accumulated organizational memory**.
  
  The specific mechanism varies (curated files vs. automatic knowledge graphs), but the outcome is the same: agent effectiveness compounds over time.
  
  ---
- ## Why Human-Curated Approach Works
- ### Manual Curation Creates Quality
  From [[Manual context curation is the work]]:
- Automation tries to capture everything → noise accumulates
- Manual curation captures what matters → signal compounds
- Human judgment determines relevance
- No schema maintenance, no retrieval tuning
- ### The Filesystem Forces Intentionality
  From [[The Filesystem as Agentic Ba]]:
  > "The filesystem doesn't support Nonaka's 'Socialization' phase — only externalized knowledge can enter."
  
  This constraint is a feature:
- Forces articulation of tacit knowledge
- Creates audit trail of reasoning
- Enables handoff across sessions
- Makes context curation visible
  
  ---
- ## Case Study 1: mem-agent (Agent-Managed Memory)
  
  The mem-agent approach ([Dria, 2025](https://huggingface.co/blog/driaforall/mem-agent)) represents a fascinating middle ground: **structured, human-readable memory managed by the agent itself**.
- ### Key Design Decisions
  
  **Memory structure** (Obsidian-like markdown):
  ```
  memory/
  ├── user.md              # Main user information + relationship links
  └── entities/
      ├── entity_1.md      # Linked entities (employers, projects, etc.)
      └── entity_2.md
  ```
  
  **Agent capabilities** (file operation tools):
- `create_file()`, `read_file()`, `update_file()`, `delete_file()`
- `create_dir()`, `list_files()` (shows tree structure)
- `go_to_link()` (follows markdown links between files)
  
  **Trained behaviors**:
  1. **Retrieval with filtering** — Agent can selectively obfuscate information based on privacy rules
  2. **Memory updates** — Agent decides what to store and where
  3. **Clarification** — Agent asks when memory lacks needed information
- ### What This Solves
  
  From the article:
  > "LLMs today are stateless. Unless connected to external tools or specialized scaffolds, they cannot acquire new declarative or procedural knowledge without additional training."
  
  The solution: **Train the agent to be its own memory manager**.
  
  Example interaction:
- User: "I need my exact job title from my contract"
- Agent: Reads `user.md` → follows link to `entities/dria.md` → finds no job title
- Agent: "I don't have your job title in memory. What is it?"
- User: "AI Researcher"
- Agent: Updates `user.md` with `job_title: AI Researcher`
  
  The agent **autonomously manages continuity** without human curation.
- ### Alignment with Framework Principles
  
  **What it preserves from human-curated approach**:
- ✓ Persistence (filesystem survives sessions)
- ✓ Structure (organized by type: user info vs. entities)
- ✓ Human-readable (markdown, inspectable by humans)
- ✓ Editability (humans can manually edit memory files)
- ✓ Explicit links (Obsidian-style `[[links]]`)
  
  **What it changes**:
- ✗ Human no longer curates (agent decides what/where to store)
- ✗ Manual curation replaced by trained behavior
- ~ Agent asks for clarification (semi-supervised)
- ### Performance Reality
  
  From benchmark (57 hand-crafted tasks):
- **Overall score**: 76.8% (4-bit quantized model)
- **Retrieval**: 90.9%
- **Update**: 72.7%
- **Clarification**: 45.5%
- **Filtering**: 83.3%
  
  Notably, clarification (knowing what it doesn't know) is hardest — requiring implicit confidence assessment.
- ### The Trade-off
  
  **Gained**: Zero manual curation effort from human
  **Lost**: Human editorial control over what's remembered and how
  
  This inverts [[The Supervision Split]]:
- Human-curated: User supervises agent doing task → captures patterns
- Agent-managed: User provides information → agent supervises its own memory
  
  The question: **Can we trust the agent to curate its own memory as well as we curate it?**
  
  At 76.8% performance, mem-agent suggests "not quite yet, but promising."
  
  ---
- ## Case Study 2: Anthropic Skills Implementation
  
  Anthropic's Skills exemplify the human-curated filesystem approach with specific design choices:
  
  From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
- ### Design Principles
- **Simplicity**: "They're folders" — universal, no special tooling required
- **Progressive disclosure**: Show metadata only, load full content when needed
- **Filesystem-resident scripts**: Self-documenting, editable, zero context cost until used
- **Version control compatible**: Works with Git, Google Drive, zip files
- ### Skills vs. Traditional MCP Tools
  
  | Traditional MCP Tools | Skills (Filesystem-Resident) |
  |----------------------|------------------------------|
  | Poorly written instructions | Self-documenting code |
  | Agent can't modify when stuck | Agent can edit and evolve |
  | Always live in context window | Loaded only when needed |
  | Lost between sessions | Persist in workspace |
- ### The Key Insight
  Skills are **editable, persistent procedural memory**. MCP tools are ephemeral capabilities providing external connectivity.
  
  From the talk:
  > "MCP is providing the connection to the outside world while skills are providing the expertise."
  
  This division of labor: **MCP for connectivity, filesystem-resident skills for accumulated expertise**.
  
  ---
- ## Comparing Philosophies: Who Should Curate?
  
  The fundamental question: **Should humans or agents manage memory?**
- ### Human Curation (Skills/AGENTS.md approach)
  
  **Philosophy**: [[Manual context curation is the work]]
- Human judgment determines what's important
- Intentional selection over automatic accumulation
- High control, high effort
  
  **Best for**:
- Procedural knowledge (workflows, best practices)
- Mission-critical contexts (wrong = expensive)
- Organizational memory (team knowledge transfer)
  
  **Quote from Anthropic talk**:
  > "Fortune 100s using skills to teach agents about organizational best practices and the weird and unique ways they use bespoke internal software."
  
  The human encodes expertise. The agent executes.
- ### Agent Curation (mem-agent approach)
  
  **Philosophy**: Agent learns to manage its own memory
- Agent decides what to remember and where
- Trained behavior replaces manual curation
- Low control, low effort
  
  **Best for**:
- Personal context (user preferences, history)
- Conversational continuity (session handoffs)
- Factual information (names, dates, relationships)
  
  **From mem-agent article**:
  > "The model uses tools to interact with an external memory system... trained on retrieval, updating, and clarification."
  
  The agent becomes its own knowledge manager.
- ### The Trust Question
  
  From [[The Supervision Split]]:
- Human-supervised agents require **embedded trust** (you monitor them)
- Autonomous agents require **transferable trust** (others rely on them)
  
  Agent-managed memory adds a third dimension:
- **Self-supervised agents** require **trust in their curation judgment**
  
  At 76.8% benchmark performance, mem-agent is "good but not great" at this judgment.
  
  The question: Is 76.8% good enough for personal memory? Probably yes.
  Is it good enough for organizational procedural knowledge? Probably not yet.
  
  ---
- ## The Organizational Memory Vision
  
  From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
  > "A collecting and collective and evolving knowledge base of capabilities that's curated by people and agents inside of an organization."
  
  Benefits of accumulated procedural memory:
- **Team knowledge compounds**: "As you interact with an agent and give it feedback and more institutional knowledge, it starts to get better and all of the agents inside your team and your org get better as well."
- **Onboarding inheritance**: "When someone joins your team and starts using Claude for the first time, it already knows what your team cares about."
- **Community learning**: Skills built elsewhere make your agents better
  
  This is **organizational knowledge management** applied to human-agent collaboration.
  
  ---
- ## Non-Technical Knowledge Transfer
  
  A critical finding: memory systems work beyond developer workflows.
  
  From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
  > "We're seeing skills that are being built by people that aren't technical. These are people in functions like finance, recruiting, accounting, legal, and a lot more."
  
  The continuity problem affects all knowledge work:
- Tax preparation procedures (human-curated workflows)
- Legal document review patterns (human-curated precedents)
- Financial analysis workflows (human-curated procedures)
- Personal assistant contexts (agent-managed preferences)
  
  Different domains may benefit from different approaches:
- **High-stakes, procedural** → Human curation (Skills/AGENTS.md)
- **Personal, factual** → Agent management (mem-agent)
- **Exploratory, semantic** → Hybrid or automatic (vector DBs)
  
  ---
- ## Connection to Trust Models
  
  From [[The Supervision Split]]:
  
  **Embedded trust** (you supervise your own agent):
- Amnesia is tolerable with manual re-teaching
- But inefficient and doesn't scale
  
  **Transferable trust** (others use the agent):
- Requires persistent procedural memory
- Can't rely on original creator re-teaching every session
- Skills/AGENTS.md become essential infrastructure
  
  Solving continuity is what makes agents **transferable** beyond their original supervisor.
  
  ---
- ## Practical Implications
- ### For Individual Use
  1. Build skills/AGENTS.md incrementally as you work
  2. Capture patterns the second time you see them
  3. Expect Day 30 to be significantly better than Day 1
  4. [[Manual context curation is the work]] — this investment compounds
- ### For Teams
  1. Shared skills library = shared organizational memory
  2. Onboarding becomes inheriting procedural knowledge
  3. Domain experts encode their supervision as reusable autonomy
  4. Knowledge compounds across team members
- ### For Products
  1. Provide skill/AGENTS.md authoring tools
  2. Make supervision → externalization seamless
  3. Support progressive disclosure (minimize context cost)
  4. Enable version control and dependency management
  
  ---
- ## Why Simple "Memory" Features Fall Short
  
  Some products offer basic "memory" features. These often fail to solve continuity because they lack key properties:
  
  **Chat history**:
- ✗ Unstructured accumulation
- ✗ No organization by type (factual vs. procedural)
- ✗ Fills context window with noise
- ✗ Not editable or curate-able
  
  **Basic vector databases** (without structure):
- ✗ Semantic search is opaque
- ✗ Human can't easily inspect or correct
- ✗ Retrieval unpredictable
- ✗ No explicit procedural organization
  
  **What's needed** (at minimum):
- **Structured** organization (by knowledge type)
- **Editable** by both human and agent
- **Inspectable** by human supervisor
- **Persistent** across sessions
  
  Different implementations achieve these properties differently:
- Filesystem approach: explicit structure, manual curation
- Knowledge graph approach: automatic capture, semantic structure
- Hybrid: combine benefits of both
  
  ---
- ## Related
- [[The Filesystem as Agentic Ba]]
- [[Knowledge Externalization as Agentic Interface]]
- [[Manual context curation is the work]]
- [[The Autonomy Slider]]
- [[The Supervision Split]]
- [[Human-Agent Collaboration Framework]]