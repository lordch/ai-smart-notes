"""
Report generator for AI Digest
"""

from datetime import date
from pathlib import Path


def generate_report(data: dict) -> str:
    """
    Generate markdown report from digest data.

    Args:
        data: Dict containing:
            - date: Target date
            - is_historical: Whether this is historical mode
            - is_scan: Whether this is scan mode (high priority only)
            - project_filter: Optional project filter
            - topic_filter: Optional topic filter
            - high_priority: List of high priority items
            - medium_priority: List of medium priority items
            - low_priority: List of low priority items
            - all_items: All items
            - sources_checked: Number of sources fetched
            - errors: List of error messages
            - config: Full config dict

    Returns:
        Markdown string
    """
    target_date = data['date']
    day_name = target_date.strftime('%A')

    lines = []

    # Header
    header = f"# AI Digest {target_date}"
    if data.get('is_historical'):
        header += " (historical)"
    lines.append(header)
    lines.append("")

    # Meta line
    meta_parts = [day_name]
    if data.get('project_filter'):
        meta_parts.append(f"Project: {data['project_filter']}")
    if data.get('topic_filter'):
        meta_parts.append(f"Topic: {data['topic_filter']}")
    if data.get('is_scan'):
        meta_parts.append("Quick scan")
    meta_parts.append(f"Sources: {data['sources_checked']}")

    lines.append(f"> {'. '.join(meta_parts)}.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # High Priority section
    high_items = data.get('high_priority', [])
    lines.append("## High Priority")
    lines.append("")

    if high_items:
        lines.append("Items requiring attention or directly relevant to active projects.")
        lines.append("")
        for item in high_items:
            lines.extend(_format_item_full(item))
    else:
        lines.append("No high priority items today.")
        lines.append("")

    # Worth Reading section (skip in scan mode)
    if not data.get('is_scan'):
        lines.append("---")
        lines.append("")
        lines.append("## Worth Reading")
        lines.append("")

        medium_items = data.get('medium_priority', [])
        if medium_items:
            lines.append("Interesting items worth deeper look when time permits.")
            lines.append("")
            for item in medium_items:
                lines.extend(_format_item_brief(item))
        else:
            lines.append("No medium priority items.")
            lines.append("")

    # Radar section (skip in scan mode)
    if not data.get('is_scan'):
        lines.append("---")
        lines.append("")
        lines.append("## Radar")
        lines.append("")

        low_items = data.get('low_priority', [])
        if low_items:
            lines.append("Tracked but not urgent. For awareness.")
            lines.append("")
            for item in low_items:
                lines.append(f"- [{item['title']}]({item['url']}) - {item.get('source_name', 'Unknown')}")
            lines.append("")
        else:
            lines.append("No radar items.")
            lines.append("")

    # Project Relevance section
    lines.append("---")
    lines.append("")
    lines.append("## Project Relevance")
    lines.append("")

    all_items = data.get('all_items', [])
    projects_config = data.get('config', {}).get('projects', {})

    for project_id, project_info in projects_config.items():
        project_items = [i for i in all_items if project_id in i.get('projects', [])]
        lines.append(f"### {project_id.title()}")
        lines.append(f"- {len(project_items)} items today")
        if project_items:
            notable = next((i for i in project_items if i.get('priority') == 'high'), None)
            if notable:
                lines.append(f"- Notable: [{notable['title']}]({notable['url']})")
        lines.append("")

    # Stats section
    lines.append("---")
    lines.append("")
    lines.append("## Stats")
    lines.append("")
    lines.append(f"- Sources checked: {data['sources_checked']}")
    lines.append(f"- Items found: {len(all_items)}")
    lines.append(f"- High priority: {len(high_items)}")
    lines.append(f"- Medium priority: {len(data.get('medium_priority', []))}")
    lines.append(f"- Low priority: {len(data.get('low_priority', []))}")
    lines.append("")

    # Errors section (if any)
    errors = data.get('errors', [])
    if errors:
        lines.append("---")
        lines.append("")
        lines.append("## Errors")
        lines.append("")
        for err in errors:
            lines.append(f"- {err}")
        lines.append("")

    # Full source log (collapsible)
    lines.append("---")
    lines.append("")
    lines.append("## Full Source Log")
    lines.append("")
    lines.append("<details>")
    lines.append(f"<summary>All {len(all_items)} items found today</summary>")
    lines.append("")
    lines.append("| Title | Author | Type | Topics | Priority |")
    lines.append("|-------|--------|------|--------|----------|")

    for item in all_items:
        title_link = f"[{_truncate(item['title'], 40)}]({item['url']})"
        author = item.get('author', 'Unknown')
        source_type = item.get('source_type', 'unknown')
        topics = ', '.join(item.get('topics', [])[:2])
        priority = item.get('priority', 'medium')
        lines.append(f"| {title_link} | {author} | {source_type} | {topics} | {priority} |")

    lines.append("")
    lines.append("</details>")
    lines.append("")

    return '\n'.join(lines)


def _format_item_full(item: dict) -> list:
    """Format item with full details"""
    lines = []
    lines.append(f"### [{item['title']}]({item['url']})")
    lines.append(f"**{item.get('author', 'Unknown')}** · {item.get('source_type', 'unknown')} · {item.get('date', 'no date')}")
    lines.append("")

    if item.get('summary'):
        lines.append(item['summary'])
        lines.append("")

    topics = item.get('topics', [])
    projects = item.get('projects', [])

    if topics:
        lines.append(f"**Topics:** {', '.join(topics)}")
    if projects:
        lines.append(f"**Projects:** {', '.join(projects)}")

    lines.append("")
    return lines


def _format_item_brief(item: dict) -> list:
    """Format item as brief one-liner"""
    lines = []
    summary = item.get('summary', '')
    if summary:
        summary = _truncate(summary, 100)

    topics = ', '.join(item.get('topics', [])[:2])
    lines.append(f"- **[{item['title']}]({item['url']})** ({item.get('author', 'Unknown')}, {item.get('source_type', 'unknown')})")
    if summary:
        lines.append(f"  {summary}")
    if topics:
        lines.append(f"  Topics: {topics}")
    lines.append("")
    return lines


def _truncate(text: str, max_len: int) -> str:
    """Truncate text to max length"""
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + '...'


def save_report(content: str, reports_dir: Path, target_date: date, is_historical: bool = False) -> Path:
    """
    Save report to file.

    Args:
        content: Report markdown content
        reports_dir: Directory to save to
        target_date: Date for filename
        is_historical: Whether to add suffix

    Returns:
        Path to saved file
    """
    filename = f"{target_date}"
    if is_historical:
        filename += "-historical"
    filename += ".md"

    report_path = reports_dir / filename

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return report_path
