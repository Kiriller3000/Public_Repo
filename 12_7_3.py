per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите желаемую сумму вклада: '))
print(money,'₽\n')

tkb  = int(money * per_cent['ТКБ'] / 100)
skb  = int(money * per_cent['СКБ'] / 100)
vtb  = int(money * per_cent['ВТБ'] / 100)
sber = int(money * per_cent['СБЕР'] /100)

deposit = [tkb, skb, vtb, sber]
#print(deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit),'₽' )
