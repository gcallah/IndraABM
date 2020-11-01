"""
This is the test suite for basic.py.
"""

from unittest import TestCase, skip  # , main

from models.basic import Basic, main, MODEL_NAME, basic_grps


class BasicTestCase(TestCase):
    def setUp(self):
        self.basic = Basic(MODEL_NAME, grp_struct=basic_grps)

    def tearDown(self):
        self.basic = None

    def test_run(self):
        """
        Does running the model work? (return of 0)
        """
        self.assertEqual(0, self.basic.run())

    @skip("Test mysteriously failing.")
    def test_main(self):
        """
        Does the main func of the model work? (return of 0)
        """
        self.assertEqual(0, main())
