from dataclasses import dataclass, field
from typing import List, Optional
import datetime

@dataclass
class Workspace:
    workspace_id: str
    name: str
    created_at: datetime.datetime

@dataclass
class User:
    user_id: str
    name: str
    email: str
    role: str
    created_at: datetime.datetime

@dataclass
class Team:
    team_id: str
    workspace_id: str
    name: str
    description: Optional[str]
    created_at: datetime.datetime

@dataclass
class TeamMembership:
    team_id: str
    user_id: str

@dataclass
class Project:
    project_id: str
    team_id: str
    name: str
    description: Optional[str]
    due_date: Optional[datetime.date]
    created_at: datetime.datetime
    status: str

@dataclass
class Section:
    section_id: str
    project_id: str
    name: str
    created_at: datetime.datetime

@dataclass
class Task:
    task_id: str
    project_id: str
    section_id: str
    parent_task_id: Optional[str]
    name: str
    description: Optional[str]
    assignee_id: Optional[str]
    due_date: Optional[datetime.date]
    created_at: datetime.datetime
    completed: bool
    completed_at: Optional[datetime.datetime]

@dataclass
class Comment:
    comment_id: str
    task_id: str
    user_id: str
    created_at: datetime.datetime
    text_content: str

@dataclass
class CustomFieldDefinition:
    field_id: str
    project_id: Optional[str]
    name: str
    type: str
    enum_options: Optional[str]

@dataclass
class CustomFieldValue:
    value_id: str
    task_id: str
    field_id: str
    value: str

@dataclass
class Tag:
    tag_id: str
    name: str
    color: Optional[str]

@dataclass
class TaskTag:
    task_id: str
    tag_id: str
