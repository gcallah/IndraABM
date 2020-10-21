"""
This is the test suite for model.py.
"""

from unittest import TestCase, main, skip

from lib.model import Model, def_action
from lib.agent import Agent, DONT_MOVE
from lib.env import Env
from lib.user import User

MSG = "Hello world"


class ModelTestCase(TestCase):
    def setUp(self):
        self.agent = Agent("Test agent")
        self.model = Model(model_nm="Test model")

    def tearDown(self):
        self.agent = None
        self.model = None

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
