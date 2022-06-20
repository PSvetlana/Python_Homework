# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.

from random import randint


# сортировка пузырьком
def bubble_sorting(list_to_sort):
    for i in range(len(list_to_sort)-1, 0, -1):
        for j in range(i):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort

# исходный список случайный чисел
random_list = [randint(1, 50) for _ in range(10)]

with open('sem4_task1.txt', 'w') as file:
    file.write("\n".join(map(str, random_list)))

print(f'Исходный список: {random_list}')

with open('sem4_task1.txt', 'r') as file:
    random_list = list(map(int, file.readlines()))
    random_list = bubble_sorting(random_list)

with open('sem4_task1.txt', 'w') as file:
    file.write("\n".join(map(str, random_list)))

print(f'Отсортированный список: {random_list}')
