# Задача 58
# Спиральные простые числа
# Начиная с 1 и продвигаясь по спирали в направлении против часовой стрелки, получается квадратная спираль с длиной стороны 7
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# Интересно заметить, что нечетные квадраты лежат на правой нижней полудиагонали. Еще интереснее то,
# что среди 13 чисел, лежащих на обеих диагоналях, 8 являются простыми; т.е. отношение составляет 8/13 ≈ 62%.
#
# Если добавить еще один целый слой вокруг изображенной выше спирали, получится квадратная спираль с длиной стороны 9.
# Если продолжать данный процесс, какой будет длина стороны квадратной спирали, у которой отношение количества простых
# чисел к количеству всех чисел на обеих диагоналях упадет ниже 10%?
from math import sqrt

def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True

for n in range(10001, 10003, 2):
    size = n
    x1 = y1 = size // 2
    A = [[0] * size for i in range(size)]

    Flag = 'right'

    A[x1][y1] = 1
    for i in range(2, size * size + 1):
        if Flag == 'right':
            A[x1][y1 + 1] = i
            y1 += 1
            if A[x1 - 1][y1] == 0:
                Flag = 'up'
                continue
        if Flag == 'down':
            A[x1 + 1][y1] = i
            x1 += 1
            if A[x1][y1 + 1] == 0:
                Flag = 'right'
                continue
        if Flag == 'left':
            A[x1][y1 - 1] = i
            y1 -= 1
            if A[x1 + 1][y1] == 0:
                Flag = 'down'
                continue
        if Flag == 'up':
            A[x1 - 1][y1] = i
            x1 -= 1
            if A[x1][y1 - 1] == 0:
                Flag = 'left'
                continue

        #  right -> up ->  left -> down
    # for i in range(len(A)):
    #     print(A[i])

    B = []

    for i in range(size):
        if i == size - i - 1:
            B.append(A[i][i])
        else:
            B.append(A[i][i])
            B.append(A[i][size - i - 1])
        # print(A[i][i] , A[i][size - i - 1])

    simpl = 0
    for i in B:
        if is_simple(i):
            simpl += 1
    print(simpl/len(B))
    if simpl/len(B) < 0.1:
        print(n)
        break
#10001
#0.11254437278136094
