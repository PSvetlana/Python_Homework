# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference_max_min(list):
    for i in range(0, len(list)):
        if list[i] % 1 != 0:
            list[i] = float('0.' + (str(list[i]).split('.'))[1])
            if i == 0:
                max = list[i]
                min = list[i]
            if max < list[i]:
                max = list[i]
            if min > list[i]:
                min = list[i]
    return max - min


float_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f'Исходный список = {float_list}')
result = difference_max_min(float_list)
print(f'Разница между MAX и MIN дробной части элементов списка = {result}')
