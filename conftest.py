"""
Pytest configuration for Django tests.
This conftest.py ensures Django is properly set up before any tests are collected.
"""

import os
import sys

# Ensure the project root is in the path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

# Import and setup Django
import django

django.setup()
