type:: [[Permanent Note]]
status:: Settled
date-created:: 2025-12-08
sources:: [[Literature - Governance for AI Agent Deployment (MLOps Community)]]

# Meeting Users Where They Are

**Agent capabilities should be accessible through interfaces users already understand, not force users to learn new interaction paradigms.**

---

## The Core Insight

**Quote from source**: "The most successful customers... building different UIs that try to meet that person where they are and what they're doing... you're taking the interface that you work in that makes sense and you're bringing the AI or the technology to it."

**The principle**: Design agent interactions around existing user workflows, not vice versa.

---

## The Spectrum of Integration

There are three main patterns, each appropriate for different contexts:

### 1. Native Tool Embedding (Autonomous Output)

**Pattern**: Agent output appears directly in tools users already use, with no visible AI interface.

**Example from source**: "An AI that just looks through your inbox and then puts a draft reply... in your drafts for each of the emails you have in your inbox. You didn't go to a chat... it's right there."

**Characteristics**:
- No chat interface
- Agent acts autonomously
- Output in native format (email draft, calendar event, form data)
- User interacts only with the output, not the agent

**When to use**:
- Simple, predictable tasks
- [[The Supervision Split]] → autonomous agent pattern
- User doesn't need to steer during execution
- Existing tool can display agent output natively

**Examples**:
- Email draft generation → drafts in email client
- Calendar scheduling → events in calendar
- Document summarization → summary as document comment
- Spreadsheet population → filled cells in existing spreadsheet

---

### 2. Dual Interface in Existing Tool (Collaborative)

**Pattern**: Add chat/steering interface to existing tool, enabling both direct manipulation and conversational commands.

**Example**: Form interface where:
- Agent can fill in form fields
- User can edit fields directly (traditional UI)
- User can also chat with agent: "Change the date to next Tuesday"
- Agent and user both work on same artifact

**Characteristics**:
- Existing UI remains usable
- Chat interface added alongside
- Both direct manipulation and conversation available
- Supports [[The Supervision Split]] → user-supervised pattern

**When to use**:
- Complex workflows requiring judgment
- User needs to steer agent during execution
- Existing tool is central to workflow
- Task benefits from both modes (quick edits + complex requests)

**Examples**:
- Form filling: Traditional fields + chat for "fill shipping same as billing"
- Document editing: Standard editor + chat for "make this section more formal"
- Data analysis: Spreadsheet UI + chat for "create pivot table for top customers"
- Design tools: Canvas manipulation + chat for "adjust all margins to brand standard"

---

### 3. Purpose-Built Agentic Workspace

**Pattern**: Create new integrated environment designed for artifact-based collaboration, when existing tools don't support the collaboration pattern.

**Example**: Cursor for code → Cursor-like workspace for research/legal/consulting work

**The insight**: This IS "meeting users where they are" when their mental model is file/document-based workflows.

**Research workflow example**:
```
workspace/
  sources/        ← Agent gathers PDFs, articles, case law
  notes/          ← Agent takes notes from sources
  datasets/       ← Agent prepares data files
  analysis/       ← Agent writes intermediate analyses
  drafts/         ← Agent composes draft sections
  final/          ← User assembles final deliverable
```

**Characteristics**:
- New interface, but maps to existing mental models (folders, documents)
- Chat + file browser + document viewer integrated
- Hierarchical navigation matches how user thinks about work
- Supports sophisticated collaboration ([[Agentic UX — The Dual Interface Requirement]])

**When to use**:
- Existing tools don't support dual editability
- Work naturally maps to hierarchical file structure
- Multiple artifact types (docs, spreadsheets, images, PDFs)
- Complex workflows requiring high supervision
- [[The Supervision Split]] → user-supervised with gradual autonomy

**Examples**:
- Research analysis: Sources → notes → analysis → report
- Legal case work: Briefs → discovery → memos → filings
- Consulting projects: Data → models → slides → recommendations
- Content production: Research → outlines → drafts → published pieces

**Extension needs**: Beyond code, these workspaces need:
- PDF viewers (for reading sources)
- Spreadsheet viewers (for data inspection)
- Image/diagram display (for visual artifacts)
- Cross-reference navigation (links between documents)

---

## The Unifying Principle: [[Integrated Environment Principle]]

All three patterns aim to reduce context switching:

| Pattern | Integration Approach | Context Switch Count |
|---------|---------------------|---------------------|
| **Native embedding** | Agent output in existing tool | Zero (already there) |
| **Dual interface** | Chat added to existing tool | Zero (one window) |
| **Agentic workspace** | Purpose-built integrated environment | Zero (everything visible) |

**The goal**: User never has to "go somewhere else" to interact with agent or see results.

---

## Beyond Text: Modality Considerations

"Meeting users where they are" also means matching output and input modalities to the task.

### Output Modality

**Don't force everything to text**. Present agent output in native formats:

- Code → Syntax-highlighted diffs, not prose descriptions
- Data analysis → Charts and tables, not textual summaries
- Design → Visual mockups, not written specifications  
- Planning → Gantt charts or dependency graphs, not bullet lists
- Comparison → Side-by-side views, not "A differs from B in these ways..."

**The insight**: Text is the agent's native language, but not always the user's best consumption format.

### Input Modality

**Don't force everything through chat**. Provide quick actions for high-frequency operations:

- Accept/reject diffs → Button, not "please apply these changes"
- Apply context bundle → Button: "Use these 5 files"
- Adjust autonomy → Slider, not "be more careful"
- Enable/disable capabilities → Checkboxes: "Can email externally? Can delete files?"
- Mode switching → Toggle: "Search and answer" vs "Just search"

**The insight**: Language is the programming interface, but high-frequency operations benefit from direct manipulation.

**Quote from source** (discussing the desire for more controls): "In Lightroom... you have a histogram and you can bring up certain colors... you have much more controllability. But with agents, we just have chat."

---

## Implementation Patterns

### For Existing Tools

**Can the tool be extended?**
- Yes, and it's core to workflow → Add dual interface (Pattern 2)
- Yes, but task is simple → Embed outputs only (Pattern 1)
- No, or tool is inadequate → Build workspace (Pattern 3)

**Questions to ask**:
- Does the tool support programmatic access? (API, extensions)
- Can we add UI elements? (Plugins, embedded views)
- Can agent outputs be represented in tool's native format?
- Does the tool support the collaboration properties we need?

### For New Workflows

**Map the work structure**:
- Linear, single-artifact → Pattern 1 or 2 might work
- Hierarchical, multi-artifact → Pattern 3 likely needed
- Cross-system → Consider [[Integrated Environment Principle]] for supervision layer

**Questions to ask**:
- What artifacts does this work produce?
- How does user currently organize them?
- What tools do they use today?
- Can those tools support agent collaboration?

---

## Connection to Browser/Tool Automation

**The insight**: MCP servers and browser automation extend "meeting users where they are" to existing systems.

- Agent can act in Salesforce (via MCP) → user doesn't leave CRM
- Agent can navigate websites (via browser tools) → handles GUIs built for humans
- Agent can update Jira (via API) → changes appear in issue tracker

**The supervision question**: Where does user supervise these actions?

**Option A**: User supervises in the target system
- Good for simple tasks
- Example: Approve the email draft that agent wrote

**Option B**: User supervises in agentic workspace, agent reaches into systems
- Good for complex multi-system workflows
- Agent shows plans/logs in workspace
- User reviews before agent executes
- Maintains [[Integrated Environment Principle]] while acting across systems

---

## Design Principles Summary

1. **Minimize context switching** - Goal is zero switches to see results
2. **Match mental models** - Structure reflects how user thinks about work
3. **Native formats** - Output in format user already understands
4. **Dual modality** - Text for complex requests, buttons for frequent actions
5. **Progressive disclosure** - Simple tasks simple, complex tasks possible
6. **Consistent location** - User knows where to look for outputs

---

## Relation to Framework

### Validates
- [[The human works through the agent's hands]] - Agent acts in user's workspace
- [[Middle artifacts as collaboration checkpoints]] - Visible in native tools

### Implements
- [[Integrated Environment Principle]] - All patterns aim for this
- [[Agentic UX — The Dual Interface Requirement]] - Pattern 2 and 3 provide this

### Extends
- [[The Filesystem as Agentic Ba]] - Pattern 3 shows filesystem works beyond code
- [[The Supervision Split]] - Different patterns map to autonomous vs collaborative

---

## Open Questions

1. How do you provide [[The Autonomy Slider]] controls when agent is embedded in third-party tool?
2. For multi-system workflows, is supervision workspace always better than supervising in each system?
3. Can Pattern 1 (autonomous embedding) ever evolve to support Pattern 2 (dual interface), or are they architecturally different?
4. What viewer/editor capabilities does an agentic workspace need for different professions? (legal, consulting, research, finance)

---

## Related
- [[Integrated Environment Principle]]
- [[Agentic UX]]
- [[Agentic UX — The Dual Interface Requirement]]
- [[The Supervision Split]]
- [[The human works through the agent's hands]]
- [[Tight feedback loops through artifact visibility]]



