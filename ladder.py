import sys

def ladder():
    # Получение значения с проверкой
    if len(sys.argv) > 1:
        steps_str = sys.argv[1]
    else:
        steps_str = input("Введите количество ступенек: ")

    if not steps_str.isdigit():
        print("Ошибка: введите целое положительное число.")
        sys.exit(1)

    steps = int(steps_str)

    for step in range(1, steps + 1):
        spaces = steps - step
        hashes = step
        print(" " * spaces + "#" * hashes)

if __name__ == "__main__":
    ladder()