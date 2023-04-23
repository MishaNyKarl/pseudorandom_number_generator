import time


def pseudorandom(num):
    """Функция по нахождению серединного квадрата данного числа"""

    new_num = int(str(num**2)[0:3])

    return new_num


def random_by_your_num(num, depth):
    """Генератор псевдо случайных чисел с определяемой глубиной
    (кол-во повторений функции нахождения серединнго квадрата)"""

    all_num = [num]
    result = ''

    for i in range(depth):
        all_num.append(pseudorandom(all_num[i]))
    all_num.pop(0)

    for j in all_num:
        result += str(j)

    return int(result)


def random_num_by_using_time(length):
    """Функция для создания рандомного числа с помощью времени (длинной до 30 символов)"""

    str_num = str(time.time())
    if str_num[9] == '0':
        num = int('1' + str_num[8] + str_num[15])
    else:
        num = int(str_num[9] + str_num[14] + str_num[8])

    result = random_by_your_num(num, 10)

    return int(str(result)[:length])


"""Примеры использования функций"""

print(pseudorandom(132))

print(random_by_your_num(174, 10))

print(random_num_by_using_time(10))