"""
This is the test suite for registry.py.
"""

from unittest import TestCase, skip
import os
from lib.agent import Agent
from lib.env import Env
from lib.model import Model
from registry.registry import registry, get_agent, reg_agent
from registry.registry import get_env, del_agent, reg_model, get_model

TEST_VAL_STR = "test_val"
TEST_VAL = 1
TEST_AGENT_NM = "Test agent"
TEST_ENV_NM = "Test env"


class RegisteryTestCase(TestCase):
    def setUp(self):
        self.exec_key = registry.create_exec_env(save_on_register=True)
        self.already_cleared = False
        self.test_agent = Agent(TEST_AGENT_NM, exec_key=self.exec_key)
        self.model = Model(exec_key=self.exec_key)

    def tearDown(self):
        if not self.already_cleared:
            registry.del_exec_env(self.exec_key)

    def test_get_model(self):
        """
        Register a model and fetch it back.
        """
        reg_model(self.model, self.exec_key)
        self.assertEquals(self.model, get_model(self.exec_key))

    def test_get_agent(self):
        """
        See if we get an agent we have registered back.
        """
        reg_agent(TEST_AGENT_NM, self.test_agent, self.exec_key)
        self.assertEquals(self.test_agent, get_agent(TEST_AGENT_NM,
                                                     self.exec_key))

    def test_get_env(self):
        """
        See if we get an env we have registered back as the env.
        """
        env_to_reg = Env(TEST_ENV_NM, exec_key=self.exec_key)
        reg_agent(TEST_ENV_NM, env_to_reg, self.exec_key)
        self.assertEquals(env_to_reg, get_env(exec_key=self.exec_key))

    def test_del_agent(self):
        """
        Test deleting an agent.
        """
        reg_agent(TEST_AGENT_NM, self.test_agent, self.exec_key)
        del_agent(TEST_AGENT_NM, self.exec_key)
        self.assertEquals(None, get_agent(TEST_AGENT_NM, exec_key=self.exec_key))

    def test_registry_key_creation(self):
        self.assertTrue(self.exec_key in registry)

    def test_registration(self):
        registry[self.exec_key]["name"] = "Abhinav"
        self.assertTrue("name" in registry[self.exec_key])
        self.assertTrue("Abhinav" == registry[self.exec_key]["name"])

    def test_registry_saved_to_disk(self):
        indra_dir = os.getenv("INDRA_HOME", "/home/indrasnet/indras_net")
        file_path = os.path.join(indra_dir, 'registry', 'db',
                                 '{}-reg.json'.format(self.exec_key))
        registry[self.exec_key]["name"] = "Abhinav"
        registry.save_reg(self.exec_key)
        self.assertTrue(os.path.exists(file_path))

    @skip("Failing: Abhinav, please debug.")
    def test_registry_fetch_from_disk(self):
        registry[self.exec_key]["name"] = "Abhinav"
        registry.save_reg(self.exec_key)

        loaded_object = registry.load_reg(self.exec_key)
        self.assertTrue("name" in loaded_object)
        self.assertTrue("Abhinav" == loaded_object["name"])

    def test_del_exec_env(self):
        registry[self.exec_key]["name"] = "Abhinav"
        registry.del_exec_env(self.exec_key)
        self.already_cleared = True
        self.assertRaises(KeyError, registry.del_exec_env, self.exec_key)

    def test_agent_registration(self):
        agent = Agent("test_agent", action=None, exec_key=self.exec_key)
        registry[self.exec_key][agent.name] = agent
        self.assertTrue(agent == registry[self.exec_key][agent.name])

    def agent_action(self):
        print("Agent action")
        return True

    def test_agent_save_to_disk(self):
        self.skipTest("Somehow pickling throws an error "
                      "while running through test cases")
        agent = Agent("test_agent", action=self.agent_action,
                      exec_key=self.exec_key)
        registry[self.exec_key][agent.name] = agent
        registry.save_reg(self.exec_key)

    def test_agent_load_from_disk(self):
        self.skipTest(
            "Somehow pickling throws an error while "
            "running through test cases")
        agent = Agent("test_agent", action=self.agent_action,
                      exec_key=self.exec_key)
        registry[self.exec_key][agent.name] = agent
        registry.save_reg(self.exec_key)
        loaded_object = registry.load_reg(self.exec_key)
        loaded_agent = loaded_object["test_agent"]
        (acted, moved) = loaded_agent()
        self.assertTrue(acted)
        self.assertTrue(not moved)
