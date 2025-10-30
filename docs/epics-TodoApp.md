# Todo App - Epic Breakdown

**Author:** Product Team
**Date:** 2025-10-30
**Project Level:** Level 2
**Total Epics:** 8

---

## Overview

This document provides the complete tactical implementation roadmap for Todo App.
Each epic contains sequenced user stories with acceptance criteria and prerequisites.

**Epic Sequencing Rules:**
1. Epic 1 establishes foundation (infrastructure, CI/CD, core setup)
2. Subsequent epics build upon previous work
3. No forward dependencies across epics

**Story Requirements:**
- **Vertical slices**: Each story delivers complete, testable functionality
- **Sequential**: Stories are logically ordered within each epic
- **AI-agent sized**: Completable in single focused session (2-4 hours)
- **No forward dependencies**: No story depends on work from later stories

---

## Epic 1: Core Task Management (Foundation)

**Priority:** P1
**Estimated Duration:** 2 weeks
**Goal:** Establish fundamental task CRUD operations and data persistence

### Story 1.1: Project Setup & Infrastructure
**Effort:** 2 hours

**Description:**
Initialize project with build tooling, linting, testing framework, and CI/CD pipeline.

**Acceptance Criteria:**
- [ ] Project repository created with appropriate structure
- [ ] Build system configured (webpack/vite/next.js)
- [ ] TypeScript configured with strict mode
- [ ] ESLint and Prettier configured
- [ ] Testing framework installed (Jest/Vitest)
- [ ] CI/CD pipeline configured (GitHub Actions or equivalent)
- [ ] README with setup instructions

**Technical Notes:**
- Choose modern framework (React, Vue, or Svelte)
- Configure absolute imports
- Set up pre-commit hooks

---

### Story 1.2: Task Data Model & Database Schema
**Effort:** 3 hours
**Prerequisites:** Story 1.1

**Description:**
Define task entity schema and set up database/storage layer.

**Acceptance Criteria:**
- [ ] Task entity defined with fields: id, title, description, completed, createdAt, updatedAt
- [ ] Database schema created (or local storage schema)
- [ ] Data access layer/repository pattern implemented
- [ ] Database migrations set up (if applicable)
- [ ] Type definitions for Task entity
- [ ] Unit tests for data layer

**Data Model:**
```typescript
interface Task {
  id: string;
  title: string;
  description?: string;
  completed: boolean;
  createdAt: Date;
  updatedAt: Date;
  listId: string;
}
```

**Technical Decisions:**
- Use UUID for task IDs
- Store dates as ISO 8601 strings
- Validate title is non-empty (max 500 chars)

---

### Story 1.3: Create Task Functionality
**Effort:** 3 hours
**Prerequisites:** Story 1.2

**Description:**
Implement UI and logic for creating new tasks with title and optional description.

**Acceptance Criteria:**
- [ ] Task input component with title field
- [ ] Optional description field (expandable/collapsible)
- [ ] "Add Task" button or Enter key to submit
- [ ] Validation: title required, max length enforced
- [ ] New task appears in list immediately
- [ ] Input clears after successful creation
- [ ] Loading state during creation
- [ ] Error handling with user-friendly messages
- [ ] Unit tests for create logic
- [ ] Integration tests for create flow

**UX Requirements:**
- Input field auto-focused on page load
- Enter key creates task
- Escape key clears input
- Character counter for title field

---

### Story 1.4: Display Tasks in List View
**Effort:** 2 hours
**Prerequisites:** Story 1.3

**Description:**
Render list of tasks with basic information and layout.

**Acceptance Criteria:**
- [ ] Task list component displays all tasks
- [ ] Each task shows title, completion status, timestamp
- [ ] Empty state with friendly message when no tasks
- [ ] Loading state while fetching tasks
- [ ] Responsive layout (mobile and desktop)
- [ ] Tasks sorted by creation date (newest first)
- [ ] Accessibility: proper semantic HTML and ARIA labels
- [ ] Unit tests for list rendering

**UI Requirements:**
- Card/row layout for each task
- Hover states for interactivity
- Timestamps displayed as relative time ("2 hours ago")

---

### Story 1.5: Mark Task Complete/Incomplete
**Effort:** 3 hours
**Prerequisites:** Story 1.4

**Description:**
Add checkbox to toggle task completion status with visual feedback.

**Acceptance Criteria:**
- [ ] Checkbox component on each task
- [ ] Click checkbox toggles completed state
- [ ] Visual distinction for completed tasks (strikethrough, opacity)
- [ ] Optimistic UI update (immediate visual feedback)
- [ ] Persistence of completion state
- [ ] Undo capability within 3 seconds
- [ ] Completion animation (smooth transition)
- [ ] Unit tests for toggle logic
- [ ] Integration tests for completion flow

**UX Requirements:**
- Satisfying click animation
- Completed tasks remain in list (don't disappear)
- Keyboard accessible (Space to toggle)

---

### Story 1.6: Edit Task Inline
**Effort:** 4 hours
**Prerequisites:** Story 1.5

**Description:**
Enable inline editing of task title and description.

**Acceptance Criteria:**
- [ ] Click task title to enter edit mode
- [ ] Inline text input replaces static text
- [ ] Save on Enter or click outside
- [ ] Cancel on Escape key
- [ ] Validation on save (required title)
- [ ] Optimistic update
- [ ] Revert on cancel or error
- [ ] Visual indicator for edit mode
- [ ] Unit tests for edit logic
- [ ] Integration tests for edit flow

**UX Requirements:**
- Smooth transition to edit mode
- Cursor positioned at end of text
- No page refresh or modal

---

### Story 1.7: Delete Task with Confirmation
**Effort:** 3 hours
**Prerequisites:** Story 1.6

**Description:**
Implement delete functionality with confirmation and undo option.

**Acceptance Criteria:**
- [ ] Delete button/icon on each task (visible on hover)
- [ ] Confirmation dialog or toast before delete
- [ ] Optimistic removal from UI
- [ ] Undo option available for 5 seconds
- [ ] Permanent deletion after undo window
- [ ] Success message after deletion
- [ ] Unit tests for delete logic
- [ ] Integration tests for delete flow

**UX Requirements:**
- Non-destructive by default
- Clear undo mechanism
- Keyboard shortcut for delete (Del key when selected)

---

### Story 1.8: Task Persistence & Auto-Save
**Effort:** 2 hours
**Prerequisites:** Story 1.7

**Description:**
Ensure all task operations persist across sessions with automatic saving.

**Acceptance Criteria:**
- [ ] All CRUD operations persist to storage
- [ ] No manual save button required
- [ ] Data loads on app initialization
- [ ] Sync status indicator (saved/saving/error)
- [ ] Retry logic for failed saves
- [ ] Offline capability (operations queue)
- [ ] Integration tests for persistence
- [ ] E2E tests for full user flow

**Technical Notes:**
- Implement debouncing for rapid edits
- Use optimistic updates with rollback on error
- Cache data for instant load

---

## Epic 2: Task Organization & Lists

**Priority:** P1
**Estimated Duration:** 1.5 weeks
**Goal:** Enable multi-list organization for task categorization

### Story 2.1: List Data Model & Relationships
**Effort:** 2 hours
**Prerequisites:** Epic 1 complete

**Description:**
Define list entity and establish task-list relationships.

**Acceptance Criteria:**
- [ ] List entity defined with fields: id, name, color, order, createdAt
- [ ] Foreign key relationship: Task.listId → List.id
- [ ] Database schema updated with lists table
- [ ] Type definitions for List entity
- [ ] Data access layer for lists
- [ ] Unit tests for list data operations

**Data Model:**
```typescript
interface List {
  id: string;
  name: string;
  color?: string;
  order: number;
  createdAt: Date;
  isDefault: boolean;
}
```

---

### Story 2.2: Default "Inbox" List Implementation
**Effort:** 2 hours
**Prerequisites:** Story 2.1

**Description:**
Create system-managed default list for uncategorized tasks.

**Acceptance Criteria:**
- [ ] "Inbox" list created on app initialization
- [ ] Inbox list cannot be deleted
- [ ] New tasks default to Inbox
- [ ] Inbox displayed prominently in UI
- [ ] Unit tests for default list behavior

**Business Rules:**
- Inbox is always the first list
- ID: "inbox" (constant)
- User can rename but not delete

---

### Story 2.3: Create Custom Lists
**Effort:** 3 hours
**Prerequisites:** Story 2.2

**Description:**
UI and logic for users to create additional task lists.

**Acceptance Criteria:**
- [ ] "New List" button in sidebar
- [ ] Modal or inline form for list creation
- [ ] List name required (max 50 chars)
- [ ] Optional color picker
- [ ] New list appears in sidebar immediately
- [ ] Validation and error handling
- [ ] Unit tests for list creation
- [ ] Integration tests for create flow

**UX Requirements:**
- Quick create (keyboard shortcut: Cmd+L)
- Color presets for quick selection
- Default to next available color

---

### Story 2.4: Display Tasks Grouped by List
**Effort:** 3 hours
**Prerequisites:** Story 2.3

**Description:**
Update UI to show tasks organized by their assigned list.

**Acceptance Criteria:**
- [ ] List selector in sidebar
- [ ] Active list highlighted
- [ ] Task count badge on each list
- [ ] Clicking list filters tasks to that list
- [ ] URL reflects current list selection
- [ ] All lists view shows tasks from all lists
- [ ] Empty state per list
- [ ] Unit tests for list filtering

**UI Requirements:**
- Sidebar shows all lists with counts
- Active list visually distinct
- Smooth transitions between lists

---

### Story 2.5: Move Tasks Between Lists
**Effort:** 4 hours
**Prerequisites:** Story 2.4

**Description:**
Enable moving tasks from one list to another.

**Acceptance Criteria:**
- [ ] Dropdown or context menu on task to select destination list
- [ ] Drag-and-drop between lists (optional)
- [ ] Task immediately updates to new list
- [ ] Undo capability for moves
- [ ] Bulk move selected tasks
- [ ] Keyboard shortcut for move (M key)
- [ ] Unit tests for move logic
- [ ] Integration tests for move operations

**UX Requirements:**
- Visual feedback during drag
- Confirmation for bulk moves
- Quick-access to recent lists

---

### Story 2.6: Rename & Delete Lists
**Effort:** 3 hours
**Prerequisites:** Story 2.5

**Description:**
List management operations with safety checks.

**Acceptance Criteria:**
- [ ] Rename list inline or via modal
- [ ] Delete list option in context menu
- [ ] Confirmation dialog for delete
- [ ] Choose action for tasks: move to Inbox or delete
- [ ] Cannot delete Inbox list
- [ ] Undo for accidental deletions
- [ ] Unit tests for list operations
- [ ] Integration tests for edge cases

**Business Rules:**
- Deleting list with tasks requires user choice
- Renamed lists update immediately
- Deleted lists removed from all views

---

### Story 2.7: List Navigation in Sidebar
**Effort:** 2 hours
**Prerequisites:** Story 2.6

**Description:**
Polished sidebar navigation with list management.

**Acceptance Criteria:**
- [ ] Collapsible sidebar on mobile
- [ ] Reorder lists via drag-and-drop
- [ ] List context menu (rename, delete, color)
- [ ] Keyboard navigation (arrow keys)
- [ ] Persist sidebar state (collapsed/expanded)
- [ ] Accessibility: ARIA labels and keyboard access
- [ ] Unit tests for navigation logic

**UX Requirements:**
- Smooth animations
- Touch-friendly on mobile
- Visual feedback for interactions

---

## Epic 3: Filtering & Search

**Priority:** P1
**Estimated Duration:** 1 week
**Goal:** Help users find and focus on relevant tasks

### Story 3.1: Search Functionality
**Effort:** 4 hours
**Prerequisites:** Epic 2 complete

**Description:**
Full-text search across task titles and descriptions.

**Acceptance Criteria:**
- [ ] Search input in header/toolbar
- [ ] Search as user types (debounced)
- [ ] Matches on title and description
- [ ] Case-insensitive search
- [ ] Highlight search terms in results
- [ ] Empty state when no matches
- [ ] Clear search button
- [ ] Keyboard shortcut (/)
- [ ] Unit tests for search logic
- [ ] Integration tests for search UX

**Technical Notes:**
- Debounce search input (300ms)
- Use fuzzy matching for better UX
- Maintain list filter during search

---

### Story 3.2: Filter - Active Tasks Only
**Effort:** 2 hours
**Prerequisites:** Story 3.1

**Description:**
Toggle to show only incomplete tasks.

**Acceptance Criteria:**
- [ ] "Active" filter button in toolbar
- [ ] Shows only incomplete tasks when enabled
- [ ] Visual indicator when filter active
- [ ] Persists across sessions
- [ ] Works with search and list filters
- [ ] Unit tests for filter logic

**UX Requirements:**
- Toggle button with clear label
- Count of active tasks displayed
- Smooth list transitions

---

### Story 3.3: Filter - Completed Tasks Only
**Effort:** 2 hours
**Prerequisites:** Story 3.2

**Description:**
View completed tasks separately for review.

**Acceptance Criteria:**
- [ ] "Completed" filter button in toolbar
- [ ] Shows only completed tasks when enabled
- [ ] Visual indicator when filter active
- [ ] Can mark tasks incomplete from this view
- [ ] Works with search and list filters
- [ ] Unit tests for filter logic

**UX Requirements:**
- Separate toggle from Active filter
- Option to bulk delete completed tasks
- Archive older completed tasks

---

### Story 3.4: View All Tasks Across Lists
**Effort:** 2 hours
**Prerequisites:** Story 3.3

**Description:**
"All Tasks" view that shows tasks from every list.

**Acceptance Criteria:**
- [ ] "All Tasks" option in list navigation
- [ ] Displays tasks from all lists with list badges
- [ ] Supports all filters and search
- [ ] Group by list option
- [ ] Sort options available
- [ ] Unit tests for cross-list view

**UI Requirements:**
- Visual indicators of task's list
- Option to group by list or show flat
- Counts for each list

---

### Story 3.5: Filter Persistence & URL State
**Effort:** 3 hours
**Prerequisites:** Story 3.4

**Description:**
Persist filter state in URL and local storage for shareability.

**Acceptance Criteria:**
- [ ] URL query params reflect active filters
- [ ] Shareable URLs maintain filter state
- [ ] Browser back/forward works correctly
- [ ] Filters persist across sessions (localStorage)
- [ ] Deep linking to specific views works
- [ ] Unit tests for URL state management

**Technical Notes:**
- Use URL query parameters: `?list=inbox&status=active`
- Sync URL with component state
- Handle invalid URL params gracefully

---

## Epic 4: Due Dates & Time Management

**Priority:** P2
**Estimated Duration:** 1.5 weeks
**Goal:** Add temporal context to tasks with due dates

### Story 4.1: Due Date Field on Tasks
**Effort:** 3 hours
**Prerequisites:** Epic 3 complete

**Description:**
Add optional due date field to task model and UI.

**Acceptance Criteria:**
- [ ] Task model updated with dueDate field (nullable)
- [ ] Database schema updated
- [ ] Due date displayed on task cards
- [ ] Relative date display ("Due tomorrow", "Overdue by 2 days")
- [ ] Type definitions updated
- [ ] Data migration for existing tasks
- [ ] Unit tests for date field

**Data Model Update:**
```typescript
interface Task {
  // ... existing fields
  dueDate?: Date;
}
```

---

### Story 4.2: Date Picker Component
**Effort:** 4 hours
**Prerequisites:** Story 4.1

**Description:**
Date picker UI for setting task due dates.

**Acceptance Criteria:**
- [ ] Date picker accessible from task detail
- [ ] Calendar view for date selection
- [ ] Quick options: Today, Tomorrow, Next Week, Next Month
- [ ] Remove date option
- [ ] Keyboard accessible
- [ ] Mobile-friendly date input
- [ ] Timezone handling
- [ ] Unit tests for date picker
- [ ] Integration tests for date selection

**UX Requirements:**
- Natural language input ("tomorrow", "next friday")
- Calendar icon indicator on tasks with dates
- Visual distinction for different date ranges

---

### Story 4.3: Today View
**Effort:** 3 hours
**Prerequisites:** Story 4.2

**Description:**
Smart list showing tasks due today.

**Acceptance Criteria:**
- [ ] "Today" view in sidebar navigation
- [ ] Shows tasks with due date = today
- [ ] Includes overdue tasks
- [ ] Tasks without dates optionally included
- [ ] Updates automatically at midnight
- [ ] Empty state encourages planning
- [ ] Unit tests for today filter logic

**Business Rules:**
- "Today" includes: dueDate = today OR dueDate < today
- Sort: overdue first, then by priority

---

### Story 4.4: Upcoming View
**Effort:** 3 hours
**Prerequisites:** Story 4.3

**Description:**
View tasks due in the next 7 days.

**Acceptance Criteria:**
- [ ] "Upcoming" view in sidebar
- [ ] Shows tasks due within next 7 days
- [ ] Grouped by date (Today, Tomorrow, This Week)
- [ ] Excludes completed tasks by default
- [ ] Sort by due date then priority
- [ ] Unit tests for upcoming filter

**UX Requirements:**
- Clear date groupings
- Count of tasks per date
- Quick reschedule options

---

### Story 4.5: Overdue Task Highlighting
**Effort:** 2 hours
**Prerequisites:** Story 4.4

**Description:**
Visual indicators for overdue tasks requiring attention.

**Acceptance Criteria:**
- [ ] Red color/icon for overdue tasks
- [ ] "Overdue" badge or label
- [ ] Overdue count in navigation
- [ ] Sort overdue tasks to top by default
- [ ] Notification or alert for overdue items
- [ ] Unit tests for overdue logic

**Visual Design:**
- Red accent color (urgent)
- Exclamation icon
- "X days overdue" text

---

### Story 4.6: Sort by Due Date
**Effort:** 2 hours
**Prerequisites:** Story 4.5

**Description:**
Sorting option to order tasks by due date.

**Acceptance Criteria:**
- [ ] Sort dropdown with "Due Date" option
- [ ] Ascending/descending toggle
- [ ] Tasks without dates at end (or option to hide)
- [ ] Sort persists across sessions
- [ ] Works with filters and search
- [ ] Unit tests for sort logic

**Sort Options:**
- Due Date (soonest first)
- Due Date (latest first)
- Created Date
- Priority

---

## Epic 5: Priorities & Subtasks

**Priority:** P2
**Estimated Duration:** 1.5 weeks
**Goal:** Enhanced organization for complex tasks

### Story 5.1: Priority Field Implementation
**Effort:** 3 hours
**Prerequisites:** Epic 4 complete

**Description:**
Add priority levels to tasks for importance ranking.

**Acceptance Criteria:**
- [ ] Task model updated with priority field (enum)
- [ ] Priority options: High, Medium, Low, None (default)
- [ ] Database schema updated
- [ ] Type definitions for Priority enum
- [ ] Data migration for existing tasks
- [ ] Unit tests for priority field

**Data Model:**
```typescript
enum Priority {
  None = 0,
  Low = 1,
  Medium = 2,
  High = 3
}

interface Task {
  // ... existing fields
  priority: Priority;
}
```

---

### Story 5.2: Priority Visual Indicators
**Effort:** 3 hours
**Prerequisites:** Story 5.1

**Description:**
Visual design for priority levels with colors and icons.

**Acceptance Criteria:**
- [ ] Priority dropdown on task detail
- [ ] Color coding: High=Red, Medium=Orange, Low=Blue, None=Gray
- [ ] Priority icon/badge on task cards
- [ ] Visual distinction in task list
- [ ] Accessible color choices (not color-only)
- [ ] Integration tests for priority selection

**Visual Design:**
- High: Red flag icon
- Medium: Orange circle
- Low: Blue dot
- None: No indicator

---

### Story 5.3: Sort by Priority
**Effort:** 2 hours
**Prerequisites:** Story 5.2

**Description:**
Sorting option to rank tasks by priority level.

**Acceptance Criteria:**
- [ ] "Priority" sort option in dropdown
- [ ] High priority tasks at top
- [ ] Secondary sort by due date or created date
- [ ] Works with all filters
- [ ] Sort persists across sessions
- [ ] Unit tests for priority sorting

**Sort Logic:**
- Primary: Priority (High → Medium → Low → None)
- Secondary: Due Date (soonest first)
- Tertiary: Created Date (newest first)

---

### Story 5.4: Subtask Data Model
**Effort:** 3 hours
**Prerequisites:** Story 5.3

**Description:**
Data structure for subtasks (checklist items) within tasks.

**Acceptance Criteria:**
- [ ] Subtask entity defined: id, parentTaskId, title, completed, order
- [ ] Database schema for subtasks table
- [ ] One-to-many relationship: Task → Subtasks
- [ ] Type definitions
- [ ] Data access layer for subtasks
- [ ] Unit tests for subtask operations

**Data Model:**
```typescript
interface Subtask {
  id: string;
  parentTaskId: string;
  title: string;
  completed: boolean;
  order: number;
  createdAt: Date;
}
```

---

### Story 5.5: Add/Edit/Delete Subtasks
**Effort:** 4 hours
**Prerequisites:** Story 5.4

**Description:**
UI for managing subtasks within task detail view.

**Acceptance Criteria:**
- [ ] Subtask list in expanded task view
- [ ] Add subtask input field
- [ ] Edit subtask inline
- [ ] Delete subtask with confirmation
- [ ] Reorder subtasks via drag-and-drop
- [ ] Keyboard shortcuts for subtask management
- [ ] Unit tests for subtask CRUD
- [ ] Integration tests for subtask UI

**UX Requirements:**
- Indent subtasks visually under parent
- Quick add (Enter key in input)
- Checkboxes for completion

---

### Story 5.6: Subtask Completion Tracking
**Effort:** 3 hours
**Prerequisites:** Story 5.5

**Description:**
Track and display subtask completion progress.

**Acceptance Criteria:**
- [ ] Toggle subtask completion status
- [ ] Subtask completion updates parent task
- [ ] Cannot complete parent while subtasks incomplete (optional)
- [ ] Optimistic updates
- [ ] Unit tests for completion logic

**Business Rules:**
- Completing parent task auto-completes all subtasks
- Subtask changes don't auto-complete parent

---

### Story 5.7: Progress Indicator for Parent Tasks
**Effort:** 2 hours
**Prerequisites:** Story 5.6

**Description:**
Visual progress bar showing subtask completion percentage.

**Acceptance Criteria:**
- [ ] Progress bar on tasks with subtasks
- [ ] Percentage display (e.g., "3/5 completed")
- [ ] Updates in real-time as subtasks complete
- [ ] Visual distinction for fully complete
- [ ] Works in collapsed task view
- [ ] Unit tests for progress calculation

**Visual Design:**
- Horizontal progress bar
- Percentage text (60%)
- Green fill for completed portion

---

## Epic 6: Tags & Advanced Filtering

**Priority:** P3
**Estimated Duration:** 1 week
**Goal:** Flexible categorization with tags

### Story 6.1: Tag Data Model & Relationships
**Effort:** 3 hours
**Prerequisites:** Epic 5 complete

**Description:**
Many-to-many relationship between tasks and tags.

**Acceptance Criteria:**
- [ ] Tag entity: id, name, color
- [ ] TaskTag join table for many-to-many
- [ ] Database schema for tags and relationships
- [ ] Type definitions
- [ ] Data access layer for tags
- [ ] Unit tests for tag operations

**Data Model:**
```typescript
interface Tag {
  id: string;
  name: string;
  color?: string;
}

interface TaskTag {
  taskId: string;
  tagId: string;
}
```

---

### Story 6.2: Add/Remove Tags on Tasks
**Effort:** 4 hours
**Prerequisites:** Story 6.1

**Description:**
UI for tagging tasks with multiple labels.

**Acceptance Criteria:**
- [ ] Tag input on task detail (autocomplete)
- [ ] Create new tags on-the-fly
- [ ] Display tags as chips on task cards
- [ ] Remove tag from task (click X on chip)
- [ ] Tag suggestions based on existing tags
- [ ] Keyboard navigation for tag input
- [ ] Unit tests for tagging logic
- [ ] Integration tests for tag UI

**UX Requirements:**
- Autocomplete dropdown
- Color-coded tag chips
- Quick add common tags

---

### Story 6.3: Tag Management Interface
**Effort:** 3 hours
**Prerequisites:** Story 6.2

**Description:**
Centralized tag management for renaming, coloring, and deleting.

**Acceptance Criteria:**
- [ ] Tag management page/modal
- [ ] List all tags with usage counts
- [ ] Rename tag (updates all tasks)
- [ ] Change tag color
- [ ] Delete tag (removes from all tasks)
- [ ] Merge duplicate tags
- [ ] Unit tests for tag management

**UI Requirements:**
- Search tags
- Sort by name or usage
- Bulk operations

---

### Story 6.4: Filter by Tags
**Effort:** 3 hours
**Prerequisites:** Story 6.3

**Description:**
Filter task list by selected tags.

**Acceptance Criteria:**
- [ ] Tag filter dropdown or sidebar section
- [ ] Select single or multiple tags
- [ ] Shows tasks matching ANY selected tag (OR logic)
- [ ] Clear filter option
- [ ] Works with other filters
- [ ] URL state for tag filters
- [ ] Unit tests for tag filtering

**UX Requirements:**
- Tag cloud or list in sidebar
- Count of tasks per tag
- Quick toggle tags on/off

---

### Story 6.5: Multi-Tag Filtering (AND/OR)
**Effort:** 3 hours
**Prerequisites:** Story 6.4

**Description:**
Advanced filtering with AND/OR logic for multiple tags.

**Acceptance Criteria:**
- [ ] Toggle between AND/OR filter modes
- [ ] AND: Tasks must have ALL selected tags
- [ ] OR: Tasks have ANY selected tag
- [ ] Visual indicator of current mode
- [ ] Persists filter mode preference
- [ ] Unit tests for complex tag queries

**UX Requirements:**
- Clear mode indicator
- Results count updates live
- Explain difference (tooltip)

---

## Epic 7: User Experience Enhancements

**Priority:** P2
**Estimated Duration:** 1 week
**Goal:** Polish and accessibility improvements

### Story 7.1: Keyboard Shortcuts Implementation
**Effort:** 4 hours
**Prerequisites:** All core features complete

**Description:**
Comprehensive keyboard shortcuts for power users.

**Acceptance Criteria:**
- [ ] Shortcut guide modal (? key)
- [ ] N: New task
- [ ] /: Focus search
- [ ] Cmd/Ctrl+K: Command palette
- [ ] Enter: Save/Submit
- [ ] Esc: Cancel/Close
- [ ] Arrow keys: Navigate tasks
- [ ] Space: Toggle task completion
- [ ] Del: Delete task
- [ ] E: Edit task
- [ ] M: Move to list
- [ ] P: Set priority
- [ ] D: Set due date
- [ ] Cmd/Ctrl+Z: Undo
- [ ] Prevent conflicts with browser shortcuts
- [ ] Unit tests for keyboard handlers

**Documentation:**
- In-app shortcut reference
- Visual hints for common shortcuts

---

### Story 7.2: Drag-and-Drop Task Reordering
**Effort:** 4 hours
**Prerequisites:** Story 7.1

**Description:**
Intuitive drag-and-drop for manual task ordering.

**Acceptance Criteria:**
- [ ] Drag handle on each task
- [ ] Drag to reorder within list
- [ ] Drag to move between lists
- [ ] Visual feedback during drag (ghost image)
- [ ] Drop zones highlighted
- [ ] Touch support for mobile
- [ ] Persist custom order
- [ ] Unit tests for drag logic
- [ ] Integration tests for drag UX

**UX Requirements:**
- Smooth animations
- Clear drop targets
- Undo capability

---

### Story 7.3: Task Completion Animations
**Effort:** 2 hours
**Prerequisites:** Story 7.2

**Description:**
Satisfying animations to celebrate task completion.

**Acceptance Criteria:**
- [ ] Subtle animation when marking complete
- [ ] Checkmark animation
- [ ] Strikethrough animation
- [ ] Optional confetti for completing all tasks
- [ ] Performance optimized (60fps)
- [ ] Respects reduced motion preferences
- [ ] Unit tests for animation triggers

**Animation Design:**
- 300ms duration
- Ease-out timing
- Subtle and professional

---

### Story 7.4: Dark Mode Support
**Effort:** 4 hours
**Prerequisites:** Story 7.3

**Description:**
Full dark theme for reduced eye strain.

**Acceptance Criteria:**
- [ ] Dark color palette defined
- [ ] Toggle between light/dark modes
- [ ] Respects system preference (prefers-color-scheme)
- [ ] All components styled for both themes
- [ ] Proper contrast ratios (WCAG AA)
- [ ] Theme preference persists
- [ ] Smooth theme transitions
- [ ] Integration tests for theme switching

**Color Palette:**
- Background: #1a1a1a
- Surface: #2d2d2d
- Text: #e0e0e0
- Accent: Adjusted brand colors

---

### Story 7.5: Accessibility Audit & Fixes
**Effort:** 4 hours
**Prerequisites:** Story 7.4

**Description:**
Comprehensive accessibility review and WCAG 2.1 AA compliance.

**Acceptance Criteria:**
- [ ] Semantic HTML throughout
- [ ] ARIA labels on interactive elements
- [ ] Keyboard navigation for all features
- [ ] Focus indicators visible
- [ ] Color contrast meets WCAG AA
- [ ] Screen reader tested (NVDA, VoiceOver)
- [ ] Alt text for images/icons
- [ ] Form labels properly associated
- [ ] Error messages accessible
- [ ] Automated accessibility tests (axe, lighthouse)

**Testing:**
- Manual screen reader testing
- Keyboard-only navigation test
- Color blindness simulation

---

### Story 7.6: Mobile Responsive Improvements
**Effort:** 3 hours
**Prerequisites:** Story 7.5

**Description:**
Optimize layout and interactions for mobile devices.

**Acceptance Criteria:**
- [ ] Responsive breakpoints defined
- [ ] Mobile-optimized task list layout
- [ ] Touch-friendly tap targets (44x44px min)
- [ ] Swipe gestures for actions
- [ ] Collapsible sidebar on mobile
- [ ] Mobile-friendly date picker
- [ ] Bottom navigation on mobile
- [ ] Tested on iOS and Android
- [ ] Performance optimized for mobile

**Mobile UX:**
- Swipe right: Complete task
- Swipe left: Delete task
- Pull to refresh
- Bottom sheet for task details

---

## Epic 8: Authentication & User Management

**Priority:** P1
**Estimated Duration:** 1 week
**Goal:** User accounts and data isolation

### Story 8.1: User Authentication System
**Effort:** 4 hours
**Prerequisites:** Core features complete

**Description:**
Implement user authentication with email/password.

**Acceptance Criteria:**
- [ ] User data model: id, email, passwordHash, createdAt
- [ ] Password hashing (bcrypt or similar)
- [ ] Authentication service/middleware
- [ ] Protected API routes
- [ ] Session management (JWT or cookies)
- [ ] Security best practices (rate limiting, HTTPS)
- [ ] Unit tests for auth logic
- [ ] Integration tests for auth flows

**Security Requirements:**
- Min password length: 8 characters
- Password complexity requirements
- Secure session tokens
- CSRF protection

---

### Story 8.2: Registration & Login Flows
**Effort:** 4 hours
**Prerequisites:** Story 8.1

**Description:**
User-facing registration and login pages.

**Acceptance Criteria:**
- [ ] Registration page with email/password
- [ ] Email validation
- [ ] Login page
- [ ] "Remember me" option
- [ ] Form validation and error messages
- [ ] Loading states during submission
- [ ] Redirect to app after successful auth
- [ ] "Welcome" message for new users
- [ ] Integration tests for auth flows

**UX Requirements:**
- Clean, distraction-free forms
- Inline validation
- Clear error messages
- Password visibility toggle

---

### Story 8.3: User-Specific Data Isolation
**Effort:** 3 hours
**Prerequisites:** Story 8.2

**Description:**
Ensure data is scoped to authenticated user.

**Acceptance Criteria:**
- [ ] User ID foreign key on tasks and lists
- [ ] Database queries filtered by user
- [ ] API endpoints validate user ownership
- [ ] Authorization checks on all operations
- [ ] No cross-user data leakage
- [ ] Unit tests for data isolation
- [ ] Security tests for unauthorized access

**Database Schema:**
```typescript
interface Task {
  // ... existing fields
  userId: string;
}

interface List {
  // ... existing fields
  userId: string;
}
```

---

### Story 8.4: Session Management
**Effort:** 3 hours
**Prerequisites:** Story 8.3

**Description:**
Secure session handling with timeout and renewal.

**Acceptance Criteria:**
- [ ] Session tokens with expiration
- [ ] Automatic token renewal
- [ ] Logout functionality
- [ ] Logout on all devices option
- [ ] Session timeout after inactivity
- [ ] Secure token storage (httpOnly cookies)
- [ ] Unit tests for session logic

**Security:**
- 7-day session duration
- Refresh token rotation
- Logout clears all session data

---

### Story 8.5: Password Reset Functionality
**Effort:** 4 hours
**Prerequisites:** Story 8.4

**Description:**
Self-service password recovery flow.

**Acceptance Criteria:**
- [ ] "Forgot password" link on login
- [ ] Email input to request reset
- [ ] Generate password reset token
- [ ] Send reset email (or log for dev)
- [ ] Reset token expiration (1 hour)
- [ ] New password input page
- [ ] Password updated successfully
- [ ] Invalidate old sessions
- [ ] Integration tests for reset flow

**Email Template:**
- Clear instructions
- Secure reset link
- Expiration notice
- Contact support link

---

## Summary & Dependencies

### Epic Dependency Chart
```
Epic 1 (Foundation)
  ↓
Epic 2 (Lists) ← Epic 8 (Auth)
  ↓
Epic 3 (Search/Filter)
  ↓
Epic 4 (Due Dates)
  ↓
Epic 5 (Priorities/Subtasks)
  ↓
Epic 6 (Tags) ← Epic 7 (UX Polish)
```

### Priority Ranking for MVP
1. **Epic 1** - Core Task Management (MUST)
2. **Epic 2** - Lists (MUST)
3. **Epic 8** - Authentication (MUST)
4. **Epic 3** - Search/Filter (MUST)
5. **Epic 7** - UX Enhancements (SHOULD)
6. **Epic 4** - Due Dates (SHOULD)
7. **Epic 5** - Priorities/Subtasks (SHOULD)
8. **Epic 6** - Tags (NICE TO HAVE)

### Total Story Count: 47 stories
### Estimated Total Effort: ~140 hours (8-10 weeks with testing/QA)

---

## Implementation Notes

**Development Approach:**
- Work through epics sequentially
- Each story should be independently deployable
- Test thoroughly before moving to next story
- Maintain feature flags for incomplete epics

**Quality Standards:**
- 80%+ unit test coverage
- Integration tests for all user flows
- E2E tests for critical paths
- Code review required for all stories

**Definition of Done:**
- Code complete and tested
- Documentation updated
- Accessibility verified
- Performance benchmarks met
- Product owner approval

---

**Next Steps:**
1. Review and prioritize epic/story breakdown
2. Assign stories to sprints
3. Begin technical design for Epic 1
4. Set up development environment
5. Start implementation with Story 1.1
