from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class AgentSchedule(BaseModel):
    agent_id: Optional[int]
    start_time: datetime
    recurrence_interval: Optional[str] = None
    expiry_date: Optional[datetime] = None
    expiry_runs: Optional[int] = -1


class AgentConfig(BaseModel):
    name: str
    description: str
    project_id: Optional[int]
    goal: List[str]
    instruction: List[str]
    agent_workflow: str
    constraints: List[str]
    tools: List[dict]
    LTM_DB: Optional[str]
    exit: Optional[str]
    permission_type: Optional[str]
    iteration_interval: int
    model: str
    schedule: Optional[AgentSchedule]
    max_iterations: int
    user_timezone: Optional[str]
    knowledge: Optional[int]


class AgentUpdateConfig(BaseModel):
    name: Optional[str]
    description: Optional[str]
    project_id: Optional[int]
    goal: Optional[List[str]]
    instruction: Optional[List[str]]
    agent_workflow: Optional[str]
    constraints: Optional[List[str]]
    tools: Optional[List[dict]]
    LTM_DB: Optional[str]
    exit: Optional[str]
    permission_type: Optional[str]
    iteration_interval: Optional[int]
    model: Optional[str]
    schedule: Optional[AgentSchedule]
    max_iterations: Optional[int]
    user_timezone: Optional[str]
    knowledge: Optional[int]


class AgentRun(BaseModel):
    name: str
    goal: Optional[List[str]]
    instruction: Optional[List[str]]


class AgentRunFilter(BaseModel):
    run_ids: Optional[List[int]]
    run_status_filter: Optional[str]
