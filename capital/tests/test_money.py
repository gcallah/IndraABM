"""
This is the test suite for trade.py.
"""

from unittest import TestCase, main
from capital.trade_utils import AMT_AVAIL
# from indra.agent import Agent
# from capital.trade_utils import endow, get_rand_good,
# is_depleted, transfer
# from capital.trade_utils import rand_dist, equal_dist, GOODS
from capital.trade_utils import GOODS
import capital.money as mn
# import capital.trade_utils as tu


def header(s):
    print("\n==================")
    print(s)
    print("==================")


class MoneyTestCase(TestCase):
    def setUp(self, props=None):
        header("Setting up")
        self.goodA = {AMT_AVAIL: 10, mn.DUR: 0.6}
        self.goodB = {AMT_AVAIL: 8, mn.DUR: 0.9}
        self.trader = {}
        self.goods = {"a": self.goodA, "b": self.goodB}
        self.goods_dict_empty = {}

    def tearDown(self):
        header("Tearing down")
        self.goodA = None
        self.goodB = None
        self.trader = None
        self.goods = None

    def test_create_trader(self):
        header("Testing create_trader")
        self.trader[0] = mn.create_trader('Trader', 0)
        self.assertEqual(self.trader[0].name, "Trader0")
        self.assertEqual(self.trader[0][GOODS], {})
        self.assertEqual(self.trader[0]["util"], 0)

    def test_nature_to_traders(self):
        header("Testing nature_to_traders")
        self.trader[0] = mn.create_trader('Trader', 0)
        self.trader[1] = mn.create_trader('Trader', 1)
        mn.nature_to_traders(self.trader, self.goods)
        self.assertNotEqual(self.trader[0]["goods"], {})
        self.assertNotEqual(self.trader[1]["goods"], {})

    def test_main(self):
        self.assertEqual(mn.main(), 0)

    if __name__ == '__main__':
        main()
