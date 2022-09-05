import pytz

from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .logger import Logger


def write_logfile(logger: 'Logger', msg) -> int:
    if logger.log_file is None:
        return 0

    with open(logger.log_file, 'w+') as f:
        f.write(msg + "\n")


def prefix(date: bool, name: str, tz: Optional[str] = "Europe/Berlin") -> str:
    ret = ''
    if date:
        ret += f'{datetime.now(tz=pytz.timezone(tz)):%d-%m-%Y/%H:%M:%S} | '

    ret += f'{name} | '
    return ret
