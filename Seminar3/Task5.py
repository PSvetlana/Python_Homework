# Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа

print('\nДанные на входе:')
print(open("Seminar3\in.txt").read())

file_out = open("Seminar3\out.txt", "w")
with open("Seminar3\in.txt", "r") as file_in:
    for str in file_in:
        if len(str) > 0: # проход по списку
            new_list = str.split()
            tmp = ""
            for s in new_list: # если элемент нечетный, добавляем в новый список
                if int(s) % 2 != 0:
                    tmp += s + " "
            file_out.write(tmp + "\n")
        else:
            file_out.write("\n")

file_out.close()

print('\nДанные на выходе:')
print(open("Seminar3\out.txt").read())

