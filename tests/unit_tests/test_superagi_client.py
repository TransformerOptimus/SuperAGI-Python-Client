import pytest
from unittest.mock import patch
from superagi_client import SuperagiClient
from superagi_client.types import (
    AgentConfig,
    AgentUpdateConfig,
    AgentRun,
    AgentRunFilter,
)


@pytest.fixture
def client():
    return SuperagiClient(api_key="test_key", url="http://mockurl.com")


def test_create_agent(client):
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
        client.superagi, "create_agent", return_value={"id": 1}
    ) as mock_create_agent:
        response = client.create_agent(agent_config)
        mock_create_agent.assert_called_once_with(agent_config=agent_config)
        assert response == {"id": 1}


def test_update_agent(client):
    agent_update_config = AgentUpdateConfig(name="test")
    with patch.object(
        client.superagi, "update_agent", return_value={"id": 1}
    ) as mock_update_agent:
        response = client.update_agent(1, agent_update_config)
        mock_update_agent.assert_called_once_with(
            agent_id=1, agent_update_config=agent_update_config
        )
        assert response == {"id": 1}


def test_pause_agent(client):
    with patch.object(
        client.superagi, "pause_agent", return_value={"status": "paused"}
    ) as mock_pause_agent:
        response = client.pause_agent(1)
        mock_pause_agent.assert_called_once_with(agent_id=1, agent_run_ids=None)
        assert response == {"status": "paused"}


def test_resume_agent(client):
    with patch.object(
        client.superagi, "resume_agent", return_value={"status": "resumed"}
    ) as mock_resume_agent:
        response = client.resume_agent(1)
        mock_resume_agent.assert_called_once_with(agent_id=1, agent_run_ids=None)
        assert response == {"status": "resumed"}


def test_create_agent_run(client):
    agent_run = AgentRun(name="test")
    with patch.object(
        client.superagi, "create_agent_run", return_value={"id": 1}
    ) as mock_create_agent_run:
        response = client.create_agent_run(1, agent_run)
        mock_create_agent_run.assert_called_once_with(agent_id=1, agent_run=agent_run)
        assert response == {"id": 1}


def test_get_agent_run_status(client):
    agent_run_filter = AgentRunFilter(run_ids=[1])
    with patch.object(
        client.superagi, "get_agent_run_status", return_value={"status": "running"}
    ) as mock_get_run_status:
        response = client.get_agent_run_status(1, agent_run_filter)
        mock_get_run_status.assert_called_once_with(
            agent_id=1, agent_run_filter=agent_run_filter
        )
        assert response == {"status": "running"}


def test_get_agent_run_resources(client):
    with patch.object(
        client.superagi, "get_agent_run_resources", return_value={"resources": []}
    ) as mock_get_run_resources:
        response = client.get_agent_run_resources([1])
        mock_get_run_resources.assert_called_once_with(agent_resource_ids=[1])
        assert response == {"resources": []}
