import json

import requests

from superagi_client.exceptions import http_status_code_to_exception
from superagi_client.types import *


class Superagi:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def create_agent(self, agent_config: AgentConfig):
        response = requests.post(
            f"{self.base_url}/api/v1/agent",
            headers={"X-api-key": self.api_key},
            data=json.dumps(agent_config.dict()),
        )
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                status_code=response.status_code, additional_info=response.text
            )
        )

    def update_agent(self, agent_id: int, agent_update_config: AgentUpdateConfig):
        response = requests.put(
            f"{self.base_url}/api/v1/agent/{agent_id}",
            headers={"X-api-key": self.api_key},
            data=json.dumps(agent_update_config.dict()),
        )
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                status_code=response.status_code, additional_info=response.text
            )
        )

    def pause_agent(self, agent_id: int, agent_run_ids: Optional[List[int]] = None):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/{agent_id}/pause",
            headers={"X-api-key": self.api_key},
            data=json.dumps(
                {"run_ids": agent_run_ids} if agent_run_ids is not None else {}
            ),
        )
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                status_code=response.status_code, additional_info=response.text
            )
        )

    def resume_agent(self, agent_id: int, agent_run_ids: Optional[List[int]] = None):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/{agent_id}/resume",
            headers={"X-api-key": self.api_key},
            data=json.dumps(
                {"run_ids": agent_run_ids} if agent_run_ids is not None else {}
            ),
        )
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                status_code=response.status_code, additional_info=response.text
            )
        )

    def create_agent_run(self, agent_id: int, agent_run: Optional[AgentRun] = None):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/{agent_id}/run",
            headers={"X-api-key": self.api_key},
            data=json.dumps(agent_run.dict() if agent_run is not None else {}),
        )
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                status_code=response.status_code, additional_info=response.text
            )
        )

    def get_agent_run_status(
        self, agent_id: int, agent_run_filter: Optional[AgentRunFilter] = None
    ):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/{agent_id}/run-status",
            headers={"X-api-key": self.api_key},
            data=json.dumps(
                agent_run_filter.dict() if agent_run_filter is not None else {}
            ),
        )
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                status_code=response.status_code, additional_info=response.text
            )
        )

    def get_agent_run_resources(self, agent_run_ids: List[int]):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/resources/output",
            headers={"X-api-key": self.api_key},
            data=json.dumps({"run_ids": agent_run_ids}),
        )
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                status_code=response.status_code, additional_info=response.text
            )
        )
