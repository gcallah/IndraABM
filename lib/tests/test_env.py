"""
This is the test suite for env.py.
"""
import os
from unittest import TestCase, main, skip

import lib.display_methods as disp
from lib.group import Group
from lib.env import Env, PopHist, POP_HIST_HDR, POP_SEP
from lib.space import DEF_HEIGHT, DEF_WIDTH
from lib.tests.test_agent import create_newton
from lib.tests.test_group import create_calcguys, create_cambguys
from lib.user import TEST, API
from lib.tests.test_agent import get_exec_key

travis = False

GRP1 = "Group1"
GRP2 = "Group2"

X = 0
Y = 1

ENV_ACT_RET = 10


def env_action(env, **kwargs):
    env.duration = ENV_ACT_RET


class EnvTestCase(TestCase):
    def setUp(self):
        self.exec_key = get_exec_key()
        self.newton = create_newton()
        self.calcs = create_calcguys(self.exec_key, [])
        self.cambs = create_cambguys(self.exec_key)
        self.pop_hist = PopHist()
        self.env = Env("Test env", action=env_action, exec_key=self.exec_key)

    def tearDown(self):
        self.exec_key = None
        self.newton = None
        self.calcs = None
        self.cambs = None
        self.pop_hist = None
        self.env = None

    def fill_pop_hist(self):
        self.pop_hist.record_pop(GRP1, 10)
        self.pop_hist.record_pop(GRP2, 10)
        self.pop_hist.record_pop(GRP1, 20)
        self.pop_hist.record_pop(GRP2, 20)
        return self.pop_hist

    def test_user_type(self):
        """
        Make sure our user type is test.
        """
        self.assertEqual(self.env.user_type, TEST)

    @skip("This test awaits new registry.")
    def test_runN(self):
        """
        Test running for N turns.
        """
        new_env = Env("Test1 env", action=env_action,
                      members=[self.newton])
        num_periods = 10
        acts = new_env.runN(num_periods)
        self.assertEqual(acts, num_periods)

    def test_str_pop(self):
        """
        Test converting the pop history to a string.
        """
        self.fill_pop_hist()
        s = str(self.pop_hist)
        self.assertEqual(s, POP_HIST_HDR + GRP1 + POP_SEP + GRP2 + POP_SEP)

    def test_record_pop(self):
        self.assertTrue(True)

    @skip("This now works differently and the test needs to be re-written")
    def test_add_child(self):
        self.env.add_child(self.newton, self.calcs)
        self.assertIn((self.newton, self.calcs), self.env.womb)

    def test_has_disp(self):
        if not disp.plt_present:
            self.assertTrue(not self.env.has_disp())
        else:
            self.assertTrue(self.env.has_disp())

    def test_line_data(self):
        """
        Test the construction of line graph data.
        This test must be changed to handle new color param!
        Commented out for the moment.
        """
        global travis
        travis = os.getenv("TRAVIS")
        if not travis:
            self.env.pop_hist = self.fill_pop_hist()
            ret = self.env.line_data()
            self.assertIn(GRP1, ret[1])
            self.assertIn(GRP2, ret[1])
            self.assertIn("color", ret[1][GRP1])
            self.assertIn("color", ret[1][GRP2])
            self.assertIn("data", ret[1][GRP1])
            self.assertIn("data", ret[1][GRP2])
#            self.assertEqual(ret, (2,
#                                   {GRP1: {"color": "navy", "data": [10, 20]},
#                                    GRP2: {"color": "blue", "data": [10, 20]}}))

    @skip("Some problem with returned plot data: also test is too coupled to code.")
    def test_plot_data(self):
        """
        Test the construction of scatter plot data.
        """
        global travis
        travis = os.getenv("TRAVIS")
        if not travis:
            our_grp = Group(GRP1, members=[self.newton], exec_key=self.exec_key)
            self.env = Env("Test env", members=[our_grp], exec_key=self.exec_key)
            ret = self.env.plot_data()
            (x, y) = self.newton.pos
            self.assertEqual(ret, {GRP1: {X: [x], Y: [y], 'color': None, 'marker': None}})

    def test_headless(self):
        if (self.env.user_type == API) or (self.env.user_type == TEST):
            self.assertTrue(self.env.headless())
        else:
            self.assertTrue(not self.env.headless())

    def test_env_action(self):
        self.env()
        self.assertEqual(self.env.duration, ENV_ACT_RET)

    @skip
    def test_restore_env(self):
        """
        This test depends upon a particular, stored json
        format: must be re-written.
        """
        tests_env = env_json_basic.ret()
        ret_env = Env("env", serial_obj=tests_env)
        self.assertEqual(str(type(ret_env)), "<class 'indra.env.Env'>")


if __name__ == '__main__':
    main()
