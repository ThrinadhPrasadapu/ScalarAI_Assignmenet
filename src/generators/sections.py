import uuid
import datetime
from src.models.models import Section

def generate_sections(projects):
    """Generates default sections for each project."""
    sections = []
    default_sections = ['To Do', 'In Progress', 'Done']

    for project in projects:
        for section_name in default_sections:
            section = Section(
                section_id=str(uuid.uuid4()),
                project_id=project.project_id,
                name=section_name,
                created_at=project.created_at
            )
            sections.append(section)
            
    return sections
