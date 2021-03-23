"""
prop_args2.py
Set, read, and write program-wide properties in one location. Includes logging.
"""
import json
from typing import Optional

from propargs.exceptions import PropsNotInitializedException
from propargs.prop import Prop
from propargs import data_store, env, property_dict, command_line, user
from propargs.constants import *


def get_prop(key, default_val=None):
    """
    Get a particular property.
    If key is missing (or no props) return default_val.
    """
    if _the_props is None:
        return default_val
    else:
        return _the_props.get(key, default_val)


def set_prop(key, val):
    """
    Set a property's value.
    """
    if _the_props is None:
        raise PropsNotInitializedException("PropArgs not initialized yet.")

    _the_props[key] = val


class PropArgs:
    """
    This class holds named properties for program-wide values.
    It enables getting properties from a file, a database,
    or from the user, either via the command line or a prompt.
    """

    @staticmethod
    def create_props(name, ds_file=None, prop_dict=None,
                     skip_user_questions=False):
        """
        Create a property object with values in 'props'.
        """
        if prop_dict is None:
            prop_dict = dict()

        pa = PropArgs(name, ds_file=ds_file, prop_dict=prop_dict,
                      skip_user_questions=skip_user_questions)

        return pa

    def __init__(self, name, logfile=None, ds_file=None,
                 prop_dict=None, skip_user_questions=False):
        """
        Loads and sets properties in the following order:
        1. The Data Store
        2. Property Dictionary
        3. The User's Environment (operating system, dev/prod settings, etc.)
        4. Command Line
        5. Questions Prompts During Run-Time
        """
        global _the_props
        _the_props = self

        self.name = name
        self.logfile = logfile
        self.ds_file = ds_file
        self.props = prop_dict or dict()

        # 1. The Data Store
        if self.ds_file:
            data_store.set_props_from_ds(self)

        # 2. Property Dictionary
        property_dict.set_props_from_dict(self, prop_dict)

        # 3. The Environment
        env.set_props_from_env(self)

        # 4. process command line args and set them as properties:
        command_line.set_props_from_cl(self)

        if not skip_user_questions and user.can_ask_through_cl(self):
            # 5. Ask the user questions.
            user.ask_user_through_cl(self)

    def get_questions(self):
        all_props = self.to_json()
        question_props = {key: all_props[key] for key in all_props if
                          all_props[key]['question'] is not None}
        return question_props

    def _answer_within_bounds(self, prop_nm, typed_answer):
        if (self.props[prop_nm].atype is None
                or self.props[prop_nm].atype in (STR, BOOL)):
            return True

        if (self.props[prop_nm].lowval is not None
                and self.props[prop_nm].lowval > typed_answer):
            return False

        if (self.props[prop_nm].hival is not None
                and self.props[prop_nm].hival < typed_answer):
            return False

        return True

    def display(self):
        """
        How to represent the properties on screen.
        """
        ret = "Properties in " + self.name + "\n"
        for prop_nm in self:
            ret += "\t" + prop_nm + ": " + str(self.props[prop_nm].val) + "\n"

        return ret

    def __iter__(self):
        return iter(self.props)

    def __str__(self):
        return self.display()

    def __len__(self):
        return len(self.props)

    def __contains__(self, key):
        return key in self.props

    def __setitem__(self, key, v):
        """
        Set a property value.
        """
        if key in self:
            self.props[key].val = v
        else:
            self.props[key] = Prop(val=v)

    def __getitem__(self, key):
        return self.props[key].val

    def __delitem__(self, key):
        del self.props[key]

    def items(self):
        return self.props.items()

    def get_logfile(self):
        """
        Special get function for logfile name
        """
        return self.props["log_fname"].val

    def write(self, file_nm):
        """
        Write properties to json file.
        Useful for storing interesting parameter sets.
        """
        dict_for_json = {}
        for prop_name in self.props:
            dict_for_json[prop_name] = self.props[prop_name].to_json()
        f = open(file_nm, 'w')
        json.dump(dict_for_json, f, indent=4)
        f.close()

    def to_json(self):
        return {prop_nm: self.props[prop_nm].to_json() for prop_nm in
                self.props}

    def get(self, key, default=None):
        if key not in self.props or self.props[key].val is None:
            self.props[key] = Prop(val=default)
        return self.props[key].val


_the_props = None
