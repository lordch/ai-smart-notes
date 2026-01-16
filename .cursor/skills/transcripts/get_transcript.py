#!/usr/bin/env python3
"""
YouTube Transcript Retrieval Script
Fetches YouTube video transcripts and saves them as markdown files

Usage from project root:
    venv/bin/python .cursor/skills/transcripts/get_transcript.py <youtube_url>
"""

import sys
import re
from pathlib import Path
from datetime import datetime

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
except ImportError:
    print("Error: youtube-transcript-api not installed")
    print("Install with: pip install youtube-transcript-api")
    sys.exit(1)

try:
    from yt_dlp import YoutubeDL
except ImportError:
    print("Error: yt-dlp not installed")
    print("Install with: pip install yt-dlp")
    sys.exit(1)


def extract_video_id(url):
    """Extract video ID from various YouTube URL formats"""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]+)',
        r'youtube\.com\/embed\/([^&\n?#]+)',
        r'youtube\.com\/v\/([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    if len(url) == 11 and not '/' in url:
        return url
    
    return None


def get_video_metadata(video_id):
    """Fetch video metadata using yt-dlp"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f'https://www.youtube.com/watch?v={video_id}', download=False)
            return {
                'title': info.get('title', 'Unknown Title'),
                'channel': info.get('uploader', 'Unknown Channel'),
                'upload_date': info.get('upload_date', 'Unknown Date'),
                'duration': info.get('duration', 0),
                'url': f'https://www.youtube.com/watch?v={video_id}'
            }
    except Exception as e:
        print(f"Warning: Could not fetch metadata: {e}")
        return {
            'title': f'YouTube Video {video_id}',
            'channel': 'Unknown',
            'upload_date': 'Unknown',
            'duration': 0,
            'url': f'https://www.youtube.com/watch?v={video_id}'
        }


def get_transcript(video_id):
    """Fetch transcript for the given video ID"""
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id, languages=['en'])
        return transcript
    
    except TranscriptsDisabled:
        print(f"Error: Transcripts are disabled for video {video_id}")
        return None
    except NoTranscriptFound:
        print(f"Error: No English transcript found, trying any available language...")
        try:
            transcript = api.fetch(video_id)
            return transcript
        except Exception as e:
            print(f"Error: Could not fetch any transcript: {e}")
            return None
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None


def format_transcript_markdown(metadata, transcript):
    """Format transcript as markdown"""
    lines = [
        f"# {metadata['title']}",
        "",
        f"**Source**: {metadata['url']}",
        f"**Channel**: {metadata['channel']}",
        f"**Date Retrieved**: {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "---",
        "",
        "## Transcript",
        ""
    ]
    
    buffer = []
    for snippet in transcript:
        text = snippet.text.strip().replace('\n', ' ')
        if text:
            buffer.append(text)
            if len(buffer) == 3:
                lines.append(' '.join(buffer))
                buffer = []
    
    if buffer:
        lines.append(' '.join(buffer))
    
    return '\n'.join(lines)


def sanitize_filename(filename):
    """Remove invalid characters from filename"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '')
    return filename.strip()


def save_transcript(content, output_dir, title):
    """Save transcript to markdown file"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    safe_title = sanitize_filename(title)
    filename = f"YouTube - {safe_title}.md"
    filepath = output_path / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def main():
    if len(sys.argv) < 2:
        print("Usage: python get_transcript.py <youtube_url> [output_directory]")
        print("Example: python get_transcript.py https://www.youtube.com/watch?v=CEvIs9y1uog")
        sys.exit(1)
    
    url = sys.argv[1]
    
    script_dir = Path(__file__).parent.parent.parent.parent
    output_dir = sys.argv[2] if len(sys.argv) > 2 else str(script_dir / 'sources')
    
    print(f"Processing: {url}")
    
    video_id = extract_video_id(url)
    if not video_id:
        print(f"Error: Could not extract video ID from URL: {url}")
        sys.exit(1)
    
    print(f"Video ID: {video_id}")
    
    print("Fetching video metadata...")
    metadata = get_video_metadata(video_id)
    print(f"Title: {metadata['title']}")
    
    print("Fetching transcript...")
    transcript_data = get_transcript(video_id)
    if not transcript_data:
        sys.exit(1)
    
    print("Formatting transcript...")
    markdown_content = format_transcript_markdown(metadata, transcript_data)
    
    print(f"Saving to: {output_dir}")
    filepath = save_transcript(markdown_content, output_dir, metadata['title'])
    
    print(f"✓ Transcript saved to: {filepath}")


if __name__ == '__main__':
    main()




