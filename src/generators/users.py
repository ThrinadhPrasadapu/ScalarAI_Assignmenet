import uuid
import datetime
import random
import numpy as np
from src.models.models import User

# Pre-defined lists to replace Faker
first_names = ['John', 'Jane', 'Peter', 'Emily', 'Michael', 'Sarah', 'David', 'Laura']
last_names = ['Smith', 'Jones', 'Williams', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore']

def generate_users(num_users, company_name):
    """Generates a list of users for the simulation."""
    users = []
    roles = ['Engineer', 'Product Manager', 'Designer', 'Marketing', 'Operations', 'Sales']
    role_distribution = [0.4, 0.15, 0.1, 0.15, 0.1, 0.1]

    for i in range(num_users):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        email_name = name.lower().replace(' ', '.')
        domain = f"{company_name.lower().replace(' ', '').replace('.', '')}.com"
        email = f"{email_name}{i}@{domain}"
        role = np.random.choice(roles, p=role_distribution)
        
        user = User(
            user_id=str(uuid.uuid4()),
            name=name,
            email=email,
            role=role,
            created_at=datetime.datetime.now() - datetime.timedelta(days=np.random.randint(0, 365*2))
        )
        users.append(user)
        
    return users
