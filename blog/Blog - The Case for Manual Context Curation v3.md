type:: [[Blog Draft]]
status:: Draft
date-created:: 2025-01-12
version:: 3
sources:: [[Human-Agent Collaboration Framework]], [[Manual context curation is the work]], [[The Filesystem as Agentic Ba]], [[Middle artifacts as collaboration checkpoints]], [[Supervision is context curation, not action approval]], [[Brevity Bias and Context Collapse]], [[Literature - Context Engineering Workflows (Dex Horthy)]]

# The Case for Manual Context Curation

*A framework for human-AI collaboration that keeps creation in human hands*

---

## The reframe: Supervision is context curation, not action approval

The standard mental model of human-AI supervision looks like this:

> Agent proposes action → Human approves or rejects → Agent executes

This frames the human as a gatekeeper. You're clicking "yes" or "no" on things the AI wants to do. It's reactive. It's tedious. And naturally, you'd want to automate it away.

But this isn't what effective collaboration actually looks like.

**The high-leverage work isn't approving outputs — it's shaping what the agent sees before it acts.**

When you curate context — deciding which files to include, what background to provide, which constraints matter, what "good" looks like — you're not supervising *outputs*. You're shaping *inputs*. By the time the agent proposes something, the context has already constrained it toward useful proposals.

Consider the leverage hierarchy:

- Research framing wrong → everything downstream is wrong
- Plan wrong → 10-100 wasted outputs
- Individual output wrong → 1 wasted output

Human attention should be proportional to leverage. Review the research closely. Review the plan. The individual outputs? Less scrutiny if the upstream context was curated well.

**Supervision is context curation.** The bottleneck isn't the final action. It's the context that shaped it.

---

## The autonomy slider

Karpathy articulated this in his recent talk on software in the AI era. He calls it "the autonomy slider" — you don't choose between full human control and full AI autonomy. You dial it based on the task.

The same principle applies across all knowledge work:

**High autonomy:**
"Process all documents in this folder, produce a summary following this template."

**Medium autonomy:**
"Here are three sources I've selected. Synthesize them into an analysis of X."

**Low autonomy:**
"Read this specific document. Answer this specific question."

You adjust based on task complexity, stakes, how well-organized your knowledge base is, and how battle-tested the workflow is.

Karpathy's key insight: even when AI output comes instantly, you're still the bottleneck for verification. A 10,000-line diff isn't useful if you can't verify it's correct. His framing: "Less Iron Man robots and more Iron Man suits." The suit augments you. You're still in control.

The autonomy slider moves right over time as patterns become reliable. "This is the *decade* of agents, not the year," Karpathy says. Gradual progression. Verification at each step. Human judgment retained where it matters.

---

## The workspace: Filesystem as collaboration space

If context curation is the work, where does it happen?

For practitioners who've figured this out, the answer is surprisingly mundane: **the filesystem.**

Not a special-purpose memory system. Not a vector database. Not an elaborate agent framework. Folders and files — organized intentionally.

Why does this work?

| Property | Why it matters |
|----------|----------------|
| **Persistent** | Survives session boundaries, agent amnesia |
| **Navigable** | Hierarchical structure maps to cognitive categories |
| **Editable by both** | Human and agent read/write the same artifacts |
| **Inspectable** | You can see everything the agent sees |
| **Transparent** | No hidden state, no black boxes |

There's a deeper insight here. Ikujiro Nonaka, the knowledge management theorist, introduced "ba" (場) — a shared space where knowledge creation happens. The filesystem is ba for human-agent collaboration.

But unlike human-to-human collaboration, where tacit knowledge can transfer through observation and shared experience, **the filesystem requires externalization**. For knowledge to enter the collaboration space, it must be written down.

This constraint is a feature. It forces articulation. Creates audit trails. Enables handoffs across sessions. The filesystem doesn't let you be vague — and that's precisely why it works for AI collaboration.

---

## Intermediate artifacts as human-verified compression

Here's the pattern that emerges across effective workflows:

```
Raw inputs (messy, large) 
    → Agent synthesizes → Intermediate artifact (condensed, structured)
        → Human reviews/edits → Selected artifacts 
            → Agent uses as context for downstream task
```

Each intermediate artifact is a **lossy compression** of upstream work. The research summary doesn't contain everything from source documents. The plan doesn't capture every nuance. Information is lost at each step.

But it's *human-verified* lossy compression.

You're not trusting the agent to autonomously decide what matters across a large research project. You're reviewing the summary, keeping what's useful, discarding what's not, and feeding that forward.

Why does this matter? Because automated compression fails in predictable ways:

**Brevity bias**: Automated summarization drops domain-specific insights. The summary looks adequate but lacks the tacit knowledge that made the original valuable.

**Context collapse**: Iterative rewriting erodes details over time. Each compression loses fidelity. Losses compound. By the time you notice, the knowledge is unrecoverable.

Human review at intermediate checkpoints prevents both. You catch important nuance before it compresses away. You preserve domain-specific insights that automated systems would optimize out.

**Intermediate artifacts aren't overhead. They're alignment infrastructure.**

---

## What this looks like outside of coding

The pattern applies wherever work is document-heavy, research-intensive, or involves multi-step synthesis.

**Legal research**: Raw case files and statutes → Agent produces case summary with relevant precedents → Lawyer reviews, selects what's relevant to this matter → Agent drafts arguments using curated precedents → Lawyer edits, adds judgment → Final brief.

At each step, the lawyer curates context. The agent never operates on 10,000 pages of raw case law autonomously. It works on human-selected, human-verified condensations.

**Consulting engagement**: Client transcripts and documents → Agent extracts key problems and themes → Consultant reviews, identifies the real issue → Agent produces analysis framework → Consultant refines → Agent drafts recommendations → Consultant adds expertise and judgment.

The consultant decides what the real problem is. The agent provides leverage for synthesis and drafting.

**Research synthesis**: Collection of papers and sources → Agent produces structured literature notes → Researcher reviews, identifies connections → Agent drafts synthesis → Researcher adds interpretation and argument.

The researcher maintains intellectual direction. The agent handles volume.

**Business operations**: Meeting recordings → Agent extracts action items, decisions, open questions → Manager reviews, prioritizes → Agent drafts follow-ups → Manager approves.

The manager curates what matters. The agent handles extraction and drafting at scale.

In each case:
- The human decides what to include in context
- The agent produces intermediate artifacts
- The human reviews and selects what moves forward
- Autonomy varies by step — lower for framing, higher for execution

---

## The human as creator, not just verifier

Here's what the automation framing misses: **the people getting most value from AI agents aren't excited about having their work done for them. They're excited about what they can create.**

When you have capable tools, you think bigger. You attempt things you wouldn't have attempted. You become more ambitious, not less.

The shift isn't from "human does work" to "AI does work." It's from "human does constrained work within capabilities" to "human directs ambitious work through AI amplification."

The framework I'm describing — manual context curation, intermediate artifacts, the autonomy slider — isn't about keeping humans in the loop as a safety measure. It's about keeping humans in the loop as *creators*.

The human decides what to build. The human curates context. The human reviews intermediate artifacts and steers direction. The human adjusts autonomy based on the task. The agent provides leverage, speed, capability at scale.

You work *through* the agent's hands, but the creative direction remains yours.

This is why the excitement around AI tools feels different from previous automation waves. It's not "my job is being replaced." It's "I can finally build the thing I've been imagining." That's not replacement. That's creative liberation.

---

## The pragmatic case

People building elaborate autonomous agent frameworks are often solving future problems. The practitioners capturing value now are doing something simpler:

1. **Organize knowledge intentionally.** The folder structure is cognitive architecture for both human and agent.

2. **Create intermediate artifacts.** Don't go from raw inputs to final output in one step. Research → plan → draft → final. Each artifact is a checkpoint.

3. **Review at high-leverage points.** Spend attention proportional to impact. The framing phase matters more than final formatting.

4. **Select context explicitly.** Know what's going into each prompt. Curate deliberately.

5. **Use the autonomy slider.** High autonomy for routine tasks with clear patterns. Low autonomy for novel, high-stakes, or ambiguous work.

This approach captures most of the value right now, with tools that exist, without waiting for perfect autonomous systems.

And it positions the human not as overhead to eventually remove, but as the creative director working through increasingly capable tools.

---

## Two visions

There are two ways to think about AI-augmented work:

**Vision A: Automation.** AI does the work. Humans supervise, approve outputs, catch errors. The goal is to minimize human involvement. Human attention is overhead.

**Vision B: Amplification.** AI extends human capability. Humans become more ambitious. The goal is to maximize what humans can create. Human judgment is the product.

Manual context curation, filesystem as collaboration space, intermediate artifacts, the autonomy slider — this framework is built for Vision B.

The human isn't overhead to eventually remove. The human is the creative force working through increasingly capable tools.

That's the bet. And that's why keeping humans in the loop — as curators, as creators — isn't a compromise with current technology limitations.

It's the architecture that actually works.

---

## Related

- [[Manual context curation is the work]]
- [[Supervision is context curation, not action approval]]
- [[The Filesystem as Agentic Ba]]
- [[Middle artifacts as collaboration checkpoints]]
- [[Brevity Bias and Context Collapse]]
- [[Human-Agent Collaboration Framework]]
