"""
This is the test suite for forest_fire.py.
"""

from unittest import TestCase, skip

from lib.agent import DONT_MOVE
from lib.model import create_agent
from models.forest_fire import ForestFire, main, MODEL_NAME, ff_grps
from models.forest_fire import tree_action


class ForestFireTestCase(TestCase):
    def setUp(self):
        self.ff = ForestFire(MODEL_NAME, grp_struct=ff_grps)
        self.tree = create_agent("tree", 1,
                                 exec_key=self.ff.exec_key)

    def tearDown(self):
        self.ff = None
        self.tree = None

    def test_tree_action(self):
        self.assertEqual(tree_action(self.tree), DONT_MOVE)

    def test_run(self):
        """
        Does running the model work? (return of 0)
        """
        self.assertEqual(0, self.ff.run())

    def test_main(self):
        """
        Does the main func of the model work? (return of 0)
        """
        self.assertEqual(0, main())
