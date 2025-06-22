from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    user: int
    project: Optional[int] = None
    tags: Optional[list[int]] = None
    name: str
    is_important: Optional[bool] = False
    notificate_date: Optional[datetime] = None
    end_at: Optional[datetime] = None
   
class TaskUpdate(BaseModel):
    name: Optional[str] = None
    is_important: Optional[bool] = None
    end_at: Optional[datetime] = None 
    notificate_date: Optional[datetime] = None

class Task(BaseModel):
    id: int
    name: str
    is_complete: Optional[bool] = False

class TaskDetailed(Task):
    user_id: int
    project_id: Optional[int] = None
    tags_id: Optional[list[int]] = None
    completed_by_user_id: Optional[int] = None
    notificate_date: Optional[datetime] = None
    is_important: Optional[bool] = False
    end_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

