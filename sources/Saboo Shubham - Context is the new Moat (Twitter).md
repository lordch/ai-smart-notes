# Context is the new Moat

**Source**: https://x.com/Saboo_Shubham_/status/2011278901939683676
**Author**: Saboo Shubham (@Saboo_Shubham_)
**Platform**: Twitter/X
**Date Retrieved**: 2025-01-06

---

Everyone has access to the same models today.

You're using Claude Opus 4.5. So is your competitor. You're using GPT-5.2. So is the startup that launched last week. You're using Gemini 3 Pro. So is everyone else building AI products.

The models are commoditizing. Prices are dropping. Capabilities are converging. What was SOTA a few months ago is now available to anyone with an API key.

So where does the real alpha come from?

Context.

The team that can externalize what they know and feed it to agents in a structured way will build things competitors can't copy just by using the same model.

## Same model, different results

I watched two developers build nearly identical agents using the same model.

One prompted Claude: "Build a multi-agent system that handles customer support tickets with escalation."

The other fed Claude context about their specific product: actual questions users ask, the tone their brand uses, examples of responses that got 5-star ratings vs. complaints, edge cases requiring human handoff, internal tools agents need to access, what "resolved" actually means for their users.

Same model. Same task. Completely different outputs.

The first developer got a generic support bot that sounded like every other AI customer service agent. The second got something that felt like it had been trained on their specific product for months.

The model was identical. The context was the moat. 

And unlike the model, context can't be downloaded. It has to be earned.

## What context actually means

Context isn't just "more words in the prompt." It's structured knowledge that helps the model understand your specific situation.

**User context.** Not personas. Real details. "Our users are developers who want to quickly prototype AI apps. They care about working code they can run immediately, not theoretical explanations. They'll abandon anything that requires more than 10 minutes of setup."

**Domain context.** The specific patterns and constraints of your field. "In multi-agent systems, the coordinator agent should never call tools directly. It delegates to specialized agents. Here's why that matters for reliability."

**Historical context.** What you've tried before and why it didn't work. "We built a similar agent in Q2 2025 using a single prompt approach. It failed because the context window filled up too fast. Here's what we learned about chunking and summarization."

**Quality context.** Examples of what good looks like in your specific situation. Not abstract principles. Actual examples. "This is an agent response that users found helpful. This is one that confused them. Here's the difference."

**Constraint context.** The real limitations that shape solutions. "We need this to work with the free tier of the API. Latency has to stay reasonable for interactive use. The solution needs to be simple enough that someone can understand it by reading the code."

This is the stuff that lives in your head. In your GitHub issues. In slack threads. In the feedback you've gotten. In the intuition you've built from shipping things.

## Why this compounds

Context accumulates over time.

Every project you do, every failure you document, every user insight you capture, every example you collect adds to your context library.

Team A starts every project from scratch. They prompt the model, get generic output, spend hours correcting and adjusting, and then move on. The learning stays in their heads or disappears entirely.

Team B maintains context docs. After every project, they update what they learned. What worked. What didn't. New user insights. New examples of good output. New edge cases to watch for.

Six months later, Team A is still getting generic outputs and spending hours on corrections.

Team B's agents produce better results on day one than Team A gets after a week of iteration.

This is the flywheel. Good context → better outputs → learning what context mattered → improved context docs → repeat.

## What this looks like in practice

I maintain the Awesome LLM Apps repo, an open source collection of 100+ AI agents and RAG implementations. When I build a new agent, I never start from scratch.

Here's a sample of the context I've accumulated:

```markdown
Target user: Developers who want to prototype AI agents fast. 
They'll clone, run, and decide in 10 minutes if it's useful.
They won't read a wall of text. They'll scan the README for a quickstart.

Setup requirements:
- Maximum 3 environment variables (API keys only)
- Single requirements.txt, no complex dependency chains
- "pip install + run" in under 5 minutes or they bounce

Tech stack:
- Python only
- Streamlit for UI (fast to build, easy to understand)
- OpenAI/Anthropic/Google AI SDKs directly, minimal abstraction layers

What gets stars:
- Solves a real problem people actually have (not a toy demo)
- Code is readable without extensive comments
- Easy to extend or modify for their own use case
- Good README with a GIF or screenshot showing it working

What doesn't land:
- "Hello world" level demos (too basic)
- Overly complex architectures for simple problems
- Agents that require 10+ minutes of config before first run

Common failure patterns to avoid:
- Context window overflow on long conversations
- Tool call loops where agent gets stuck
- Unclear error messages when API calls fail
- No graceful handling of rate limits

Agent patterns that work:
- Single-purpose agents that do one thing well
- Multi-agent systems with clear role separation
- Coordinator pattern for complex workflows
- Human-in-the-loop for high-stakes decisions
```

When I open Claude Code (CLAUDE.md) or Antigravity (GEMINI.md) to build a new agent, this context goes in first. The agent already knows what "good" looks like for this repo, what patterns to use, what mistakes to avoid.

First output is 90% there instead of 50%.

That's the moat. Not the model. The accumulated context that makes the model work better for my specific situation.

## Make it automatic

The best context systems are invisible. The context is just there, ready to go, every time.

Every major AI coding tool now supports persistent context files. You create them once, drop them in your project, and they load automatically into every conversation.

The file names vary but the pattern is the same:
- Antigravity / Gemini CLI: GEMINI.md
- Cursor: .cursor/rules
- Claude Code: CLAUDE.md
- Windsurf: .windsurfrules
- Codex: AGENTS.md
- Claude Projects: Upload as Project Knowledge

I keep my agent patterns, quality standards, and failure modes in these files. Every session starts with the agent already understanding my world.

Externalize what you know into files that live in your repo. Stop re-explaining your stack. Stop re-describing your patterns. Stop correcting the same mistakes.

Set it up once. Benefit on every single prompt after that.

## How to start

**Today:** Start a context doc. Who are your users really? What does good look like? What have you tried that failed? Doesn't need to be perfect. Just start.

**After every project:** What did you learn? What surprised you? What will you do differently? Add it.

**Ongoing:** Collect examples obsessively. Good outputs, bad outputs, edge cases. Examples are the highest-leverage context you can provide.

**Make it automatic:** Add a GEMINI.md or CLAUDE.md to your project. It loads automatically. You never think about it again.

That's it. Four steps. The rest is just reps.

Prompting will get easier. Models will understand you better with fewer words.

Context will always matter.

The people who treat context as a first-class engineering problem will build better things faster.

Not because they have better models. Because they're better at teaching.

That's the real skill.

Not telling agents what to do. Helping them understand why it matters.

