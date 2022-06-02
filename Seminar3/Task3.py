# Составить список простых множителей натурального числа N

def factorization(number):
    multipliers = []
    divisor = 2    
    while divisor * divisor <= number:
        if number % divisor == 0:
            multipliers.append(divisor)
            number //= divisor
        else:
            divisor += 1
    if number > 1:
        multipliers.append(number)
    return multipliers

user_number = int(input('Введите целое число: '))
print(f'{user_number} состоит из следующих множителей => {factorization(user_number)}')