"""
"""
import json
import random
import string
from unittest import TestCase, main, skip

from flask_restplus import Resource

from registry.model_db import get_models, MODEL_PATH, MODEL_ID
from APIServer.api_endpoints import Props, ModelMenu, RunModel
from APIServer.api_endpoints import Props, ModelMenu, RunModel
from APIServer.api_endpoints import app, HelloWorld, Endpoints, Models
from APIServer.api_endpoints import indra_dir
from APIServer.api_utils import err_return
from lib.utils import get_prop_path

BASIC_ID = 0
MIN_NUM_ENDPOINTS = 2


def random_name():
    return "".join(random.choices(string.ascii_letters,
                                  k=random.randrange(1, 10)))

class Test(TestCase):
    def setUp(self):
        self.hello_world = HelloWorld(Resource)
        self.endpoints = Endpoints(Resource)
        self.model = Models(Resource)
        self.props = Props(Resource)
        self.run = RunModel(Resource)
        self.models = get_models(indra_dir)

    def test_hello_world(self):
        """
        See if HelloWorld works.
        """
        rv = self.hello_world.get()
        self.assertEqual(rv, {'hello': 'world'})

    def test_endpoints(self):
        '''
        Check that /endpoints lists these endpoints.
        '''
        endpoints = self.endpoints.get()["Available endpoints"]
        self.assertGreaterEqual(len(endpoints), MIN_NUM_ENDPOINTS)

    def test_get_models(self):
        """
        See if we can get models.
        """
        api_ret = self.model.get()
        for model in api_ret:
            self.assertIn(MODEL_ID, model)

    def test_get_props(self):
        """
        See if we can get props.
        This test is way too coupled to model db details: Must re-write!
        """
        basic_api_props = self.props.get(BASIC_ID)
        self.assertNotEqual(basic_api_props, None)


if __name__ == "__main__":
    main()
