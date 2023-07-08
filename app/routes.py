from fastapi import APIRouter
from schemas.task import Task as SchemaTask
from controllers.task_controller import TaskController

router = APIRouter()
task_controller = TaskController()


@router.get('/')
async def api_root():
    return {'message': 'API is working!'}


@router.post('/tasks/', response_model=SchemaTask)
async def new_task(task: SchemaTask):
    return task_controller.add_new_task(task)


@router.get('/tasks/')
async def task():
    return task_controller.get_all_tasks()
