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
#  PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
#  LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT
#  OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#  OTHER DEALINGS IN THE SOFTWARE.
from __future__ import annotations

import socket
from collections import namedtuple

from ..utils.loggerUtils import create_prefix, Ansi, LogLevel, write_logfile, get_api_back

level = namedtuple('level', ['level', 'color'])

log_levels = {
    'critical': level(1, Ansi.RED),
    'error': level(2, Ansi.RED),
    'warn': level(3, Ansi.YELLOW),
    'info': level(4, Ansi.GREEN),
    'debug': level(5, Ansi.RESET),
}


class Logger:
    def __init__(self, log_level: int | LogLevel,
                 name: str = '',
                 log_file: str = None,
                 prefix: str = '',
                 disp_type: bool = True,
                 api_url: str = '') -> None:

        """ **This is the base Logger class.**

        Parameters:
        ----------
        log_level : int
            Set the log level.<br>
            0: None, 1: Info, 2: Warning, 3: Error, 4: Debug

        name : str, optional
            Set the name for the Logger. <br>
            Default: hostname of the machine.

        log_file : str, optional
            Set the path to a Logfile.

        prefix : str, optional
            Create a Prefix that appears in front of the msg. <br>
            You can set a completely custom prefix, but also generate one from the create_prefix function.
            <br>[default]: DD-MM-YYYY/HH:MM:SS | hostname | msg

        disp_type : bool, optional
            Should the Logger display the type of the message.
        """

        self.log_file = log_file
        self.log_level = log_level
        self.prefix = prefix
        self.disp_type = disp_type
        self.api = api_url

        self.hostname = name if name else socket.gethostname()

    def __prepare_mod_msg(self, msg: str, name: str) -> str:
        """ Prepare the Log message. Appends the Prefix and color codes

        Parameters
        ----------
        msg : str
            The base message from the User.
        name : str
            The name of the function that called it.

        Returns
        -------
        str
            The modified message from the User.

        """
        prefix = self.prefix

        if not self.prefix:
            prefix = create_prefix(True, self.hostname, mtype=name if self.disp_type else '')

        mod_msg = log_levels[name].color.value + prefix + msg + Ansi.RESET.value

        write_logfile(self, prefix + msg)

        return mod_msg

    def __can_log(self, name) -> bool:
        """ This function checks if the log level is says it can log.

        Parameters
        ----------
        name : str
            The name of the log function that was called.

        Returns
        -------
        bool
            Does the loglevel match the required level
        """

        if not log_levels[name][0] <= self.log_level:
            return False
        return True

    def info(self, msg: str) -> Logger:
        """ This represents a Green message with info content. """
        if self.__can_log('info'):
            print(self.__prepare_mod_msg(msg, 'info'))

        return self

    def warning(self, msg: str) -> Logger:
        """ This represents a Yellow message with warning content. """
        if self.__can_log('warn'):
            print(self.__prepare_mod_msg(msg, 'warn'))

        return self

    def error(self, msg: str) -> Logger:
        """ This represents a Red message with error content. """
        if self.__can_log('error'):
            print(self.__prepare_mod_msg(msg, 'error'))

        return self

    def debug(self, msg: str) -> Logger:
        """ This represents a White message with Debug content. """
        if self.__can_log('debug'):
            print(self.__prepare_mod_msg(msg, 'debug'))

        return self

    def critical(self, msg: str) -> Logger:
        """ This represents a Red message with Critical content. """
        if self.__can_log('critical'):
            print(self.__prepare_mod_msg(msg, 'critical'))

        return self

    def get_api(self, hook: str, **params) -> Logger:
        if self.api:
            get_api_back(self, hook, params, cookies=params.pop('cookies', ''),
                         headers=params.pop('headers', ''), timeout=params.pop('timeout', ''))

        return self
