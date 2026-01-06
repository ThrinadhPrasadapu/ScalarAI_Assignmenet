import uuid
import datetime
import numpy as np
from src.models.models import Team, TeamMembership

def generate_teams(workspace_id, users, num_teams):
    """Generates teams and team memberships."""
    teams = []
    team_memberships = []
    team_names = ['Engineering', 'Product', 'Design', 'Marketing', 'Operations', 'Sales', 'Customer Support']
    
    for i in range(num_teams):
        team_name = np.random.choice(team_names) + f' {i+1}'
        team = Team(
            team_id=str(uuid.uuid4()),
            workspace_id=workspace_id,
            name=team_name,
            description=f'Team for {team_name}',
            created_at=datetime.datetime.now() - datetime.timedelta(days=np.random.randint(0, 365))
        )
        teams.append(team)

        # Assign users to the team
        num_members = np.random.randint(5, 15)
        members = np.random.choice(users, num_members, replace=False)
        for user in members:
            membership = TeamMembership(
                team_id=team.team_id,
                user_id=user.user_id
            )
            team_memberships.append(membership)
            
    return teams, team_memberships
