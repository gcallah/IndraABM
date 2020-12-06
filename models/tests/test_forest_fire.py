"""
This is the test suite for forest_fire.py.
"""

from unittest import TestCase, skip

from lib.agent import DONT_MOVE
from models.forest_fire import ForestFire, main, MODEL_NAME, ff_grps, OF
from models.forest_fire import tree_action, plant_tree


class ForestFireTestCase(TestCase):
    def setUp(self):
        self.ff = ForestFire(MODEL_NAME, grp_struct=ff_grps)
        self.htree = plant_tree("htree", 1,
                                exec_key=self.ff.exec_key)
        self.oftree = plant_tree("oftree", 1, state=OF,
                                 exec_key=self.ff.exec_key)

    def tearDown(self):
        self.ff = None
        self.htree = None
        self.oftree = None

    @skip
    def test_tree_action(self):
        """
        Does the tree action return DONT_MOVE?
        """
        self.assertEqual(tree_action(self.htree), DONT_MOVE)

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
