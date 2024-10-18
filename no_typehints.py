from collections.abc import Collection


class MyObject:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def define_object_factory(object_type):
    def inner(*args, **kwargs):
        return object_type(*args, **kwargs)

    return inner


class MyCollection(Collection):
    def __init__(self, values):
        self._values = list(values)

    def __contains__(self, value):
        return value in self._values

    def __iter__(self):
        return iter(self._values)

    def __len__(self):
        return len(self._values)


def create_collection(values):
    return MyCollection(values=values)


create_myobject = define_object_factory(MyObject)

create_myobject(1, "a", False)

collection = create_collection(values=[MyObject(x=1, y="a", z=False)])

obj = next(iter(collection))
