# Indra API server
import logging
import os
from flask import request
from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api, fields
from propargs.constants import VALUE, ATYPE, INT, HIVAL, LOWVAL
from registry.registry import registry, get_agent, create_exec_env
from registry.model_db import get_models
from APIServer.api_utils import err_return
from APIServer.api_utils import json_converter
from APIServer.props_api import get_props
from APIServer.model_api import run_model, create_model
from lib.user import APIUser

HEROKU_PORT = 1643

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


@api.route('/models/')
class Models(Resource):
    @api.doc(params={'active': 'Show only active models'})
    def get(self, active=False):
        """
        Get a list of pre-existing models available through the API.
        """
        if request.args.get('active') is not None:
            active = request.args.get('active')
        if active == "True" or active == "true":
            return get_models(indra_dir, active)
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
        exec_key = create_exec_env(save_on_register=True)
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
        APIUser("API_USER", exec_key=exec_key)
        model = json_converter(create_model(model_id, api.payload, indra_dir))
        registry.save_reg(exec_key)
        return model


@api.route('/models/menu/<int:execution_id>')
class ModelMenu(Resource):

    def get(self, execution_id):
        """
        This returns the menu with which a model interacts with a user.
        """
        user = get_agent("API_USER", exec_key=execution_id)
        return user()


env = api.model("env", {
    "model": fields.String("Should be json rep of model.")
})


@api.route('/models/run/<int:run_time>')
class RunModel(Resource):
    """
    This endpoint runs the model `run_time` periods.
    """

    @api.expect(env)
    def put(self, run_time):
        """
        Put a model env to the server and run it `run_time` periods.
        """
        exec_key = api.payload['exec_key']
        print(f'Executing for key {exec_key}')
        model = run_model(api.payload, run_time, indra_dir)
        if model is None:
            return err_return("Model not found: " + api.payload["module"])
        registry.save_reg(exec_key)
        return json_converter(model)


@api.route('/registry/get/<int:exec_key>')
class GetRegistry(Resource):
    """
    This returns a JSON version of the registry for
    session `exec_key` to the client.
    """


@api.route('/registry/clear/<int:exec_key>')
class ClearRegistry(Resource):
    """
    This clears the entries for one `exec_key` out of the registry.
    Q: What is this for?
    """
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
    app.run(port=HEROKU_PORT, debug=True)
