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

import enum
from typing import Any

from ..utils import create_arg_entry, show_help, is_in


class Flags(enum.IntFlag):
    NONE = 0


class Argparse:
    def __init__(self, name: str = '',
                 description: str = '',
                 _help: bool = True,
                 exit_on_exception: bool = False,
                 flags: Flags = Flags.NONE) -> None:
        """

        Parameters
        ----------
        name : str, optional
            Give the parser a name :)

        description : str, optional
            Give it a description.

        _help : bool, optional
            Create a help site or not.

        flags : Flags, optional
            Not implemented yet.
        """

        self.name = name
        self.description = description
        self.flags = flags
        self.exit_on_exception = exit_on_exception

        self._opt_args = {}

        if _help:
            self._opt_args = create_arg_entry('-h', '--help',
                                              des='Show this page',
                                              fallback=lambda: print(show_help()))

    def parse(self, args: list) -> dict:
        """ parse arguments.

        Parameters
        ----------
        args

        Returns
        -------

        """
        found_args = is_in(list(self._opt_args.keys()), args)
        ret = {}

        for arg, pos in found_args:
            ret = {**ret, arg: True}
            pos += 1
            pos2 = pos + self._opt_args[arg].get('count', 0)

            self._opt_args[arg].get('fallback', lambda: None)()

            if self._opt_args[arg].get('count'):
                ret[arg] = args[pos:pos2]

            if self._opt_args[arg].get('only', False):
                return {arg: args[pos:pos2]}

        return ret

    def add_argument(self, *names: list | str, **kw: Any) -> None:
        """ This method adds arguments to the argument list

        Parameters
        ----------
        *names : list of strings
            Set the name's for the argument you want to add

        **kw : dict
            des : str, optional
                Set a description for the argument, will be only shown inside the help

            count : int, optional
                default : False, Set a count of result's to be passed.

                example: p.add_argument('--rgb', count=3) -> [23, 23, 23]

            fallback : function reference | lambda, optional
                Give a fallback function/lambda that should be run when the argument is passed.

                Example: knxrcore/utils/argparseUtils.py -> show_help()

            only : bool
                If the argument is given only this arg will return the result when it's get executed.
                On multiple arguments with this parameter, the first one that is passed will be returned.
        """

        temp_dict = {**create_arg_entry(*names,
                                        des=kw.pop('des', ''),
                                        count=kw.pop('count', False), **kw)}

        self._opt_args.update(**temp_dict)

    @property
    def opt_arguments(self) -> dict:
        return self._opt_args

    def __repr__(self) -> str:
        args = [k for k, _ in self._opt_args.items()]
        return f'<name={self.name!r} {args=}>'
