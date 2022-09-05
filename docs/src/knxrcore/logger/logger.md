Module src.knxrcore.logger.logger
=================================

Classes
-------

`Logger(log_level: int | LogLevel, name: str = '', log_file: str = None, prefix: str = '', disp_type: bool = True)`
:   **This is the base Logger class.**
    
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

    ### Methods

    `debug(self, msg: str) ‑> None`
    :   This represents a White message with Debug content.

    `error(self, msg: str) ‑> None`
    :   This represents a Red message with error content.

    `info(self, msg: str) ‑> None`
    :   This represents a Green message with info content.

    `warning(self, msg: str) ‑> None`
    :   This represents a Yellow message with warning content.

`level(level, color)`
:   level(level, color)

    ### Ancestors (in MRO)

    * builtins.tuple

    ### Instance variables

    `color`
    :   Alias for field number 1

    `level`
    :   Alias for field number 0