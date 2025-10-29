#!/usr/bin/env python3
"""
BMAD Sprint Status Manager
Manages sprint-status.yaml for tracking story development progress
"""

import yaml
from pathlib import Path
from datetime import datetime

class SprintStatus:
    """Manages BMAD sprint status YAML file"""

    def __init__(self, docs_dir='docs'):
        self.docs_dir = Path(docs_dir)
        self.status_file = self.docs_dir / 'sprint-status.yaml'

    def init_from_epics(self, epics_file='docs/epics.md'):
        """Initialize sprint status from epics.md"""
        epics_path = Path(epics_file)

        if not epics_path.exists():
            raise FileNotFoundError(f"Epics file not found: {epics_file}")

        # Parse epics.md to extract stories
        stories = self._parse_epics(epics_path)

        # Create sprint status structure
        status = {
            'project_metadata': {
                'created': datetime.now().strftime('%Y-%m-%d'),
                'last_updated': datetime.now().strftime('%Y-%m-%d'),
                'total_epics': len(set(s['epic_num'] for s in stories)),
                'total_stories': len(stories),
            },
            'epic_status': {},
            'development_status': {},
        }

        # Group by epic
        epics = {}
        for story in stories:
            epic_num = story['epic_num']
            if epic_num not in epics:
                epics[epic_num] = []
            epics[epic_num].append(story)

        # Build epic and development status
        for epic_num in sorted(epics.keys()):
            epic_stories = epics[epic_num]
            epic_key = f'epic-{epic_num}'

            status['epic_status'][epic_key] = {
                'title': epic_stories[0]['epic_title'],
                'total_stories': len(epic_stories),
                'completed': 0,
                'in_progress': 0,
                'status': 'backlog',
            }

            for story in epic_stories:
                story_key = f"{story['epic_num']}-{story['story_num']}-{story['story_slug']}"
                status['development_status'][story_key] = {
                    'title': story['story_title'],
                    'status': 'backlog',  # backlog, drafted, ready, in-progress, review, done
                    'assigned_to': None,
                    'started': None,
                    'completed': None,
                }

        # Save to file
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        with open(self.status_file, 'w') as f:
            yaml.dump(status, f, default_flow_style=False, sort_keys=False)

        return self.status_file

    def _parse_epics(self, epics_path):
        """Parse epics.md to extract story information"""
        with open(epics_path, 'r') as f:
            content = f.read()

        stories = []
        lines = content.split('\n')
        current_epic = None
        current_epic_title = None

        for line in lines:
            # Epic header: ## Epic 1: Title
            if line.startswith('## Epic '):
                parts = line.replace('## Epic ', '').split(':', 1)
                current_epic = int(parts[0].strip())
                current_epic_title = parts[1].strip() if len(parts) > 1 else f"Epic {current_epic}"

            # Story header: #### Story 1.1: Title
            elif line.startswith('#### Story ') and current_epic:
                parts = line.replace('#### Story ', '').split(':', 1)
                story_id = parts[0].strip()
                story_title = parts[1].strip() if len(parts) > 1 else ""

                epic_num, story_num = story_id.split('.')
                story_slug = story_title.lower().replace(' ', '-').replace('/', '-')
                story_slug = ''.join(c for c in story_slug if c.isalnum() or c == '-')

                stories.append({
                    'epic_num': int(epic_num),
                    'story_num': int(story_num),
                    'story_title': story_title,
                    'story_slug': story_slug,
                    'epic_title': current_epic_title,
                })

        return stories

    def update_story_status(self, story_key, new_status, assigned_to=None):
        """Update status of a story"""
        if not self.status_file.exists():
            raise FileNotFoundError(f"Sprint status file not found: {self.status_file}")

        with open(self.status_file, 'r') as f:
            status = yaml.safe_load(f)

        if story_key not in status['development_status']:
            raise ValueError(f"Story not found: {story_key}")

        story = status['development_status'][story_key]
        old_status = story['status']
        story['status'] = new_status

        if assigned_to:
            story['assigned_to'] = assigned_to

        if new_status == 'in-progress' and not story.get('started'):
            story['started'] = datetime.now().strftime('%Y-%m-%d')

        if new_status == 'done' and not story.get('completed'):
            story['completed'] = datetime.now().strftime('%Y-%m-%d')

        # Update epic status
        epic_num = int(story_key.split('-')[0])
        epic_key = f'epic-{epic_num}'

        if epic_key in status['epic_status']:
            self._recalculate_epic_status(status, epic_key)

        # Update metadata
        status['project_metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

        with open(self.status_file, 'w') as f:
            yaml.dump(status, f, default_flow_style=False, sort_keys=False)

        return self.status_file

    def _recalculate_epic_status(self, status, epic_key):
        """Recalculate epic status based on its stories"""
        epic_num = int(epic_key.replace('epic-', ''))

        # Find all stories for this epic
        epic_stories = [
            story for key, story in status['development_status'].items()
            if key.startswith(f'{epic_num}-')
        ]

        completed = sum(1 for s in epic_stories if s['status'] == 'done')
        in_progress = sum(1 for s in epic_stories if s['status'] in ['in-progress', 'review'])

        status['epic_status'][epic_key]['completed'] = completed
        status['epic_status'][epic_key]['in_progress'] = in_progress

        # Determine epic status
        if completed == len(epic_stories):
            status['epic_status'][epic_key]['status'] = 'done'
        elif in_progress > 0 or completed > 0:
            status['epic_status'][epic_key]['status'] = 'in-progress'
        else:
            status['epic_status'][epic_key]['status'] = 'backlog'

    def get_next_backlog_story(self):
        """Get next story in backlog status"""
        if not self.status_file.exists():
            return None

        with open(self.status_file, 'r') as f:
            status = yaml.safe_load(f)

        for story_key, story_data in status['development_status'].items():
            if story_data['status'] == 'backlog':
                return story_key, story_data

        return None

    def get_story_status(self, story_key):
        """Get status of a specific story"""
        if not self.status_file.exists():
            return None

        with open(self.status_file, 'r') as f:
            status = yaml.safe_load(f)

        return status['development_status'].get(story_key)

    def list_stories_by_status(self, target_status):
        """List all stories with given status"""
        if not self.status_file.exists():
            return []

        with open(self.status_file, 'r') as f:
            status = yaml.safe_load(f)

        return [
            (key, data) for key, data in status['development_status'].items()
            if data['status'] == target_status
        ]

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python sprint_status.py init [epics_file]")
        print("  python sprint_status.py update <story_key> <status> [assigned_to]")
        print("  python sprint_status.py next-backlog")
        print("  python sprint_status.py list-status <status>")
        sys.exit(1)

    command = sys.argv[1]
    ss = SprintStatus()

    if command == 'init':
        epics_file = sys.argv[2] if len(sys.argv) > 2 else 'docs/epics.md'
        file_path = ss.init_from_epics(epics_file)
        print(f"✅ Sprint status initialized: {file_path}")

    elif command == 'update':
        story_key, new_status = sys.argv[2], sys.argv[3]
        assigned_to = sys.argv[4] if len(sys.argv) > 4 else None
        file_path = ss.update_story_status(story_key, new_status, assigned_to)
        print(f"✅ Story updated: {story_key} → {new_status}")

    elif command == 'next-backlog':
        result = ss.get_next_backlog_story()
        if result:
            story_key, story_data = result
            print(f"Next backlog story: {story_key} - {story_data['title']}")
        else:
            print("No backlog stories found")

    elif command == 'list-status':
        target_status = sys.argv[2]
        stories = ss.list_stories_by_status(target_status)
        print(f"Stories with status '{target_status}':")
        for key, data in stories:
            print(f"  - {key}: {data['title']}")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
