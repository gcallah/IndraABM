"""
"""
import json
import random
import string
from unittest import TestCase, main, skip

from flask_restplus import Resource

from APIServer.api_endpoints import Props, ModelMenu, RunModel
from APIServer.api_endpoints import Props, ModelMenu, RunModel
from APIServer.api_endpoints import app, HelloWorld, Endpoints, Models
from APIServer.api_endpoints import indra_dir
from APIServer.api_utils import err_return
from APIServer.models_api import load_models, MODEL_FILE, MODEL_ID


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
        self.models = load_models(indra_dir)

    def test_load_models(self):
        """
        See if models can be loaded.
        """
        rv = self.models
        test_model_file = indra_dir + MODEL_FILE
        with open(test_model_file) as file:
            test_rv = json.loads(file.read())["models_database"]
        self.assertEqual(rv, test_rv)

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

    @skip("Skipping get props.")
    def test_get_props(self):
        """
        See if we can get props.
        This test is way too coupled to model db details: Must re-write!
        """
        model_id = random.randint(0, 10)
        rv = self.props.get(model_id)

        test_model_file = indra_dir + MODEL_FILE
        with open(test_model_file) as file:
            test_models_db = json.loads(file.read())["models_database"]

        with open(indra_dir + "/" + test_models_db[model_id]["props"]) as file:
            test_props = json.loads(file.read())

        self.assertEqual(rv, test_props)


if __name__ == "__main__":
    main()
