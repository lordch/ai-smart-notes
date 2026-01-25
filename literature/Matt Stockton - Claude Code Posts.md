# Matt Stockton - Claude Code Posts

Seria postów blogowych o używaniu Claude Code do pracy nie-kodowej. Matt Stockton jest konsultantem, który używa Claude Code jako "knowledge management system" i "local AI agent".

## Źródło
- Blog: https://mattstockton.com
- Pełna lista postów: https://mattstockton.com/writing.html

## Kluczowy insight

> *"Claude Code runs locally and can see all your files"* — to nie jest tool do kodu, to **local AI agent z dostępem do systemu plików**.

Stockton używa Claude Code głównie do:
- Zarządzania wiedzą i dokumentacją klientów
- Voice-to-document workflows
- Interaktywnych dashboardów
- Debugowania i development

## Posty o Claude Code

| Data | Tytuł | URL | Use case'y |
|------|-------|-----|------------|
| Jan 7, 2026 | How I Use Claude Code for Non-Technical Work | [link](https://mattstockton.com/2026/01/07/claude-code-for-non-technical-work.html) | Knowledge mgmt, voice-to-doc, email drafting, status updates |
| Jan 6, 2026 | How I Build Dashboards Now with Claude Code | [link](https://mattstockton.com/2026/01/06/custom-dashboards-with-claude-code.html) | Interactive dashboards, exploratory analysis, schema discovery |
| Jan 1, 2026 | Using Claude Code to Debug Code You Didn't Write | [link](https://mattstockton.com/2026/01/01/using-claude-code-to-debug-third-party-library-code.html) | Third-party library debugging |
| Oct 17, 2025 | Claude Skills: Organization for Agent Instructions | [link](https://mattstockton.com/2025/10/17/claude-skills-better-organization-for-agent-instructions.html) | Reusable commands, workflow organization |
| Sep 19, 2025 | How Claude Code Became My Knowledge Management System | [link](https://mattstockton.com/2025/09/19/how-claude-code-became-my-knowledge-management-system.html) | CLAUDE.md, work logs, compounding knowledge |
| Jun 21, 2025 | AI Coding Tools Amplify What You Already Know | [link](https://mattstockton.com/2025/06/21/ai-coding-tools-amplify-what-you-already-know.html) | ML pipelines, multi-file changes, audio prompts |
| Jun 14, 2025 | AI Coding Tools: Why I Use Claude Code | [link](https://mattstockton.com/2025/06/14/ai-coding-tools-journey.html) | ML pipelines, presentations, prototyping |

## Powiązane posty

| Data | Tytuł | URL | Temat |
|------|-------|-----|-------|
| Jan 3, 2026 | Four Building Blocks for Document Generation Agents | [link](https://mattstockton.com/2026/01/03/four-building-blocks-for-document-generation-agents.html) | Document synthesis |
| Nov 25, 2025 | How I Prototype Agentic Workflows Before Writing Code | [link](https://mattstockton.com/2025/11/25/how-i-prototype-agentic-workflows.html) | Workflow prototyping, slash commands |
| Nov 24, 2025 | Tool Calling and Understanding AI More Deeply | [link](https://mattstockton.com/2025/11/24/tool-calling-and-the-value-of-understanding-ai-more-deeply.html) | Tool calling patterns |
| Dec 29, 2025 | Tool Calling and File Access | [link](https://mattstockton.com/2025/12/29/why-tool-calling-and-file-system-access-matter.html) | File system access |

## Główne tematy

### 1. Knowledge Management System
Stockton używa Claude Code jako systemu zarządzania wiedzą:
- **CLAUDE.md** — preferencje klienta, styl komunikacji, guidelines
- **Work logs** — automatyczne dzienniki pracy z każdej sesji
- **Git history** — commit messages jako persistent memory
- **Compounding effect** — każda sesja buduje na poprzedniej

### 2. Voice-to-Document Pipeline
Workflow: nagranie audio → transcript → ustrukturyzowany dokument
- Meeting summaries (komenda `/meeting-summary`)
- Requirements documents z "brain dumps"
- Email drafting z dyktowania
- Czas: 5 min vs 30 min manualnie

### 3. Interactive Dashboards
Budowanie dashboardów Streamlit dla small/medium business:
- Automatyzacja manualnych raportów
- Exploratory data analysis (pandas, outliers)
- Database schema discovery
- Filtrowanie i drill-down

### 4. Development & Debugging
- Debugging third-party libraries (analiza pip packages)
- ML pipelines z cross-validation
- Multi-file code changes
- Prototypowanie

### 5. Claude Skills / Reusable Commands
Organizacja instrukcji agenta:
- Konwersja ad-hoc workflow → slash command (markdown)
- Centralne repozytorium capabilities
- Code review workflows, document templates, git patterns

## Cytowane w use case'ach
- [knowledge-management-system.md](../use-cases/knowledge-management-system.md)
- [database-schema-discovery.md](../use-cases/database-schema-discovery.md)
- [third-party-debugging.md](../use-cases/third-party-debugging.md)
- [claude-skills-reusable-commands.md](../use-cases/claude-skills-reusable-commands.md)
- [document-synthesis.md](../use-cases/document-synthesis.md)
- [ml-pipeline-building.md](../use-cases/ml-pipeline-building.md)
- [meeting-notes-to-actions.md](../use-cases/meeting-notes-to-actions.md) (wzbogacony)
- [automated-monthly-reports.md](../use-cases/automated-monthly-reports.md) (wzbogacony)
