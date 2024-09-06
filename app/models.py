from pydantic import BaseModel
from typing import List, Optional, Any
from datetime import datetime

class Job(BaseModel):
    id: Optional[str]
    name: str
    next_run: datetime
    weekdays: List[str]
    job_type: str
    job_details: str  # New field to store job details
    parameters: Optional[dict[str, Any]] = None

    class Config:
        from_attributes = True