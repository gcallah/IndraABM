
from propargs.constants import *
from propargs.type import try_type_val
from propargs.prop import Prop


def set_props_from_dict(prop_args, prop_dict):
    """
    Dict Example:

    {
        "prop_name_1": {
            "val": 1,
            "question": "What value should this property have?",
            "atype": "int",
            "hival": 10,
            "lowval": 0
        },
        "prop_name_2": {
            "val": "Hello World."
        }
    }
    """
    if prop_dict is None:
        return

    for prop_nm in prop_dict:
        atype = prop_dict[prop_nm].get(ATYPE, None)
        val = try_type_val(prop_dict[prop_nm].get(VALUE, None),
                                      atype)
        question = prop_dict[prop_nm].get(QUESTION, None)
        hival = prop_dict[prop_nm].get(HIVAL, None)
        lowval = prop_dict[prop_nm].get(LOWVAL, None)
        prop_args.props[prop_nm] = Prop(val=val, question=question, atype=atype,
                                   hival=hival, lowval=lowval)
