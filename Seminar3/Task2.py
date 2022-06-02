# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c = 3.141.

import math


# Функция для преобразования точности вида 0.001 => 3
def transformation_d(number):
    i = 0
    while(1 > number):
        i += 1
        number *= 10
    return i


# Функция для вычисления π с заданной точностью
def rounding_pi(accuracy_d):
    return round(math.pi, accuracy_d)


accuracy_d = float(input('Введите точность округления π (пример: 0.001), d = '))
print(f'При d = {accuracy_d}, π = {rounding_pi(transformation_d(accuracy_d))}')
