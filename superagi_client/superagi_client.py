from typing import Any

from pydantic import validate_arguments

from superagi_client.lib.auth import validate_api_key
from superagi_client.lib.superagi import Superagi
from superagi_client.types import *


class SuperagiClient:
    def __init__(
        self,
        api_key: str,
        url: Optional[str] = "app.superagi.com:80",
        superagi=None,
        **kwargs: Any,
    ):
        self.api_key = api_key
        self.url = url
        self.superagi = None

        validate_api_key(base_url=f"{self.url}", api_key=self.api_key)

        if superagi is None:
            superagi = Superagi(base_url=self.url, api_key=self.api_key)
        self.superagi = superagi

    @validate_arguments
    def create_agent(self, agent_config: AgentConfig):
        response = self.superagi.create_agent(agent_config=agent_config)
        return response

    @validate_arguments
    def update_agent(self, agent_id: int, agent_update_config: AgentUpdateConfig):
        response = self.superagi.update_agent(
            agent_id=agent_id, agent_update_config=agent_update_config
        )
        return response

    @validate_arguments
    def pause_agent(self, agent_id: int, agent_run_ids: Optional[List[int]] = None):
        response = self.superagi.pause_agent(
            agent_id=agent_id, agent_run_ids=agent_run_ids
        )
        return response

    @validate_arguments
    def resume_agent(self, agent_id: int, agent_run_ids: Optional[List[int]] = None):
        response = self.superagi.resume_agent(
            agent_id=agent_id, agent_run_ids=agent_run_ids
        )
        return response

    @validate_arguments
    def create_agent_run(self, agent_id: int, agent_run: Optional[AgentRun] = None):
        response = self.superagi.create_agent_run(
            agent_id=agent_id, agent_run=agent_run
        )
        return response

    @validate_arguments
    def get_agent_run_status(
        self, agent_id: int, agent_run_filter: Optional[AgentRunFilter] = None
    ):
        response = self.superagi.get_agent_run_status(
            agent_id=agent_id, agent_run_filter=agent_run_filter
        )
        return response

    @validate_arguments
    def get_agent_run_resources(self, agent_resource_ids: List[int]):
        response = self.superagi.get_agent_run_resources(
            agent_resource_ids=agent_resource_ids
        )
        return response
