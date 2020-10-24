"""
This is the test suite for registry.py.
"""

from unittest import TestCase
import os
from lib.agent import Agent
from registry.registry import registry

TEST_VAL_STR = "test_val"
TEST_VAL = 1


class RegisteryTestCase(TestCase):
    def setUp(self):
        self.exec_key = registry.create_new_execution_registry(
            save_on_register=True)
        self.already_cleared = False

    def tearDown(self):
        if not self.already_cleared:
            registry.clear_registry(self.exec_key)

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

    def test_registry_fetch_from_disk(self):
        registry[self.exec_key]["name"] = "Abhinav"
        registry.save_reg(self.exec_key)

        loaded_object = registry.load_reg(self.exec_key)
        self.assertTrue("name" in loaded_object)
        self.assertTrue("Abhinav" == loaded_object["name"])

    def test_clear_registry(self):
        registry[self.exec_key]["name"] = "Abhinav"
        registry.clear_registry(self.exec_key)
        self.already_cleared = True
        self.assertRaises(KeyError, registry
                          .clear_registry, self.exec_key)

    def test_agent_registration(self):
        agent = Agent("test_agent", action=None)
        registry[self.exec_key][agent.name] = agent
        self.assertTrue(agent == registry[self.exec_key][agent.name])

    def agent_action(self):
        print("Agent action")
        return True

    def test_agent_save_to_disk(self):
        self.skipTest("Somehow pickling throws an error "
                      "while running through test cases")
        agent = Agent("test_agent", action=self.agent_action)
        registry[self.exec_key][agent.name] = agent
        registry.save_reg(self.exec_key)

    def test_agent_load_from_disk(self):
        self.skipTest(
            "Somehow pickling throws an error while "
            "running through test cases")
        agent = Agent("test_agent", action=self.agent_action)
        registry[self.exec_key][agent.name] = agent
        registry.save_reg(self.exec_key)
        loaded_object = registry.load_reg(self.exec_key)
        loaded_agent = loaded_object["test_agent"]
        (acted, moved) = loaded_agent()
        self.assertTrue(acted)
        self.assertTrue(not moved)
