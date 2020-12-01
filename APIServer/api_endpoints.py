# Indra API server
import logging
import os
from flask import Flask
from flask_cors import CORS
from flask_restplus import Resource, Api, fields
from APIServer.api_utils import err_return
# from lib.user import APIUser
from APIServer.models_api import get_models
from APIServer.props_api import get_props_for_current_execution, put_props
from propargs.constants import VALUE, ATYPE, INT, HIVAL, LOWVAL
# from registry.registry import get_agent, del_exec_env
from registry.registry import registry
# from APIServer.run_model_api import run_model_put

app = Flask(__name__)
CORS(app)
api = Api(app)

# the hard-coded dir is needed for Python Anywhere, until
# we figure out how to get the env var set there.
indra_dir = os.getenv("INDRA_HOME", "/home/IndraABM/IndraABM")


@api.route('/test', endpoint="test",
           doc={"description": "An endpoint just to mess around with."})
class Test(Resource):
    def get(self):
        """
        A trivial endpoint just to demo adding something.
        """
        return {'hello': 'susanna'}


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


@api.route('/models')
class Models(Resource):
    def get(self):
        """
        Get a list of pre-existing models available through the API.
        """
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

        props = \
            get_props_for_current_execution(model_id, indra_dir)
        exec_key = registry.create_exec_env(save_on_register=True)
        props["execution_key"] = {
            VALUE: exec_key,
            ATYPE: INT,
            HIVAL: None,
            LOWVAL: None
        }
        return props

    @api.expect(props)
    def put(self, model_id):
        """
        Put a revised list of properties (parameters) for a model
        back to the server.
        """
        print(api.payload.get("exec_key"))
        return put_props(model_id, api.payload, indra_dir)


@api.route('/models/menu/<int:execution_id>')
class ModelMenu(Resource):
    '''
    def get(self, execution_id):
        """
        This returns the menu with which a model interacts with a user.
        """
        user = get_agent("Dennis")
        return user()
    '''


env = api.model("env", {
    "env": fields.String("Should be json rep of env.")
})


@api.route('/models/run/<int:run_time>')
class RunModel(Resource):
    '''
    @api.expect(env)
    def put(self, run_time):
        """
        Put a model env to the server and run it `run_time` periods.
        """
        return  run_model_put(api.payload, run_time)
    '''


@api.route('/registry/clear/<int:execution_key>')
class ClearRegistry(Resource):

    def get(self, execution_key):
        print("Clearing registry for key - {}".format(execution_key))
        try:
            registry.del_exec_env(execution_key)
        except KeyError:
            return err_return(
                "Key - {} does not exist in registry".format(execution_key))
        return {'success': True}


if __name__ == "__main__":
    logging.warning("Warning: you should use api.sh to run the server.")
    app.run(host="127.0.0.1", port=8000, debug=True)
