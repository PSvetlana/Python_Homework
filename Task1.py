# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

number = int(input('Введите количество членов последовательности: '))
list_of_numbers = []
for i in range(number):
    list_of_numbers.append((-3)**i)
print(list_of_numbers)