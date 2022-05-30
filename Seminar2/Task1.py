# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

def find_sum_of_odd_items(list):
    sum = 0
    for i in range(0, len(list), 2):
        sum += list[i]
    print(f'Сумма чисел списка, стоящих на нечетной позиции = {sum}')


list_of_numbers = [1, 2, 3, 4]
print(f'Исходный массив:', list_of_numbers)

find_sum_of_odd_items(list_of_numbers)