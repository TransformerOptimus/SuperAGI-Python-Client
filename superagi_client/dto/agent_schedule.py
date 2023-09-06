from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AgentSchedule(BaseModel):
    agent_id: Optional[int]
    start_time: datetime
    recurrence_interval: Optional[str] = None
    expiry_date: Optional[datetime] = None
    expiry_runs: Optional[int] = -1
