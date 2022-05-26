# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

user_n = int(input('Введите число:  '))
result = int(1)
for i in range(1, user_n + 1):
    result *= i
    print(result)
