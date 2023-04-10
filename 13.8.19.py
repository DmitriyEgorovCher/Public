tikets = int(input('введите количество билетов которое хотите приобрести - '))
cost = []
for i in range(tikets):
    years = int(input('Введите возраст: '))
    if years < 18:
        continue
    elif 18 <= years < 25:
        cost.append(990)
    else:
        cost.append(1390)
if tikets > 3:
    cost = [i * 0.9 for i in cost]
print(sum(cost))