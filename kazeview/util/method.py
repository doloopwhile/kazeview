from functools import wraps

def getter(*attr_names):
    def _getter(class_):
        for name in attr_names:
            define_getter(class_, name, "_" + name)
        return class_
    return _getter


def define_method(class_, name=None):
    def _define_method(f):
        if name is not None:
            f.__name__ = name
        setattr(class_, f.__name__, f)
    return _define_method


def define_getter(class_, getter_method_name, attribute_name):
    @define_method(class_, getter_method_name)
    def method(self):
        return getattr(self, attribute_name)


def eq_by_attr(*attr_names):
    def _eq(class_):
        @define_method(class_)
        def __eq__(self, other):
            return all(getattr(self, attr_name) == getattr(other, attr_name)
                       for attr_name in attr_names)
        return class_
    return _eq

