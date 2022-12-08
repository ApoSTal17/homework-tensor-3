
print("""Введите коэффициенты квадр. уравнения вида
        ax^2 + bx + c = 0:\n""")
abc_names = ['a', 'b', 'c']
abc = [None, None, None]
for i in range(len(abc_names)):
    while (abc[i] == None):
        try:
            abc[i] = complex(input(f"Введите коэффициент {abc_names[i]}: "))
        except ValueError:
            print('Неправильный ввод. Попробуй ещё раз:\n')

discriminant = abc[1] ** 2 - 4 * abc[0] * abc[2]
if discriminant.imag == 0:
    print(f"Дискриминант D вещественный = {discriminant.real}")
else: 
    print(f"Дискриминант D комплексный = {discriminant}")

x1 = (-abc[1] + (discriminant ** 0.5)) / (2 * abc[0])
x2 = (-abc[1] - (discriminant ** 0.5)) / (2 * abc[0])

is_complex = True
for i in [x1, x2]:
    if i.imag == 0:
        is_complex = False
        break

if is_complex:
    print(f"Комплексные корни: \nx1 = ({x1.real}, {x1.imag}) \nx2 = ({x2.real}, {x2.imag})")
else:
    print(f"Вещественные: x1 = {x1.real}, x2 = {x2.real}")
