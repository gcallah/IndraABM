"""
This is the test suite for utils.py.
"""

import os
from unittest import TestCase, skip

from lib.utils import Debug
from lib.utils import INDRA_DEBUG_VAR, INDRA_DEBUG2_VAR, INDRA_DEBUG3_VAR
from lib.utils import INDRA_DEBUG_LIB_VAR, INDRA_DEBUG2_LIB_VAR


def set_debug_env_vars_to(variables, value):
    """
    Sets the environment variables for debugging to the given value
    """
    for var in variables:
        os.environ[var] = value


class DebugTestCase(TestCase):
    def setUp(self):
        """
        Remove related environment variables for this test
        """
        self.debug_variables = [
            INDRA_DEBUG_VAR,
            INDRA_DEBUG2_VAR,
            INDRA_DEBUG3_VAR,
            INDRA_DEBUG_LIB_VAR,
            INDRA_DEBUG2_LIB_VAR,
        ]

        for var in self.debug_variables:
            os.environ.pop(var, None)

    def tearDown(self):
        """
        There is no need to restore the environment variables since they were temporarily set
        """
        pass

    def test_debug_without_env_var_set(self):
        """
        Test the default value without any environment variable set

        Debug statements are expected to be disabled when not related environment variables are set
        """
        self.assertFalse(Debug().debug)
        self.assertFalse(Debug().debug2)
        self.assertFalse(Debug().debug3)

        self.assertFalse(Debug().debug_lib)
        self.assertFalse(Debug().debug2_lib)

    def test_debug_wit_env_var_set_to_1(self):
        """
        Test debugging statements when they are set to "1"
        """
        set_debug_env_vars_to(self.debug_variables, "1")

        self.assertTrue(Debug().debug)
        self.assertTrue(Debug().debug2)
        self.assertTrue(Debug().debug3)

        self.assertTrue(Debug().debug_lib)
        self.assertTrue(Debug().debug2_lib)

    def test_debug_wit_env_var_set_to_True(self):
        """
        Test debugging statements when they are set to "True"
        """
        set_debug_env_vars_to(self.debug_variables, "True")

        self.assertTrue(Debug().debug)
        self.assertTrue(Debug().debug2)
        self.assertTrue(Debug().debug3)

        self.assertTrue(Debug().debug_lib)
        self.assertTrue(Debug().debug2_lib)

    def test_debug_wit_env_var_set_to_true(self):
        """
        Test debugging statements when they are set to "true"
        """
        set_debug_env_vars_to(self.debug_variables, "true")

        self.assertTrue(Debug().debug)
        self.assertTrue(Debug().debug2)
        self.assertTrue(Debug().debug3)

        self.assertTrue(Debug().debug_lib)
        self.assertTrue(Debug().debug2_lib)

    def test_debug_wit_env_var_set_to_0(self):
        """
        Test debugging statements when they are set to "0"
        """
        set_debug_env_vars_to(self.debug_variables, "0")

        self.assertFalse(Debug().debug)
        self.assertFalse(Debug().debug2)
        self.assertFalse(Debug().debug3)

        self.assertFalse(Debug().debug_lib)
        self.assertFalse(Debug().debug2_lib)

    def test_debug_wit_env_var_set_to_False(self):
        """
        Test debugging statements when they are set to "False"
        """
        set_debug_env_vars_to(self.debug_variables, "False")

        self.assertFalse(Debug().debug)
        self.assertFalse(Debug().debug2)
        self.assertFalse(Debug().debug3)

        self.assertFalse(Debug().debug_lib)
        self.assertFalse(Debug().debug2_lib)

    def test_debug_wit_env_var_set_to_false(self):
        """
        Test debugging statements when they are set to "false"
        """
        set_debug_env_vars_to(self.debug_variables, "false")

        self.assertFalse(Debug().debug)
        self.assertFalse(Debug().debug2)
        self.assertFalse(Debug().debug3)

        self.assertFalse(Debug().debug_lib)
        self.assertFalse(Debug().debug2_lib)

    def test_debug_wit_env_var_set_to_Nothing(self):
        """
        Test debugging statements when they are set to nothing
        """
        set_debug_env_vars_to(self.debug_variables, "")

        self.assertFalse(Debug().debug)
        self.assertFalse(Debug().debug2)
        self.assertFalse(Debug().debug3)

        self.assertFalse(Debug().debug_lib)
        self.assertFalse(Debug().debug2_lib)
