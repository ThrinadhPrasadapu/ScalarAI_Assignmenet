import uuid
import json
import numpy as np
from src.models.models import CustomFieldDefinition, CustomFieldValue

def generate_custom_fields(projects, tasks):
    """Generates custom field definitions and values."""
    definitions = []
    values = []

    # Define a few custom fields
    priority_field = CustomFieldDefinition(
        field_id=str(uuid.uuid4()),
        project_id=None, # Workspace-level
        name='Priority',
        type='enum',
        enum_options=json.dumps(['High', 'Medium', 'Low'])
    )
    definitions.append(priority_field)

    status_field = CustomFieldDefinition(
        field_id=str(uuid.uuid4()),
        project_id=None, # Workspace-level
        name='Status',
        type='enum',
        enum_options=json.dumps(['Not Started', 'In Progress', 'Completed'])
    )
    definitions.append(status_field)

    # Assign custom field values to tasks
    for task in tasks:
        if np.random.rand() < 0.5: # 50% chance of having a priority
            value = CustomFieldValue(
                value_id=str(uuid.uuid4()),
                task_id=task.task_id,
                field_id=priority_field.field_id,
                value=np.random.choice(json.loads(priority_field.enum_options))
            )
            values.append(value)

        if np.random.rand() < 0.8: # 80% chance of having a status
            value = CustomFieldValue(
                value_id=str(uuid.uuid4()),
                task_id=task.task_id,
                field_id=status_field.field_id,
                value='Completed' if task.completed else np.random.choice(['Not Started', 'In Progress'])
            )
            values.append(value)

    return definitions, values
