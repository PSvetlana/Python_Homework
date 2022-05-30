# Подсчитать сумму цифр в вещественном числе.

user_float = input('Введите вещественное число: ')

sum = 0
for digit in user_float:
    if digit != "." and digit != ",":
        sum += int(digit)

print(f'Сумма цифр в числе {user_float} = {sum}')
