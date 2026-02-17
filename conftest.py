import os
import django
from django.conf import settings

# Configure Django settings for pytest
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

def pytest_configure():
    django.setup()
