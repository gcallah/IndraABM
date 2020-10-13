"""
This is the test suite for model.py.
"""

from unittest import TestCase, main, skip

from lib.model import Model
from lib.env import Env

MSG = "Hello world"


class ModelTestCase(TestCase):
    def setUp(self):
        self.model = Model(model_nm="Test model")

    def tearDown(self):
        self.model = None

    def test_create_env(self):
        env = self.model.create_env()
        self.assertTrue(isinstance(env, Env))

    def test_create_groups(self):
        groups = self.model.create_groups()
        self.assertTrue(isinstance(groups, list))

    def test_to_json(self):
        rep = self.model.to_json()
        self.assertTrue(isinstance(rep, dict))


if __name__ == '__main__':
    main()
