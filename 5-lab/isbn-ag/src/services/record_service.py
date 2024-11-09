from consumers.users_ms.user_consumer import *
from consumers.tasks_ms.task_consumer import *

class RecordService:

    @staticmethod
    def create_record_service(data):

        user_data = {
            "name": data['user_name'],
            "email": data['user_email']
        }

        user = create_user(user_data)

        if user.status_code == 201:

            user_id = user.json()['user']['id']

            task_data = {
                "id": data['task_id'],
                "details":{
                    "name": data['task_name'],
                    "description": data['task_description'],
                    "user_id": user_id
                }
            }

            task = create_task(task_data)

            if task.status_code == 201:

                return True

        return False
