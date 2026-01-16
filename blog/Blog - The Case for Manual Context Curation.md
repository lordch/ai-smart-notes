type:: [[Blog Draft]]
status:: Draft
date-created:: 2025-01-12
sources:: [[Human-Agent Collaboration Framework]], [[Manual context curation is the work]], [[The Filesystem as Agentic Ba]], [[Middle artifacts as collaboration checkpoints]], [[Supervision is context curation, not action approval]], [[Brevity Bias and Context Collapse]]

# The Case for Manual Context Curation

*A framework for human-AI collaboration that keeps creation in human hands*

---

## The automation model and its limits

"2025 is the year of agents." That was the narrative. Autonomous systems that research, plan, execute. Orchestration frameworks coordinating fleets of AI workers. Memory systems that manage themselves. The human would step back — maybe check in occasionally, approve some outputs — while the agents handle the actual work.

The enterprise ROI reports came back disappointing. The elaborate autonomous frameworks underperformed. Workflows that were supposed to run themselves failed in unpredictable ways.

Meanwhile, a different pattern was emerging among practitioners actually shipping work. They weren't trying to maximize autonomy. They were staying close to the work — more hands-on, not less. And they were getting extraordinary results.

The automation model treats human involvement as overhead — friction on the path to full autonomy. But what if that framing is wrong? What if the human in the loop isn't a bottleneck to remove, but the reason it works?

---

## The reframe: Supervision is context curation, not action approval

The standard mental model of human-AI supervision looks like this:

> Agent proposes action → Human approves or rejects → Agent executes

This frames the human as a gatekeeper. You're clicking "yes" or "no" on things the AI wants to do. It's reactive. It's tedious. And naturally, you'd want to automate it away.

But this isn't what effective practitioners actually do.

**The high-leverage work isn't clicking "approve" — it's shaping what the agent sees before it acts.**

When you curate context — deciding which files to include, what background to provide, which constraints matter, what "good" looks like — you're not supervising *outputs*. You're shaping *inputs*. By the time the agent proposes something, the context has already constrained it toward useful proposals.

This is the reframe: **Supervision is context curation.**

The Boundaryml team quantifies this with a leverage hierarchy:

- Core prompts/setup wrong → 100,000 bad lines of code
- Research phase wrong → 1,000 bad lines
- Implementation plan wrong → 10-100 bad lines  
- Individual code line wrong → 1 bad line

Human attention should be proportional to leverage. Review the research closely. Review the plan. The individual outputs? Less scrutiny if the upstream context was curated well.

The bottleneck isn't the final action. It's the context that shaped it.

---

## The filesystem as collaboration space

If context curation is the work, where does that curation happen?

The answer, for practitioners who've figured this out, is surprisingly mundane: **the filesystem.**

Not a special-purpose memory system. Not a vector database. Not an elaborate agent framework. Just... folders and markdown files.

This seems almost embarrassingly low-tech. But there's a reason it works, and the reason is theoretically interesting.

Ikujiro Nonaka, the knowledge management theorist, introduced the concept of "ba" (場) — a shared space where knowledge creation happens. Ba can be physical (a meeting room), virtual (a digital platform), or mental (shared experiences). The key insight: knowledge doesn't just transfer between people, it gets *created* in shared spaces.

**The filesystem is ba for human-agent collaboration.**

Think about what the filesystem offers:

| Property | Why it matters |
|----------|----------------|
| **Persistent** | Survives session boundaries, agent amnesia |
| **Navigable** | Hierarchical structure maps to cognitive categories |
| **Editable by both** | Human and agent read/write the same artifacts |
| **Inspectable** | You can see everything the agent sees |
| **Transparent** | No hidden state, no black boxes |

Unlike a vector database where you can't see what the agent retrieved, the filesystem is *legible*. Unlike chat history that fills the context window with noise, the filesystem is *organized*. Unlike special-purpose memory systems, the filesystem is *universal* — it works with any tool, any framework, any agent.

But here's the deeper insight: **the filesystem requires externalization.**

In human-to-human collaboration, tacit knowledge can transfer through socialization — watching, imitating, experiencing together. But agents can't access tacit knowledge. For knowledge to enter the human-agent collaboration space, it must become *explicit*. It must be written down.

This constraint is a feature. It forces articulation. Creates audit trails. Enables handoffs across sessions. The filesystem doesn't support Nonaka's "socialization" phase — and that's precisely why it works for AI collaboration.

---

## Intermediate artifacts as human-verified lossy compression

Here's a pattern that emerges across every effective human-agent workflow:

```
Raw inputs (messy, large) 
    → Agent synthesizes → Intermediate artifact (condensed, structured)
        → Human reviews/edits → Selected artifacts 
            → Agent uses as context for downstream task
```

Each intermediate artifact is a **lossy compression** of the upstream work. The research summary doesn't contain everything from the source documents. The plan doesn't capture every nuance of the research. Information is lost at each step.

But — and this is crucial — it's *human-verified* lossy compression.

You're not trusting the agent to autonomously decide what matters across a 50-document research project. You're reviewing the summary of documents 1-10, keeping what's useful, discarding what's not, and feeding that forward.

Why does this matter? Because automated compression fails in predictable ways.

**Brevity bias**: Automated summarization drops domain-specific insights in favor of concise summaries. The summary looks adequate but lacks the tacit knowledge that made the original valuable.

**Context collapse**: Iterative rewriting erodes details over time. Round 1 loses some fidelity. Round 2 loses more. By round N, the context is a skeleton of what it once was.

Human review at intermediate checkpoints prevents both failure modes. You catch the important nuance before it gets compressed away. You preserve domain-specific insights that would look "redundant" to an automated system.

**Intermediate artifacts aren't overhead. They're alignment infrastructure.**

---

## The autonomy gradient

None of this means agents should never act autonomously. The point is that autonomy should be *variable* — a slider, not a switch.

With filesystem-based context curation, you can dial autonomy per task:

**High autonomy:**
```
"Process all files in /research/interviews, produce summary in /outputs"
```

**Medium autonomy:**
```
"Here are 3 files I selected, synthesize them into X"
```

**Low autonomy:**
```
"Read this one file, answer this specific question"
```

You adjust based on:
- Task complexity (simple tasks → more autonomy)
- Context quality (well-organized knowledge base → more autonomy)
- Stakes (high-stakes output → less autonomy, more checkpoints)
- Your trust in this particular workflow (battle-tested → more autonomy)

Try implementing this graduated autonomy with a memory system that manages itself. You can't. The filesystem gives you granular control because you're explicitly selecting what the agent sees.

---

## The pragmatic philosophy: Don't wait for perfect

Here's the uncomfortable truth about the autonomous agent frameworks people are building: they're solving 2027 problems.

The elaborate multi-agent orchestration, the self-managing memory systems, the automatic context optimization — these might work eventually. But they don't work reliably now.

Meanwhile, practitioners with manual curation are capturing 80% of the value *today*.

The people building toward full autonomy are, in effect, betting that the remaining engineering challenges will be solved soon. The practitioners are betting that human judgment at intermediate steps is not a bug to fix but a feature to embrace.

I'm betting with the practitioners.

Not because autonomous systems will never work. But because:

1. **Current technology rewards supervision.** LLMs are fallible. They hallucinate. They have jagged intelligence. Human checkpoints catch failures before they cascade.

2. **The value capture is immediate.** You don't need to wait for the perfect system. Filesystem + manual curation + intermediate artifacts works *now*.

3. **The approach scales with capability.** As models improve, you slide autonomy right. You don't need to rebuild your entire architecture.

4. **Human judgment is alignment infrastructure.** Even if agents become more reliable, having humans curate context and review intermediate artifacts keeps the system aligned with actual goals.

Karpathy gets this. "This is the *decade* of agents, not the year," he says. "Less Iron Man robots and more Iron Man suits."

The suit augments you. You're still in control. And that's not a limitation of current technology — it's appropriate humility about what we're building.

---

## What this means for knowledge work

If you're using AI agents for knowledge work — research, writing, analysis, consulting, legal work, anything document-heavy — here's the practical upshot:

**Embrace manual context curation as a practice, not a workaround.**

This means:

1. **Organize your filesystem intentionally.** The folder structure is cognitive architecture. Make it navigable for both you and the agent.

2. **Create intermediate artifacts.** Don't go from raw inputs to final output in one step. Research summary → plan → draft → final. Each artifact is a checkpoint.

3. **Review at high-leverage points.** Spend attention proportional to impact. The research phase matters more than the final formatting.

4. **Select context explicitly.** Don't rely on automatic retrieval. Know what's going into each prompt. If you wouldn't give this context to a human collaborator, don't give it to the agent.

5. **Use the autonomy slider.** High autonomy for routine tasks with clear patterns. Low autonomy for novel, high-stakes, or ambiguous work.

6. **Build persistent context (AGENTS.md, knowledge base).** Procedural knowledge about "how we do things" compounds over time. Capture it.

This isn't glamorous. It doesn't demo well. You can't tweet "look at my autonomous agent doing everything while I sleep."

But it works. And it works *now*.

---

## The missing theory

What I've tried to articulate here is the theory that practitioners have been using intuitively but not expressing:

**Manual context curation is not a limitation of current AI. It's the appropriate collaboration model for systems that are powerful but fallible.**

The filesystem as shared workspace. Intermediate artifacts as human-verified compression. Supervision as context shaping, not action approval. Autonomy as a gradient, not a binary.

This is the case for keeping humans in the loop — not as a temporary safety measure, but as the architecture that actually works.

The automation seekers will eventually build impressive demos. The practitioners will keep quietly getting work done.

I know which approach I'm betting on.

---

## Related

- [[Manual context curation is the work]]
- [[Supervision is context curation, not action approval]]
- [[The Filesystem as Agentic Ba]]
- [[Middle artifacts as collaboration checkpoints]]
- [[Brevity Bias and Context Collapse]]
- [[Human-Agent Collaboration Framework]]
