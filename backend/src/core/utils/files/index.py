import os
from pathlib import Path
from src.core.constants.file_attribute import FileMode, FileEncoding

# handle open file, delete file and verify path
def validate_path(file_path: str):
    file_path = Path(file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Permission denied: {file_path}")
    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")
    
def open_file(file_path: str, mode, encoding):
    file_path = Path(file_path)
    validate_path(file_path)
    return open(file_path, mode, encoding=encoding)

def delete_file(file_path: str):
    file_path = Path(file_path)
    validate_path(file_path)
    os.remove(file_path)
    

