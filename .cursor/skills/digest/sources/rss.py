"""
RSS/Atom feed fetcher for AI Digest
"""

from datetime import date, datetime
from typing import Optional
import feedparser
from dateutil import parser as date_parser


class RSSFetcher:
    """Fetches and parses RSS/Atom feeds"""

    def fetch(self, source: dict, target_date: date, days_back: int = 0) -> list:
        """
        Fetch items from RSS feed, filtering by date.

        Args:
            source: Source config with 'rss' URL
            target_date: Target date for the digest
            days_back: How many days back to include (0 = only target_date)

        Returns:
            List of parsed items
        """
        rss_url = source.get('rss')
        if not rss_url:
            return []

        feed = feedparser.parse(rss_url)

        if feed.bozo and not feed.entries:
            raise Exception(f"Failed to parse feed: {feed.bozo_exception}")

        items = []
        source_priority = source.get('priority', 'medium')
        source_topics = source.get('topics', [])

        # Calculate date range
        from datetime import timedelta
        start_date = target_date - timedelta(days=days_back)

        for entry in feed.entries:
            # Parse publication date
            pub_date = self._parse_date(entry)

            # Filter by date range
            if pub_date:
                if pub_date > target_date:
                    continue  # Skip future items
                if pub_date < start_date:
                    continue  # Skip items before range

            # Extract item data
            item = {
                'title': entry.get('title', 'Untitled'),
                'url': entry.get('link', ''),
                'author': self._extract_author(entry, source),
                'author_id': source.get('id'),
                'date': pub_date,
                'source_type': source.get('type', 'blog'),
                'source_name': source.get('name', source.get('id', 'Unknown')),
                'summary': self._extract_summary(entry),
                'priority': source_priority,
                'topics': source_topics,
                'projects': self._match_projects(source_topics),
                'fetched_at': datetime.now(),
            }

            items.append(item)

        return items

    def _parse_date(self, entry) -> Optional[date]:
        """Parse publication date from feed entry"""
        date_fields = ['published', 'updated', 'created']

        for field in date_fields:
            if field in entry:
                try:
                    parsed = date_parser.parse(entry[field])
                    return parsed.date()
                except (ValueError, TypeError):
                    continue

            # Try _parsed variants
            parsed_field = f'{field}_parsed'
            if parsed_field in entry and entry[parsed_field]:
                try:
                    from time import mktime
                    timestamp = mktime(entry[parsed_field])
                    return datetime.fromtimestamp(timestamp).date()
                except (ValueError, TypeError, OverflowError):
                    continue

        return None

    def _extract_author(self, entry, source: dict) -> str:
        """Extract author from entry or fall back to source name"""
        if 'author' in entry:
            return entry['author']
        if 'author_detail' in entry and 'name' in entry['author_detail']:
            return entry['author_detail']['name']
        return source.get('name', 'Unknown')

    def _extract_summary(self, entry) -> str:
        """Extract summary/description from entry"""
        if 'summary' in entry:
            # Strip HTML tags (basic)
            summary = entry['summary']
            import re
            summary = re.sub(r'<[^>]+>', '', summary)
            # Truncate to reasonable length
            if len(summary) > 500:
                summary = summary[:497] + '...'
            return summary.strip()

        if 'description' in entry:
            desc = entry['description']
            import re
            desc = re.sub(r'<[^>]+>', '', desc)
            if len(desc) > 500:
                desc = desc[:497] + '...'
            return desc.strip()

        return ''

    def _match_projects(self, topics: list) -> list:
        """Match topics to projects (hardcoded for MVP)"""
        projects = []

        legal_topics = {'legal-ai', 'compliance', 'rag', 'document-generation'}
        consulting_topics = {'ai-adoption', 'context-engineering', 'future-of-work',
                            'ai-agents', 'organizational-change', 'ai-education'}

        topic_set = set(topics)

        if topic_set & legal_topics:
            projects.append('lawly')
        if topic_set & consulting_topics:
            projects.append('consulting')

        return projects
