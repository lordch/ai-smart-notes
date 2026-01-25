# Database Schema Discovery Agent

## Domena
Data / Analytics / Business Intelligence

## Problem klienta
- Odziedziczona baza danych bez dokumentacji
- Nikt nie wie co jest w poszczególnych tabelach
- ERD nie istnieje lub jest nieaktualny
- Nowy analityk spędza tygodnie na "rozpoznaniu terenu"
- Ad-hoc pytania wymagają knowledge transfer od "jedynej osoby która wie"

## Workflow agentowy

1. Agent łączy się z bazą danych (read-only access)
2. Pobiera listę tabel i kolumn (metadata)
3. Dla każdej tabeli:
   - Sample data (TOP 10 rows)
   - Distinct values dla key columns
   - NULL counts, data types
4. Analizuje relacje:
   - Foreign keys (explicit)
   - Naming conventions (implicit: `customer_id` → `customers`)
5. Generuje dokumentację:
   - Plain-language opisy tabel
   - Entity relationships
   - Data dictionary
   - Suggested queries dla common questions

## Przykładowy prompt
```
Connect to the database and create documentation:

1. List all tables with row counts
2. For each table:
   - Describe what it likely contains based on column names and sample data
   - Identify primary key and foreign keys
   - Note any unusual patterns (all NULLs, single value, etc.)
3. Map relationships between tables
4. Create plain-language summary: "This database tracks..."
5. Generate example queries for:
   - "Show me all orders for customer X"
   - "What's the revenue by month?"
   - "Which products are most popular?"

Output as markdown documentation with ERD diagram (mermaid).
```

## Before / After
| Manual | Z agentem |
|--------|-----------|
| Tygodnie na "poznanie" bazy | Godziny na dokumentację |
| Tribal knowledge w głowach | Written documentation |
| Każdy nowy analityk od zera | Onboarding w minuty |
| "Zapytaj Marka, on wie" | Self-service docs |
| Guessing co tabela zawiera | Sample data + descriptions |

## ROI / Metryki
- Onboarding time: tygodnie → godziny
- Knowledge transfer: eliminacja single point of failure
- Query development: szybsze pisanie SQL dzięki zrozumieniu schematu
- Data quality: wykrycie anomalii (empty tables, orphaned records)

## Wymagania wdrożeniowe
- Dane: read-only access do bazy danych
- Narzędzia: Claude Code + database connector
- Complexity: **Medium**
- Security: tylko read access, credentials w .env (nie w CLAUDE.md!)

## Przykładowy output
```markdown
# Database: E-commerce Platform

## Overview
This database tracks an e-commerce operation including customers,
orders, products, and inventory.

## Tables

### customers
- **Purpose**: Customer master data
- **Key columns**:
  - `id` (PK)
  - `email` (unique)
  - `created_at`
- **Row count**: 45,231
- **Notes**: ~5% have NULL phone numbers

### orders
- **Purpose**: Order transactions
- **Key columns**:
  - `id` (PK)
  - `customer_id` (FK → customers)
  - `status` (enum: pending, shipped, delivered, cancelled)
  - `total_amount`
- **Row count**: 128,456

## Relationships
- customers 1:N orders (customer_id)
- orders N:M products (via order_items)
- products N:1 categories (category_id)
```

## Warianty / Rozszerzenia
- Automated data dictionary updates (scheduled refresh)
- Data quality checks: "Te kolumny mają >50% NULLs"
- Query builder: natural language → SQL
- Change detection: "Te tabele zmieniły się od ostatniego sprawdzenia"
- Lineage tracking: "Skąd pochodzą dane w tej tabeli?"

## Failure Modes (uwaga!)
- Brak read access → agent nie może pracować
- Huge tables → sampling zamiast full scan
- Sensitive data (PII) → maskowanie w sample output
- Misinterpretation → zawsze human verification

## Źródło
[Matt Stockton - How I Build Dashboards Now with Claude Code](https://mattstockton.com/2026/01/06/custom-dashboards-with-claude-code.html)
[Matt Stockton - Claude Code Posts](../literature/Matt%20Stockton%20-%20Claude%20Code%20Posts.md)
