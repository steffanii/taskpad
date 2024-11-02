#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Create new database migrations based on changes to models
python manage.py makemigrations

# Apply any outstanding database migrations
python manage.py migrate