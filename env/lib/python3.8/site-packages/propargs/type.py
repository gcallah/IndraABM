
from propargs.constants import *


def try_type_val(val, atype):
    if val is None:
        return type_for_none[atype]

    if atype in type_dict:
        type_cast = type_dict[atype]
        return type_cast(val)

    else:
        return val


def boolean(val):
    if type(val) is str:
        return val.lower() == 'true' or val.lower() == 'yes'

    if type(val) in (int, float):
        return val == 1

    return bool(val)


type_dict = {BOOL: boolean, INT: int, FLT: float, CMPLX: complex, STR: str}
type_for_none = {BOOL: False, INT: 0, FLT: 0.0, CMPLX: 0j, STR: ''}
