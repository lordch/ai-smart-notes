# Skill: AI Digest

## Purpose

Generate a daily digest of AI-related content from monitored sources using multiple strategies (RSS, WebSearch, YouTube, etc.).

## When to Use

- User invokes `/digest` command
- User wants to catch up on AI news
- User asks "co nowego w AI?" / "what's new in AI?"

---

## Agent Workflow

### 1. Load Sources

Read source configs from `digest/sources/`:
- `people.yaml` — key people to monitor
- `news.yaml` — news sites
- `podcasts.yaml` — podcasts
- `custom.yaml` — user-added sources

### 2. Fetch by Strategy

For each source, use the appropriate strategy:

#### Strategy: RSS (primary for blogs)
```bash
venv/bin/python .cursor/skills/digest/digest.py --date YYYY-MM-DD --days 0
```

Use for: Blogs with RSS feeds (Mollick, Willison, Torres, news sites)

#### Strategy: WebSearch (for Twitter, topics, recent news)
Use WebSearch tool directly:
```
WebSearch: "from:@emollick" site:x.com
WebSearch: "Ethan Mollick" AI site:oneusefulthing.org after:2026-01-20
WebSearch: "context engineering" AI 2026
```

Use for: Twitter/X, topic monitoring, sources without RSS

#### Strategy: YouTube (for video creators)
1. WebSearch for recent videos:
   ```
   WebSearch: "Andrej Karpathy" site:youtube.com 2026
   ```
2. If interesting video found, use transcript skill:
   ```bash
   venv/bin/python .cursor/skills/transcripts/get_transcript.py <youtube_url>
   ```

Use for: Karpathy, podcast video versions

#### Strategy: Podcast RSS
Many podcasts have RSS feeds:
- AI Daily Brief: https://feeds.megaphone.fm/GMAYL4628016451
- Latent Space: https://api.substack.com/feed/podcast/1084089.rss
- Vanishing Gradients: https://feeds.fireside.fm/vanishinggradients/rss

### 3. Analyze & Prioritize

For each item found:

**High Priority if:**
- From high-priority source (Mollick, Karpathy)
- Matches active project topics (consulting: ai-agents, context-engineering)
- Breaking news / major announcement

**Medium Priority if:**
- From medium-priority source
- Relevant to watched topics
- Interesting but not urgent

**Low Priority (Radar):**
- General AI news
- Not directly relevant but worth tracking

### 4. Generate Report

Create report in `digest/reports/YYYY-MM-DD.md` with sections:
- High Priority (with full summaries)
- Worth Reading (brief descriptions)
- Radar (links only)
- Project Relevance
- Stats

### 5. Deep Analysis & Verification

**For each item in the report, verify relevance:**

Use WebFetch to read the full article and answer:
1. Does it relate to user's core topics? (Human-Agent Collaboration, Context Engineering, AI Adoption)
2. Is it actionable or just news?
3. Does it contain original insights or just repackaged content?

**Relevance scoring:**

| Score | Criteria | Action |
|-------|----------|--------|
| **BARDZO WYSOKA** | Directly matches user's messaging/framework | Must-read, save to literature/ |
| **WYSOKA** | Relevant research/data for consulting | Worth reading in full |
| **ŚREDNIA** | Interesting but not actionable | Skim, note key points |
| **NISKA** | General news, not relevant | Skip |

**User's core topics (for filtering):**
- Human-Agent Collaboration
- Context Engineering
- AI Adoption / Enterprise AI
- AI Workspace / Agentic Workflows
- Future of Work

### 6. Extended Research

After processing RSS items, expand with WebSearch:

```
WebSearch: "context engineering" AI agents 2026
WebSearch: "human-agent collaboration" AI workflow 2026
WebSearch: AI adoption enterprise challenges 2026
```

Fetch and analyze top results. Look for:
- Industry reports (KPMG, Deloitte, McKinsey)
- Technical guides (Anthropic, LangChain)
- Research papers (ArXiv, Stanford)

### 7. Generate Analysis Report

Save analysis to `digest/reports/YYYY-MM-DD-analysis.md` with:
- Verification table (link, relevance, verdict)
- Key insights extracted
- Actionable items (to read, to note, to concepts)
- Source links

---

## Source Registry

### People (High Value)

| Person | Strategy | URLs |
|--------|----------|------|
| **Ethan Mollick** | RSS + WebSearch | [oneusefulthing.org](https://oneusefulthing.org), [@emollick](https://x.com/emollick) |
| **Andrej Karpathy** | YouTube + WebSearch | [YouTube](https://youtube.com/@AndrejKarpathy), [@karpathy](https://x.com/karpathy) |
| **Simon Willison** | RSS | [simonwillison.net](https://simonwillison.net/atom/everything/) |
| **Nate B Jones** | RSS + WebSearch | [natesnewsletter.substack.com](https://natesnewsletter.substack.com) |
| **Teresa Torres** | RSS | [producttalk.org](https://producttalk.org/feed/) |

### Podcasts

| Podcast | Strategy | Feed |
|---------|----------|------|
| **AI Daily Brief** | RSS | [Apple](https://podcasts.apple.com/us/podcast/the-ai-daily-brief-artificial-intelligence-news/id1680633614) |
| **Latent Space** | RSS + Substack | [latent.space](https://latent.space/podcast) |
| **Vanishing Gradients** | RSS | [Fireside](https://vanishinggradients.fireside.fm/) |

### Newsletters

| Newsletter | Strategy | URL |
|------------|----------|-----|
| **There's An AI For That** | RSS | 2.5M subscribers, daily AI tools |
| **Towards AI** | RSS | [newsletter.towardsai.net](https://newsletter.towardsai.net/) |

### News Sites

| Site | Strategy | RSS |
|------|----------|-----|
| Ars Technica | RSS | feeds.arstechnica.com |
| TechCrunch AI | RSS | techcrunch.com/category/artificial-intelligence/feed/ |
| ArXiv cs.AI | RSS | rss.arxiv.org/rss/cs.AI |

---

## Topic Clusters (for WebSearch)

### context-engineering
```
"context engineering" AI 2026
"context window" management LLM
"RAG" retrieval augmented generation
```

### ai-agents
```
"AI agent" architecture 2026
"autonomous agent" LLM
"Claude Code" OR "Cursor" agent
"agentic" workflow
```

### future-of-work
```
"AI" "future of work" 2026
"AI productivity" study research
"AI augmentation" workforce
```

---

## Example Session

```
User: /digest

Agent:
1. Checking RSS sources via script...
   → Found 5 items from Willison, 2 from Torres

2. Searching Twitter for Mollick...
   WebSearch: "from:@emollick" site:x.com after:2026-01-25
   → Found 3 tweets about AI adoption

3. Checking Karpathy YouTube...
   WebSearch: "Andrej Karpathy" site:youtube.com 2026
   → No new videos this week

4. Searching topic clusters...
   WebSearch: "context engineering" AI 2026
   → Found 2 relevant articles

5. Generating report...
   → Saved to digest/reports/2026-01-26.md

## Summary

**Must-read today:**
- Willison on "Claude's new constitution" - relevant for understanding Claude behavior
- Mollick thread on AI adoption patterns - directly relevant to consulting

**Themes:**
- Growing interest in context engineering
- More discussion of agentic workflows

**For your projects:**
- Consulting: 4 relevant items
- Lawly: 0 items today
```

---

## Helper Script

For RSS sources, use the helper script:

```bash
# Single day
venv/bin/python .cursor/skills/digest/digest.py --date 2026-01-26

# Week back
venv/bin/python .cursor/skills/digest/digest.py --date 2026-01-26 --days 7

# Verbose
venv/bin/python .cursor/skills/digest/digest.py -v
```

The script handles RSS feeds only. Use WebSearch/WebFetch for other sources.

---

## Adding New Sources

When user provides a URL via `/add-source`:

1. **Detect type:**
   - `*.substack.com` → Substack (RSS available)
   - `twitter.com` / `x.com` → Twitter (WebSearch strategy)
   - `youtube.com` → YouTube (WebSearch + transcript)
   - Other → Check for RSS feed

2. **Find RSS:**
   - Try `{domain}/feed`, `{domain}/rss`, `{domain}/atom.xml`
   - For Substack: `{publication}.substack.com/feed`

3. **Propose config:**
   ```yaml
   source-id:
     name: "Source Name"
     type: person|news|podcast|newsletter
     rss: https://...
     twitter: handle (optional)
     topics: [topic1, topic2]
     priority: high|medium|low
     fetch_strategy: rss|websearch|youtube
   ```

4. **Save to appropriate file** in `digest/sources/`

---

## Configuration Files

- `digest/config.yaml` - Main settings, tier schedule
- `digest/sources/people.yaml` - Person sources
- `digest/sources/news.yaml` - News sources
- `digest/sources/podcasts.yaml` - Podcast sources
- `digest/topics.yaml` - Topic clusters for WebSearch

## Dependencies

See `requirements.txt` in this folder.
