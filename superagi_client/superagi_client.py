from typing import Optional, Any

from superagi_client.lib.auth import validate_api_key
from superagi_client.services.agent import Agent


class SuperagiClient:
    def __init__(
        self,
        api_key: str,
        host: Optional[str] = "app.superagi.com",
        port: Optional[int] = 80,
        agent=None,
        **kwargs: Any,
    ):
        self.host = host
        self.port = port
        self.api_key = api_key

        validate_api_key(base_url=f"{self.host}:{self.port}", api_key=self.api_key)

        if agent is None:
            agent = Agent(base_url=f"{self.host}:{self.port}", api_key=self.api_key)
        self.agent = agent
