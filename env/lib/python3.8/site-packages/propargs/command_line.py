import argparse

from propargs.type import try_type_val

parser = argparse.ArgumentParser(description='parse key pairs into a dictionary')


def set_props_from_cl(prop_args):

    args, _ = parser.parse_known_args()
    cl_dict = vars(args)['my_dict']
    if not cl_dict:
        return

    for prop_nm in cl_dict :
        arg = cl_dict[prop_nm]
        if prop_nm in prop_args:
            arg = try_type_val(arg, prop_args.props[prop_nm].atype)
        prop_args[prop_nm] = arg


class StoreDictKeyPair(argparse.Action):
     def __call__(self, parser, namespace, values, option_string=None):
         my_dict = {}
         for kv in values.split(","):
             k,v = kv.split("=")
             my_dict[k] = v
         setattr(namespace, self.dest, my_dict)

parser.add_argument("--props", dest="my_dict", action=StoreDictKeyPair, metavar="KEY1=VAL1,KEY2=VAL2...")
