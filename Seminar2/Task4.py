# Написать программу преобразования десятичного числа в двоичное

# Функция преобразования десятичного числа в двоичное
def dec_to_bin(number):
    binary = ''
    get_list = []
    if number == 0:
        return '0'
    while number != 0:        
        get_list.insert(0, number % 2) # добавляет указанный элемент в список на указанную позицию
        number = number // 2
    get_list = list(map(str, get_list))
    binary = "".join(get_list)    
    return binary


# более оптимальный вариант
# def dec_to_bin(number):
#     binary = ''
#     if number == 0:
#         return '0'
#     while number > 0:
#         binary = str(number % 2) + binary
#         number //= 2
#     return binary


user_number = int(input('Введите целое число: '))
print(f'Число "{user_number}" в двоичной системе = {dec_to_bin(user_number)}')
