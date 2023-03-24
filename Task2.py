# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

mi = int(input('Введите минимальное значение: '))
ma = int(input('Введите максимальное значение: '))
mass = [random.randint(1, 15) for _ in range(10)]
print(mass)
print(min(mass), max(mass))
for i in range(len(mass)):
    if mi <= mass[i] <= ma:
        print(i, end=' , ')