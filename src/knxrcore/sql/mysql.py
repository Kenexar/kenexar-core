#  Copyright (c) 2022. exersalza
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
#  associated documentation files (the "Software"), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following
#  conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial
#  portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
#  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#  LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
#  OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#  OTHER DEALINGS IN THE SOFTWARE.

from __future__ import annotations

from typing import Any

from mysql.connector import connect


class Connection:
    def __init__(self, **kw) -> None:
        """ Create a new connection

        Parameters
        ----------
        kw : dict
            [user] : sql username
            [password] : sql password
            [host] : sql host
            [db] : sql database
            [buffered] : create simultaneous query's
        """
        self.user = kw.pop('user', 'root')
        self.password = kw.pop('password', '')
        self.host = kw.pop('host', 'localhost')
        self.db = kw.pop('db', '')

        self.buff = kw.pop('buffered', False)
        self.kw = kw

    def get(self, sql: str, params: Any = '') -> list[dict | tuple] | None:
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

        conn = connect(user=self.user, password=self.password, host=self.host, database=self.db, **self.kw)
        cur = conn.cursor(self.buff)

        cur.execute(sql, params)
        result = cur.fetchall()

        conn.commit()
        cur.close()
        return result

    def update(self, sql: str, params: Any = '') -> Any:
        """ With this method you can Update the Database, like `UPDATE` or `DELETE` query's

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

        conn = connect(user=self.user, password=self.password, host=self.host, database=self.db, **self.kw)
        cur = conn.cursor(self.buff)

        cur.execute(sql, params)

        conn.commit()
        cur.close()

        return []

    def get_table_count(self, table: str) -> int:
        """ Returns the number of rows in the table.

        Parameters
        ----------
        table : :class:`str`
            Table name

        Returns
        -------
        int
            Number of rows in the table.
        """

        c = self.get('SELECT count(*) FROM %s', table)
        return c[0] if len(c) > 1 else 0

    async def aget(self, sql: str, params: Any = '') -> list[dict | tuple | None]:
        """ Here we can select asynchronous something from the Database.

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

        return self.get(sql, params)

    async def aupdate(self, sql: str, params: Any = '') -> Any:
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

        return self.update(sql, params)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return
