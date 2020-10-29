"""
This is the test suite for agent_registry.py.
"""

from unittest import TestCase, main

from lib.agent import Agent
from lib.env import Env
from registry.agent_registry import get_agent, reg_agent, get_env
from registry.agent_registry import del_agent, agent_reg

TEST_AGENT_NM = "Test agent"
TEST_ENV_NM = "Test env"


class AgentRegistryTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_agent(self):
        """
        See if we get an agent we have registered back.
        """
        agent_to_reg = Agent(TEST_AGENT_NM)
        reg_agent(TEST_AGENT_NM, agent_to_reg)
        self.assertEquals(agent_to_reg, get_agent(TEST_AGENT_NM))

    def test_get_env(self):
        """
        See if we get an env we have registered back as the env.
        """
        env_to_reg = Env(TEST_ENV_NM)
        reg_agent(TEST_ENV_NM, env_to_reg)
        self.assertEquals(env_to_reg, get_env())

    def test_reg_agent(self):
        """
        Test registering an agent.
        """
        reg_agent(TEST_AGENT_NM, Agent(TEST_AGENT_NM))
        self.assertIn(TEST_AGENT_NM, agent_reg)

    def test_del_agent(self):
        """
        Test deleting an agent.
        """
        reg_agent(TEST_AGENT_NM, Agent(TEST_AGENT_NM))
        del_agent(TEST_AGENT_NM)
        self.assertNotIn(TEST_AGENT_NM, agent_reg)
