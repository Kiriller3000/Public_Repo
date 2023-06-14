#Блок ввода данных
try:
    num_of_tickets = int(input('Сколько билетов Вы хотите купить? \nПри покупке от 4 билетов скидка 10%\n>>'))

    list_of_age = []
    for i in range(1, num_of_tickets + 1):
        Age = int(input(f'Укажите возраст посетителя № {i}: '))
        list_of_age.append(Age)
except ValueError as error:
    exit('Введите число!')

#Блок расчетов
summary = 0
for age in list_of_age:
    if 15 < age < 18:
        summary += 0
    elif 18 <= age < 25:
        summary += 990
    elif 25 <= age <= 100:
        summary += 1390
    else:
        num_of_tickets -= 1
        print(f'Не соответствует возраст {age} лет.')

summ = ''
if num_of_tickets > 3:
    summary -= summary * 0.1
    summ = 'c учетом скидки в 10%'

#Блок вывода
print(f'\nСтоимость {num_of_tickets} билетов', summ, '= %10.2f ₽' % summary)
