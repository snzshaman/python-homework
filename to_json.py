import json
from functools import wraps
from typing import Any, Callable


def to_json(func: Callable[..., Any]) -> Callable[..., str]:
    """
    Декоратор, сериализующий результат функции в JSON-строку.

    Args:
    func (Callable): Функция, результат которой будет преобразован в JSON-строку.

    Returns:
    Callable[..., str]: Функция, возвращающая строку в формате JSON.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = func(*args, **kwargs)
        json_result = json.dumps(result)
        return json_result

    return wrapper
