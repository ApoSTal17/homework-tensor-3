x = y = 0
direction_info = """Куда движемся?
    1 - вперед, 2 - назад, 3 - вправо, 4 - влево
    stop - выход\n"""
move_info = """Ha сколько?
        Целое неотрицательное число (>= 0):\n"""

def move(info):
    amount = int(input(info))
    if amount >= 0:
        return amount
    else:
        print('Число меньше 0')
        return 0

while True:
    error = False
    print(f'-#-#-# Исходная позиция: {x, y}')
    s = input(direction_info)
    match s:
        case '1':
            x += move(f'Вперед! {move_info}')
        case '2':
            x -= move(f'Назад! {move_info}')
        case '3':
            y += move(f'Вправо! {move_info}')
        case '4':
            y -= move(f'Влево! {move_info}')
        case 'stop':
            print('До свидания!')
            break
        case _:
            error = True
            print('Неправильный ввод!')
    if not error:
        print(f'-#-#-# Текущая позиция: {x, y}')