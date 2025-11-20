import tempfile
import os
import argparse
import sys
import json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ключ-значение хранилище. Позволяет сохранять и получать значения по ключам.",
        epilog="""Примеры использования:
          python storage.py --key mykey --val myvalue  # Добавить значение
          python storage.py --key mykey               # Получить значение
          python storage.py --clear                   # Очистить хранилище""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--key', type=str, help='Ключ')
    parser.add_argument('--val', type=str, help='Значение')
    parser.add_argument('--clear', action='store_true', help='Очистить')

    # Если нет аргументов — спрашиваем через input
    if len(sys.argv) == 1:
        user_input = input("Введите параметры (например: --key test --val 42): ")
        user_args = user_input.strip().split()
        return parser.parse_args(user_args)
    return parser.parse_args()



def load_storage() -> dict[str, list[str]]:
    """
    Загружает хранилище из JSON-файла.

    Returns:
        dict[str, list[str]]: Словарь с ключами и списками значений.
    """
    file_path = os.path.join(tempfile.gettempdir(), "storage.data")

    # Если файл не существует — создаём его с пустым словарём
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("{}")
        return {}

    # Читаем данные из файла
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            return data
        except json.JSONDecodeError:
            # Если файл повреждён или пустой — возвращаем пустой словарь
            return {}


def save_storage(data: dict[str, list[str]]) -> None:
    """
    Сохраняет хранилище в JSON-файл.

    Args:
        data (dict[str, list[str]]): Словарь с ключами и списками значений.
    """
    file_path = os.path.join(tempfile.gettempdir(), "storage.data")

    # Записываем данные в файл в формате JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)



def main():
    """Основная функция программы."""
    args = parse_args()
    print(args)
    # print('key:', args.key)
    # print('val:', args.val)
    # print('clear:', args.clear)
    print("="*30)

    # Загружаем текущее хранилище
    storage = load_storage()

    # Сценарий 1: Очистка хранилища (--clear)
    if args.clear:
        storage = {}
        save_storage(storage)
        print("Хранилище очищено.")
        return

    # Сценарий 2: Запись значения (--key и --val)
    if args.key and args.val:
        if args.key not in storage:
            storage[args.key] = []
        storage[args.key].append(args.val)
        save_storage(storage)
        print(f"Добавлено: {args.key} = {args.val}")
        return

    # Сценарий 3: Получение значений по ключу (только --key)
    if args.key:
        if args.key in storage:
            result = ", ".join(storage[args.key])
            print(result)
        else:
            print("None")
        return


if __name__ == "__main__":
    main()