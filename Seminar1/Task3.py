# Подсчитать сумму цифр в вещественном числе.


user_float = input('Введите вещественное число: ')

sum = 0
for digit in user_float:
    if digit != "." and digit != "," and digit != "-":
        sum += int(digit)

print(f'Сумма цифр в числе {user_float} = {sum}')

# user_float = input('Введите вещественное число: ')
# num = user_float.split('.')  # разбивка числа на две части
# integer_part = int(num[0])  # целая часть числа
# fractional_part = int(num[1])  # дробная часть числа

# sum = 0

# while (integer_part != 0): # подсчет суммы цифр целой части
#     sum = sum + (integer_part % 10)
#     integer_part = integer_part // 10

# while (fractional_part != 0): # подсчет суммы цифр дробной части
#     sum = sum + (fractional_part % 10)
#     fractional_part = fractional_part // 10

# print(f'Сумма цифр в числе {user_float} = {sum}')
