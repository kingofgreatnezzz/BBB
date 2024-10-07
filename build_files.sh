#!/bin/bash
# Install the required dependencies
pip install -r requirements.txt

# Run collectstatic (for static files if needed)
python manage.py collectstatic --noinput
