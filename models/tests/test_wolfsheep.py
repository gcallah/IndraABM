"""
This is the test suite for wolfsheep.py.
"""

from unittest import TestCase, skip  # , main

from models.wolfsheep import WolfSheep, main, MODEL_NAME, basic_grps


class WolfSheepTestCase(TestCase):
    def setUp(self):
        self.wolfsheep = WolfSheep(MODEL_NAME, grp_struct=basic_grps)

    def tearDown(self):
        self.wolfsheep = None

    def test_run(self):
        """
        Does running the model work? (return of 0)
        """
        self.assertEqual(0, self.wolfsheep.run())

    def test_main(self):
        """
        Does the main func of the model work? (return of 0)
        """
        self.assertEqual(0, main())
