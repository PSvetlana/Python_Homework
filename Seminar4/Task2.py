# 2. Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
# и содержащие максимальное количество элементов. Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

from itertools import combinations


# ищет последовательность, содержащую максимальное количество элементов
def finding_of_max_sequence(list_to_find):
    for length_sequence in range(len(list_to_find), 2, -1):
        # combinations() - возвращает итератор со всеми возможными комбинациями
        # элементов входной последовательности 
        for item in combinations(list_to_find, length_sequence): 
            if check_sequence(item):
                return list(item)


# проверяет является ли последовательность возрастающей
def check_sequence(cort: tuple):
    my_list = list(cort)
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i+1]:
            return False
    return True


test_list1 = [1, 5, 2, 3, 4, 6, 1, 7]
test_list2 = [5, 2, 3, 4, 6, 1, 7]
print (f'{test_list1} => {finding_of_max_sequence(test_list1)}')
print (f'{test_list2} => {finding_of_max_sequence(test_list2)}')


