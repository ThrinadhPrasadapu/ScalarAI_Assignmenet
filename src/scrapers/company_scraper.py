import os

def scrape_company_names():
    """Scrapes company names from a local file."""
    file_path = os.path.join(os.path.dirname(__file__), 'company_names.txt')
    with open(file_path, 'r') as f:
        names = [line.strip() for line in f.readlines()]
    return names
