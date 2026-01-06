import uuid
import datetime
import numpy as np
from src.models.models import Comment

def generate_comments(tasks, users, num_comments):
    """Generates comments for tasks."""
    comments = []
    comment_templates = [
        "@{} what's the status on this?",
        "This is blocked by {}.",
        "Just pushed a fix for this.",
        "Can you review my latest changes?",
        "This is ready for QA."
    ]

    for _ in range(num_comments):
        task = np.random.choice(tasks)
        user = np.random.choice(users)
        mentioned_user = np.random.choice(users)
        blocking_task = np.random.choice(tasks)

        text_content = np.random.choice(comment_templates).format(mentioned_user.name, blocking_task.name)

        comment = Comment(
            comment_id=str(uuid.uuid4()),
            task_id=task.task_id,
            user_id=user.user_id,
            created_at=task.created_at + datetime.timedelta(days=np.random.randint(1, 5)),
            text_content=text_content
        )
        comments.append(comment)

    return comments
