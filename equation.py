import sys
import math

def equation():
    # Получаем коэффициенты a, b, c
    if len(sys.argv) > 3:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            c = int(sys.argv[3])
        except ValueError:
            print("Ошибка: коэффициенты должны быть числами.")
            sys.exit(1)
    else:
        try:
            print("Введите коэффициенты квадратного уравнения:")
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
        except ValueError:
            print("Ошибка: введите корректные целые числа.")
            sys.exit(1)

    if a == 0:
        print("Ошибка: коэффициент 'a' не может быть равен 0 (уравнение не квадратное).")
        sys.exit(1)

    # Вычисляем дискриминант
    D = b**2 - 4*a*c

    if D > 0:
        sqrt_D = math.sqrt(D)
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (-b - sqrt_D) / (2*a)
        print(f"Два корня: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"Один корень: x = {x}")
    else:
        print("Корней нет (дискриминант меньше нуля)")

if __name__ == "__main__":
    equation()