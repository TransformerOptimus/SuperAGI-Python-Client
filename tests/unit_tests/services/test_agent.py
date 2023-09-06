import pytest
from unittest.mock import patch

from superagi_client.dto.agent_config import AgentConfig
from superagi_client.dto.agent_execution import AgentExecution
from superagi_client.dto.agent_run_filter import AgentRunFilter
from superagi_client.dto.agent_update_config import AgentUpdateConfig
from superagi_client.services.agent import Agent


@pytest.fixture
def agent():
    return Agent(base_url="http://test.com", api_key="test_key")


def test_create(agent):
    agent_config = AgentConfig(
        name="test",
        description="test",
        iteration_interval=1,
        model="test",
        max_iterations=1,
        goal=["goal1", "goal2"],
        instruction=["instruction1", "instruction2"],
        agent_workflow="workflow",
        constraints=["constraint1", "constraint2"],
        tools=[{"name": "tool1"}, {"name": "tool2"}],
    )
    with patch.object(
        agent.superagi, "create_agent", return_value={"id": 1}
    ) as mock_create_agent:
        response = agent.create(agent_config)
        mock_create_agent.assert_called_once_with(agent_config=agent_config)
        assert response == {"id": 1}


def test_update(agent):
    agent_update_config = AgentUpdateConfig(name="test")
    with patch.object(
        agent.superagi, "update_agent", return_value={"id": 1}
    ) as mock_update_agent:
        response = agent.update(1, agent_update_config)
        mock_update_agent.assert_called_once_with(
            agent_id=1, agent_update_config=agent_update_config
        )
        assert response == {"id": 1}


def test_pause(agent):
    with patch.object(
        agent.superagi, "pause_agent", return_value={"status": "paused"}
    ) as mock_pause_agent:
        response = agent.pause(1)
        mock_pause_agent.assert_called_once_with(agent_id=1, agent_execution_ids=None)
        assert response == {"status": "paused"}


def test_resume(agent):
    with patch.object(
        agent.superagi, "resume_agent", return_value={"status": "resumed"}
    ) as mock_resume_agent:
        response = agent.resume(1)
        mock_resume_agent.assert_called_once_with(agent_id=1, agent_execution_ids=None)
        assert response == {"status": "resumed"}


def test_create_run(agent):
    agent_execution = AgentExecution(name="test")
    with patch.object(
        agent.superagi, "create_agent_run", return_value={"id": 1}
    ) as mock_create_agent_run:
        response = agent.create_run(1, agent_execution)
        mock_create_agent_run.assert_called_once_with(
            agent_id=1, agent_execution=agent_execution
        )
        assert response == {"id": 1}


def test_get_run_status(agent):
    agent_run_filter = AgentRunFilter(run_ids=[1])
    with patch.object(
        agent.superagi, "get_agent_run_status", return_value={"status": "running"}
    ) as mock_get_run_status:
        response = agent.get_run_status(1, agent_run_filter)
        mock_get_run_status.assert_called_once_with(
            agent_id=1, agent_run_filter=agent_run_filter
        )
        assert response == {"status": "running"}


def test_get_run_resources(agent):
    with patch.object(
        agent.superagi, "get_agent_run_resources", return_value={"resources": []}
    ) as mock_get_run_resources:
        response = agent.get_run_resources([1])
        mock_get_run_resources.assert_called_once_with(agent_resource_ids=[1])
        assert response == {"resources": []}
