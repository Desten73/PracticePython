import types
from pprint import pprint


def check_types(attr, typelist):
    for typeattr in typelist:
        if isinstance(attr, typeattr):
            return True
    return False


def introspection_info(obj):
    res = dict()
    res["type"] = type(obj)
    attributes = []
    methods = []

    for some in dir(obj):
        # print(some, type(getattr(obj, some)))
        if check_types(getattr(obj, some), [types.MethodType, types.MethodWrapperType,
                                            types.FunctionType, types.BuiltinFunctionType]):
            methods.append(some)
        else:
            attributes.append(some)

    res["attributes"] = attributes
    res["methods"] = methods
    res["module"] = type(obj).__module__
    return res


number_info = introspection_info(42)
pprint(number_info)
