from mysql.connector import connect
from typing import Any, Union, List, Optional


class Connection:
    def __init__(self, **kw) -> None:
        self.user = kw.get('user', 'root')
        self.password = kw.get('password', '')
        self.host = kw.get('host', 'localhost')
        self.db = kw.get('db', '')

    def get(self, sql: str, params: Any = '') -> Union[list, None, List[Optional[dict]], List[tuple]]:
        """ Here we can select something from the Database.

        Parameters
        ----------
        sql : :class:`str`
            An sql string to select something from the Database.

        params : :class:`Any`
            The parameters for the sql execution.

        Returns
        -------
        list | List[Optional[dict]] | List[Tuple]
            Returns the result of the given query.
        """

        conn = connect(user=self.user, password=self.password, host=self.host, database=self.db)
        cur = conn.cursor(buffered=True)

        cur.execute(sql, params)
        result = cur.fetchall()

        cur.close()
        return result

    def update(self, sql: str, params: Any = '') -> None:
        """ With this method you can Update the Database, such things like `UPDATE` or `DELETE` query's

        Parameters
        ----------
        sql : :class:`str`
            An sql string to select something from the Database.

        params : :class:`Any`
            The parameters for the sql execution.

        Returns
        -------
        None
            Nothing.
        """
        conn = connect(user=self.user, password=self.password, host=self.host, database=self.db)
        cur = conn.cursor(buffered=True)

        cur.execute(sql, params)
        conn.commit()
        cur.close()
        return None
