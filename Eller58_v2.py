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
n = 3
# B = []
# B.append(1)
sim = 1

while True:
    if is_simple(n*n):
        sim += 1
    if is_simple(n*n -n +1):
        sim += 1
    if is_simple(n*n -n*2 +2):
        sim += 1
    if is_simple(n*n -n*3 +3):
        sim += 1
    if sim / (2*n -1) < 0.1:
        print(n)
        break
    n += 2

#26247

