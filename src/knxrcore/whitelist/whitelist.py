from logging import Logger
from typing import Iterable, TypeVar, Generic, Mapping

T = TypeVar('T')
S = TypeVar('S', int, str)


class MyDict(Mapping[str, T]):
    pass


class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)


def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)
