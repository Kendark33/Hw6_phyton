# Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.     Если а1=-3: и d=0.7 | a11 = -3 + 0.7(11-1) = 4
# Каждое число вводится с новой строки.

a_1 = int(input('Первый элемент массива: '))
d = int(input('Разность: '))
n = int(input('Количество элементов: '))
arr = []
for i in range(1, n + 1):
    arr.append(a_1 + (i - 1) * d)
print(arr)