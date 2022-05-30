# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def form_list (number):
    list_of_numbers = []
    for i in range(number):
        list_of_numbers.append((-3)**i)
    print(f'Для N = {user_number}: {list_of_numbers}')

user_number = int(input('Введите количество членов последовательности, N = '))
form_list (user_number)