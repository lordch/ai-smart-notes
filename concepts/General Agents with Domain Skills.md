type:: [[Permanent Note]]
status:: Working
date-created:: 2025-12-08
sources:: [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]

# General Agents with Domain Skills

**The agent ecosystem is converging on general-purpose agents with domain-specific skills rather than specialized agents for each use case.**

---

## The Architectural Shift

### Old Paradigm: Specialized Agents
- Different agent for each domain/use case
- Each with custom tools, scaffolding, workflows
- Separate development and maintenance per domain
- Expertise baked into agent implementation

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:
> "We used to think agents in different domains will look very different. Each one will need its own tools and scaffolding and that means we'll have a separate agent for each use case for each domain."

### New Paradigm: General Agent + Skills
- **One general-purpose agent** (thin scaffolding)
- **Domain expertise externalized** into skills/context
- Same agent, different skill libraries
- Expertise separate from execution capability

From the talk:
> "The agent underneath is actually more universal than we thought. What we realized is that code is not just a use case but the universal interface to the digital world."

---

## Why This Convergence Happened

### 1. Code as Universal Interface

Agents with code execution can handle diverse domains:
- Financial reporting: API calls → filesystem organization → Python analysis → document synthesis
- Scientific research: Data retrieval → bioinformatics libraries → statistical analysis → paper writing
- Web automation: Browser control → form filling → data extraction → result formatting

All through **code**.

From the talk:
> "The core scaffolding can suddenly become as thin as just bash and file system which is great and really scalable."

### 2. The Bottleneck Shifted

The problem isn't agent capability, it's **domain expertise**:

> "Agents today are a lot like Mahesh. They're brilliant, but they lack expertise. They can do no more slow. They can do amazing things when you really put in the effort and give proper guidance, but they're often missing the important context up front."

The "300 IQ genius vs. experienced professional" problem:
> "Who do you want doing your taxes? Is it going to be Mahesh, the 300 IQ mathematical genius, or is it Barry, an experienced tax professional? I would pick Barry every time."

**Intelligence is commoditizing. Expertise is the constraint.**

### 3. Externalized Knowledge Scales Better

Building a new specialized agent for each domain:
- ✗ Requires developer with domain expertise
- ✗ Rebuilds scaffolding each time
- ✗ Expertise trapped in implementation
- ✗ Hard to share or transfer

Building skills for general agent:
- ✓ Domain expert can create (even if non-technical)
- ✓ Reuses proven scaffolding
- ✓ Expertise portable across agents
- ✓ Easy to version, share, distribute

From [[Knowledge Externalization as Agentic Interface]]:
> "Interaction with an agent is the process of converting tacit knowledge (intuition) into explicit knowledge (system context)."

Skills formalize this externalization.

---

## The Converged Architecture

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:

```
┌─────────────────────────────────┐
│      Agent Loop                 │  ← Token management, context control
├─────────────────────────────────┤
│  Runtime Environment            │  ← Filesystem + code execution
├─────────────────────────────────┤
│  MCP Servers                    │  ← External tools & data (connectivity)
├─────────────────────────────────┤
│  Skill Library (100s-1000s)     │  ← Domain expertise (progressively loaded)
└─────────────────────────────────┘
```

**The key insight**: "Giving an agent a new capability in a new domain might just involve equipping it with the right set of MCP servers and the right library of skills."

---

## Domain Specialization Through Context

Different domains = different skill libraries equipped:

### Financial Services
- MCP servers: Market data APIs, portfolio management systems
- Skills: Financial modeling procedures, regulatory compliance workflows, reporting standards

### Life Sciences
- MCP servers: EHR systems, research databases, lab equipment interfaces
- Skills: EHR data analysis procedures, bioinformatics library usage, experimental protocols

### Legal
- MCP servers: Case law databases, document management systems
- Skills: Document review patterns, precedent analysis workflows, contract drafting standards

### Software Development
- MCP servers: GitHub, issue trackers, CI/CD systems
- Skills: Code style guides, testing procedures, deployment workflows

**Same agent runtime, different knowledge base.**

---

## Division of Labor: MCP vs. Skills

From the talk:
> "MCP is providing the connection to the outside world while skills are providing the expertise."

| Layer | Purpose | Example |
|-------|---------|---------|
| **MCP Servers** | External connectivity | Connect to Notion API |
| **Skills** | How to use connections | How to do deep research across Notion workspace |

| Layer | Purpose | Example |
|-------|---------|---------|
| **MCP Servers** | External connectivity | Browser automation (Stagehand) |
| **Skills** | How to use connections | Navigate web effectively to get work done |

MCP provides **capabilities**. Skills provide **procedures**.

This aligns with [[The Filesystem as Agentic Ba]]:
- MCP = tools for accessing external world
- Skills = procedural knowledge in shared workspace
- Both needed, different purposes

---

## Connection to Framework Principles

### Validates: Separation of Concerns

**[[The human works through the agent's hands]]**:
- Agent = execution capability (universal)
- Human = domain expertise (specific)
- Skills = the transfer mechanism

The human doesn't need different agents for different tasks. The human needs to externalize different expertise.

### Validates: Context Over Capability

**[[Supervision is context curation, not action approval]]**:
- Agent capability is mostly sufficient (general-purpose)
- The work is curating domain context (skills)
- Supervision = ensuring right skills are applied

### Validates: Infrastructure That Compounds

**From [[Human-Agent Collaboration Framework]]**:
> "Not one-shot solutions: Infrastructure that compounds over time"

A skill library is compounding infrastructure:
- Each skill adds capability
- Skills compose (orchestrate multiple tools)
- Team skills compound organizational knowledge
- New employees inherit expertise

---

## Implications for Product Development

### If Building Agent Products

**Don't**: Build separate specialized agent for each vertical
**Do**: Build general agent + vertical skill libraries

From Anthropic example:
> "Just after we launched skills 5 weeks ago, we immediately launched new offerings in financial services and life sciences. And each of these came with a set of MCP servers and a set of skills."

Launch velocity increases when you can reuse agent infrastructure.

### If Building Skills/Tools

**Don't**: Try to build "one tool that does everything"
**Do**: Build composable tools (MCP) + procedural guidance (skills)

From the talk:
> "Developers are using and building skills that orchestrate workflows of multiple MCP tools stitched together to do more complex things."

Skills can orchestrate. This means tools can be simpler and more focused.

### If Building for Enterprises

**Don't**: Sell "AI solution for your industry"
**Do**: Enable domain experts to build skills for general agent

From the talk:
> "We're seeing skills that are being built by people that aren't technical. These are people in functions like finance, recruiting, accounting, legal, and a lot more."

The person who knows the domain should build the expertise layer.

---

## The Computing History Parallel

From [[Literature - Agent Skills Over Agents (Zhang & Murag, Anthropic)]]:

| Layer | Computing Analogy | AI Analogy |
|-------|-------------------|------------|
| Hardware | Processors | Models (immense potential, massive investment) |
| OS | Operating Systems | Agent runtimes (orchestration, resource management) |
| Applications | Software | Skills (where millions encode domain expertise) |

The value proposition:
> "A few companies build processors and operating systems, but millions of developers like us have built software that encoded domain expertise and our unique points of view. We hope that skills can help us open up this layer for everyone."

**Universal substrate (processor/OS) + domain-specific applications (software/skills).**

This is the pattern that scaled computing. It's likely the pattern that will scale AI agents.

---

## Why Specialized Agents Still Exist

This note isn't arguing specialized agents disappear. They remain useful for:

### 1. Deeply Integrated Workflows
- Domain logic is the agent (not just context)
- Example: AlphaFold (protein folding agent)

### 2. Proprietary Advantage
- Expertise IS the moat
- Don't want to make it portable
- Example: Trading algorithms

### 3. Constrained Environments
- Can't allow general code execution
- Need safety guarantees
- Example: Customer service chatbots

But for **knowledge work collaboration** (the focus of this framework), the general agent + skills pattern is winning.

---

## Open Questions

### Where's the Boundary?

When does domain logic belong in:
- The agent itself (specialized agent)
- Skills/procedural knowledge (general agent + context)
- Both (hybrid approach)

**Hypothesis**: If domain expert can articulate the procedure, it can be a skill. If it requires novel algorithms or deep integration, it's a specialized agent.

### How General is "General"?

Are there limits to the general agent paradigm?
- Do some domains need specialized reasoning?
- Are there cognitive architectures better suited to specific tasks?
- Or is "thin agent loop + filesystem + code execution" truly universal?

**Early evidence**: Anthropic successfully deployed to financial services and life sciences with same base agent.

### Skills vs. Fine-Tuning?

When should domain expertise be:
- Externalized (skills, context)
- Internalized (fine-tuning, weights)

**Current trend**: Externalization winning for procedural knowledge because:
- Updates are instant (no retraining)
- Human-editable and inspectable
- Transferable across agents
- Cost-effective for rapidly changing domains

But internalization may still win for:
- Deeply embodied skills (language-specific fluency)
- Performance-critical operations (latency matters)
- Stable knowledge (rarely changes)

---

## Related

- [[Knowledge Externalization as Agentic Interface]]
- [[The Filesystem as Agentic Ba]]
- [[Agent Amnesia and the Continuity Problem]]
- [[Manual context curation is the work]]
- [[The Supervision Split]]
- [[In-Context Skill Development]]
- [[Human-Agent Collaboration Framework]]




