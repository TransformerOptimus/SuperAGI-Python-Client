from typing import Optional, List

from pydantic import BaseModel


class AgentExecution(BaseModel):
    name: Optional[str]
    goal: Optional[List[str]]
    instruction: Optional[List[str]]
