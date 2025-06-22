from src.interfaces.task_service import TaskService
from src.infra.api_client import ApiClient
from src.dto.task import TaskCreate

class TaskServiceImpl(TaskService):
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client
    
    async def create(self, create_task: TaskCreate):
        json = create_task.model_dump_json()
        response = await self.api_client.post("/api/tasks")