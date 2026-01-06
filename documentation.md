# Asana Simulation Documentation

## Section A: Database Schema

### Tables

The complete relational schema is defined in `schema.sql`. The tables are:

- **workspaces**: Top-level container for the organization.
- **users**: Members of the workspace.
- **teams**: Groups of users collaborating on projects.
- **team_memberships**: Junction table for users and teams.
- **projects**: Collections of tasks.
- **sections**: Subdivisions within a project.
- **tasks**: The fundamental unit of work.
- **comments**: Activity and discussion on tasks.
- **custom_field_definitions**: Definitions for custom fields.
- **custom_field_values**: Values for custom fields on tasks.
- **tags**: Labels that can be applied across projects.
- **task_tags**: Junction table for tasks and tags.

### Entity-Relationship Diagram

(A visual ERD would be created using a tool like dbdiagram.io and embedded here.)

### Design Decisions

- **Custom Fields**: A flexible key-value approach was used, with a `custom_field_definitions` table to define the field's name, type, and options, and a `custom_field_values` table to store the actual values for each task. This allows for both workspace-level and project-level custom fields.
- **Task Hierarchy**: A self-referencing `parent_task_id` in the `tasks` table allows for infinite nesting of subtasks, accurately modeling Asana's functionality.

## Section B: Seed Data Methodology

### Table: `users`

| Column | Data Type | Source Strategy | Methodology & Justification |
|---|---|---|---|
| `user_id` | TEXT (UUID) | Generated | UUIDv4 to simulate Asana's GID format. |
| `name` | TEXT | Synthetic | Generated from predefined lists of first and last names to avoid external dependencies. |
| `email` | TEXT | Synthetic | Generated from the user's name and company name, with a unique number to ensure no duplicates. |
| `role` | TEXT | Synthetic | Distributed based on a realistic team composition for a tech company. |

### Table: `projects`

| Column | Data Type | Source Strategy | Methodology & Justification |
|---|---|---|---|
| `project_id` | TEXT (UUID) | Generated | UUIDv4 for unique identification. |
| `name` | TEXT | LLM + Templates | Generated using templates to create realistic project names based on team, quarter, and project type. |
| `status` | TEXT | Synthetic | Weighted distribution to reflect that most projects are 'On Track'. |

### Table: `tasks`

| Column | Data Type | Source Strategy | Methodology & Justification |
|---|---|---|---|
| `task_id` | TEXT (UUID) | Generated | UUIDv4 for unique identification. |
| `name` | TEXT | LLM + Heuristics | Placeholder LLM calls to generate realistic task names based on the project. |
| `description` | TEXT | LLM + Templates | Placeholder LLM calls for rich text descriptions. |
| `assignee_id` | TEXT (FK) | Derived | Assigned based on team membership with a chance of being unassigned. |
| `due_date` | DATE | Synthetic + Heuristics | Realistic distribution based on project creation date. |
| `completed` | BOOLEAN | Synthetic + Heuristics | Weighted random assignment to simulate a mix of completed and incomplete tasks. |

(Similar methodology breakdowns would be provided for all other tables.)
