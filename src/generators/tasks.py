import uuid
import datetime
import numpy as np
import openai
import os
from src.models.models import Task

# This is a placeholder for a more sophisticated LLM call
def generate_text_with_llm(prompt):
    # In a real scenario, you would use the openai library and your API key
    # For this simulation, we'll return a placeholder string
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=50)
    # return response.choices[0].text.strip()
    return f"Generated text for prompt: {prompt}"

def generate_tasks(projects, sections, users, team_memberships, num_tasks):
    """Generates tasks for the simulation."""
    tasks = []
    # Create a mapping from project_id to its sections
    project_sections = {p.project_id: [] for p in projects}
    for s in sections:
        project_sections[s.project_id].append(s)

    # Create a mapping from team_id to its members
    team_users = {t.team_id: [] for t in team_memberships}
    for tm in team_memberships:
        team_users[tm.team_id].append(tm.user_id)

    for _ in range(num_tasks):
        project = np.random.choice(projects)
        if not project_sections[project.project_id]:
            continue
        section = np.random.choice(project_sections[project.project_id])
        
        # Get users for the project's team
        assignee = None
        if team_users.get(project.team_id):
            assignee_id = np.random.choice(team_users[project.team_id] + [None], p=[0.85] + [0.15/len(team_users[project.team_id])]*(len(team_users[project.team_id])) if team_users[project.team_id] else [1.0])


        task_name_prompt = f"Generate a realistic task name for a {project.name} project."
        task_name = generate_text_with_llm(task_name_prompt)

        task_desc_prompt = f"Generate a brief description for the task '{task_name}'."
        task_description = generate_text_with_llm(task_desc_prompt)

        due_date = project.created_at + datetime.timedelta(days=np.random.randint(1, 90))
        completed = np.random.choice([True, False], p=[0.6, 0.4])
        completed_at = None
        if completed:
            completed_at = due_date - datetime.timedelta(days=np.random.randint(0, 14))

        task = Task(
            task_id=str(uuid.uuid4()),
            project_id=project.project_id,
            section_id=section.section_id,
            parent_task_id=None,  # Subtasks can be added later
            name=task_name,
            description=task_description,
            assignee_id=assignee_id,
            due_date=due_date.date(),
            created_at=project.created_at + datetime.timedelta(days=np.random.randint(0, 30)),
            completed=completed,
            completed_at=completed_at
        )
        tasks.append(task)

    return tasks
