# Non-Coding Agent Workflows (from ccforeveryone.com)

**Source**: `ccforeveryone` course content.
**Goal**: Demonstrate how "Agentic Workflow" beats "Standard Chat" for non-technical tasks.

## 1. The "Parallel Analyst" (Agents)
**Scenario**: You have 20 disparate documents (e.g., job descriptions, apartment listings, vendor proposals) and need to compare them or find specific details.

### Example: Apartment Hunting / Job Search
*   **Old Way (Chat)**: Paste one listing, ask for summary. Paste next listing, ask for summary. Scroll up and down to compare. Context window gets cluttered.
*   **Agentic Way**: "Here is a folder with 20 listings as PDFs. Launch 20 parallel agents. For each listing, extract: Price, Location, Pros, Cons. Then, synthesize a master comparison table in `comparison.md`."

### Why it wins vs Custom GPT?
1.  **Speed**: Parallel processing (Fan Out). It happens in 5 minutes vs 50 minutes of manual pasting.
2.  **Isolation**: Each agent sees only *its* document, reducing hallucination (confusing Listing A with Listing B).
3.  **Synthesis**: The final step is not just "chatting", it's generating a *tangible artifact* (`comparison.md`) that exists outside the chat.

---

## 2. The "Advisory Board" (Sub-agents)
**Scenario**: You need feedback on a subjective document (Resume, Pitch Deck, Blog Post), but generic "give me feedback" prompts give generic advice.

### Example: Resume Review
Instead of asking "Is this good?", you employ a "Board of Advisors" defined in static config files (`.claude/agents/`).
*   **Agent A (The Recruiter)**: Impatient, scans for keywords, looks for red flags.
*   **Agent B (The Hiring Manager)**: Looks for culture fit and specific outcomes.
*   **Agent C (The Career Coach)**: Encouraging, looks for narrative flow.

**Workflow**: "Have the Board review `@resume.pdf`. I want 3 separate reports."

### Why it wins vs "Chat"?
1.  **Perspective persistence**: You don't have to prompt-engineer the persona every time. The "Recruiter" *always* acts that way because it's defined in the project structure.
2.  **Conflict**: You get *competing* views (Recruiter hates the length, Coach loves the story), which is more valuable than a "blended" generic answer from a single model.

---

## 3. The "Deep Synthesis" (File Operations)
**Scenario**: Creating a deliverable based on multiple sources of truth.
**Example**: "Write a Q2 Report (`report.md`) using the data from `@Q2_metrics.xlsx` and the narrative style from `@Q1_report.pdf`."

### Why it wins?
1.  **Grounding**: The agent has *read access* to specific files, not just pasted text.
2.  **Mimicry**: By pointing to an existing file (`@Q1_report.pdf`) as a style guide, you enforce consistency without writing a 10-page style prompt.

## 4. The "Turnaround Manager" (Chaos -> Structure)
**Scenario**: You inherit a mess—scattered notes, angry customer feedback, and a vague mandate to "fix it".
**Source Example**: *Basecamp Coffee Loyalty Program* (`company-context/SCENARIO.md`)
*   **The Input**: A folder `inherited-chaos/` containing:
    *   `customer-feedback/january.md` (Raw survey responses: "Takes forever to earn a drink")
    *   `competitor-research/starbucks.md` (Unstructured notes on rivals)
    *   `old-campaigns/` (List of failed past attempts)
*   **The Task**: "Read all files in `inherited-chaos/`. Analyze why the previous manager failed. Then, propose a 3-month turnaround strategy using the format in `templates/leadership-update-template.md`."

### Why it wins?
1.  **Emotionless Analysis**: The agent reads "The app is confusing" 50 times without getting defensive.
2.  **Pattern Recognition**: It spots that "Complexity" is the root cause across 10 different files, whereas a human might get stuck on individual complaints.
3.  **Instant Formatting**: It takes that messy insight and immediately pipes it into the stiff `Leadership Update` format, saving you the mental energy of "corporate speak".

## 5. The "Interview Planning" Strategy (Ross Mike / Vibe Coding)
**Scenario**: You have a vague idea ("I need a marketing plan") but don't know the specifics. You want the agent to help you figure out the *requirements* first, not just execute a bad plan.

### Source: `mini-lessons/ross-mike-workflows.mdx` & `vibe-coding/plan.mdx`
**The Technique**: "Ask User Question"
**The Prompt**: "Read this vague idea. Interview me in detail using the ask user question tool about literally anything—constraints, budget, tone, trade-offs. Don't generate the plan until you have interviewed me."

### Why it wins?
1.  **Forced Clarity**: It forces *you* to make decisions you didn't know you needed to make (e.g., "Do you want this LinkedIn post to be viral/clickbaity or thought-leadership/sober?").
2.  **No Guessing**: The agent stops hallucinating preferences and actually asks.
3.  **The "Spec" Artifact**: The output isn't the final work; the output is a `REQUIREMENTS.md` file (a spec). Only *then* do you run the execution agent.

## 6. The "Logic vs Implementation" Split (Vibe Coding)
**Scenario**: Defining a complex process (e.g., a hiring funnel or a quiz) without knowing how to build it.
**Source**: `vibe-coding/plan.mdx`
**The Insight**: "Logic is just 'If This, Then That'. You don't need code to define logic."
**Transferable Task**: Designing a Sales Script.
*   **You define the Logic**: "If customer says price is high -> go to 'Value Proposition' block. If customer says they are happy -> go to 'Upsell' block."
*   **Agent implements**: Agent turns your logic into a flowchart, a CRM configuration, or a training doc.

## Summary of Patterns for Knowledge Work

| Pattern | Best For | Agent Advantage |
| :--- | :--- | :--- |
| **Fan Out** | Processing >5 similar items | Speed + Isolation |
| **Specialized Roles** | Creative feedback, Risk assessment | Diverse perspectives |
| **Extraction** | Unstructured notes -> Structured data | Accuracy + Automation |
| **Chaos Taming** | Inheriting messy projects | Emotionless synthesis |
| **Interview Mode** | Vague ideas -> Concrete specs | Stops guessing, forces decisions |
| **Logic/Imp Split** | Process design (Sales, Ops) | You own the *rules*, Agent owns the *form* |
