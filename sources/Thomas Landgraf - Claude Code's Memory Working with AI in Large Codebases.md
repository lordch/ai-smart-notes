# Claude Code's Memory: Working with AI in Large Codebases

**Source**: https://thomaslandgraf.substack.com/p/claude-codes-memory-working-with
**Author**: Thomas Landgraf
**Publication**: Industrial-Grade Architecture | Research-Lab Curiosity (Substack)
**Date Published**: June 29, 2025
**Date Retrieved**: 2025-01-06

---

Transform Token Costs into Team Knowledge with Smart Memory Management

## 1. Claude Code: It's Not a Tool — It's a Mindset Shift

Over the years, I've seen dozens of developer tools that promised to revolutionize the way we write code. Most of them end up helping around the edges — they autocomplete a function, suggest some refactoring, maybe speed up boilerplate generation. Useful, yes. But transformative? Rarely.

Claude Code is something else entirely.

It doesn't just sit beside you like a helpful assistant. It _thinks_ with you. Plans with you. Refactors with you. Claude Code is more like a pair-programming partner with senior-level insight — embedded right in your terminal, where the context lives and the distractions fade away. You give it a goal, and it doesn't just react. It builds a plan, breaks it into tasks, writes its own code and tests, and returns with results that often need no further tweaking.

That's what I find most refreshing: Claude Code behaves like an engineer who respects the craft. It doesn't try to impress with noisy outputs or shallow shortcuts. Instead, it embraces the complexity of the work — and gets it done.

In my humble (and terminal-prompted) opinion: Claude Code is the first AI that _codes like it gets it_. It's not just a tool in your workflow. It _is_ the workflow — when you let it be.

## 2. Why Token Efficiency Matters — and What It Costs to "Let Claude Cook"

When working with Claude Code on a large codebase, the flow of development changes fundamentally. You don't just jump between coding and prompting. Instead, Claude takes the wheel for long stretches. You hand it a task, and it quietly spins up: crawling through your codebase, absorbing patterns, understanding architecture, formulating a strategy — before it even starts writing a line of output.

This depth is what makes Claude Code powerful — but it's also what makes it **expensive** in a very concrete way.

Whether you're on a pay-as-you-go API model or a fixed monthly plan like Claude MAX, every request Claude processes consumes tokens — and those tokens come with limits. You're not just charged for how often you use it, but also for how much it reads and how deeply it thinks.

Each interaction with Claude involves three interlinked cost drivers:

Impact=(LLM Calls)×(Tokens per Call)×(Model Quality)

First, there's the number of calls you make. Every time Claude starts "thinking," it counts. Then there's how much it _needs_ to think — which is directly tied to how many tokens your request consumes. Claude often needs to load thousands of lines of context to answer even seemingly simple questions, especially on larger codebases. Finally, there's the model you choose. Claude Opus, for instance, provides deeper, more nuanced answers than Sonnet — but it also costs significantly more per token.

It's easy to fall into the trap of asking Claude to "figure it out" again and again — letting it repeatedly parse the same files, rediscover the same structures, and re-analyze your architecture from scratch. The result? You burn through your token budget without realizing it, and the efficiency gains you were hoping for evaporate.

That's why understanding and managing Claude's memory system is essential. It's the difference between working with an architect who remembers your blueprints — and one who has to re-read them every time you ask a question.

Let's explore how that works.

## 3. The Claude Code Memory System: Your Persistent Context Architect

Claude Code's memory system is deceptively simple on the surface — it's just Markdown files. But beneath this simplicity lies a sophisticated hierarchical system that fundamentally changes how AI understands your codebase.

### The Three-Tier Architecture

Think of Claude's memory as a nested set of contexts, each serving a distinct purpose:

**Project Memory (`./CLAUDE.md`)** — This is your team's shared brain. It lives in your repository root and gets committed to version control. Here's where you document your architectural decisions, coding conventions, API patterns, and anything else that should be consistent across your team. When a new developer joins, they're not just inheriting code — they're inheriting the collective wisdom of how that code should evolve.

**Local Project Memory (`./CLAUDE.local.md`)** — Your personal workspace notes. Maybe you're testing against a specific sandbox URL, or you have particular debugging strategies for this project. This file is gitignored, keeping your individual preferences and temporary context separate from the team's shared knowledge. It's like having sticky notes on your monitor — except Claude can read them too.

**User Memory (`~/.claude/CLAUDE.md`)** — Your global preferences that travel with you across all projects. Prefer tabs over spaces? Always use specific ESLint rules? Have a particular way of structuring your commits? This is where those preferences live, automatically merged into every Claude session under your home directory.

### How Claude Loads Context

The magic happens in how Claude discovers and loads these files. It's not a simple "load everything" approach — that would blow through your token budget instantly. Instead, Claude employs a recursive search strategy that's both comprehensive and efficient.

Starting from your current working directory, Claude searches upward toward the root, loading every `CLAUDE.md` and `CLAUDE.local.md` file it finds. This means you can have general guidelines at your repository root and increasingly specific instructions as you dive into subdirectories. A React component deep in your source tree can have its own memory file with component-specific patterns, while still inheriting the broader architectural context from above.

But here's the clever part: subdirectory memory files are only loaded when Claude actually accesses files in those directories. This on-demand loading keeps your active context focused and prevents token waste on irrelevant parts of your codebase.

When working on Button.tsx, Claude loads:
- ✓ ~/.claude/CLAUDE.md (global memory)
- ✓ ~/projects/awesome-app/CLAUDE.md
- ✓ ~/projects/awesome-app/CLAUDE.local.md
- ✓ ~/projects/awesome-app/apps/web/CLAUDE.md
- ✗ ~/projects/awesome-app/apps/api/CLAUDE.md (not loaded)
- ✗ ~/projects/awesome-app/infrastructure/CLAUDE.md (not loaded)

This hierarchical loading means Claude always has the right context — without paying the token cost for context it doesn't need.

## Practical Memory Management: Three Prompts That Changed My Workflow

After months of working with Claude Code on production codebases, I've developed three prompts that have become essential to my workflow. They're not magic formulas — just practical patterns for capturing and maintaining context. I'm sharing them here in the hope they'll save you some of the trial and error I went through.

### The Session Learning Capture: Turning Conversations into Knowledge

At the end of productive Claude sessions, especially after debugging or architectural discussions, I run this prompt to capture what we learned:

```
# Capture Session Learnings

**Instructions:**  
Review our conversation and identify key learnings, corrections, or clarifications that should be preserved for future sessions. Update the appropriate CLAUDE.md or CLAUDE.local.md file. If the information is relevant for a subdirectory only, place or update it in the `CLAUDE.md` file within that subdirectory.

When specific information belongs to a particular subcomponent, ensure you place it in the CLAUDE file for that component.
For example: 
* Information A belongs exclusively to the `heatsense-ui` component → put it in `apps/heatsense-ui/CLAUDE.md`
* Information B belongs exclusively to the `heatsense-api` component → put it in `apps/heatsense-api/CLAUDE.md`  
* Information C is infrastructure-as-code related → put it in `cdk/CLAUDE.md`

This ensures important knowledge is retained and available in future sessions.
```

I run this prompt at the end of productive sessions, especially after deep debugging or architectural discussions. It's like having Claude write its own notes for the next meeting — except the next meeting might be with a different developer on your team.

### The Directory Deep Dive: Building Context from Code

When starting work in a new area of the codebase, or when Claude seems to be missing crucial context, I use this investigation prompt. It's particularly powerful because it forces Claude to actually read and understand the code before making assumptions:

```
# Investigate and Document Directory Architecture

**Instructions:**  
Focus on the specified directory $ARGUMENTS or the current working directory:

1. **Investigate Architecture**: Analyze the implementation principles and architecture of the code in this directory and its subdirectories. Look for:
   - Design patterns being used
   - Dependencies and their purposes
   - Key abstractions and interfaces
   - Naming conventions and code organization
   
2. **Create or Update Documentation**: Create a CLAUDE.md file capturing this knowledge. If one already exists, update it with newly discovered information. Include:
   - Purpose and responsibility of this module
   - Key architectural decisions
   - Important implementation details
   - Common patterns used throughout the code
   - Any gotchas or non-obvious behaviors
```

Pro tip: You can enhance this prompt by adding the session learning context from the first prompt. This creates a more comprehensive documentation update that captures both the code analysis and any corrections or clarifications from your current session.

### The Spring Cleaning: Keeping Memory Accurate

Memory files, like any documentation, can drift from reality. Code evolves, patterns change, and yesterday's truths become today's misconceptions. Here's my maintenance prompt that I run monthly (or after major refactoring):

```
# Review and Update CLAUDE Memory Files

**Instructions:**  

**Step 1: Get Overview** 
List all CLAUDE.md and CLAUDE.local.md files in the project hierarchy.

**Step 2: Iterative Review** 
Process each file systematically, starting with the root `CLAUDE.md` file:
- Load the current content
- Compare documented patterns against actual implementation
- Identify outdated, incorrect, or missing information

**Step 3: Update and Refactor**
For each memory file:
- Verify all technical claims against the current codebase
- Remove obsolete information
- Consolidate duplicate entries
- Ensure information is in the most appropriate file

When information belongs to a specific subcomponent, ensure it's placed correctly:
* UI-specific patterns → `apps/myproject-ui/CLAUDE.md`
* API conventions → `apps/myproject-api/CLAUDE.md`
* Infrastructure details → `cdk/CLAUDE.md` or `infrastructure/CLAUDE.md`

Focus on clarity, accuracy, and relevance. Remove any information that no longer serves the project.
```

This isn't just housekeeping — it's an investment in future productivity. Clean, accurate memory files mean Claude starts every session with the right context, reducing both token usage and frustration.

### Making These Prompts Your Own

These prompts work well for my workflow, but the real power comes from adapting them to your needs. Some teams add sections for testing strategies, others include deployment notes, and I've seen developers create specialized prompts for API documentation or database schema updates.

The key insight? Treat these prompts as templates, not gospel. Start with what I've shared, but evolve them based on your project's unique needs. The best memory management system is the one your team actually uses.

One final thought: I've noticed that teams who commit to memory maintenance see compound benefits. Not only does Claude become more helpful over time, but the memory files themselves become valuable onboarding documents for human developers. It's documentation that writes itself — and stays current because it's actively used.

That's the beauty of Claude Code's memory system. It's not just about making AI smarter. It's about capturing and preserving the collective intelligence of your entire development process.

# Conclusion: We're All Still Learning

I've been coding for more years than I care to admit, and Claude Code is the first tool that made me fundamentally rethink how I approach development. Not because it writes perfect code — it doesn't. Not because it never makes mistakes — it does. But because it showed me that the real bottleneck in AI-assisted development isn't the AI's capabilities. It's our ability to share context effectively.

The memory techniques I've shared here aren't perfect. They're simply what's worked for me and my teams after experimentation, occasional frustration, and more than a few expensive token bills. I'm sure there are better patterns waiting to be discovered. That's the exciting part — we're all pioneers in this space, figuring out together how to build software in fundamentally new ways.

If you've found your own patterns for managing Claude's memory, I'd love to hear about them. If you try these approaches and find ways to improve them, even better. The best thing about working with tools like Claude Code is that we're not just consumers of technology — we're actively shaping how future developers will work.

One final thought: As powerful as these memory systems are, they're just the beginning. The real magic happens when you stop thinking of Claude as a tool and start thinking of it as a team member — one who happens to have perfect recall, infinite patience, and an eagerness to learn your specific way of building software. Here's to fewer repeated explanations, more preserved insights, and codebases that remember their own stories. May your tokens be few and your context be rich.

Happy coding — and happy teaching your AI partner to remember.

