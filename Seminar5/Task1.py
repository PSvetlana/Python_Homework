# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
# Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»


def delete_words(text, value):
    return ' '.join(list(filter(lambda x: x.lower().find(value) < 0, text.split())))


example_text = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
delete_text = 'абв'
print(delete_words(example_text, delete_text))


