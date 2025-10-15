import sys

def solution():
    # Если аргумент командной строки указан
    if len(sys.argv) > 1:
        digit_string = sys.argv[1]
    else:
        # Иначе запрашиваем ввод вручную
        digit_string = input("Введите строку, состоящую только из цифр: ")

    # Проверяем, что строка состоит только из цифр
    if not digit_string.isdigit():
        print("Ошибка: Введите строку, состоящую только из цифр.")
        sys.exit(1)

    digit_sum = sum(int(digit) for digit in digit_string)
    print(f"Сумма цифр равна {digit_sum}")

if __name__ == "__main__":

    solution()