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

from src.knxrcore.utils import create_arg_entry


class Flags(enum.IntFlag):
    NONE = 0


class Argparse:
    def __init__(self, name: str = '',
                 description: str = '',
                 auto_help: bool = True,
                 flags: Flags = Flags.NONE) -> None:
        """

        Parameters
        ----------
        name : str, optional
            Give the parser a name :)

        description : str, optional
            Give it a description.

        auto_help : bool, optional
            Create a help site or not.

        flags : Flags, optional
            Not implemented yet.
        """

        self.name = name
        self.description = description
        self.flags = flags

        # { '-N': { 'des': 'Some good argument to get some stuff',
        #          'count': int,
        #          }
        self._opt_arguments = {}

        if auto_help:
            self._opt_arguments = create_arg_entry('-h', '--help', des='Show this page')

    def parse(self, args: list) -> dict:
        pass

    def add_argument(self, *names: list | str, **kw: dict) -> None:
        """ This method adds arguments to the argument list

        Parameters
        ----------
        *names : list of strings
            Set the name's for the argument you want to add
        **kw : dict
            des : str
                Set a description for the argument, will be only shown inside the help

            count : int
                default : False, Set a count of result's to be passed.

                example: p.add_argument('--rgb', count=3) -> [23, 23, 23]
        """

        temp_dict = {**create_arg_entry(*names, **kw)}

        self._opt_arguments.update(**temp_dict)

    @property
    def opt_arguments(self) -> dict:
        return self._opt_arguments

    def __repr__(self) -> str:
        args = [k for k, _ in self._opt_arguments.items()]
        return f'<name={self.name!r} {args=}>'
