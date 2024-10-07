#!/bin/bash
# Install pip (if needed)
if ! command -v pip &> /dev/null
then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --user
fi

# Install the required dependencies
pip install -r requirements.txt

# Run collectstatic (for static files if needed)
python manage.py collectstatic --noinput
