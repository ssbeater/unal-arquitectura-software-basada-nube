import requests

from config import ISBN_TASKS_MS_API_URL

base_url = ISBN_TASKS_MS_API_URL

# Create Task
def create_task(data):

    url = base_url

    response = requests.post(url, json=data)

    return response
