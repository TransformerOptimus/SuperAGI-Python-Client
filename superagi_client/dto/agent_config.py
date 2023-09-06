from typing import Optional, List

from pydantic import BaseModel

from superagi_client.dto.agent_schedule import AgentSchedule


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
