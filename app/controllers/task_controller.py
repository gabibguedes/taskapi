from schemas.task import Task as SchemaTask
from models.task import Task as ModelTask
from fastapi_sqlalchemy import db


class TaskController:
    def add_new_task(self, task: SchemaTask):
      db_task = ModelTask(title=task.title, description=task.description)
      db.session.add(db_task)
      db.session.commit()
      return db_task

    def get_all_tasks(self):
      return db.session.query(ModelTask).all()
