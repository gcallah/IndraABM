"""
This is the test suite for panic.py.
"""

from unittest import TestCase, skip  # , main

from models.panic import Panic, main, MODEL_NAME, panic_grps
from models.panic import create_pagent, CM, PN, is_calm, is_panicking


class PanicTestCase(TestCase):
    def setUp(self):
        self.panic = Panic(MODEL_NAME, grp_struct=panic_grps)
        self.calm_agent = create_pagent("calm", 1, state=CM,
                                        exec_key=self.panic.exec_key)
        print(self.calm_agent["state"])
        self.panic_agent = create_pagent("panic", 1, state=PN,
                                         exec_key=self.panic.exec_key)

    def tearDown(self):
        self.panic = None
        self.calm_agent = None
        self.panic_agent = None

    def test_is_calm(self):
        self.assertTrue(is_calm(self.calm_agent))
        self.assertFalse(is_calm(self.panic_agent))

    def test_is_panicking(self):
        self.assertTrue(is_panicking(self.panic_agent))
        self.assertFalse(is_panicking(self.calm_agent))

    def test_run(self):
        """
        Does running the model work? (return of 0)
        """
        self.assertEqual(0, self.panic.run())

    def test_main(self):
        """
        Does the main func of the model work? (return of 0)
        """
        self.assertEqual(0, main())
