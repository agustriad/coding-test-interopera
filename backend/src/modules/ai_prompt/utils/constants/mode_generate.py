from enum import Enum

class ModeGenerator(Enum):
    TEXT = ("TEXT")
    IMAGE = ("TEXT","IMAGE")
    GEMINI_MODEL: str = "gemini-2.0-flash"

    # without tuple
    def __getitem__(self, index):
        return self.value[index]