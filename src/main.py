import sqlite3
import os
import datetime
import uuid
import sys
from dotenv import load_dotenv

# Add project root to sys.path to resolve module imports
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)

from src.scrapers.company_scraper import scrape_company_names
from src.generators.users import generate_users
from src.generators.teams import generate_teams
from src.generators.projects import generate_projects
from src.generators.sections import generate_sections
from src.generators.tasks import generate_tasks
from src.generators.comments import generate_comments
from src.generators.tags import generate_tags_and_associations
from src.generators.custom_fields import generate_custom_fields
from src.models.models import Workspace

load_dotenv()

DATABASE_PATH = os.path.join(PROJECT_ROOT, 'output', 'asana_simulation.sqlite')
SCHEMA_PATH = os.path.join(PROJECT_ROOT, 'schema.sql')

def setup_database():
    """Sets up the SQLite database and creates tables from schema.sql."""
    output_dir = os.path.dirname(DATABASE_PATH)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if os.path.exists(DATABASE_PATH):
        os.remove(DATABASE_PATH)
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    with open(SCHEMA_PATH, 'r') as f:
        schema = f.read()
        cursor.executescript(schema)
        
    conn.commit()
    return conn

def main():
    """Main orchestration script for data generation."""
    conn = setup_database()
    cursor = conn.cursor()

    # Configuration
    NUM_USERS = 5000
    NUM_TEAMS = 50
    NUM_PROJECTS = 100
    NUM_TASKS = 20000
    NUM_COMMENTS = 5000

    # --- Data Generation ---
    company_name = scrape_company_names()[0] # Use the first company name

    # Workspace
    workspace = Workspace(
        workspace_id=str(uuid.uuid4()),
        name=company_name,
        created_at=datetime.datetime.now()
    )
    cursor.execute("INSERT INTO workspaces VALUES (?, ?, ?)", (workspace.workspace_id, workspace.name, workspace.created_at))

    # Users
    users = generate_users(NUM_USERS, company_name)
    for user in users:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (user.user_id, user.name, user.email, user.role, user.created_at))

    # Teams and Memberships
    teams, team_memberships = generate_teams(workspace.workspace_id, users, NUM_TEAMS)
    for team in teams:
        cursor.execute("INSERT INTO teams VALUES (?, ?, ?, ?, ?)", (team.team_id, team.workspace_id, team.name, team.description, team.created_at))
    for membership in team_memberships:
        cursor.execute("INSERT INTO team_memberships VALUES (?, ?)", (membership.team_id, membership.user_id))

    # Projects
    projects = generate_projects(teams, NUM_PROJECTS)
    for project in projects:
        cursor.execute("INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?)", (project.project_id, project.team_id, project.name, project.description, project.due_date, project.created_at, project.status))

    # Sections
    sections = generate_sections(projects)
    for section in sections:
        cursor.execute("INSERT INTO sections VALUES (?, ?, ?, ?)", (section.section_id, section.project_id, section.name, section.created_at))

    # Tasks
    tasks = generate_tasks(projects, sections, users, team_memberships, NUM_TASKS)
    for task in tasks:
        cursor.execute("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (task.task_id, task.project_id, task.section_id, task.parent_task_id, task.name, task.description, 
                        task.assignee_id, task.due_date, task.created_at, task.completed, task.completed_at))

    # Comments
    comments = generate_comments(tasks, users, NUM_COMMENTS)
    for comment in comments:
        cursor.execute("INSERT INTO comments VALUES (?, ?, ?, ?, ?)", (comment.comment_id, comment.task_id, comment.user_id, comment.created_at, comment.text_content))

    # Tags
    tags, task_tags = generate_tags_and_associations(tasks)
    for tag in tags:
        cursor.execute("INSERT INTO tags VALUES (?, ?, ?)", (tag.tag_id, tag.name, tag.color))
    for task_tag in task_tags:
        cursor.execute("INSERT INTO task_tags VALUES (?, ?)", (task_tag.task_id, task_tag.tag_id))

    # Custom Fields
    custom_field_defs, custom_field_vals = generate_custom_fields(projects, tasks)
    for definition in custom_field_defs:
        cursor.execute("INSERT INTO custom_field_definitions VALUES (?, ?, ?, ?, ?)", (definition.field_id, definition.project_id, definition.name, definition.type, definition.enum_options))
    for value in custom_field_vals:
        cursor.execute("INSERT INTO custom_field_values VALUES (?, ?, ?, ?)", (value.value_id, value.task_id, value.field_id, value.value))

    conn.commit()
    conn.close()
    print(f"Database '{DATABASE_PATH}' created successfully.")

if __name__ == '__main__':
    main()
