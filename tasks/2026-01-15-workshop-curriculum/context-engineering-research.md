# Context Engineering — Research Notes

Pogłębiony research nt. typów i koncepcji context engineeringu. Jak ludzie to kategoryzują w branży i akademii.

---

## 1. DEFINICJA I GENEZA

**Context Engineering** to dyscyplina projektowania dynamicznych systemów dostarczających właściwe informacje i narzędzia, we właściwym formacie, we właściwym czasie, aby LLM mógł wykonać zadanie.

Termin spopularyzowany w połowie 2025 przez Tobiasa Lütke (CEO Shopify): *"Opisuje kluczową umiejętność lepiej: sztukę dostarczania całego kontekstu potrzebnego do rozwiązania zadania przez LLM."*

**Różnica vs Prompt Engineering:**
- **Prompt Engineering** → crafting pojedynczych instrukcji
- **Context Engineering** → architektura całego środowiska informacyjnego agenta

Kluczowy cytat (Anthropic): *"Find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."*

---

## 2. TAXONOMIA KONTEKSTU (7-8 Komponentów)

| Komponent | Opis |
|-----------|------|
| **System Prompt/Instructions** | Wytyczne behawioralne, reguły, przykłady |
| **User Input** | Bezpośrednie zapytanie/zadanie |
| **Short-term Memory** | Historia konwersacji (chat history) |
| **Long-term Memory** | Wiedza persistentna między sesjami |
| **Retrieved Information (RAG)** | Dane z zewnętrznych źródeł |
| **Available Tools** | Definicje funkcji/narzędzi |
| **Tool Responses** | Wyniki wykonanych akcji |
| **Structured Output** | Specyfikacje formatu odpowiedzi |

### Taxonomia z arXiv Survey (2507.13334)

Trzy foundational components:
1. **Context Retrieval and Generation** — prompt-based generation, external knowledge acquisition (CoT, RAG, Cognitive Prompting)
2. **Context Processing** — long sequence processing, self-refinement, structured information integration
3. **Context Management** — memory hierarchies, compression, optimization

System implementations:
- RAG systems
- Memory systems + tool-integrated reasoning
- Multi-agent systems

---

## 3. PROBLEMY (Failure Modes)

### Context Rot
Degradacja performance LLM w miarę wypełniania okna kontekstowego, nawet gdy limity nie są przekroczone.

- **Effective context window** << **Advertised window** (często <256k dla modeli z 200k+)
- Model z 200k tokenów reliable tylko do ~130k
- Nagłe performance drops, nie gradual degradation
- Badania Chroma pokazują non-uniform degradację nawet na prostych zadaniach

### Context Pollution
Za dużo irrelevantnej, redundantnej lub sprzecznej informacji rozpraszającej LLM.

### Context Confusion
LLM nie rozróżnia instrukcji od danych od markerów strukturalnych. Pojawia się przy 100+ narzędziach — model halucynuje parametry lub wywołuje złe narzędzie.

### Attention Dilution
Zero-sum problem: attention rozprasza się na więcej tokenów. Przy 10M tokenów pojedyncze zdanie staje się statystycznie nieistotne. Meta AI: "każdy irrelevant document kradnie attention od relevant ones."

### Lost in the Middle
U-shaped performance: modele najlepiej radzą sobie z informacją na początku i końcu kontekstu.

- Stanford research: accuracy spada z 70-75% do 55-60% dla środkowych pozycji
- Root cause: Rotary Position Embedding (RoPE) wprowadza long-term decay
- Mitigation: Ms-PoE (Multi-scale Positional Encoding), strategic information placement

---

## 4. STRATEGIE ZARZĄDZANIA (4 Główne)

### A) Context Offloading (Przenoszenie na zewnątrz)

- Zapisywanie do plików/baz danych zamiast trzymania w kontekście
- Manus: file system jako "unlimited external memory" — **100:1 compression ratio**
- Przekazywanie tylko referencji (URL, ścieżki plików)
- "The model learns to write to and read from files on demand"

### B) Context Reduction (Kompresja)

| Technika | Typ | Opis |
|----------|-----|------|
| **Compaction** | Reversible | Usuwanie redundancji istniejących w środowisku (np. kod → ścieżka pliku) |
| **Summarization** | Lossy | Streszczanie historii przez LLM przy threshold (np. 128k tokenów) |
| **Observation Masking** | Hybrid | Zastępowanie starych tool outputs placeholderem ("Previous 8 lines omitted") |

**Hierarchia preferencji:** Raw > Compaction > Summarization

JetBrains Research: observation masking redukuje koszty o ~50% bez degradacji performance. "Simple observation masking is as efficient as LLM summarization."

### C) Context Retrieval (Dynamiczne pobieranie)

- **Just-in-Time**: pobieranie tylko gdy potrzebne, nie pre-loading
- **RAG**: semantic search, chunking strategies
- **Multi-technique retrieval**: embeddings + grep + knowledge graphs + AST parsing (Windsurf: 3x better retrieval accuracy)

### D) Context Isolation (Separacja)

- Sub-agenci z własnymi oknami kontekstowymi
- Każdy subagent zwraca condensed summary (1-2k tokenów)
- "Share context by communicating, not by sharing memory"
- Best for: parallelizable, "read-only" tasks like research

---

## 5. ARCHITEKTURY PAMIĘCI

### MemGPT / Letta — Hierarchia OS-style

Inspiracja systemami operacyjnymi (Andrej Karpathy: "LLMs as a new kind of operating system"):

```
┌─────────────────────────────────────────┐
│         MAIN CONTEXT (RAM)              │
├──────────┬──────────┬───────────────────┤
│ System   │ Working  │ Conversational    │
│ Instruct.│ Context  │ Context (FIFO)    │
│ (pinned) │(scratch- │                   │
│          │ pad)     │                   │
├──────────┴──────────┴───────────────────┤
│       EXTERNAL CONTEXT (Disk)           │
├──────────────────┬──────────────────────┤
│  Recall Storage  │  Archival Storage    │
│  (searchable     │  (vector DB,         │
│   history)       │   long-term)         │
└──────────────────┴──────────────────────┘
```

Komponenty:
- **Core Memory** — always-accessible compressed essential facts
- **Recall Memory** — searchable database, semantic search
- **Archival Memory** — long-term storage, vector DB

### Scratchpad Pattern

Working memory zapisywana na zewnątrz:
- Agent zapisuje intermediate results do pliku/state
- Manus: **todo.md jako attention mechanism** — ciągłe przepisywanie listy zadań utrzymuje focus
- "By constantly rewriting the todo list, Manus is reciting its objectives into the end of the context"

---

## 6. MULTI-AGENT PATTERNS

| Pattern | Opis | Context Strategy |
|---------|------|------------------|
| **Orchestrator-Worker** | Lead agent + specialized subagents | Each subagent: fresh context, returns summary |
| **Hierarchical** | Recursive orchestration | Context isolation per level |
| **Group Chat** | Shared conversation thread | Shared context, expensive KV-cache |
| **Swarm** | Decentralized, shared memory space | Memory-based coordination |

**Kluczowa zasada:** Shared context = expensive dependency. Minimalizuj.

### Hierarchical Action Space (Manus)

Problem: 100+ tools → context confusion, hallucinations

Rozwiązanie — 3 poziomy:
- **Level 1 (Atomic)**: ~20 core tools (file_write, browser_navigate, bash, search)
- **Level 2 (Sandbox Utilities)**: General-purpose tools with CLI commands
- **Level 3 (Code/Packages)**: Libraries handling complex logic chains

---

## 7. TECHNIKI RAG/CHUNKING

| Strategia | Opis |
|-----------|------|
| **Fixed-size** | Stały rozmiar chunks + overlap |
| **Recursive** | Hierarchiczne separatory (paragraphs → sentences → words) |
| **Semantic** | Grupowanie po similarity embeddings |
| **Agentic** | LLM decyduje o podziale na podstawie meaning + structure |
| **Hierarchical** | Multi-level hierarchia zachowująca strukturę dokumentu |

**Trade-off:** Smaller chunks = better retrieval accuracy, lost context. Larger chunks = preserved meaning, more noise.

Research: 64-128 tokens dla factual queries, 512-1024 dla narrative/reasoning.

---

## 8. OPTYMALIZACJE INFRASTRUKTURALNE

### KV Cache

- Cachowanie key-value computations między inference calls
- Kompromis: memory vs compute
- Bottleneck dla long-context applications

### Prefix Caching

- Reuse KV cache dla wspólnych prefixów
- Anthropic Claude: do 90% cost savings, 85% latency reduction
- Cached tokens: $0.30/M vs uncached: $3/M (10x różnica)

### PagedAttention (vLLM)

- Virtual memory pages dla KV storage
- Eliminacja fragmentation (70% → <4%)
- Do 24x higher throughput

### Scaling Guidelines

| Context Size | Strategy |
|--------------|----------|
| <10k tokens | Simple append-only + basic caching |
| 10k-50k | Compression at boundaries + KV-cache optimization |
| 50k-100k | Offloading to external memory + smart retrieval |
| >100k | Multi-agent isolation architecture |

---

## 9. BEST PRACTICES (Synteza)

1. **Monitor pre-rot thresholds** — trigger compaction przed degradacją
2. **Hierarchical Action Space** — ~20 core tools, nie 100+
3. **File system as memory** — persistence + unlimited size
4. **todo.md pattern** — external attention anchor
5. **KV-cache hit rate jako główna metryka** — 10x cost difference cached vs uncached
6. **Observation masking before summarization** — simpler, often equally effective
7. **Position-aware information placement** — critical info na początku/końcu
8. **Prefer raw > compaction > summarization** — tylko gdy poprzednie wyczerpane
9. **Embrace iterative simplification** — performance gains from removing complexity
10. **Agent-as-Tool** — specialized agents as deterministic functions, not conversational entities

---

## Kluczowe Źródła

- [Anthropic: Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Phil Schmid: Context Engineering Part 1](https://www.philschmid.de/context-engineering) & [Part 2](https://www.philschmid.de/context-engineering-part-2)
- [Chroma: Context Rot Research](https://research.trychroma.com/context-rot)
- [Manus: Lessons from Building](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [JetBrains: Observation Masking Research](https://blog.jetbrains.com/research/2025/12/efficient-context-management/)
- [arXiv: Survey of Context Engineering (2507.13334)](https://arxiv.org/abs/2507.13334)
- [LlamaIndex: Context Engineering Techniques](https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider)
- [Stanford: Lost in the Middle](https://arxiv.org/abs/2307.03172)
- [MemGPT Paper](https://arxiv.org/abs/2310.08560)
- [Letta: Agent Memory](https://www.letta.com/blog/agent-memory)
- [Redis: Context Rot Explained](https://redis.io/blog/context-rot/)
- [Galileo: Deep Dive Context Engineering](https://galileo.ai/blog/context-engineering-for-agents)
