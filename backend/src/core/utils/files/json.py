import json
from src.core.utils.files.index import validate_path, delete_file, open_file
from src.core.constants.file_attribute import FileMode, FileEncoding


def read_json(path):
    if path is None:
        return None
    
    validate_path(path)
    with open_file(path, FileMode.READ, FileEncoding.UTF8) as file:
        data = json.load(file)
    return data


def write_json(path=None ,data=None, mode=FileMode.WRITE, encoding=FileEncoding.UTF8 ):
    if data is None:
        return None

    validate_path(path)
    with open_file(path, mode, encoding) as file:
        json.dump(data, file, indent=4)
    
    return data