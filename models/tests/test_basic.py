"""
This is the test suite for basic.py.
"""

from unittest import TestCase, main

from lib.composite import Composite
from models.basic import Basic


class BasicTestCase(TestCase):
    def setUp(self):
        self.basic = Basic()

    def tearDown(self):
        self.basic = None

    def test_create_groups(self):
        """
        See if we get a list of groups back from create_groups.
        """
        groups = self.basic.create_groups()
        for group in groups:
            if not isinstance(group, Composite):
                return False
        return True

    def test_run(self):
        """
        Does running the model work? (return of 0)
        """
        self.assertEqual(0, self.basic.run())
