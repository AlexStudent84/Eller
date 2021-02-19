# Задача 28
# Диагонали числовой спирали
# Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# Можно убедиться, что сумма чисел в диагоналях равна 101.
#
# Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?
#
# Оригинал
size = 1001
x1 = y1 = size // 2

A = [[0] * size for i in range(size)]

Flag = 'right'

A[x1][y1] = 1
for i in range(2, size * size + 1):
    if Flag == 'right':
        A[x1][y1 + 1] = i
        y1 += 1
        if A[x1 + 1][y1] == 0:
            Flag = 'down'
            continue
    if Flag == 'down':
        A[x1 + 1][y1] = i
        x1 += 1
        if A[x1][y1 - 1] == 0:
            Flag = 'left'
            continue
    if Flag == 'left':
        A[x1][y1 - 1] = i
        y1 -= 1
        if A[x1 - 1][y1] == 0:
            Flag = 'up'
            continue
    if Flag == 'up':
        A[x1 - 1][y1] = i
        x1 -= 1
        if A[x1][y1 + 1] == 0:
            Flag = 'right'
            continue

    #  right -> down  ->  left -> up
s1 = 0
s2 = 0

for i in range(size):
    s1 += A[i][i]
    s2 += A[i][size - i - 1]

print(s1 + s2 - 1)  # 669171001
