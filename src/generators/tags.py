import uuid
import numpy as np
from src.models.models import Tag, TaskTag

def generate_tags_and_associations(tasks):
    """Generates tags and associates them with tasks."""
    tags = []
    task_tags = []
    tag_names = ['Bug', 'Feature', 'Design', 'Marketing', 'Urgent', 'Internal']
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

    for i, name in enumerate(tag_names):
        tag = Tag(
            tag_id=str(uuid.uuid4()),
            name=name,
            color=colors[i]
        )
        tags.append(tag)

    for task in tasks:
        if np.random.rand() < 0.3: # 30% chance of having a tag
            tag = np.random.choice(tags)
            task_tag = TaskTag(
                task_id=task.task_id,
                tag_id=tag.tag_id
            )
            task_tags.append(task_tag)

    return tags, task_tags
