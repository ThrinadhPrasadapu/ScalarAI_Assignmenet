import uuid
import datetime
import numpy as np
from src.models.models import Project

def generate_projects(teams, num_projects):
    """Generates projects for the simulation."""
    projects = []
    project_name_templates = [
        'Q{q} {year} {team_name} Roadmap',
        '{team_name} Website Redesign',
        'New Feature: {feature}',
        'Mobile App v{version} Launch',
        '{campaign} Marketing Campaign'
    ]
    features = ['SSO Integration', 'Dashboard Analytics', 'User Profile Overhaul', 'API v2']
    campaigns = ['Summer Sale', 'Holiday Promotion', 'New User Onboarding']
    statuses = ['On Track', 'At Risk', 'Off Track']

    for _ in range(num_projects):
        team = np.random.choice(teams)
        q = np.random.randint(1, 5)
        year = datetime.date.today().year
        template = np.random.choice(project_name_templates)
        name = template.format(
            q=q, 
            year=year, 
            team_name=team.name, 
            feature=np.random.choice(features), 
            version=f'{np.random.randint(1, 4)}.{np.random.randint(0, 10)}', 
            campaign=np.random.choice(campaigns)
        )

        project = Project(
            project_id=str(uuid.uuid4()),
            team_id=team.team_id,
            name=name,
            description=f'Project to deliver on {name}',
            due_date=datetime.date.today() + datetime.timedelta(days=np.random.randint(30, 180)),
            created_at=datetime.datetime.now() - datetime.timedelta(days=np.random.randint(0, 180)),
            status=np.random.choice(statuses, p=[0.7, 0.2, 0.1])
        )
        projects.append(project)
        
    return projects
