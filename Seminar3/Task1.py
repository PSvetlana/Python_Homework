# Найти НОК двух чисел

import math

user_number_a = int(input(f'Введите целое число, a = '))
user_number_b = int(input(f'Введите целое число, b = '))

# lcm - возвращает наименьшее общее кратное указанных чисел
print(f'Способ 1. НОК (a, b) = {math.lcm(user_number_a, user_number_b)}')

# gcd - возвращает наибольший общий делитель указанных чисел
nok = (user_number_a * user_number_b) // math.gcd(user_number_a, user_number_b)
print(f'Способ 2. НОК (a, b) = {nok}')

