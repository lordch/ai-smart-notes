type:: [[Literature Note]]
status:: Processed
date-created:: 2025-12-06
source-url:: https://www.builder.io/blog/agents-md
author:: Steve Sewell
publication:: Builder.io Blog
date-published:: 2025-09-09

- # Literature Note: AGENTS.md Best Practices
- **Source**: [Improve your AI code output with AGENTS.md](https://www.builder.io/blog/agents-md) — Steve Sewell, Builder.io (September 2025)
- ---
- ## Core Argument
	- A small `AGENTS.md` file at project root dramatically improves AI code generation quality.
	- "Instead of repeating yourself in every prompt, you write the defaults once and let the agent start from there."
	- It's "a README for AI agents" — supported by multiple tools as emerging standard.
- ---
- ## The Problem Without AGENTS.md
	- Agent must **rediscover project structure** on every fresh chat
	- Discovery phase "burns time and credits and repeats on every fresh chat"
	- Results are visually correct but details wrong:
		- Wrong library versions
		- Wrong styling patterns
		- Wrong state management approach
		- Hardcoded values instead of tokens
		- Generic solutions instead of project conventions
	- "The output can clearly be better and save us more time"
- ---
- ## Recommended Sections
	- ### 1. Dos and Don'ts
		- "Your opportunity to be as nitpicky as you like. AI thrives on clear guidelines."
		- Examples:
			- Use MUI v3 (version specificity)
			- Use emotion `css={{}}` prop format (pattern specificity)
			- Use mobx for state management (technology choice)
			- Use design tokens, no hard coding (constraints)
			- Default to small components, small diffs (style preferences)
		- **Why it helps**: "Version specificity removes subtle bugs... State choice removes guessing."
	- ### 2. File-Scoped Commands
		- Problem: "Agents try to run full project-wide build commands way too often"
		- Solution: Specify per-file commands for tsc, prettier, eslint, tests
		- **Why it helps**:
			- "Faster loops. Type check a single file in seconds instead of minutes."
			- "Cheaper runs. Not burning tokens or CI minutes on full builds."
			- "When things are fast and cheap, you can instruct the AI to always run them."
	- ### 3. Safety and Permissions
		- Explicit allow/deny lists in natural language
		- Allowed without prompt: read files, single-file checks
		- Ask first: package installs, git push, deleting files, full builds
		- **Why it helps**: "Fewer surprises. No 'why did it npm install' moments."
	- ### 4. Project Structure Hints
		- "A few pointers can save a lot of time from having to re-explore your codebase"
		- Point to: routes file, sidebar, components directory, design tokens location
		- **Why it helps**: "The agent starts where humans would start."
	- ### 5. Good and Bad Examples
		- "Examples beat abstractions. Point to real files that show your best patterns."
		- Also call out legacy files to avoid
		- **Why it helps**: Concrete patterns are clearer than abstract rules
	- ### 6. API Documentation References
		- Point to where API docs live
		- List key endpoints with file references
	- ### 7. PR Checklist
		- Format and type check requirements
		- Test requirements
		- Diff size expectations
	- ### 8. When Stuck Behavior
		- "Ask a clarifying question, propose a short plan, or open a draft PR with notes"
	- ### 9. Test First Mode (Optional)
		- "Write or update unit tests first, then code to green"
		- "Enforces correctness. You lock behavior in tests before the code drifts."
	- ### 10. Design System Index
		- Index your design system so agent learns component APIs
		- Reference indexed output in AGENTS.md
- ---
- ## Key Quotes
	- "Trial and error is key — run prompts, when things aren't the way you prefer, put the feedback in your AGENTS.md"
	- "Keep your AGENTS.md small and scoped"
	- "Lead with concrete examples and file paths"
	- "Iterate and add a rule the second time you see the same mistake"
- ---
- ## Tool Compatibility
	- AGENTS.md is "growing standard" supported by many tools
	- For tools that don't support it (yet), create tool-specific files that point to AGENTS.md:
	- ```
	  # CLAUDE.md
	  Strictly follow the rules in ./AGENTS.md
	  ```
	- Or use symlinks
- ---
- ## Relation to My Framework
	- **This is Procedural Context implementation**: AGENTS.md is exactly [[Context curation taxonomy]]'s "How should agent act here?"
	- **Validates manual curation**: "Trial and error is key" — you build this through use, not upfront
	- **Validates workspace model**: Project structure hints = making filesystem navigable for agent
	- **Validates small diffs principle**: Explicit preference for "small components, small diffs"
	- **Extends my thinking**:
		- File-scoped commands as procedural optimization (fast feedback loops)
		- Safety/permissions as explicit trust boundaries
		- "When stuck" behavior as procedural context for edge cases
		- The iterative process: "add a rule the second time you see the same mistake"
- ---
- ## Extracted Concepts
	- → Consider: Should my framework explicitly recommend AGENTS.md-style files?