from enum import Enum

class FileMode(str, Enum):
    READ = "r"
    READ_WRITE = "r+"
    WRITE = "w"
    WRITE_READ = "w+"
    APPEND = "a"
    APPEND_READ = "a+"
    EXCLUSIVE = "x"

class FileEncoding(str, Enum):
    UTF8 = "utf-8"
    ASCII = "ascii"

