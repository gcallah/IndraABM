"""
This is the test suite for forest_fire.py.
"""

from unittest import TestCase, skip

from lib.agent import DONT_MOVE
from models.forest_fire import ForestFire, main, MODEL_NAME, ff_grps
from models.forest_fire import tree_action, plant_tree, is_healthy, is_on_fire


class ForestFireTestCase(TestCase):
    def setUp(self):
        self.ff = ForestFire(MODEL_NAME, grp_struct=ff_grps)
        self.htree = plant_tree("tree", 1,
                                exec_key=self.ff.exec_key)

    def tearDown(self):
        self.ff = None
        self.htree = None

    def test_tree_action(self):
        """
        Does the tree action return DONT_MOVE?
        """
        self.assertEqual(tree_action(self.htree), DONT_MOVE)

    def test_is_healthy(self):
        """
        Checking whether the state is healthy or not
        """
        self.assertTrue(is_healthy(self.htree))


    def test_is_on_fire(self):
        """
        Checking whether the state is on fire or not
        """
        pass

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
