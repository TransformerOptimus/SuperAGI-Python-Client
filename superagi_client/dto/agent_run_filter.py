from typing import Optional, List

from pydantic import BaseModel


class AgentRunFilter(BaseModel):
    run_ids: Optional[List[int]]
    run_status_filter: Optional[str]
