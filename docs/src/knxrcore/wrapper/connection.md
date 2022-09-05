Module src.knxrcore.wrapper.connection
======================================

Classes
-------

`ApiConnection(host)`
:   This class allows communication via SSL.
    
    This is the Base connection class for generel wrappers that we maybe want to write.

    ### Ancestors (in MRO)

    * http.client.HTTPSConnection
    * http.client.HTTPConnection

    ### Methods

    `delete(self, url: str, headers: dict) ‑> tuple`
    :   This will send a `DELETE` request
        
        Parameters
        ----------
        url : str
            The url to send the request to.
        
        headers : dict
            The headers to send with the request. This is for the jwt token
            and accept thingies.
        
        Returns
        -------
        bytes and HTTPMessage
            The read response from the server. When it responds something.

    `get(self, url: str, headers: dict) ‑> tuple`
    :   This will send a `GET` request
        
        Parameters
        ----------
        url : :class:`str`
            The url to send the request to.
        
        headers : :class:`dict`
            The headers to send with the request. This is for the jwt token
            and to tell the API what we want back from them.
        
        Returns
        -------
        :class:`bytes`
            The read response from the server.
        Notes
        -----
        The JWT token will be only used for non-read-only requests.

    `post(self, url: str, headers: dict, data: dict) ‑> tuple`
    :   This will send a `POST` request
        
        Parameters
        ----------
        url : str
            The url to send the request to.
        
        headers : dict
            The headers to send with the request. This is for the jwt token
            and accept thingies.
        
        data : dict
            The body of the request. This is the data that will be sent to
            the server.
        
        Returns
        -------
        bytes and HTTPMessage
            The read response from the server.

    `put(self, url: str, headers: dict, data: dict) ‑> tuple`
    :   Here you can create entries on the api
        
        Parameters
        ----------
        url : str
            The endpoints url to access.
        
        headers : dict
            The default headers.
        
        data : dict
            The data for the creation.
        
        Returns
        -------
        bytes and HTTPMessage
            The response from the endpoint.