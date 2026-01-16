type:: [[Permanent Note]]
status:: Working
date-created:: 2025-12-08
sources:: [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]], [[The Supervision Split]], [[Agentic UX — The Dual Interface Requirement]]

# In-Context Skill Development

**When skills are editable in the same interface where work happens, domain experts can build agent capabilities directly during task execution, not as separate meta-activity. This is long-term in-context learning — the agent learns procedures through supervised work, with knowledge captured immediately in the working context.**

---

## The Core Insight

Skills/AGENTS.md don't need to be authored by developers in advance. They can **emerge from supervised work** when the environment supports dual editability.

The key properties:
- **Skills are human-readable** (domain expert can understand them)
- **Skills are editable by both** human and agent (in shared workspace)
- **Skills live in working context** (same interface, no tool switch)
- **Scripts created during work** can be immediately captured as reusable tools

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
> "We kept seeing Claude write the same Python script over and over again to apply styling to slides. So we just asked cloud to save it inside of the skill as a tool for his version for his future self."

The script was built "in the meantime" — during work — and immediately became reusable.

---

## Why This Matters

### It Changes Who Can Build Agent Capabilities

From [[The Supervision Split]]:
> "The user who supervises daily IS the person who should encode the skills, not a separate developer."

But this only works if skill creation happens **during supervision**, not as separate authoring task.

**Old model**:
1. Developer builds agent capability
2. User tries to use it
3. User reports issues
4. Developer fixes capability
5. Repeat

**New model**:
1. User supervises agent on task
2. User notices pattern (agent does X wrong repeatedly)
3. User edits AGENTS.md directly in working context
4. Agent immediately follows new rule
5. User continues work

The domain expert becomes the capability builder **while doing their actual work**.

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
> "We're seeing skills that are being built by people that aren't technical. These are people in functions like finance, recruiting, accounting, legal, and a lot more."

This is only possible because skills are:
- Human-readable (markdown, not code)
- Editable in context (no separate IDE or authoring tool)
- Immediately effective (agent reads updated context)

---

## The Mechanism: Dual Editability During Work

From [[Agentic UX — The Dual Interface Requirement]]:

The dual interface must provide:
- **Agent can make changes** — write files, create scripts, produce artifacts
- **Human quickly sees changes** — diffs visible, navigation easy
- **Human can make changes too** — same surface, editable by both

This enables the **in-context skill development loop**:

### Phase 1: Work With Supervision
- User: "Analyze this dataset and create visualizations"
- Agent: Writes analysis script, generates charts
- User: Reviews output (visible immediately, same interface)

### Phase 2: Notice Pattern
- User observes: Agent's charts always use default colors (not brand colors)
- Pattern emerges through repetition across multiple tasks
- User decides: This should be standard procedure

### Phase 3: Capture Pattern (No Context Switch)
- User opens AGENTS.md in same workspace
- User adds: "Always use brand colors: primary #2E5C8A, accent #F2A900"
- Or agent adds script to skills/ folder with color definitions
- **No switching to separate tool, no "authoring mode"**

### Phase 4: Immediate Effect
- User: "Create another visualization"
- Agent: Reads updated AGENTS.md, applies brand colors
- User: Continues work with improved capability

### Phase 5: Refinement
- User notices: Colors work but contrast insufficient for certain chart types
- User edits AGENTS.md again: "For line charts, use darker variants..."
- Pattern iteratively refined **during ongoing work**

This is [[Knowledge Externalization as Agentic Interface]] happening in real-time:
> "By guiding the agent, the user is forced to articulate: Context (what matters here?), Procedure (how do we do this?), Standard (what does 'good' look like?)"

The articulation happens **in the flow of work**, captured immediately in editable files.

---

## Scripts as Captured Expertise

A powerful variant: **procedural knowledge as executable code**.

### The Pattern

1. **Agent builds script during task**
   - User: "Generate monthly report"
   - Agent: Writes Python script to fetch data, format tables, calculate metrics
   
2. **Script works well**
   - User reviews output, it's correct
   - User notices: This same script will be needed every month

3. **Immediately capture as reusable tool**
   - Agent/user saves script to `skills/monthly_report.py`
   - Agent/user adds entry to skill.md: "For monthly reports, use monthly_report.py"
   - **Done in same interface, same session**

4. **Next time**
   - User: "Generate monthly report"
   - Agent: Reads skill, finds existing script, runs it
   - Consistency + efficiency from captured expertise

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:

Scripts as tools have key advantages:
- **Self-documenting** (code explains itself)
- **Modifiable** (agent can edit when requirements change)
- **Filesystem-resident** (zero context cost until needed)
- **Built during work** (not pre-authored)

This is why [[General Agents with Domain Skills]] emphasizes:
> "Code is not just a use case but the universal interface to the digital world."

The domain expert doesn't write the script. The agent does. But the domain expert recognizes it's reusable and promotes it to skill — **directly in the working context**.

---

## Connection to Supervision Progression

From [[The Supervision Split]], the progression model:

**Phase 1: High Supervision**
- User watches every action
- Frequent intervention
- **Work happens here**: User sees what agent does wrong

**Phase 2: Checkpoint Supervision**
- User reviews intermediate artifacts
- **Skill development happens here**: Patterns captured in AGENTS.md/skills
- Agent autonomy increases between checkpoints

**Phase 3: Outcome Supervision**
- User reviews final results
- Agent handles full workflow using accumulated skills

**Key insight**: Phase 1 → Phase 2 transition happens **during work** when skills are editable in context.

Without dual editability in working context:
- User must stop work, switch to authoring tool, document pattern, return to work
- Friction prevents skill capture
- Patterns remain tacit, agent never learns

With dual editability in working context:
- User edits AGENTS.md in same window (keyboard shortcut, no context switch)
- Minimal friction enables immediate capture
- Patterns become explicit immediately, agent improves instantly

This is why [[Manual context curation is the work]]:
> "After each task: Update knowledge base with what you learned"

But "after" doesn't mean "in separate session later." It can mean "during, immediately, in flow."

---

## The Double-Loop Learning Connection

From [[Knowledge Externalization as Agentic Interface]]:

**Single-Loop Learning**: Solving the immediate problem (fix this chart)
**Double-Loop Learning**: Solving the problem AND updating the rules/system (fix this chart + add rule about brand colors)

Double-loop learning has traditionally been **deferred**:
- Do work (single-loop)
- Later, reflect on what was learned
- Update documentation/procedures (double-loop)
- Resume work

With in-context skill development, double-loop learning is **immediate**:
- Do work (single-loop)
- Notice pattern worth capturing
- Edit AGENTS.md right now (double-loop, same session)
- Continue work with improved system

The "distraction" of teaching the agent becomes **part of the workflow**, not interruption to it.

From [[Knowledge Externalization as Agentic Interface]]:
> "The work compounds: each session of context curation enables more delegation next time."

When skill capture happens in-context, the compounding happens **within the session**, not just across sessions.

---

## Why Filesystem-Based Skills Enable This

From [[The Filesystem as Agentic Ba]]:

The filesystem has properties that make in-context skill development possible:

| Property | Why It Enables In-Context Development |
|----------|--------------------------------------|
| **Editable by both** | Human can edit AGENTS.md, agent can edit scripts, same files |
| **Inspectable** | Human can see what agent created (scripts, tools) immediately |
| **Diffable** | Human can review changes to skills before accepting |
| **Interoperable** | Skills work with any tool (Cursor, VS Code, text editor) |
| **No schema** | Just files — add/edit without database migrations |
| **Persistent** | Changes take effect immediately, survive sessions |

Compare to alternative approaches:

**Vector DB memory**:
- ✗ Not human-editable (embedding space)
- ✗ Not inspectable (can't see why agent "remembers" something)
- ✗ Can't directly edit during work

**Separate skill authoring tool**:
- ✗ Requires context switch (leave work, open authoring UI)
- ✗ High friction discourages capture
- ✗ Authoring feels like meta-work, not work

**Filesystem in dual-editable interface**:
- ✓ Human-readable markdown
- ✓ Editable in same window as work (Cmd+P, open AGENTS.md)
- ✓ Immediate effect (agent reads updated context)
- ✓ Feels like part of work, not meta-work

This is why [[Integrated Environment Principle]] matters:
> "Effective human-agent collaboration requires an integrated environment where both parties can perceive and act on shared artifacts without context switching."

Skills ARE shared artifacts. When they're in the integrated environment, they develop naturally during work.

---

## The Anthropic Skills Design Validates This

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:

Anthropic's design choices specifically enable in-context development:

### 1. "They're Just Folders"
> "This simplicity is deliberate. We want something that anyone human or agent can create and use as long as they have a computer."

No special tooling = can edit during work in any environment.

### 2. Human-Readable Format
> "Skills are organized collections of files that package composable procedural knowledge"

Markdown + scripts = domain expert can read and edit without programming.

### 3. Progressive Disclosure
> "At runtime, only this metadata is shown to the model... When an agent needs to use a skill, it can read in the rest"

Low context cost = can have many skills available = encourages creating more = lowers barrier to in-context capture.

### 4. Agent Can Create Skills
> "Claude can already create skills for you today using our skill creator skill"

This is the key enabler:
- User: "Save that script as a reusable tool"
- Agent: Creates skill structure, adds script, updates manifest
- User: Reviews and edits if needed
- **All in working context**

From the talk:
> "Anything that cloud writes down can be used efficiently by a future version of itself."

This standardization enables:
- Agent creates draft skill during work
- Human reviews/edits in same interface
- Immediately becomes organizational memory

---

## Contrast: When Skills Must Be Pre-Authored

Some approaches require skills to be built before work begins:

### Developer-Supervised Autonomous Agents (from [[The Supervision Split]])
- Developer builds capabilities pre-deployment
- User uses finished agent
- Changes require developer intervention
- **Skill development happens outside work context**

This works for:
- Simple, repetitive tasks (email drafts)
- Well-defined procedures (known in advance)
- Autonomous deployment (no supervision)

This fails for:
- Exploratory work (procedures emerge during task)
- Complex domains (too many edge cases to pre-specify)
- Rapidly changing contexts (procedures become outdated)

### User-Supervised Collaborative Agents
- User supervises during work
- Procedures emerge through observation
- **Skills develop in context of work**

This is enabled by:
- [[Agentic UX — The Dual Interface Requirement]]
- [[The Filesystem as Agentic Ba]]
- [[Integrated Environment Principle]]

When these are present, the domain expert can build capabilities **while working**, not before or after.

---

## The Trust Progression Connection

From [[Agent Amnesia and the Continuity Problem]]:

The progression from amnesia to autonomy requires accumulated procedural memory. When skills develop in context:

**Day 1**: No skills, high supervision
- User does most thinking
- Agent executes under close guidance
- Every task requires full instructions

**Day 10**: Skills accumulating during work
- User notices: "Agent keeps doing X wrong"
- User edits AGENTS.md immediately: "Always do X this way"
- Skills = captured supervision patterns
- **This happens during tasks, not between them**

**Day 30**: Substantial skill library
- Most common patterns captured
- Agent handles workflows more autonomously
- User supervises at higher level
- New skills still added during work as new patterns emerge

The key: **Skills accumulate during work because editing happens in working context.**

Without in-context editability:
- Day 30 looks like Day 1 (nothing captured)
- Or: Skills lag reality (captured later, become outdated)

With in-context editability:
- Day 30 shows genuine improvement
- Skills stay current (edited when reality changes)

This is [[The Autonomy Slider]] moving right in practice:
> "As knowledge base improves, autonomy can safely increase."

The knowledge base improves **during work** when skills are editable in context.

---

## Implementation Requirements

For skills to develop in context of work, the environment must provide:

### 1. Spatial Proximity
From [[Integrated Environment Principle]]:
- Agent output and AGENTS.md visible in same window
- Quick navigation (Cmd+P to open AGENTS.md)
- No context switching to separate authoring tool

### 2. Dual Editability
From [[Agentic UX — The Dual Interface Requirement]]:
- Human can edit AGENTS.md directly
- Agent can create/modify skills with permission
- Same files, both parties can write

### 3. Immediate Effect
- Agent reads updated AGENTS.md on next action
- No deploy step, no reload required
- Changes take effect in current session

### 4. Low Friction
- Markdown (easy to edit)
- No schema to maintain
- No validation required (unless you want it)
- Just files in filesystem

### 5. Visibility
- File tree shows skills/ folder
- Diffs show what changed
- Human can review before accepting

---

## Current Implementation Landscape

### ✓ Supports In-Context Skill Development

**Cursor + AGENTS.md**:
- File tree visible alongside chat
- Cmd+P quick open to AGENTS.md
- Agent can edit, human can edit, same files
- Diffs show changes
- **This is why it works well for agentic workflows**

**Claude Projects (with filesystem access)**:
- Agent can create/edit files
- User can review in file view
- Skills can be markdown files in project
- Works, but less integrated than Cursor

### ✗ Does Not Support In-Context Development

**Claude Desktop (artifacts)**:
- Artifacts are read-only to human
- No way to edit agent's outputs directly
- Can't create persistent skills in shared space
- **Breaks dual editability**

**ChatGPT (GPTs with actions)**:
- Skills must be pre-configured by developer
- User can't edit capabilities
- No shared filesystem
- **Requires pre-authoring**

**Traditional RPA tools**:
- Workflows built in separate authoring UI
- Not editable during execution
- Developer creates, user consumes
- **No in-context development**

---

## Open Questions

### How Much Guidance Should Agents Need?

When creating skills in-context:
- User: "Save that as a skill" (high-level instruction)
- Agent: Determines structure, naming, organization
- User: Reviews and edits result

**Question**: How much skill creation can agents handle autonomously?

Current state (from mem-agent research in [[Agent Amnesia and the Continuity Problem]]):
- 76.8% overall performance on memory management
- Clarification (knowing what to ask) hardest at 45.5%

This suggests: **Agents can draft skills, humans should review** — which is exactly what dual editability enables.

### What Belongs in Skills vs. What Doesn't?

Not every script belongs in skills/. Not every pattern needs AGENTS.md entry.

**Hypothesis**: If you do it twice and expect to do it again → capture it.

But this is judgment that emerges during work. The domain expert decides in context:
- "This is one-off" → Don't capture
- "This will repeat" → Save to skills/
- "This is team-wide" → Add to AGENTS.md

In-context editability lets this judgment happen naturally.

### Does This Scale to Teams?

When multiple people work with same agent + same skill library:

**Benefits**:
- Everyone's improvements benefit everyone
- New team members inherit accumulated knowledge
- Skills become organizational memory

**Challenges**:
- Who can edit what? (permissions)
- How to review changes? (git-like approval)
- What if skills conflict? (organization/namespacing)

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
> "When someone joins your team and starts using Claude for the first time, it already knows what your team cares about."

This vision requires skills developed by entire team, not just one person. In-context development by each team member → shared skill library.

**Open question**: What's the right collaboration model for shared skill editing?

---

## Related

- [[Agentic UX — The Dual Interface Requirement]] — The interface requirement that enables this
- [[The Supervision Split]] — Domain experts should encode skills, not developers
- [[Integrated Environment Principle]] — No context switching enables in-context development
- [[The Filesystem as Agentic Ba]] — Why filesystem specifically enables editability
- [[Knowledge Externalization as Agentic Interface]] — Double-loop learning in real-time
- [[General Agents with Domain Skills]] — Non-technical users building skills
- [[Agent Amnesia and the Continuity Problem]] — Skills as solution, built during work
- [[Manual context curation is the work]] — Curation happens during work, not after
- [[The Autonomy Slider]] — Skills accumulate → autonomy increases

