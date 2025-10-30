#!/usr/bin/env python3
"""
BMAD Workflow Status Manager
Manages workflow-status.md file for tracking project progress through BMAD phases
"""

from datetime import datetime
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
ARTIFACTS_DIR = RUNTIME_ROOT.parent / "artifacts"
DEFAULT_ARTIFACTS_DIR = ARTIFACTS_DIR  # Backwards compatibility

class WorkflowStatus:
    """Manages BMAD workflow status file"""

    def __init__(self, docs_dir=None):
        self.docs_dir = Path(docs_dir) if docs_dir else DEFAULT_ARTIFACTS_DIR
        self.status_file = self.docs_dir / 'workflow-status.md'
        self.legacy_status_file = self.docs_dir / 'bmm-workflow-status.md'

        # Ensure we preserve existing workflow state even if it uses the
        # deprecated filename from earlier revisions of the tool.
        if self.legacy_status_file.exists() and not self.status_file.exists():
            self.docs_dir.mkdir(parents=True, exist_ok=True)
            self.legacy_status_file.rename(self.status_file)

    def init_workflow(self, project_name, project_type, project_level, user_name):
        """Initialize a new workflow status file"""
        self.docs_dir.mkdir(parents=True, exist_ok=True)

        content = f"""# BMAD Workflow Status

**Project**: {project_name}
**Type**: {project_type}
**Level**: {project_level}
**Created**: {datetime.now().strftime('%Y-%m-%d')}
**Owner**: {user_name}

---

## Current Status

**Phase**: Analysis
**Status**: In Progress
**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

---

## Phase Progress

### Phase 1: Analysis (Optional for Level 0-2, Recommended for 3-4)
- [ ] Brainstorm
- [ ] Product Brief
- [ ] Research
Status: Not Started

### Phase 2: Planning (Required for Level 2-4)
- [ ] PRD
- [ ] Epics Breakdown
- [ ] UX Design (if UI-heavy)
Status: Not Started

### Phase 3: Solutioning (Required for Level 2-4)
- [ ] Architecture
- [ ] Tech Stack Decisions
- [ ] Implementation Patterns
Status: Not Started

### Phase 4: Implementation (Iterative)
- [ ] Story Creation
- [ ] Story Implementation
- [ ] Testing
- [ ] Code Review
Status: Not Started

---

## Next Recommended Action

{self._get_next_action(project_level, 'Analysis')}

---

## Artifacts Created

None yet.

---

_Managed by BMAD Workflow Skills v1.0.0_
"""

        with open(self.status_file, 'w') as f:
            f.write(content)

        return self.status_file

    def _get_next_action(self, level, current_phase):
        """Get next recommended action based on level and phase"""
        recommendations = {
            ('Analysis', 0): "Skip Analysis. Proceed directly to implementation.",
            ('Analysis', 1): "Skip Analysis. Consider creating a brief tech-spec.",
            ('Analysis', 2): "Analysis optional. Recommend starting with PRD (bmad-pm).",
            ('Analysis', 3): "Recommend Product Brief (bmad-analyst) before PRD.",
            ('Analysis', 4): "Recommend full Analysis: Brainstorm + Product Brief + Research (bmad-analyst).",

            ('Planning', 2): "Create PRD and Epics (bmad-pm).",
            ('Planning', 3): "Create PRD and Epics (bmad-pm). Consider UX Design (bmad-ux) if UI-heavy.",
            ('Planning', 4): "Create PRD and Epics (bmad-pm). Create UX Design (bmad-ux) if UI-heavy.",

            ('Solutioning', 2): "Create Architecture (bmad-architecture).",
            ('Solutioning', 3): "Create comprehensive Architecture (bmad-architecture).",
            ('Solutioning', 4): "Create comprehensive Architecture with Novel Patterns (bmad-architecture).",

            ('Implementation', 2): "Create Stories (bmad-stories) then Implement (bmad-dev).",
            ('Implementation', 3): "Create Stories (bmad-stories) then Implement (bmad-dev). Consider ATDD (bmad-tea).",
            ('Implementation', 4): "Create Stories (bmad-stories) then Implement (bmad-dev). Use ATDD (bmad-tea).",
        }

        key = (current_phase, level)
        return recommendations.get(key, "Continue with current phase.")

    def update_phase(self, phase, status='In Progress'):
        """Update current phase"""
        if not self.status_file.exists():
            raise FileNotFoundError(f"Workflow status file not found: {self.status_file}")

        with open(self.status_file, 'r') as f:
            content = f.read()

        # Update Current Status section
        lines = content.split('\n')
        project_level = self._extract_project_level(lines)

        updated_lines = []
        for line in lines:
            if line.startswith('**Phase**:'):
                updated_lines.append(f'**Phase**: {phase}')
            elif line.startswith('**Status**:'):
                updated_lines.append(f'**Status**: {status}')
            elif line.startswith('**Last Updated**:'):
                updated_lines.append(f'**Last Updated**: {datetime.now().strftime("%Y-%m-%d")}')
            else:
                updated_lines.append(line)

        if project_level is not None:
            recommendation = self._get_next_action(project_level, phase)
        else:
            recommendation = "Continue with current phase."

        self._update_next_action(updated_lines, recommendation)

        with open(self.status_file, 'w') as f:
            f.write('\n'.join(updated_lines))

        return self.status_file

    def mark_phase_complete(self, phase):
        """Mark a phase as complete"""
        if not self.status_file.exists():
            raise FileNotFoundError(f"Workflow status file not found: {self.status_file}")

        with open(self.status_file, 'r') as f:
            content = f.read()

        # Update phase checklist
        phase_markers = {
            'Analysis': '### Phase 1: Analysis',
            'Planning': '### Phase 2: Planning',
            'Solutioning': '### Phase 3: Solutioning',
            'Implementation': '### Phase 4: Implementation',
        }

        if phase not in phase_markers:
            raise ValueError(f"Unknown phase: {phase}")

        lines = content.split('\n')
        updated_lines = []
        in_target_phase = False

        for line in lines:
            if phase_markers[phase] in line:
                in_target_phase = True
                updated_lines.append(line)
                continue

            if in_target_phase:
                stripped = line.strip()

                if stripped.startswith('- ['):
                    updated_lines.append(line.replace('- [ ]', '- [x]', 1))
                    continue

                if stripped == '':
                    updated_lines.append(line)
                    continue

                if stripped.startswith('Status:'):
                    updated_lines.append('Status: Complete')
                    in_target_phase = False
                    continue

            updated_lines.append(line)

        with open(self.status_file, 'w') as f:
            f.write('\n'.join(updated_lines))

        return self.status_file

    def add_artifact(self, artifact_path, description):
        """Add created artifact to status"""
        if not self.status_file.exists():
            raise FileNotFoundError(f"Workflow status file not found: {self.status_file}")

        with open(self.status_file, 'r') as f:
            content = f.read()

        # Find Artifacts section and add
        lines = content.split('\n')

        placeholder_index = None
        header_index = None

        for idx, line in enumerate(lines):
            if line.strip() == '## Artifacts Created':
                header_index = idx
                break

        if header_index is None:
            raise ValueError('Artifacts section not found in workflow status file.')

        for idx in range(header_index + 1, len(lines)):
            stripped = lines[idx].strip()
            if stripped == '':
                break
            if stripped.lower() == 'none yet.':
                placeholder_index = idx
                break

        if placeholder_index is not None:
            lines.pop(placeholder_index)

        insertion_index = header_index + 1
        while insertion_index < len(lines) and lines[insertion_index].strip() != '':
            insertion_index += 1

        artifact_entry = f'- `{artifact_path}` - {description} ({datetime.now().strftime("%Y-%m-%d")})'
        lines.insert(insertion_index, artifact_entry)

        with open(self.status_file, 'w') as f:
            f.write('\n'.join(lines))

        return self.status_file

    def get_current_phase(self):
        """Get current phase from status file"""
        if not self.status_file.exists():
            return None

        with open(self.status_file, 'r') as f:
            for line in f:
                if line.startswith('**Phase**:'):
                    return line.split(':')[1].strip()
        return None

    def get_project_level(self):
        """Get project level from status file"""
        if not self.status_file.exists():
            return None

        with open(self.status_file, 'r') as f:
            for line in f:
                if line.startswith('**Level**:'):
                    return int(line.split(':')[1].strip())
        return None

    def _extract_project_level(self, lines):
        """Extract project level from cached content lines."""
        for line in lines:
            if line.startswith('**Level**:'):
                try:
                    return int(line.split(':', 1)[1].strip())
                except (ValueError, IndexError):
                    return None
        return None

    def _update_next_action(self, lines, recommendation):
        """Update the next recommended action section in-place."""
        header_index = None
        for idx, line in enumerate(lines):
            if line.strip() == '## Next Recommended Action':
                header_index = idx
                break

        if header_index is None:
            return

        line_index = header_index + 1
        while line_index < len(lines) and lines[line_index].strip() == '':
            line_index += 1

        if line_index >= len(lines):
            lines.append(recommendation)
        else:
            lines[line_index] = recommendation

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage:")
        print("  python workflow_status.py init <project_name> <project_type> <level> <user>")
        print("  python workflow_status.py update-phase <phase> [status]")
        print("  python workflow_status.py mark-complete <phase>")
        print("  python workflow_status.py add-artifact <path> <description>")
        print("  python workflow_status.py get-phase")
        sys.exit(1)

    command = sys.argv[1]
    ws = WorkflowStatus()

    if command == 'init':
        project_name, project_type, level, user = sys.argv[2:6]
        file_path = ws.init_workflow(project_name, project_type, int(level), user)
        print(f"✅ Workflow status initialized: {file_path}")

    elif command == 'update-phase':
        phase = sys.argv[2]
        status = sys.argv[3] if len(sys.argv) > 3 else 'In Progress'
        file_path = ws.update_phase(phase, status)
        print(f"✅ Phase updated to: {phase} ({status})")

    elif command == 'mark-complete':
        phase = sys.argv[2]
        file_path = ws.mark_phase_complete(phase)
        print(f"✅ Phase marked complete: {phase}")

    elif command == 'add-artifact':
        path = sys.argv[2]
        description = ' '.join(sys.argv[3:]) if len(sys.argv) > 3 else ''
        file_path = ws.add_artifact(path, description)
        print(f"✅ Artifact added: {path}")

    elif command == 'get-phase':
        phase = ws.get_current_phase()
        print(phase if phase else "No workflow status file found")

    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == '__main__':
    main()
