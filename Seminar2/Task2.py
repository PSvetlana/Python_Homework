# 2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

import math

# Функция поиска произведение пар чисел в списке  
def find_product_of_numbers(list):
    list_of_products = []
    for i in range(0, math.ceil(len(list) / 2)):
        list_of_products.append(list[i] * list[len(list) - i - 1]) 
    print(f'Произведение пар чисел в списке {list} => {list_of_products}')


list_of_numbers1 = [2, 3, 4, 5, 6]
list_of_numbers2 = [2, 3, 5, 6]

find_product_of_numbers(list_of_numbers1)
find_product_of_numbers(list_of_numbers2)