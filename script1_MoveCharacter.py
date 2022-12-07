x = y = 0
print(f'Исходная позиция: {x, y}')

direction_info = """Введите целое число:
        1 - вперед, 2 - назад
        3 - вправо, 4 - влево\n"""
move_info = """Ha сколько?
        Целое неотрицательное число (>= 0):\n"""
error = False

def move(info):
    amount = int(input(info))
    if amount >= 0:
        return amount
    else:
        print('Число меньше 0')
        return 0

match int(input(direction_info)):
    case 1:
        x += move(f'Вперед! {move_info}')
    case 2:
        x -= move(f'Назад! {move_info}')
    case 3:
        y += move(f'Вправо! {move_info}')
    case 4:
        y -= move(f'Влево! {move_info}')
    case _:
        print('Неправильный ввод!')
        error = True

if not error:
    print(f'Текущая позиция: {x, y}')