from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..sql import Connection


class User:
    """User class"""
    def __init__(self):
        pass


class Whitelist:
    def __init__(self, connection: 'Connection', **kwargs) -> None:
        self.conn = connection

        self.local_list = kwargs.pop('local_list') if kwargs.get('local_list') else []

        self.__init_local_list()

    def __init_local_list(self, sql: str = None) -> list:
        ret = self.conn.get(f'select * from {self.conn.db}.whitelist' if sql is not None else sql)

        if not ret:
            return []

    def add(self, user: str, perm: int | object | str):
        pass

    def remove(self, user: str):
        pass

    def update(self, user: str, perm: int | str | object):
        pass

