from collections.abc import Callable, Collection, Iterable, Iterator
from typing import ParamSpec, TypeVar

from mypy_extensions import Arg
from typing_extensions import assert_type


class MyObject:
    def __init__(self, x: int, y: str, z: bool):
        self.x = x
        self.y = y
        self.z = z


T = TypeVar("T")
P = ParamSpec("P")


def define_object_factory(object_type: Callable[P, T]) -> Callable[P, T]:
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        return object_type(*args, **kwargs)

    return inner


class MyCollection(Collection[T]):
    def __init__(self, values: Iterable[T]):
        self._values = list(values)

    def __contains__(self, value: object) -> bool:
        return value in self._values

    def __iter__(self) -> Iterator[T]:
        return iter(self._values)

    def __len__(self) -> int:
        return len(self._values)


def create_collection(values: Iterable[T] = ()) -> MyCollection[T]:
    return MyCollection(values=values)


create_myobject = define_object_factory(MyObject)

create_myobject(1, "a", False)

collection = create_collection(values=[MyObject(x=1, y="a", z=False)])

obj = next(iter(collection))


assert_type(
    create_myobject,
    Callable[[Arg(int, "x"), Arg(str, "y"), Arg(bool, "z")], MyObject],
)
