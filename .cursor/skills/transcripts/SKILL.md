# Skill: YouTube Transcript Retrieval

## Purpose
Retrieve transcripts from YouTube videos and save them as markdown files in the Zettelkasten vault's `sources/` folder for knowledge management and note-taking.

## When to Use
- User provides a YouTube URL and asks for a transcript
- User wants to capture video content as text for later processing
- User mentions "transcript", "YouTube", or "video content"

## Usage

### Command Invocation
```bash
venv/bin/python .cursor/skills/transcripts/get_transcript.py <youtube_url> [output_directory]
```

### Parameters
- `youtube_url` (required): Full YouTube URL or video ID
  - Examples: 
    - `https://www.youtube.com/watch?v=CEvIs9y1uog`
    - `https://youtu.be/CEvIs9y1uog`
    - `CEvIs9y1uog` (video ID only)
    
- `output_directory` (optional): Where to save the transcript
  - Default: `sources/` (relative to project root)
  - Can be absolute or relative path

### Example Commands

Basic usage (saves to default `sources/` folder):
```bash
venv/bin/python .cursor/skills/transcripts/get_transcript.py https://www.youtube.com/watch?v=CEvIs9y1uog
```

Custom output directory:
```bash
venv/bin/python .cursor/skills/transcripts/get_transcript.py https://www.youtube.com/watch?v=CEvIs9y1uog sources/videos
```

## Output Format

The script generates a markdown file with:
- Filename: `YouTube - {video_title}.md`
- Location: `sources/` folder (or specified directory)

### Markdown Structure
```markdown
# Video Title

**Source**: https://www.youtube.com/watch?v=VIDEO_ID
**Channel**: Channel Name
**Date Retrieved**: YYYY-MM-DD

---

## Transcript

[Full transcript text with original formatting preserved]
```

## Agent Workflow

When a user requests a YouTube transcript:

1. **Identify the request**: User provides YouTube URL
   
2. **Execute the script**:
   ```bash
   venv/bin/python .cursor/skills/transcripts/get_transcript.py <youtube_url>
   ```

3. **Verify output**: Check that file was created in `sources/` folder
   ```bash
   ls -lh sources/YouTube*.md | tail -1
   ```

4. **Divide into paragraphs**: Read the transcript file and analyze the content to divide it into logical paragraphs
   - Identify topic changes, speaker transitions, or natural breaks in the content
   - Insert blank lines between paragraphs to improve readability
   - Preserve the original metadata (title, source, channel, date)
   - Save the formatted version back to the same file

5. **Inform user**: Report the saved file location and name, mention that paragraphs have been formatted

## Cursor Command

You can use this quick command:
```
@transcript <youtube_url>
```

This command will:
- Run the transcript retrieval script
- Save to the default `sources/` folder
- Return the file path

## Error Handling

Common errors and solutions:

### "Transcripts are disabled"
- Video owner has disabled transcripts
- No automatic solution available

### "No transcript found"
- Video doesn't have captions/subtitles
- Try a different video or check if captions exist on YouTube

### "Could not fetch metadata"
- Network issue or video is private/deleted
- Script will still attempt to save transcript with generic title

## Integration with Zettelkasten

The transcript is saved as a **source note** in `sources/` folder. Workflow:

1. **Retrieve transcript** → `sources/YouTube - Title.md`
2. **Process & extract insights** → Create literature notes in `pages/`
3. **Link to permanent notes** → Connect ideas to existing knowledge graph

## Technical Details

- Script location: `.cursor/skills/transcripts/get_transcript.py`
- Dependencies: `youtube-transcript-api`, `yt-dlp` (see `requirements.txt`)
- Virtual environment: `venv/` (project root)

## Post-Processing: Paragraph Formatting

After saving the raw transcript, agents should divide the text into paragraphs for better readability:

### How to Format Paragraphs

1. **Read the transcript file** (skip the metadata header, focus on content after `## Transcript`)

2. **Analyze content** to identify paragraph breaks:
   - Look for topic transitions (e.g., "Now let's talk about...", "Moving on to...")
   - Detect conceptual shifts or new ideas being introduced
   - Identify speaker changes or significant pauses in speech flow
   - Group related sentences together (typically 3-8 lines per paragraph)

3. **Insert blank lines** between identified paragraphs

4. **Save the formatted version** back to the file

### Example Approach

Read the transcript, identify logical breaks every 5-10 lines or where topics shift, then insert blank lines to create paragraph structure. This makes the transcript much more readable for later processing and note-taking.

## Notes
- Script automatically handles various YouTube URL formats
- Sanitizes filenames (removes invalid characters)
- Creates output directory if it doesn't exist
- Defaults to English transcripts (auto-generated if manual not available)
- Post-processing paragraph formatting improves readability for literature note creation




