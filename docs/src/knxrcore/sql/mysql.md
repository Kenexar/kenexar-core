Module src.knxrcore.sql.mysql
=============================

Classes
-------

`Connection(**kw)`
:   

    ### Methods

    `aget(self, sql: str, params: Any = '') ‑> list[dict | tuple | None]`
    :   Here we can select asynchronous something from the Database.
        
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

    `aupdate(self, sql: str, params: Any = '') ‑> Any`
    :   With this method you can Update the Database, such things like `UPDATE` or `DELETE` query's
        
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

    `get(self, sql: str, params: Any = '') ‑> list[dict | tuple] | None`
    :   Here we can select something from the Database.
        
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

    `update(self, sql: str, params: Any = '') ‑> Any`
    :   With this method you can Update the Database, like `UPDATE` or `DELETE` query's
        
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