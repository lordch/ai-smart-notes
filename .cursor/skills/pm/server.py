#!/usr/bin/env python3
"""
Project Management Server
FastAPI backend for the PM dashboard UI.
"""

import os
import re
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import frontmatter
import uvicorn

# Paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent
STRATEGY_DIR = PROJECT_ROOT / "strategy"
PEOPLE_DIR = STRATEGY_DIR / "people"
PROJECTS_DIR = STRATEGY_DIR / "projects"
TASKS_DIR = STRATEGY_DIR / "pm-tasks"
UI_DIR = SCRIPT_DIR / "ui"

app = FastAPI(title="PM Dashboard API")

# Models
class StatusUpdate(BaseModel):
    status: str

class Entity(BaseModel):
    id: str
    name: str
    type: str
    status: str
    path: str
    metadata: dict
    content: str

# Helper functions
def slugify(name: str) -> str:
    """Convert filename to slug ID."""
    # Remove prefix like "Person - ", "Project - ", "Task - "
    name = re.sub(r'^(Person|Project|Task)\s*-\s*', '', name)
    # Remove .md extension
    name = name.replace('.md', '')
    # Convert to lowercase and replace spaces with dashes
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def parse_wikilink(link: str) -> Optional[str]:
    """Extract name from [[wikilink]]."""
    if not link:
        return None
    match = re.search(r'\[\[([^\]]+)\]\]', str(link))
    if match:
        return match.group(1)
    return link if link else None

def read_entities(directory: Path, entity_type: str) -> list[Entity]:
    """Read all markdown files from a directory and parse frontmatter."""
    entities = []

    if not directory.exists():
        return entities

    for file_path in directory.glob("*.md"):
        try:
            post = frontmatter.load(file_path)

            # Extract name from filename
            name = file_path.stem
            name = re.sub(r'^(Person|Project|Task)\s*-\s*', '', name)

            entity = Entity(
                id=slugify(file_path.stem),
                name=name,
                type=entity_type,
                status=post.metadata.get('status', 'Unknown'),
                path=str(file_path.relative_to(PROJECT_ROOT)),
                metadata=dict(post.metadata),
                content=post.content
            )
            entities.append(entity)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

    return entities

def update_entity_status(file_path: Path, new_status: str) -> bool:
    """Update the status field in a markdown file's frontmatter."""
    try:
        post = frontmatter.load(file_path)
        post.metadata['status'] = new_status

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter.dumps(post))

        return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

# API Routes
@app.get("/api/people")
def get_people():
    """Get all people."""
    return read_entities(PEOPLE_DIR, "Person")

@app.get("/api/projects")
def get_projects():
    """Get all projects."""
    return read_entities(PROJECTS_DIR, "Project")

@app.get("/api/tasks")
def get_tasks():
    """Get all tasks."""
    return read_entities(TASKS_DIR, "Task")

@app.get("/api/all")
def get_all():
    """Get all entities."""
    return {
        "people": read_entities(PEOPLE_DIR, "Person"),
        "projects": read_entities(PROJECTS_DIR, "Project"),
        "tasks": read_entities(TASKS_DIR, "Task")
    }

@app.patch("/api/tasks/{task_id}")
def update_task_status(task_id: str, update: StatusUpdate):
    """Update task status."""
    for file_path in TASKS_DIR.glob("*.md"):
        if slugify(file_path.stem) == task_id:
            if update_entity_status(file_path, update.status):
                return {"success": True, "id": task_id, "status": update.status}
            else:
                raise HTTPException(status_code=500, detail="Failed to update file")

    raise HTTPException(status_code=404, detail=f"Task not found: {task_id}")

@app.patch("/api/projects/{project_id}")
def update_project_status(project_id: str, update: StatusUpdate):
    """Update project status."""
    for file_path in PROJECTS_DIR.glob("*.md"):
        if slugify(file_path.stem) == project_id:
            if update_entity_status(file_path, update.status):
                return {"success": True, "id": project_id, "status": update.status}
            else:
                raise HTTPException(status_code=500, detail="Failed to update file")

    raise HTTPException(status_code=404, detail=f"Project not found: {project_id}")

@app.patch("/api/people/{person_id}")
def update_person_status(person_id: str, update: StatusUpdate):
    """Update person status."""
    for file_path in PEOPLE_DIR.glob("*.md"):
        if slugify(file_path.stem) == person_id:
            if update_entity_status(file_path, update.status):
                return {"success": True, "id": person_id, "status": update.status}
            else:
                raise HTTPException(status_code=500, detail="Failed to update file")

    raise HTTPException(status_code=404, detail=f"Person not found: {person_id}")

# Serve static files
@app.get("/")
def serve_index():
    """Serve the main UI."""
    return FileResponse(UI_DIR / "index.html")

# Mount static files (CSS, JS)
if UI_DIR.exists():
    app.mount("/static", StaticFiles(directory=UI_DIR), name="static")

if __name__ == "__main__":
    print(f"Starting PM Dashboard server...")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"People dir: {PEOPLE_DIR}")
    print(f"Projects dir: {PROJECTS_DIR}")
    print(f"Tasks dir: {TASKS_DIR}")
    print(f"\nOpen http://localhost:8787 in your browser")

    uvicorn.run(app, host="127.0.0.1", port=8787)
