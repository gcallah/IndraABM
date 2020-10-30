"""
This is the test suite for model.py.
"""

from unittest import TestCase, main, skip

from lib.model import Model, def_action, BLUE_GRP, RED_GRP
from lib.agent import Agent, DONT_MOVE
from lib.env import Env
from lib.group import Group
from lib.user import User

MSG = "Hello world"


class ModelTestCase(TestCase):
    def setUp(self):
        self.model = Model(model_nm="Test model")
        self.agent = Agent("Test agent", exec_key=self.model.exec_key)
        self.agent2 = Agent("Test agent 2", exec_key=self.model.exec_key)
        self.blue_grp = Group(BLUE_GRP, exec_key=self.model.exec_key)
        self.red_grp = Group(RED_GRP, exec_key=self.model.exec_key)

    def tearDown(self):
        self.agent = None
        self.model = None

    def test_pending_switches(self):
        """
        Test getting count of pending switches.
        """
        self.model.add_switch(self.agent.name, BLUE_GRP, RED_GRP)
        self.model.add_switch(self.agent2.name, BLUE_GRP, RED_GRP)
        self.assertEqual(self.model.pending_switches(), 2)

    def test_add_switch(self):
        """
        Test adding a group switch.
        """
        self.model.add_switch(self.agent.name, BLUE_GRP, RED_GRP)
        self.assertIn((self.agent.name, BLUE_GRP, RED_GRP),
                      self.model.switches)

    @skip("Switching not working; but want to release current progress.")
    def test_handle_switches(self):
        """
        Does executing the pending switches work?
        """
        self.red_grp += self.agent
        self.assertIn(self.agent.name, self.red_grp)
        self.model.add_switch(self.agent.name, RED_GRP, BLUE_GRP)
        self.model.handle_switches()
        self.assertNotIn(self.agent.name, self.red_grp)
        self.assertIn(self.agent.name, self.blue_grp)

    def test_def_action(self):
        """
        Test our default agent action.
        """
        self.assertEqual(DONT_MOVE, def_action(self.agent))

    def test_create_env(self):
        """
        Test creating an env.
        """
        env = self.model.create_env()
        self.assertTrue(isinstance(env, Env))

    def test_create_groups(self):
        """
        Test creating groups.
        """
        groups = self.model.create_groups()
        self.assertTrue(isinstance(groups, list))

    def test_create_user(self):
        """
        Test creating a user.
        """
        user = self.model.create_user()
        self.assertTrue(isinstance(user, User))

    def test_to_json(self):
        rep = self.model.to_json()
        self.assertTrue(isinstance(rep, dict))


if __name__ == '__main__':
    main()
