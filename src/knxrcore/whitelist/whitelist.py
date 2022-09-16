from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..sql import Connection


class Whitelist:
    def __init__(self, connection: 'Connection', **kwargs) -> None:
        self.conn = connection

        self.local_list = kwargs.pop('local_list') if kwargs.get('local_list') else []

        self.__init_local_list()

    def __init_local_list(self, sql: str = None) -> list:
        ret = self.conn.get('select * from whitelist' if sql is not None else sql)

        if not ret:
            return []

        
