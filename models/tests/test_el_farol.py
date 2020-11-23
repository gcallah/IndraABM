"""
This is the test suite for el_farol.py.
"""

from unittest import TestCase, main,skip


import models.el_farol as el_farol
from models.el_farol import AT_BAR, AT_HOME, MOTIV, MODEL_NAME
from models.el_farol import ElFarol, el_farol_grps

def header(s):
    print("\n==================")
    print(s)
    print("==================")

class ElFarolTestCase(TestCase):
    
    def setUp(self):
        header("Setting up")
        groups = []
        self.ef = ElFarol(MODEL_NAME, grp_struct=el_farol_grps)
        #create an evirement for testing and get exect key

    def tearDown(self):
        """
        This should undo what setup() does!
        """
        header("Tearing Down")
        self.bob = None
    def test_main(self):
        self.assertEqual(el_farol.main(), 0)

    @skip("Not implimented yet")
    def test_create_non_drinker(self):
        """
        Test creating a non-drinker.
        """
        agent = el_farol.create_non_drinker(DRINKERS, 0)
        self.assertIn(MOTIV, agent)

    @skip("Not implimented yet")
    def test_create_drinker(self):
        """
        Test creating a drinker.
        """
        agent = el_farol.create_drinker(NON_DRINKERS, 0)
        self.assertIn(MOTIV, agent)
    @skip("Not implimented yet")
    def test_discourage(self):
        discouraged = el_farol.discourage(1)
        self.assertEqual(discouraged, 1)

    if __name__ == '__main__':
        main()
