per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('введите сумму для внесения: '))
a = per_cent.get('ТКБ')
b = per_cent.get('СКБ')
c = per_cent.get('ВТБ')
d = per_cent.get('СБЕР')
bank_1 = money*a/100
bank_2 = money*b/100
bank_3 = money*c/100
bank_4 = money*d/100
deposit = [bank_1, bank_2, bank_3, bank_4]
print(list(map(float, deposit)))
max_deposit = max(deposit)
print('Максимальный депозит = ' + str(max_deposit))