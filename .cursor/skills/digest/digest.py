#!/usr/bin/env python3
"""
AI Digest - Main entry point
Generates daily digest of AI-related content from monitored sources.
"""

import argparse
import sys
from datetime import datetime, date
from pathlib import Path

# Add skill directory to path for imports
SKILL_DIR = Path(__file__).parent
PROJECT_ROOT = SKILL_DIR.parent.parent.parent
sys.path.insert(0, str(SKILL_DIR))

from config import load_config, get_sources_for_today
from sources.rss import RSSFetcher
from report import generate_report, save_report


def parse_args():
    parser = argparse.ArgumentParser(description='Generate AI Digest')
    parser.add_argument('--scan', action='store_true',
                        help='Quick scan - high priority only')
    parser.add_argument('--project', type=str,
                        help='Filter by project (e.g., lawly, consulting)')
    parser.add_argument('--topic', type=str,
                        help='Filter by topic cluster')
    parser.add_argument('--date', type=str,
                        help='Historical mode - digest for specific date (YYYY-MM-DD)')
    parser.add_argument('--days', type=int, default=0,
                        help='How many days back to include (0 = only target date, 7 = week)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Verbose output')
    return parser.parse_args()


def main():
    args = parse_args()

    # Determine target date
    if args.date:
        try:
            target_date = datetime.strptime(args.date, '%Y-%m-%d').date()
            is_historical = True
        except ValueError:
            print(f"Error: Invalid date format '{args.date}'. Use YYYY-MM-DD")
            sys.exit(1)
    else:
        target_date = date.today()
        is_historical = False

    days_back = args.days

    if args.verbose:
        print(f"AI Digest for {target_date}")
        if is_historical:
            print("(historical mode)")
        if days_back > 0:
            print(f"(including {days_back} days back)")

    # Load configuration
    config = load_config(PROJECT_ROOT / 'digest')
    if not config:
        print("Error: Could not load config from digest/config.yaml")
        sys.exit(1)

    # Get sources to fetch today
    sources = get_sources_for_today(config, PROJECT_ROOT / 'digest', target_date)

    if args.verbose:
        print(f"Sources to fetch: {len(sources)}")

    # Initialize fetchers
    rss_fetcher = RSSFetcher()

    # Fetch all sources
    all_items = []
    errors = []

    for source in sources:
        if args.verbose:
            print(f"Fetching: {source.get('name', source.get('id', 'unknown'))}")

        strategy = source.get('fetch_strategy', 'rss')
        if isinstance(strategy, list):
            strategy = strategy[0]  # Use first strategy for MVP

        if strategy == 'rss' and source.get('rss'):
            try:
                items = rss_fetcher.fetch(source, target_date, days_back)
                all_items.extend(items)
                if args.verbose:
                    print(f"  Found {len(items)} items")
            except Exception as e:
                errors.append(f"{source.get('name', 'unknown')}: {e}")
                if args.verbose:
                    print(f"  Error: {e}")

    # Filter by project if specified
    if args.project:
        all_items = [item for item in all_items
                     if args.project in item.get('projects', [])]

    # Filter by topic if specified
    if args.topic:
        all_items = [item for item in all_items
                     if args.topic in item.get('topics', [])]

    # Prioritize items
    high_priority = [i for i in all_items if i.get('priority') == 'high']
    medium_priority = [i for i in all_items if i.get('priority') == 'medium']
    low_priority = [i for i in all_items if i.get('priority') == 'low']

    # Generate report
    report_data = {
        'date': target_date,
        'is_historical': is_historical,
        'is_scan': args.scan,
        'project_filter': args.project,
        'topic_filter': args.topic,
        'high_priority': high_priority,
        'medium_priority': medium_priority if not args.scan else [],
        'low_priority': low_priority if not args.scan else [],
        'all_items': all_items,
        'sources_checked': len(sources),
        'errors': errors,
        'config': config,
    }

    report_content = generate_report(report_data)

    # Save report
    reports_dir = PROJECT_ROOT / 'digest' / 'reports'
    reports_dir.mkdir(parents=True, exist_ok=True)

    report_path = save_report(report_content, reports_dir, target_date, is_historical)

    print(f"Digest generated: {report_path}")
    print(f"Items found: {len(all_items)} (high: {len(high_priority)}, medium: {len(medium_priority)}, low: {len(low_priority)})")

    if errors:
        print(f"Errors: {len(errors)}")
        for err in errors:
            print(f"  - {err}")


if __name__ == '__main__':
    main()
