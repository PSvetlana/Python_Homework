# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

user_string = input('Введите исходную строку: ')
user_char = input('Введите символы, которые будем искать в исходной строке: ')

count, i = 0, 0
while i < (len(user_string) - len(user_char) + 1):
    if user_char == user_string[i: i + len(user_char)]:
        count += 1
        i += len(user_char)
    else:
        i += 1
print('Количество вхождений = ' + str(count))
