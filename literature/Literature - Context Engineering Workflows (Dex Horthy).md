type:: [[Literature Note]]
status:: Processed
date-created:: 2025-12-09
source-url:: https://www.youtube.com/watch?v=BNhRnx_O95c
author:: Dex Horthy (@dexhorthy), Jeff (Chroma)
publication:: Chroma YouTube
date-published:: 2025-12
date-retrieved:: 2025-12-09

# Literature Note: Context Engineering Workflows (Dex Horthy)

**Source**: [Chatting agents, context engineering and more with Dex Horthy](https://www.youtube.com/watch?v=BNhRnx_O95c) — Chroma (December 2025)

---

## Why This Source Matters

Dex Horthy runs Human Layer (agent collaboration infrastructure company) and has built his entire operational system—CRM, task management, knowledge management—on markdown files, Claude, and manual curation. He doesn't explicitly argue for these patterns. He just uses them because they work.

His system independently validates several framework principles: manual curation, filesystem as shared workspace, markdown as format, procedural memory externalization. But more importantly, his system reveals *why* these patterns work through the constraints he navigates and the choices he makes.

This isn't prescriptive theory. It's descriptive evidence of what actually works in practice.

---

## Manual Curation in Practice: What It Actually Looks Like

### The Human Curates Structure, Automation Executes

Dex has a weekly automation that scans his calendar: "I have a hook set up that basically uh every week it goes and looks at everything on my calendar... check who's not already in the CRM. If it's external and they're not in the CRM and it looks like, you know, think about does it look like a sales meeting or whatever it is. Pull them in."

But who decided which categories matter? Who defined "sales meeting" vs "investor meeting" vs "random user"? Dex did. The automation executes his judgment.

The CRM writer agent: "We have like a CRM writer agent, which is like a sub agent that is like prompted to like, hey, if you're going to create a person or a company and like link them together, whether you're creating a person or you're creating a company, always go search the web."

Who wrote "always go search the web"? Who decided data enrichment is mandatory for new contacts? Who structured the prompt? **The agent doesn't decide its own procedures. Dex manually curated them.**

Even merge conflict resolution: "When there's merge conflicts we have instructions in the prompts of like here's how to here's how to resolve merge conflicts and like if it's really simple just do it for these sorts of files just keep both always because it's like a journal."

Who decided journals should keep both sides? Who classified which files are journals? Who encoded these rules? Dex manually curated the conflict resolution policy.

**Pattern: Automation handles repetition. The human curates what the automation does, when, and how.**

### The Human Curates Access, Not Retrieval

During calls: "When I'm on a call with somebody, I open up my editor and I can pretty consistently just be like okay cool here's who this person is. And it's so much faster than clicking around a web UI."

He's not asking an agent "tell me about this person." He's **directly opening the markdown file**. He knows where it is. He navigated there instantly. Why can he do this? Because he curated the file structure well enough that retrieval is trivial.

The weekly review: "I just like run it as part of my like Friday review process." The automation isn't running autonomously. **Dex initiates it.** He's integrated it into his manually curated workflow.

When deciding what to track: "We have like a folder of like just like they don't get an account, but they just have like a CRM contact." Who decided the distinction between "gets an account" and "just a contact"? Who created that folder structure? Manual curation of organizational categories.

**Pattern: Manual curation of structure pays off in instant access. The work happens upfront—organizing, structuring, naming—so retrieval is fast later.**

### What Manual Curation Means Operationally

Based on Dex's practices:
- **You decide what matters** (what goes in the CRM, what categories exist)
- **You design the workflows** (calendar → enrichment → CRM on Friday reviews)
- **You organize the structure** (folders, file naming, front matter schema)
- **You write the prompts** (agent behaviors, enrichment policies, conflict resolution)
- **You initiate automation** (workflows trigger when you invoke them)
- **You inspect outputs** (open files directly, review what agent created)

This isn't "doing everything manually." It's **curating the system that automates the work**. The judgment stays human. The repetition becomes automated.

---

## Why Filesystem? The Implicit Arguments Revealed Through Choices

### Tool Independence as Core Value

Dex never argues "you should use a filesystem." But look at his reasoning when asked about Git: "I basically just use it as like S3 or like a like generic document store right like I mean being able to merge conflicts is great but again the CRDT thing is the actual answer."

He's not using Git for version control. He's using it because it's **a durable place to put plain text files**. When asked about the complexity: "Even even without an air table like separate sync system there's still like the repo."

The repository is the source of truth. Airtable is just a view. Why? Because **files are universal**. They work in VS Code. They work in Obsidian. They work in Google Drive. They work as zip files.

Compare his reasoning on specialized tools: "I could go do like clay and zoom info and like learn all this stuff but again I was just like if we can just do it with cloud and markdown then that works great and like that makes everything a lot simpler and I'd rather have the like 80% or 90% and just all one tool versus like specialized tools for every single part of the GTM stack."

**The implicit argument: The filesystem avoids tool lock-in.** The files outlive any particular tool. You can switch editors, sync mechanisms, viewers—the files remain accessible.

### Inspectability Enables Casual Collaboration

On Git collaboration: "We store we store it all. It's like everyone's just pushing and pulling straight to master for that repo because it's like plain text documents."

Why can they push straight to master without fear? Because **plain text is inspectable and repairable**. If something breaks, you can see what broke and fix it. Try that with a proprietary database format.

The merge conflicts: "It's almost always just like additive merge. There's very rarely like for markdown files this have to like actually merge logic like you get with code."

Markdown files don't have complex interdependencies. They're mostly additive. This makes casual collaboration safe. **The filesystem + plain text enables loose coordination without elaborate tooling.**

### The Filesystem as Shared Cognitive Space

When describing the CRM structure (implicitly): files for people, files for companies, files organized by type. The **folder hierarchy maps to organizational categories**. data/ for raw information, memory/ for persistent context, task/ for current work.

He can open the right file during a call because **the filesystem structure mirrors his mental model**. He doesn't need to search—he knows where things are because he organized them intentionally.

**The implicit argument: The filesystem isn't just storage. It's a shared cognitive architecture** that humans and agents both navigate using the same structure.

---

## Why Markdown? What Front Matter Actually Enables

### Zero-Token Context Navigation

Dex mentions this once: "Front matter is nice because you can do a lot of like slicing and filtering deterministically without the model having to actually go read the whole file."

What does this mean in practice? His CRM has YAML front matter (name, company, tags, contact info) and markdown body (unstructured notes, history). The agent can **query the metadata without reading the content**. This is zero-token navigation through the knowledge base.

When syncing to Airtable: "It's a bidirectional sync that is basically taking mostly stuff from the front matter like the actual like structured data about a record and then taking the body of it and just putting it in like a notes field basically."

Front matter is machine-queryable structure. The body is human-readable context. **Markdown gives you both**—deterministic operations on metadata, rich context in prose.

### Schema Evolution Without Migration

On rigid schemas: "JSON was for humans and tune is for language models. I'm like okay JSON first of all JSON is not for humans. JSON is for programs." And: "Schemes are for humans not for AI. Or or or rigid schemas are at least."

His CRM schema evolves: "The agent itself can decide oh I need a new field great I add it. Maybe I'll back fill maybe I won't backfill."

Need to track job titles? Add a field to front matter. Need to track relationship strength? Add a field. No migration script. No schema validation. **The structure adapts as you discover what matters.**

Try that with SQL. Try that with JSON schemas that require validation. The rigidity becomes a liability when you're learning what information matters through use.

### Human Readable, Machine Parseable

When Dex works: "I open up my editor and I can pretty consistently just be like okay cool here's who this person is. And it's so much faster than clicking around a web UI."

He's reading markdown files directly. Not through an interface. Not through generated views. **The source format is human-readable.** But the same files are machine-parseable for the agent.

**The implicit argument: Markdown is the sweet spot.** Enough structure for deterministic operations (front matter). Enough flexibility for evolution (just add fields). Human-readable for inspection (markdown prose). Machine-readable for processing (YAML parsing).

---

## The System That Emerged vs. The System That Was Designed

### The GTD Failure: Over-Systematization Upfront

Dex tried to build a proper system: "I had I think I do you know the getting things done the like Robert Allen GTD? Yeah GTD. So I was like, 'Okay, cool.' Like deep research. Go make me a long summary of the GTD method and then drop that in a markdown file for Claude and just like go implement this system and then it like kind of built the whole set of stuff."

Claude built a complete Getting Things Done implementation in markdown. Inbox, contexts, projects, someday/maybe lists, weekly reviews—the whole methodology.

Result? "It actually ended up being really heavyweight."

When a co-founder joined and they needed actual collaboration: "We consolidated on like more of the like YC inspired like okay, what's the goal for the month? What's the goal for the week? What's the goal for today? Check in at the beginning of every day and at the end of every day like who did their thing? What's behind? what do we need to do?"

The elaborate system built by following best practices failed. The simple system that emerged through actual use succeeded.

And crucially: "But there's no AI in that Google doc. It's just you guys as humans typing."

**The principle revealed: The system should match the work structure, not impose one.** GTD is optimized for solo knowledge work. Two people in a room collaborating need something simpler—shared goals, daily check-ins.

### What Works: CRM Built Through Use

The CRM wasn't designed upfront. It evolved: "We have uh I have a markdown system and then like we needed to like scale it to beyond me and like basically adding a cloud command to sync it."

Started simple (Dex's personal files). Added sync when needed. Added Airtable view when less-technical team members needed access. Added calendar automation when manual entry became burdensome. Added web enrichment when data quality mattered.

**Each feature emerged from actual need, not anticipated need.**

The schema evolved organically: "The agent itself can decide oh I need a new field great I add it." When Dex discovered he needed to track something new (job title, relationship type, last contact date), he just added it.

**The principle: Systems improve through use, not through upfront design.** The work reveals what matters. Manual curation captures what matters into the system.

---

## The Oral Tradition Problem: Tacit Knowledge in Procedural Memory

### Written Instructions Are Incomplete

Dex built a research→plan→implement workflow with detailed prompts. "Thousands of people have adopted on GitHub and like have grabbed the prompts and put them in their own projects and are constantly being like these are the best this is state-of-the-art for like using cloud code to like solve hard problems."

But there's hidden knowledge: "When I use the prompts they're very different from how most people use the prompts and most people haven't used them enough to know what a good session versus a not so good session looks like."

The problem: "There's just like oh there's six instructions and if you don't reinforce the instructions like okay now we're on phase three like please also do five four five and six sometimes it'll just skip to the end or things like that."

The tacit knowledge experienced users have: "There's a lot of what I call like oral tradition this is the same thing of like people who used to be really good prompters they're just like okay cool there's this thing where like okay you use this command and then you tell it what you want and at the end you have to say like **remember stay objective we don't want you to tell me how to solve it just tell me how the codebase works today**."

**The written prompt looks complete. But practitioners have tacit knowledge—reinforcements, incantations, timing—that isn't written down.**

### Why This Matters for Knowledge Externalization

This is the externalization problem in microcosm. The documentation is missing "the weird tricks that make it actually work." The prompt has the explicit steps, but not the implicit practices.

Dex's response: "What we're trying to do now is like how do we how do we make the product um and the tooling less require that oral tradition? How do we bake that into the opinions?"

His solution direction: "If you know what the steps are, don't rely on the prompt for control flow. If you know what the workflow is, split the prompt up into smaller workflow steps."

But notice: he's **manually redesigning the prompts** based on observed failure modes. He's not automating the knowledge capture. He's observing how people fail, identifying the missing knowledge, and manually encoding it into better prompts.

**The principle: Procedural memory improves through observed use and manual capture of patterns.** The oral tradition emerges through practice. Externalization happens when practitioners notice the gap and encode it.

This is exactly [[In-Context Skill Development]] in action—but it reveals that the "in-context" part requires human observation to become "in-system."

---

## Context Engineering as Information Density Optimization

### The Core Definition

Dex defines context engineering with precision: "Context engineering for me is like how do you get the most out of today's models? Yeah. If I was going to put it like at the top. A lot of people say, 'Oh, it's all about putting the right information into the model.' But it's like it's like it's it's getting the right information in, but also like keeping it as small as possible. And the keeping it as small as possible and as dense as possible is like the the thing that actually I think like **not token dense, but like information per token density**."

Not token efficiency. **Information efficiency.** A summary might be shorter but signal-poor. A well-structured detailed document might be longer but signal-dense.

Why this is permanent: "As long as we're dealing with quadratic like transformer attention, you're always going to benefit from doing the deterministic engineering that allows you to keep the context window as small as possible for a given task."

**Context engineering isn't a workaround for limited models. It's a permanent discipline as long as attention has costs.**

### Architectural Pattern: Fast Orchestrator + Slow Oracle

The traditional pattern: "Use a really smart model as your like top level steering orchestrator something like opus 45... And then you would delegate out like with your harness has sub agents... to a bunch of sub agents that use faster cheaper models."

The new pattern inverts this: "The thing we've been exploring... is where your like main orchestrator is actually a smart but not the smartest fast model. So they've been using sonnet as the default for a really long time... and then they had this thing oh you can delegate out to a smart model."

Why? Slow models are slow at everything: "Opus is going to sit there and call tools and read every single file and it's just slow because it's a big slow model."

The solution: "If you can have the the fast orchestrator model like figure out which files are relevant without having to like really understand every line of code, you can put some deterministic layer in between that is just going to like stuff all those files into a big prompt and you kind of like step away or like you're you're deemphasizing the agentic loop loop and you're just like here's a crap ton of context tell me how it works."

**Use fast model to identify what's relevant. Use deterministic layer to load it all. Use slow model to think about it.** Don't make the slow model loop through tools.

This is context engineering: know what you need, stuff it in efficiently, let the model process it all at once.

### The Scaling Constraint: Instruction Following Limits

Research finding: "Models can follow about 100 to 200 instructions or 150 to 200 instructions. And if you give more than that, you basically like really start to lose out on you spread the attention across all the instructions."

This creates "instruction severity inflation": "You have this like almost like instruction severity inflation where everybody who wants to add a new instruction wants it to be followed. So they put theirs in all caps and then the the other ones get followed last and then everyone is coming in and suddenly your entire like memory like instruction system your whole system prompt is just like everything's in all caps and you're actually like d-tuning it from everything else in the conversation."

**This is a hard constraint on procedural memory.** You can't just keep adding rules to AGENTS.md. After ~150 instructions, you're competing for attention where everything shouts and nothing is heard.

Potential solution: "Why is like I guess agentic search not a solution to that problem? Like anthropic just launched their like tool search thing for example like seems like rules search in this context would also be like potentially very effective."

Instead of loading all rules: agent searches for relevant rules for current task. This hasn't been implemented yet, but it's a promising direction for scaling procedural memory.

---

## Model Intuition: The Cost of Switching

### Deep Intuition vs. Broad Familiarity

Dex's strongest opinion: "You will get better results if you pick one model, one tool and work with it a lot uh for a month or two and versus the like incremental gains you might get by like... using a different model for three weeks every time."

Why? "The people who are really good at this like have a really good intuition of the models and their context windows and like whe when to yell at them versus when to be supportive and all these like things that like are kind of feel a little bit like superstitious."

These practices feel superstitious but get results. And they're **model-specific**. "When CLI came out and uh especially the codex model... if you yell at codecs the way you're used to yelling at claude you completely de-tune the model and you actually like screw up the performance a lot like all the all caps and like important and you must always is like is helpful and gets like good results from opus... but um you go use the same prompts with a different model" and it fails.

**The implicit principle: Expertise is partly about tool-specific intuition.** The "best practices" that work for Claude don't necessarily work for Codex. Constantly switching prevents you from building the intuition that makes you effective.

This connects to manual curation: the experienced practitioner has tacit knowledge about when to reinforce instructions, when to be supportive, when to push back. This knowledge comes from depth, not breadth.

---

## How This System Validates Framework Principles

### [[Manual context curation is the work]]

Dex curates:
- CRM structure (what categories, what fields, what organization)
- Workflow triggers (calendar review on Fridays, enrichment after calls)
- Agent prompts (always search web, how to resolve conflicts, what makes a sales meeting)
- File organization (folders, naming, hierarchy)
- Merge policies (journals keep both sides, other files resolve semantically)

**Automation executes curated policies. The human doesn't do repetitive work, but the human curates what gets automated.**

### [[The Filesystem as Agentic Ba]]

Uses filesystem as shared workspace:
- Persistent across sessions (files survive restarts)
- Navigable by structure (folders map to categories)
- Editable by both (human opens in editor, agent writes via tools)
- Inspectable (plain text, no black boxes)
- Tool-independent (works with VS Code, Obsidian, Git, Drive)

**The filesystem is the ba—the shared space where human and agent collaborate.**

### [[Markdown as LLM-Native Format]]

Uses markdown with front matter:
- Front matter for deterministic operations (zero-token queries)
- Prose for rich context (human-readable notes)
- Structure that evolves (add fields as needed, no migration)
- Information density (hierarchical headers + YAML metadata)

**Markdown is optimal because it's human-readable AND machine-parseable, structured AND flexible.**

### [[Knowledge Externalization as Agentic Interface]]

GTD system built through conversation with Claude. CRM writer agent prompted with enrichment policies. Merge conflict resolution encoded in instructions. Weekly automation designed through articulating the workflow.

**Interacting with the agent forces externalization.** To tell the agent what to do, you must articulate tacit knowledge.

But the oral tradition problem reveals the limit: **not all tacit knowledge gets externalized upfront**. Some emerges through use and requires continuous capture.

### [[Context Continuity Engineering]]

The CRM is long-term memory (persists across sessions, accumulates expertise). The weekly review is working memory (task-specific, generates updates, archives after completion).

Front matter enables progressive disclosure (query metadata, load content on demand). The instruction limit constrains how much procedural memory fits in prompts.

**The system needs both persistence (files) and retrieval (front matter queries) to enable continuity.**

---

## What This Reveals About Effective Systems

### Principles That Emerge From Practice

1. **Tool independence**: Plain text files work everywhere, outlive any particular tool
2. **Inspectability**: Human can see what agent did, understand state, fix problems
3. **Flexible structure**: Schema evolves as you discover what matters
4. **Zero-token queries**: Metadata enables filtering without reading content
5. **Human-initiated automation**: Workflows trigger when human invokes them
6. **Curated procedures**: Agent behaviors are manually designed, not automatically learned
7. **Systems emerge from use**: What works emerges through practice, not upfront design

### Why These Patterns Work

They navigate real constraints:
- **Context window limits** → front matter enables progressive disclosure
- **Instruction following limits** → need retrieval-based rule loading
- **Tool lock-in risk** → filesystem provides universal substrate
- **Schema evolution needs** → markdown front matter adapts without migration
- **Collaboration needs** → plain text is inspectable and repairable
- **Knowledge accumulation** → files persist, structure organizes
- **Procedural memory** → prompts encode policies, humans refine through use

**These aren't arbitrary choices. They're solutions to constraints that any system working in this space will encounter.**

---

## Open Questions That Remain

**How do you externalize oral tradition?** The research→plan→implement prompts look complete but experienced users add incantations. Systems don't yet support continuous externalization of tacit knowledge that emerges through use.

**How do procedural memory systems scale past 150 instructions?** Retrieval-based rule loading hasn't been implemented. Agentic search for rules is theoretically promising but not practiced yet.

**What's the right sync primitive for collaborative agent workspaces?** Git is overkill. CRDTs don't exist yet for this use case. Multiple humans + agents editing markdown concurrently needs better primitives.

**When should you systematize vs. stay flexible?** GTD system was too rigid. Simple Google Doc worked better. But agents need explicit systems. How do you balance infrastructure with flexibility?

**Can tacit model-specific intuition be externalized?** Experienced users know when to yell at Claude, when to be supportive. This knowledge is model-specific and tacit. Can it be captured?

---

## Connection to Framework

This source provides empirical validation of framework principles through a working system built independently. Dex didn't follow the framework—he discovered these patterns through practice. That they converged suggests these aren't arbitrary preferences but **solutions to fundamental constraints**.

**Validates:**
- [[Manual context curation is the work]]
- [[The Filesystem as Agentic Ba]]
- [[Markdown as LLM-Native Format]]
- [[Knowledge Externalization as Agentic Interface]]
- [[Context Continuity Engineering]]

**Extends:**
- [[Context Engineering]] — provides concrete techniques (front matter, fast orchestrator + slow oracle, deterministic layers)
- [[Working Memory vs Long-Term Memory]] — CRM as long-term, weekly review as working memory
- [[Brevity Bias and Context Collapse]] — instruction severity inflation as third failure mode

**Challenges:**
- Instruction following limit (100-200) constrains how much procedural memory fits in prompts
- Oral tradition problem reveals continuous externalization is needed, not one-time documentation
- System that emerged through use (simple Google Doc) beat system designed upfront (GTD)

**New insights:**
- Front matter enables zero-token context navigation (query metadata without reading files)
- Git-as-dumb-storage pattern reveals need for better sync primitives
- NoSQL/flexible schemas essential for contexts that accumulate and evolve
- Model-specific intuition is real and doesn't transfer between models
- Automation should execute manually curated policies, not replace curation

---

## Related

[[Context Engineering]]
[[Context Continuity Engineering]]
[[Manual context curation is the work]]
[[The Filesystem as Agentic Ba]]
[[Markdown as LLM-Native Format]]
[[Knowledge Externalization as Agentic Interface]]
[[Working Memory vs Long-Term Memory]]
[[In-Context Skill Development]]
[[Brevity Bias and Context Collapse]]



