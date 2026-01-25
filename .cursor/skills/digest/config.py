"""
Configuration handling for AI Digest
"""

from datetime import date
from pathlib import Path
from typing import Optional
import yaml


def load_config(digest_dir: Path) -> Optional[dict]:
    """Load main config from digest/config.yaml"""
    config_path = digest_dir / 'config.yaml'
    if not config_path.exists():
        return None

    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_sources(digest_dir: Path) -> dict:
    """Load all source definitions from digest/sources/"""
    sources_dir = digest_dir / 'sources'
    all_sources = {}

    if not sources_dir.exists():
        return all_sources

    for yaml_file in sources_dir.glob('*.yaml'):
        category = yaml_file.stem  # people, news, organizations, etc.
        with open(yaml_file, 'r', encoding='utf-8') as f:
            sources = yaml.safe_load(f) or {}
            for source_id, source_data in sources.items():
                source_data['id'] = source_id
                source_data['category'] = category
                all_sources[f"{category}.{source_id}"] = source_data

    return all_sources


def load_topics(digest_dir: Path) -> dict:
    """Load topic clusters from digest/topics.yaml"""
    topics_path = digest_dir / 'topics.yaml'
    if not topics_path.exists():
        return {}

    with open(topics_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def get_sources_for_today(config: dict, digest_dir: Path, target_date: date) -> list:
    """
    Get list of sources to fetch based on tier schedule and day of week.
    Returns list of source configs with full details.
    """
    all_sources = load_sources(digest_dir)
    topics = load_topics(digest_dir)

    sources_to_fetch = []
    seen_ids = set()

    tier_schedule = config.get('tier_schedule', {})

    # Tier 1: Daily sources
    tier_1 = tier_schedule.get('tier_1_daily', {})
    for source_ref in tier_1.get('sources', []):
        if source_ref in all_sources and source_ref not in seen_ids:
            sources_to_fetch.append(all_sources[source_ref])
            seen_ids.add(source_ref)

    # Tier 2: Rotating by day of week
    tier_2 = tier_schedule.get('tier_2_rotating', {})
    day_name = target_date.strftime('%A').lower()
    day_schedule = tier_2.get('schedule', {}).get(day_name, [])

    for ref in day_schedule:
        if ref.startswith('topics.'):
            # Topic cluster - would trigger WebSearch in full implementation
            topic_id = ref.replace('topics.', '')
            if topic_id in topics:
                # For MVP, skip topic searches (would need WebSearch)
                pass
        elif ref.startswith('sources.'):
            source_id = ref.replace('sources.', '')
            # Look for source in any category
            for full_id, source in all_sources.items():
                if source['id'] == source_id and full_id not in seen_ids:
                    sources_to_fetch.append(source)
                    seen_ids.add(full_id)
                    break
        elif ref in all_sources and ref not in seen_ids:
            sources_to_fetch.append(all_sources[ref])
            seen_ids.add(ref)

    # Tier 3: Weekly (check if today matches)
    # For MVP, include tier 3 on Fridays
    if target_date.weekday() == 4:  # Friday
        tier_3 = tier_schedule.get('tier_3_weekly', {})
        for source_ref in tier_3.get('sources', []):
            if source_ref in all_sources and source_ref not in seen_ids:
                sources_to_fetch.append(all_sources[source_ref])
                seen_ids.add(source_ref)

    return sources_to_fetch
