"""
This is the test suite for forest_fire.py.
"""

from unittest import TestCase, skip

from models.forest_fire import ForestFire, main, MODEL_NAME, ff_grps


class ForestFireTestCase(TestCase):
    def setUp(self):
        self.ff = ForestFire(MODEL_NAME, grp_struct=ff_grps)

    def tearDown(self):
        self.ff = None

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
