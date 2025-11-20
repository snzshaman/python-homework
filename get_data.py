from to_json import to_json

@to_json
def get_data() -> dict[str, int]:
    """
    Возвращает словарь с одним числовым значением.

    Returns:
        dict[str, int]: Словарь с ключом 'data' и значением int.
    """
    return {"data": 42}

print(get_data())    # >>> '{"data": 42}'
print(get_data.__name__)  # >>> 'get_data'