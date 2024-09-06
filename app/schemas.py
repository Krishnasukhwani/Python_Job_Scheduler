from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class JobCreate(BaseModel):
    name: str
    next_run: datetime
    schedule: List[str]

class Job(JobCreate):
    id: int
    last_run: Optional[datetime] = None

    class Config:
        from_attributes = True