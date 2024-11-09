from consumers.ag.record_consumer import *

class RecordService:

    @staticmethod
    def create_record(user_name, user_email, task_id, task_name, task_description):

        data = {
            "user_name": user_name,
            "user_email": user_email,
            "task_id": task_id,
            "task_name": task_name,
            "task_description": task_description
        }

        return create_record(data)
