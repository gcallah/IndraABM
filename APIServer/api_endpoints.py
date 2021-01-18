# Indra API server
import logging
import os
from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api, fields
from propargs.constants import VALUE, ATYPE, INT, HIVAL, LOWVAL
from registry.registry import registry
from registry.model_db import get_models
from APIServer.api_utils import err_return
from APIServer.api_utils import json_converter
from APIServer.props_api import get_props
from APIServer.model_api import run_model, create_model
# from models.basic import create_model as cm
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

# the hard-coded dir is needed for Python Anywhere, until
# we figure out how to get the env var set there.
indra_dir = os.getenv("INDRA_HOME", "/home/IndraABM/IndraABM")


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """
        A trivial endpoint just to see if we are running at all.
        """
        return {'hello': 'world'}


@api.route('/endpoints')
class Endpoints(Resource):
    def get(self):
        """
        List our endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


group_fields = api.model("group", {
    "group_name": fields.String,
    "num_of_agents": fields.Integer,
    "color": fields.String,
    "group_actions": fields.List(fields.String),
})

# env_width/height must be >0 when adding agents
create_model_spec = api.model("model_specification", {
    "model_name": fields.String("Enter model name."),
    "env_width": fields.Integer("Enter environment width."),
    "env_height": fields.Integer("Enter environment height."),
    "groups": fields.List(fields.Nested(group_fields)),
})


@api.route('/models/<active_only>')
class Models(Resource):
    def get(self, active_only=False):
        """
        Get a list of pre-existing models available through the API.
        """
        if active_only == "True":
            return get_models(indra_dir, active_only=True)
        return get_models(indra_dir)


props = api.model("props", {
    "props": fields.String("Enter propargs.")
})


@api.route('/models/props/<int:model_id>')
class Props(Resource):
    global indra_dir

    def get(self, model_id):
        """
        Get the list of properties (parameters) for a model.
        """
        props = get_props(model_id, indra_dir)
        exec_key = registry.create_exec_env(save_on_register=True)
        props["exec_key"] = {
            VALUE: exec_key,
            ATYPE: INT,
            HIVAL: None,
            LOWVAL: None
        }
        registry.save_reg(exec_key)
        return props

    @api.expect(props)
    def put(self, model_id):
        """
        Put a revised list of properties (parameters) for a model
        back to the server.
        This should return a new model with the revised props.
        """
        exec_key = api.payload['exec_key'].get('val')
        registry.save_reg(exec_key)
        return json_converter(create_model(model_id, api.payload, indra_dir))

    @api.expect(props)
    def post(self, model_id):
        """
        The endpoint created for testing purposes.
        """
        test_path = "test_data" + "/" + "basic_model.json"
        basic_path = indra_dir + "/" + "APIServer" + "/" + test_path
        with open(basic_path) as file:
            basic_model = json.loads(file.read())
        return basic_model


@api.route('/models/menu/<int:execution_id>')
class ModelMenu(Resource):
    # ModelMenu is used by the Frontend
    '''
    def get(self, execution_id):
        """
        This returns the menu with which a model interacts with a user.
        """
        user = get_agent("Dennis")
        return user()
    '''


env = api.model("env", {
    "model": fields.String("Should be json rep of model.")
})


@api.route('/models/run/<int:run_time>')
class RunModel(Resource):
    """
    This endpoint runs the model.
    """

    @api.expect(env)
    def put(self, run_time):
        """
        Put a model env to the server and run it `run_time` periods.
        """
        exec_key = api.payload['exec_key']
        model = run_model(api.payload, run_time, indra_dir)
        if model is None:
            return err_return("Model not found: " + api.payload["module"])
        registry.save_reg(exec_key)
        return json_converter(model)


@api.route('/registry/clear/<int:exec_key>')
class ClearRegistry(Resource):
    def get(self, exec_key):
        print("Clearing registry for key - {}".format(exec_key))
        try:
            registry.del_exec_env(exec_key)
        except KeyError:
            return err_return(
                "Key - {} does not exist in registry".format(exec_key))
        return {'success': True}


if __name__ == "__main__":
    logging.warning("Warning: you should use api.sh to run the server.")
    app.run(host="127.0.0.1", port=8000, debug=True)
