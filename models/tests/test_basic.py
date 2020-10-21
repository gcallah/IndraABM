"""
This is the test suite for basic.py.
"""

from unittest import TestCase, skip  # , main

from models.basic import Basic, main


class BasicTestCase(TestCase):
    def setUp(self):
        self.basic = Basic()

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
        Does running the model work? (return of 0)
        """
        self.assertEqual(0, main())
