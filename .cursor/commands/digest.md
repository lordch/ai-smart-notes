# /digest - AI Intelligence Digest

## Usage

```
/digest              # Full daily digest with analysis
/digest scan         # Quick scan (high priority only, no deep analysis)
/digest project:X    # Filter by project (lawly, consulting)
/digest topic:X      # Filter by topic cluster
/digest --date X     # Historical mode (YYYY-MM-DD)
/digest --days N     # Include N days back (default: 0 = single day)
```

## Description

Generate a daily digest of AI-related content with deep analysis:
- Blog posts from key people (Mollick, Karpathy, Willison, Nate Jones)
- News from tech sites (Ars, TechCrunch)
- Podcasts (Latent Space, AI Daily Brief, Vanishing Gradients)
- Extended research via WebSearch
- **Verification of each item against user's research topics**

## Agent Workflow

When user invokes `/digest`:

### 1. Run RSS Script (baseline)

```bash
venv/bin/python .cursor/skills/digest/digest.py --date YYYY-MM-DD --days 1 -v
```

This fetches RSS sources and generates initial report.

### 2. Expand with WebSearch

Search for additional content:
```
WebSearch: "context engineering" AI agents 2026
WebSearch: "human-agent collaboration" AI workflow 2026
WebSearch: AI adoption enterprise challenges 2026
WebSearch: "from:@emollick" site:x.com (for Twitter)
```

### 3. Verify & Analyze Each Item

For each item found, use WebFetch to read full content and assess:

| Score | Criteria | Action |
|-------|----------|--------|
| **BARDZO WYSOKA** | Matches user's framework (Human-Agent Collaboration, Context Engineering) | Must-read |
| **WYSOKA** | Relevant data/research for consulting | Worth reading |
| **ŚREDNIA** | Interesting but not actionable | Note key points |
| **NISKA** | General news, skip | Skip |

**User's core topics:**
- Human-Agent Collaboration
- Context Engineering
- AI Adoption / Enterprise AI
- AI Workspace / Agentic Workflows

### 4. Generate Analysis Report

Save to `digest/reports/YYYY-MM-DD-analysis.md`:
- Verification table (link, relevance, verdict)
- Key insights extracted
- Actionable items
- Must-read recommendations

### 5. Present Summary

Show user:
- Must-read items (2-3 max)
- Key insights/quotes
- Relevance to their projects
- Suggested actions (save to literature/, add to concepts/)

## Output Files

- `digest/reports/YYYY-MM-DD.md` — raw digest from RSS
- `digest/reports/YYYY-MM-DD-analysis.md` — verified analysis with recommendations

## Configuration

- `digest/config.yaml` - Settings, tier schedule, topic-project mapping
- `digest/sources/people.yaml` - People (Mollick, Willison, Nate Jones, etc.)
- `digest/sources/news.yaml` - News sites
- `digest/sources/podcasts.yaml` - Podcasts
- `digest/topics.yaml` - Topic clusters for WebSearch

## See Also

- `/add-source` - Add new source to monitor
- `/sources` - List and manage sources
- `.cursor/skills/digest/SKILL.md` - Full skill documentation
