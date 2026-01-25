# AI Digest

Personal AI intelligence feed - codzienny przegląd wydarzeń, trendów i badań w obszarze AI, uruchamiany z Claude Code.

## Cel

Zbudować system który:
- Agreguje informacje z wybranych źródeł (blogi, Twitter, raporty, papery)
- Filtruje przez pryzmat moich zainteresowań i projektów
- Generuje actionable daily digest
- Akumuluje wiedzę w knowledge graph (faza 2)

## Architektura

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CONFIG    │────▶│  RESEARCH   │────▶│   REPORT    │
│  (sources,  │     │  (search,   │     │  (daily     │
│   topics)   │     │   extract)  │     │   output)   │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ KNOWLEDGE   │  ← faza 2
                    │   GRAPH     │
                    └─────────────┘
```

**Interfejs:** Claude Code custom command `/digest`

**Storage:**
```
~/ai-digest/
├── config.yaml           # źródła, tematy, priorytety
├── reports/
│   └── YYYY-MM-DD.md     # daily outputs
├── graph.db              # Neo4j (faza 2)
└── notes/                # unstructured elaboration
```

---

## Config Layer

### Source Types

| Typ | Przykłady | Strategia fetchu |
|-----|-----------|------------------|
| **Blog** | Mollick, Torres, Willison | `site:domain.com` + date filter |
| **Twitter/X** | Karpathy, innych | `@handle topic` (ograniczone) |
| **Reports** | KPMG, BCG, McKinsey | `[org] AI report [year]` periodic |
| **Academic** | ArXiv, Scholar | `[topic] site:arxiv.org` |
| **News** | Ars, TechCrunch, Wired | `AI [topic] site:domain` |
| **Newsletter** | Import/forward | Manual add lub inbox parsing |

### Sources (initial list)

```yaml
people:
  ethan-mollick:
    name: Ethan Mollick
    blog: oneusefulthing.org
    twitter: emollick
    topics: [ai-adoption, ai-education, organizational-change]
    priority: high
    
  andrej-karpathy:
    name: Andrej Karpathy
    twitter: karpathy
    youtube: true
    topics: [llm-internals, agent-architectures, ai-engineering]
    priority: high
    
  teresa-torres:
    name: Teresa Torres
    blog: producttalk.org
    topics: [product-discovery, continuous-discovery, ai-product]
    priority: medium
    
  simon-willison:
    name: Simon Willison
    blog: simonwillison.net
    topics: [llm-tools, prompt-engineering, ai-ethics]
    priority: medium

organizations:
  - id: kpmg
    type: consulting
    search: "KPMG AI report"
    frequency: monthly
    
  - id: bcg
    type: consulting  
    search: "BCG artificial intelligence"
    frequency: monthly
    
  - id: mckinsey
    type: consulting
    search: "McKinsey AI"
    frequency: monthly

news_sources:
  - arstechnica.com
  - techcrunch.com
  - wired.com
  - theverge.com
```

### Topic Clusters

```yaml
context-engineering:
  description: "Zarządzanie kontekstem w AI agents, prompt engineering 2.0"
  queries:
    - "context engineering AI"
    - "AI agent memory systems"
    - "prompt engineering 2025"
    - "context window management"
  related: [rag, memory-systems, letta-memgpt]
  project_relevance: [consulting]

ai-agents:
  description: "Architektury agentów, frameworki, praktyczne wdrożenia"
  queries:
    - "AI agent architecture"
    - "LLM agents production"
    - "autonomous AI agents"
  related: [coding-agents, claude-code, tool-use]
  project_relevance: [consulting]

ai-slop:
  description: "Problemy z AI-generated content, failures, quality issues"
  queries:
    - "AI slop"
    - "AI generated content failure"  
    - "LLM hallucination examples"
    - "AI content quality problems"
  related: [content-moderation, detection]
  project_relevance: []

future-of-work:
  description: "Wpływ AI na pracę, produktywność, organizacje"
  queries:
    - "AI jobs impact"
    - "AI productivity study"
    - "AI augmentation work"
    - "AI workforce transformation"
  related: [ai-adoption, organizational-change]
  project_relevance: [consulting]

legal-ai:
  description: "AI w branży prawniczej, compliance, automatyzacja"
  queries:
    - "legal AI tools"
    - "AI law firm"
    - "legal document automation"
    - "AI legal compliance GDPR"
  related: [document-generation, compliance, rag]
  project_relevance: [lawly]

product-discovery:
  description: "AI w product discovery, badania użytkowników"
  queries:
    - "AI product discovery"
    - "AI user research"
    - "continuous discovery AI"
  related: [teresa-torres-method]
  project_relevance: [consulting]
```

### Projects (lenses)

```yaml
lawly:
  status: exploratory
  description: "Legal AI platform for Polish small law firms"
  key_questions:
    - "Jak RODO wpływa na legal AI w Polsce?"
    - "Czy RAG wystarczy dla polskiego prawa?"
    - "Jaki jest market size dla małych kancelarii?"
  watch_concepts: [legal-ai, compliance, document-generation, rag]

consulting:
  status: active
  description: "AI workspace readiness consulting for Polish companies"
  key_questions:
    - "Jakie są best practices AI implementation?"
    - "Jak mierzyć AI readiness?"
    - "Case studies udanych wdrożeń?"
  watch_concepts: [ai-adoption, context-engineering, enterprise-ai, future-of-work]
```

---

## Research Layer

### Search Budget & Prioritization

**Constraint:** ~15-20 web searches per run

**Tier system:**

```yaml
tier_1_daily:
  description: "Always fetch, highest signal"
  budget: 6-8 searches
  sources:
    - mollick_blog
    - karpathy_twitter
    - "AI news today"
    - one rotating topic cluster

tier_2_rotating:
  description: "Rotate through week"
  budget: 4-6 searches
  schedule:
    monday: [context-engineering, ai-agents]
    tuesday: [future-of-work, legal-ai]
    wednesday: [ai-slop, product-discovery]
    thursday: [academic papers]
    friday: [consulting reports]
    weekend: [catch-up, deep dives]

tier_3_weekly:
  description: "Periodic checks"
  budget: 2-4 searches
  sources:
    - kpmg_bcg_mckinsey (1x/week)
    - arxiv_scan (2x/week)
```

### Extraction Schema

Per znaleziony item, extract:

```yaml
source_record:
  id: string                    # generated, for dedup
  url: string
  title: string
  author: string | null
  author_id: string | null      # link to person entity
  date: date
  source_type: enum
    - blog_post
    - tweet
    - thread
    - paper
    - report
    - news_article
  original_source: string       # domain

content:
  summary: string               # 2-3 sentences, essence
  key_claims:                   # atomic extractable statements
    - text: string
      concepts: [string]        # linked concept IDs
      evidence_type: enum
        - opinion
        - anecdotal
        - research_cited
        - data_presented
      
relevance:
  topic_clusters: [string]      # which of my clusters
  projects: [string]            # lawly, consulting, etc.
  priority: enum
    - high      # directly actionable or significant
    - medium    # worth reading
    - low       # radar only
  relevance_note: string        # why this matters (one-liner)

metadata:
  fetched_at: datetime
  search_query: string          # what query found this
  digest_date: date             # which daily digest
```

### Deduplication

```yaml
dedup_rules:
  - same URL → skip
  - same title + author + date → skip
  - similar title (fuzzy >0.9) + same date → flag for review
```

---

## Report Layer

### Daily Output Format

```markdown
# AI Digest [YYYY-MM-DD]

> [Day of week]. Topics: [today's focus areas]. Sources checked: [N].

---

## 🔥 High Priority

Items requiring attention or directly relevant to active projects.

### [Title](url)
**[Author]** · [source_type] · [date]

[Summary - 2-3 sentences]

**Key claims:**
- [Claim 1] `[evidence_type]`
- [Claim 2] `[evidence_type]`

**Relevant for:** [topic_clusters] · Projects: [projects]
**Why it matters:** [relevance_note]

---

## 📚 Worth Reading

Interesting items worth deeper look when time permits.

- **[Title](url)** ([author], [source_type])  
  [One-line summary]. → [topics]

- **[Title](url)** ([author], [source_type])  
  [One-line summary]. → [topics]

---

## 📡 Radar

Tracked but not urgent. For awareness.

- [Title](url) - [one-liner]
- [Title](url) - [one-liner]
- [Title](url) - [one-liner]

---

## 🎯 Project Relevance

### Lawly
- [N] items today
- Notable: [specific item if high relevance]

### Consulting  
- [N] items today
- Notable: [specific item if high relevance]

---

## 📊 Stats

- Sources checked: [N]
- Items found: [N]
- High priority: [N]
- New concepts detected: [list if any]

---

## 🔗 Full Source Log

<details>
<summary>All [N] items found today</summary>

| Title | Author | Type | Topics | Priority |
|-------|--------|------|--------|----------|
| [...](url) | ... | ... | ... | ... |

</details>
```

### Report Variants

```yaml
formats:
  full:
    description: "Complete daily digest"
    sections: all
    use_when: "default, morning review"
    
  scan:
    description: "Quick overview"
    sections: [high_priority, project_relevance, stats]
    use_when: "busy day, quick check"
    
  project:
    description: "Filtered by project"
    parameter: project_id
    sections: [items relevant to project only]
    use_when: "focused work on specific project"
    
  topic:
    description: "Filtered by topic cluster"
    parameter: topic_id
    sections: [items in topic only]
    use_when: "deep dive on topic"
```

---

## Implementation Plan

### Phase 1: MVP (current focus)

1. **Config file** - YAML z sources i topics
2. **Research command** - `/digest` wykonuje searches, extracts, generates report
3. **Report output** - Markdown file w `reports/`

Deliverables:
- `config.yaml` 
- `.claude/commands/digest.md`
- Working daily digest generation

### Phase 2: Knowledge Graph

1. **Neo4j setup** - Docker local
2. **Schema** - Nodes: Person, Concept, Source, Claim, Project
3. **Update pipeline** - Digest results → MERGE statements
4. **Query interface** - `/graph` command

### Phase 3: Intelligence

1. **Trend detection** - "X is being discussed more"
2. **Connection discovery** - "Mollick and Karpathy both mention Y"
3. **Gap identification** - "No recent sources on Z"
4. **Weekly synthesis** - Higher-level patterns

---

## Open Questions

- [ ] Twitter/X access - how reliable via web search?
- [ ] Newsletter integration - forward to parseable format?
- [ ] Report review time - 5min scan vs 15min analytical?
- [ ] Claim extraction - now or defer to Phase 2?
- [ ] My notes/reactions - inline in report or separate?

---

## Appendix: Concept Taxonomy (starter)

```
ai-technical/
├── agents/
│   ├── architectures
│   ├── memory-systems
│   │   ├── context-engineering
│   │   ├── rag
│   │   └── letta-memgpt
│   └── tool-use
├── llm/
│   ├── prompting
│   ├── fine-tuning
│   └── evaluation
└── coding/
    └── claude-code

ai-impact/
├── future-of-work/
│   ├── productivity
│   ├── job-displacement
│   └── augmentation
├── content/
│   ├── ai-slop
│   └── detection
└── adoption/
    ├── enterprise
    └── organizational-change

ai-verticals/
├── legal/
│   ├── document-automation
│   └── compliance
└── product/
    └── discovery

business/
├── consulting/
│   └── ai-readiness
└── reports/
    ├── kpmg
    ├── bcg
    └── mckinsey
```
