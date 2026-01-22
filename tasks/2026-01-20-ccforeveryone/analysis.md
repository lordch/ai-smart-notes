# Analysis of ccforeveryone.com for "Agentic Work" Course

**Source**: [ccforeveryone.com](https://ccforeveryone.com) (Claude Code for Everyone)
**Goal**: Adapt technical agent workflows for general knowledge work.

## Core Philosophy: "Learn by Doing" in the Agent's Environment
The course is unique because it is taught *inside* the agent interface.
**Transferable Principle**: Don't teach "about" agents; teach *with* agents.
- **Action**: Create a "Course Agent" prompt that users paste into their LLM. This agent then guides them through the curriculum interactively.
- **Why**: It reduces the "blank page" paralysis and proves value immediately.

---

## 5 Key Concepts & Transferable Heuristics

### 1. Project Memory (`CLAUDE.md`) -> "The Context File"
**Technical context**: A file named `CLAUDE.md` at the root of a project tells the agent about the project structure, conventions, and rules.
**Transferable Task**: **"Create Your Agent Readme"**
- **Concept**: Every major recurring task or project needs a "Context File".
- **Instruction**: "Create a file named `AGENT_CONTEXT.md` in your project folder. Write down:
    1.  What is the goal of this project?
    2.  Who is the audience?
    3.  What are the 'forbidden' things (e.g., 'never use passive voice')?
    4.  What are the required steps for every output?"
- **Heuristic**: "If you have to repeat an instruction twice, it belongs in the Context File."

### 2. File Operations (`@`) -> "Direct Source Access"
**Technical context**: Using `@filename` to give Claude read access to code.
**Transferable Task**: **"The Multi-Doc Synthesis"**
- **Concept**: Agents shine when they can "see" multiple specific sources at once.
- **Example**: "Don't copy-paste text. Instead, attach the files (PDFs, Docs) and refer to them by name: 'Compare the argument in @proposal_v1.pdf with the budget in @Q2_financials.xlsx'."
- **Rule of Thumb**: "Never summarize a document yourself for the agent. Give the agent the document and ask *it* to extract what matters."

### 3. Parallel Agents -> "The Assembly Line"
**Technical context**: Running multiple terminal instances to let agents work on different files simultaneously.
**Transferable Task**: **"The Research-Draft Loop"**
- **Concept**: Split work into "Thinking" and "Doing" streams.
- **Example**:
    - **Agent 1 (Researcher)**: "Find 5 statistics about remote work trends in 2024. Just list facts with sources."
    - **Agent 2 (Writer)**: "Take these statistics (paste from Agent 1) and write an intro paragraph."
- **Heuristic**: "Don't ask the same chat session to switch contexts deeply (e.g., from deep research to creative writing). Start a fresh chat or use a separate window."

### 4. Custom Sub-Agents -> "Expert Personas"
**Technical context**: Configuring specific "tools" or profiles for different coding tasks (e.g., a "Test Writer").
**Transferable Task**: **"The Board of Advisors"**
- **Concept**: Create specific instruction sets that "mod" the agent into a specialist.
- **Example**: **"The Editor Persona"**
    - "You are a ruthless editor. Your only job is to shorten text by 30% without losing meaning. Do not be polite. Just output the shortened text."
- **Instruction**: "Define 3 'Employees' you can hire instantly: The Critic, The Summarizer, and The Idea Generator. Write a snippet for each."

### 5. Vibe Coding -> "Outcome-Oriented Delegation"
**Technical context**: Describing the "vibe" or high-level behavior of a web app and letting the agent figure out the code.
**Transferable Task**: **"Describe the Destination, Not the Route"**
- **Concept**: Focus on the *user experience* of the result, not the steps to get there.
- **Example (Slide Deck)**:
    - *Bad*: "Add a bullet point here, then an image, then a title."
    - *Good*: "Make this slide feel urgent and data-heavy. It needs to convince the CFO that we are bleeding money."
- **Heuristic**: "If you are micro-managing the *format*, you are under-utilizing the agent's reasoning. Describe the *impact* you want first."

---

## Specific Syllabus Ideas for "Agentic Work"
Based on the `ccforeveryone` structure (Fundamentals -> Vibe -> Advanced):

1.  **Module 1: The Environment**
    - **Task**: Set up the "Context File" for your life/work.
    - **Outcome**: A reusable `ME.md` or `WORK.md` file you attach to every session.
2.  **Module 2: Direct Manipulation**
    - **Task**: "The 3-File Challenge". Give the agent 3 disparate documents (an email, a report, a meeting note) and ask for a synthesis.
    - **Outcome**: Understanding that agents are *connectors* of information.
3.  **Module 3: The Manager Mindset**
    - **Task**: "Hire" a sub-agent to critique your own work.
    - **Outcome**: Shifting from "doing" to "reviewing".

## Rules of Thumb (Meta-Level)
- **"The 15-Minute Rule"**: If you can't get the agent to do it in 15 minutes, you are likely explaining the *how* instead of the *what*.
- **"Memory over Prompting"**: Invest time in writing the context file (Memory) once, rather than perfecting the prompt every time.
- **"Show, Don't Just Tell"**: Just like `ccforeveryone` uses a split screen to show the file changing, non-coders should have the relevant document open *alongside* the chat to verify changes instantly.
