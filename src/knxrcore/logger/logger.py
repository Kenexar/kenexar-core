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
        print(ANSI_GREEN + self.prefix + msg + ANSI_RESET)

    def warning(self, msg: str):
        print(ANSI_YELLOW + self.prefix + msg + ANSI_RESET)

    def error(self, msg: str):
        print(ANSI_RED + self.prefix + msg + ANSI_RESET)

    def debug(self, msg: str):
        print(self.prefix + msg)
