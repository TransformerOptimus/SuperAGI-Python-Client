from pydantic import BaseModel
from typing import Optional, List

from superagi_client.dto.agent_schedule import AgentSchedule


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
