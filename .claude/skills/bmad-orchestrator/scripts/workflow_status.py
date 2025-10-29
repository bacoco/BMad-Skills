#!/usr/bin/env python3
"""
BMAD Workflow Status Manager
Manages workflow-status.md file for tracking project progress through BMAD phases
"""

import os
from datetime import datetime
from pathlib import Path

class WorkflowStatus:
    """Manages BMAD workflow status file"""

    def __init__(self, docs_dir='docs'):
        self.docs_dir = Path(docs_dir)
        self.status_file = self.docs_dir / 'bmm-workflow-status.md'

    def init_workflow(self, project_name, project_type, project_level, user_name):
        """Initialize a new workflow status file"""
        self.docs_dir.mkdir(parents=True, exist_ok=True)

        content = f"""# BMM Workflow Status

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
            elif in_target_phase and line.startswith('Status:'):
                updated_lines.append('Status: Complete')
                in_target_phase = False
            else:
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
        updated_lines = []
        artifacts_section = False

        for line in lines:
            updated_lines.append(line)
            if line.startswith('## Artifacts Created'):
                artifacts_section = True
            elif artifacts_section and line.strip() == '':
                # Add artifact before empty line
                updated_lines.insert(len(updated_lines) - 1,
                    f'- `{artifact_path}` - {description} ({datetime.now().strftime("%Y-%m-%d")})')
                artifacts_section = False

        with open(self.status_file, 'w') as f:
            f.write('\n'.join(updated_lines))

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
        path, description = sys.argv[2], sys.argv[3]
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
