# Asana RL Environment Seed Data Generator

## Overview

This project generates a realistic, high-quality seed dataset for a reinforcement learning environment simulating Asana. The dataset represents a B2B SaaS company with 5,000-10,000 employees, focusing on product development, marketing, and operations workflows.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy the `.env.example` file to a new file named `.env`.
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY='your-api-key'
     ```

## Usage

To generate the dataset and create the `asana_simulation.sqlite` database, run the main script:

```bash
python src/main.py
```

The final database will be saved in the `output/` directory.
