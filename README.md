# Решения домашних заданий по Python

В этом репозитории содержатся решения следующих задач:

- `solution.py` — программа для подсчёта суммы цифр в строке.
- `ladder.py` — программа для рисования лесенки из символов.
- `equation.py` — решение квадратного уравнения с коэффициентами.
- `storage.py` — key-value хранилище с поддержкой сохранения в JSON.
- `to_json.py` — декоратор для преобразования результата функции в JSON-формат.
- `get_data.py` — пример использования декоратора `to_json`.

Каждая программа поддерживает ввод как с аргументов командной строки, так и с клавиатуры.

---

# Python Homework Solutions

This repository contains solutions to the following tasks:

- `solution.py` — a program that calculates the sum of digits in a string.
- `ladder.py` — a program to draw a staircase using characters.
- `equation.py` — a quadratic equation solver that takes coefficients as input.
- `storage.py` — a key-value storage with JSON format support.
- `to_json.py` — a decorator that transforms a function's return value to JSON format.
- `get_data.py` — an example of using the `to_json` decorator.

Each program supports input both from command-line arguments and from user input.

---

## Как использовать / How to use

### Базовые задачи / Basic tasks

Для запуска программы из командной строки используйте: 

```bash
python solution.py 873 

python ladder.py 5

python equation.py 1 5 6
```

### Key-value хранилище / Key-value Storage

**Добавить значение / Add a value:**
```bash
python storage.py --key key1 --val value1
```

**Получить значение / Get a value:**
```bash
python storage.py --key key1
```

**Получить несколько значений / Get multiple values:**
```bash
python storage.py --key key1 --val value2
python storage.py --key key1
# Вывод: value1, value2
```

**Очистить хранилище / Clear storage:**
```bash
python storage.py --clear
```

### Декоратор to_json / to_json Decorator

Для использования декоратора в своём коде:

```python
from to_json import to_json

@to_json
def get_data():
    return {"data": 42}

result = get_data()  # Вернёт '{"data": 42}'
```

---

Спасибо за внимание!  
Thank you for your attention!
