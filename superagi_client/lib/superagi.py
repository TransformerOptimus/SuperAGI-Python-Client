import json
from typing import Optional, List

import requests

from superagi_client.dto.agent_config import AgentConfig
from superagi_client.dto.agent_update_config import AgentUpdateConfig
from superagi_client.dto.agent_execution import AgentExecution
from superagi_client.dto.agent_run_filter import AgentRunFilter
from superagi_client.exceptions.http_exception import http_status_code_to_exception
from superagi_client.lib.logger import logger


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
        logger.debug(response.text)
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                response.status_code, additional_info=response.text
            )
        )

    def update_agent(self, agent_id: int, agent_update_config: AgentUpdateConfig):
        response = requests.put(
            f"{self.base_url}/api/v1/agent/{agent_id}",
            headers={"X-api-key": self.api_key},
            data=json.dumps(agent_update_config.dict()),
        )
        logger.debug(response.text)
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                response.status_code, additional_info=response.text
            )
        )

    def pause_agent(
        self, agent_id: int, agent_execution_ids: Optional[List[int]] = None
    ):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/{agent_id}/pause",
            headers={"X-api-key": self.api_key},
            data=json.dumps(
                {"run_ids": agent_execution_ids}
                if agent_execution_ids is not None
                else {}
            ),
        )
        logger.debug(response.text)
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                response.status_code, additional_info=response.text
            )
        )

    def resume_agent(
        self, agent_id: int, agent_execution_ids: Optional[List[int]] = None
    ):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/{agent_id}/resume",
            headers={"X-api-key": self.api_key},
            data=json.dumps(
                {"run_ids": agent_execution_ids}
                if agent_execution_ids is not None
                else {}
            ),
        )
        logger.debug(response.text)
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                response.status_code, additional_info=response.text
            )
        )

    def create_agent_run(
        self, agent_id: int, agent_execution: Optional[AgentExecution] = None
    ):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/{agent_id}/run",
            headers={"X-api-key": self.api_key},
            data=json.dumps(
                agent_execution.dict() if agent_execution is not None else {}
            ),
        )
        logger.debug(response.text)
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                response.status_code, additional_info=response.text
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
        logger.debug(response.text)
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                response.status_code, additional_info=response.text
            )
        )

    def get_agent_run_resources(self, agent_resource_ids: List[int]):
        response = requests.post(
            f"{self.base_url}/api/v1/agent/resources/output",
            headers={"X-api-key": self.api_key},
            data=json.dumps({"run_ids": agent_resource_ids}),
        )
        logger.debug(response.text)
        return (
            response.json()
            if response.status_code == 200
            else http_status_code_to_exception(
                response.status_code, additional_info=response.text
            )
        )
