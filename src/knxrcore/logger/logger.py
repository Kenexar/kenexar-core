import socket

from utils import *

ANSI_RED = '\u001b[31m'
ANSI_YELLOW = '\u001b[33m'
ANSI_GREEN = '\u001b[32m'
ANSI_RESET = '\u001b[0m'


class Logger:
    def __init__(self, log_file: Optional[str] = None, log_level: int = 0, _prefix: Optional[str] = "") -> None:
        self.log_file = log_file
        self.log_level = log_level

        if not _prefix:
            self.prefix = prefix(True, socket.gethostname())

    def info(self, msg: str):
        ret = ANSI_GREEN + self.prefix + msg + ANSI_RESET
        write_logfile(self, ret)

        print(ret)
        return ret

    def warning(self, msg: str):
        ret = ANSI_YELLOW + self.prefix + msg + ANSI_RESET

        write_logfile(self, ret)

        print(ret)
        return ret

    def error(self, msg: str):
        ret = ANSI_RED + self.prefix + msg + ANSI_RESET

        write_logfile(self, ret)

        print(ret)
        return ret

    def debug(self, msg: str):
        ret = self.prefix + msg

        write_logfile(self, ret)

        print(ret)
        return ret
