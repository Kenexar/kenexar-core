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
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
#  associated documentation files (the "Software"), to deal in the Software without restriction, including
#  without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following
#  conditions:
#
from __future__ import annotations

import enum
from datetime import datetime
from typing import TYPE_CHECKING, Any

import pytz
import requests

if TYPE_CHECKING:
    from knxrcore.logger.logger import Logger


class LogLevel(enum.IntEnum):
    NONE = 0
    CRIT = 1
    ERROR = 2
    WARNING = 3
    INFO = 4
    DEBUG = 5


class Ansi(enum.Enum):
    RED = '\u001b[31m'
    YELLOW = '\u001b[33m'
    GREEN = '\u001b[32m'
    RESET = '\u001b[0m'


def write_logfile(logger: 'Logger', msg: str) -> int:
    """ Write the message to the log file, if no exists it will be created

    Parameters
    ----------
    logger : Logger
        The current logger, uses the logger.log_file parameter

    msg : str
        The message to be logged

    Returns
    -------
    int
    """

    if logger.log_file is None:
        return 0

    with open(logger.log_file, 'a+', encoding='utf-8') as f:
        f.write(msg + '\n')

    return 0


def create_prefix(date: bool,
                  name: str,
                  mtype: str = '',
                  tz: str = 'Europe/Berlin') -> str:
    """ Create the Prefix for log messages

    Parameters
    ----------
    date : bool
        Should be a Date inside the prefix

    name : str
        Current Logger name

    mtype : str
        Type of log message

    tz : str, optional
        Timezone for the date

    Returns
    -------
    str
        Prefix for log messages.
    """

    ret = ''
    if date:
        ret += f'{datetime.now(tz=pytz.timezone(tz)):%d-%m-%Y/%H:%M:%S} | '

    if mtype:
        ret += f'{mtype} | '

    ret += f'{name} | '
    return ret


def get_api_back(logger: Logger, hook: str, params: dict, cookies: Any | None, headers: Any | None, timeout: Any | None):
    url = (logger.api + '/' + hook).replace('///', '//').replace('//', '/').replace(':/', '://')

    requests.get(url=url, params=params, cookies=cookies, headers=headers, timeout=timeout)
