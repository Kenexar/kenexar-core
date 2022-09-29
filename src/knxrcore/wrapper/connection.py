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

from http.client import HTTPSConnection


class ApiConnection(HTTPSConnection):
    def __init__(self, host):
        """
        This is the Base connection class for generel wrappers that we maybe want to write.
        """

        super().__init__(host=host)

    def get(self, url: str, headers: dict) -> tuple:
        """ This will send a `GET` request

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
        """

        res, header = self.__request('GET', headers, url)

        self.close()
        return res, header

    def __request(self, method: str, headers: dict, url: str) -> tuple:
        """ This is just for preventing repetitive code samples

        Parameters
        ----------
        method : str
            The request method that is needed, e.x. POST or GET.

        headers : dict
            The default header for the authorization.

        url : str
            The url to send the request to.

        Returns
        -------
        bytes and HTTPMessage
            Returns the data
        """

        self.request(method, url, headers=headers)

        data = self.getresponse()
        res = data.read()
        header = data.headers

        return res, header

    def __requests_body(self, method: str, data: dict, headers: dict, url: str) -> tuple:
        """ the same as the __request method but for PUT and POST req

        Parameters
        ----------
        method : :class:`str`
            The method that you want to use, possible values POST or PUT.

        data : :class:`dict`
            The body that will be delivered with the request.

        headers : :class:`dict`
            The default headers for authorization.

        url : :class:`str`
            The endpoints url to send the request to.

        Returns
        -------
        :class:`bytes` and :class:`HTTPMessage`
            The response that the api gives us back.
        """

        self.request(method, url, headers=headers, body=data)

        rdata = self.getresponse()
        res = rdata.read()
        header = rdata.headers

        return res, header

    def post(self, url: str, headers: dict, data: dict) -> tuple:
        """
        This will send a `POST` request

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
        """

        res, header = self.__requests_body('POST', data=data, headers=headers, url=url)

        self.close()
        return res, header

    def delete(self, url: str, headers: dict) -> tuple:
        """
        This will send a `DELETE` request

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
        """

        res, header = self.__request('DELETE', url=url, headers=headers)

        self.close()
        return res, header

    def put(self, url: str, headers: dict, data: dict) -> tuple:
        """ Here you can create entries on the api

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
        """
        res, header = self.__requests_body('PUT', data=data, url=url, headers=headers)

        self.close()
        return res, header
