import enum
from datetime import datetime
from typing import TYPE_CHECKING

import pytz

if TYPE_CHECKING:
    from .logger import Logger


class LogLevel(enum.IntEnum):
    INFO = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4


class Ansi(enum.Enum):
    RED = '\u001b[31m'
    YELLOW = '\u001b[33m'
    GREEN = '\u001b[32m'
    RESET = '\u001b[0m'


def write_logfile(logger: 'Logger', msg) -> int:
    if logger.log_file is None:
        return 0

    with open(logger.log_file, 'a+', encoding='utf-8') as f:
        f.write(msg + '\n')

    return 0


def create_prefix(date: bool,
                  name: str,
                  _type: str = '',
                  tz: str = 'Europe/Berlin') -> str:
    ret = ''
    if date:
        ret += f'{datetime.now(tz=pytz.timezone(tz)):%d-%m-%Y/%H:%M:%S} | '

    if _type:
        ret += f'{_type} | '

    ret += f'{name} | '
    return ret
