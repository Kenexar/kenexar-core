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


def is_magic(name: str, exclude: bool = True) -> bool:
    """ Checks whether the given name is a magic function or not

    Parameters
    ----------
    name : str
        Name to check.

    exclude : str
        When on true, only False gets returned.

    Returns
    -------
    bool
        The result from the test.
        Can only return False when exclude is True.

    """

    return (name.startswith('__') and name.endswith('__')) if exclude else False


def get_methods_from_class(obj: object, exclude_magic: bool = True) -> list:
    """ Get all methods from an Object

    Parameters
    ----------
    obj : object
        The object where the methods get extracted from.

    exclude_magic : bool
        Exclude magic function from the list or not.

    Returns
    -------
    list
        List full of methods names, when there are some.
    """

    ret = []

    for method in dir(obj):
        if callable(getattr(obj, method)) and not is_magic(method, exclude_magic):
            ret.append(method)

    return ret
