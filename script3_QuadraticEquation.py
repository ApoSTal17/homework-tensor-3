import math

print("""Введите коэффициенты квадр. уравнения вида
        ax^2 + bx + c = 0:""")
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b ** 2 - 4 * a * c
print(f"Дискриминант D = {discriminant}")


if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Два корня: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"Один корень: x = {x}")
else:
    print("Нет корней")