-- DDL for Asana Simulation Database

-- Organizations / Workspaces
CREATE TABLE workspaces (
    workspace_id TEXT PRIMARY KEY, -- UUID
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Users
CREATE TABLE users (
    user_id TEXT PRIMARY KEY, -- UUID
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    role TEXT, -- e.g., 'Admin', 'Member'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Teams
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY, -- UUID
    workspace_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (workspace_id) REFERENCES workspaces(workspace_id)
);

-- Team Memberships (Junction Table)
CREATE TABLE team_memberships (
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Projects
CREATE TABLE projects (
    project_id TEXT PRIMARY KEY, -- UUID
    team_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status TEXT, -- e.g., 'On Track', 'At Risk', 'Off Track'
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Sections
CREATE TABLE sections (
    section_id TEXT PRIMARY KEY, -- UUID
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Tasks
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY, -- UUID
    project_id TEXT NOT NULL,
    section_id TEXT NOT NULL,
    parent_task_id TEXT, -- For subtasks
    name TEXT NOT NULL,
    description TEXT,
    assignee_id TEXT,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed BOOLEAN DEFAULT 0,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- Comments / Stories
CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY, -- UUID
    task_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    text_content TEXT NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Custom Field Definitions
CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY, -- UUID
    project_id TEXT, -- Can be null if workspace-level
    name TEXT NOT NULL,
    type TEXT NOT NULL, -- e.g., 'text', 'number', 'enum', 'date'
    enum_options TEXT, -- JSON array for 'enum' type
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- Custom Field Values
CREATE TABLE custom_field_values (
    value_id TEXT PRIMARY KEY, -- UUID
    task_id TEXT NOT NULL,
    field_id TEXT NOT NULL,
    value TEXT NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id)
);

-- Tags
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY, -- UUID
    name TEXT NOT NULL UNIQUE,
    color TEXT
);

-- Task-Tag Associations (Junction Table)
CREATE TABLE task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);
