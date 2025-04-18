def sorted_data(data:list, key_name: str, reverse: bool):
    return sorted(data, key=lambda x: x[str(key_name)], reverse=reverse)