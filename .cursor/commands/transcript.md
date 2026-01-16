# @transcript Command

## Usage
```
@transcript <youtube_url>
```

## Description
Retrieve YouTube video transcript and save it as a markdown file in the `sources/` folder.

## Parameters
- `youtube_url` (required): YouTube video URL or video ID

## Examples
```
@transcript https://www.youtube.com/watch?v=CEvIs9y1uog
@transcript https://youtu.be/CEvIs9y1uog
@transcript CEvIs9y1uog
```

## Implementation

When invoked, execute:
```bash
venv/bin/python .cursor/skills/transcripts/get_transcript.py <youtube_url>
```

Then **divide the transcript into paragraphs**:
- Read the saved file
- Analyze content to identify logical paragraph breaks (topic changes, conceptual shifts)
- Insert blank lines between paragraphs for better readability
- Save the formatted version

## Output
- Creates markdown file: `sources/YouTube - {video_title}.md`
- Includes video metadata (title, channel, source URL, retrieval date)
- Contains full transcript text formatted into paragraphs

## Related
- Full documentation: `.cursor/skills/transcripts/SKILL.md`
- Script location: `.cursor/skills/transcripts/get_transcript.py`




