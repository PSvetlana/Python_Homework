# Написать программу преобразования десятичного числа в двоичное

# Функция преобразования десятичного числа в двоичное
def dec_to_bin(number):
    binary = ''
    get_list = []
    while number != 0:
        get_list.insert(0, number % 2) # добавляет указанный элемент в список на указанную позицию
        number = number // 2
    get_list = list(map(str, get_list))

    for i in get_list:
        binary += i
    return binary


user_number = int(input('Введите целое число: '))
print(f'Число "{user_number}" в двоичной системе = {dec_to_bin(user_number)}')
