from typing import Protocol
from src.dto.task import TaskCreate, TaskUpdate, Task, TaskDetailed
from abc import abstractmethod


class TaskService(Protocol):
    
    @abstractmethod
    async def create(self, create_task: TaskCreate) -> Task: ...
    
    @abstractmethod
    async def get_all(self, user_id: int) -> list[TaskDetailed]: ...
    
    @abstractmethod
    async def get(self, task_id: int) -> TaskDetailed: ...
    
    @abstractmethod
    async def update(self, task_update: TaskUpdate): ...
    
    @abstractmethod
    async def delete(self, task_id: int): ...
    
    @abstractmethod
    async def complete(self, task_id: int): ...
    
    @abstractmethod
    async def uncomplete(self, task_id: int): ...
    
    @abstractmethod
    async def add_tag(self, task_id: int, tag_id: int): ...
    
    @abstractmethod
    async def remove_tag(self, task_id: int, tag_id: int): ...