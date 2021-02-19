# Задача 44
# Пятиугольные числа
# Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако, их разность, 70 − 22 = 48,
# не является пятиугольным числом.
#
# Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность являются пятиугольными числами и значение
# D = |Pk − Pj| минимально, и дайте значение D в качестве ответа.


# P=n(3n−1)/2
# P*2=n(3n−1)
# P*2 = 3n*n - n
# 3n*n - n - 2*p = 0
# n = 1 ± sqrt(-1*-1 - 4*3*2p) / 2 * 3
#
# Источник: https://math-prosto.ru
from math import sqrt

def is_trienglenumber(i):
    if ((1 + sqrt(1 + 4 * 3 * 2*i)) / (2 * 3)) % 1 == 0:# or ((1 - sqrt(1 + 4 * 3 * 2*i) ) / (2 * 3)) % 1 == 0:
        return True
    return False


# P = []

# if is_trienglenumber(57):
#     print(57)

for i in range(10000, 20000):
    for n in range(i-1,0,-1):
        if is_trienglenumber(i * (3 * i - 1) / 2 + n * (3 * n - 1) / 2) and is_trienglenumber(i * (3 * i - 1) / 2 - n * (3 * n - 1) / 2):
            print('All is ok ', i * (3 * i - 1)/ 2,  n * (3 * n - 1) / 2)

    # 1560090.0 7042750.0 1020 2167


    # P.append(i * (3 * i - 1) / 2)

# for n in range(len(P)):
#     for i in range(len(P)-n):
#     # for n in range(len(P)-i)
#         n1 = P[i]
#         n2 = P[i+n]
#         if ((n1 + n2) in P) and ((n2 - n1) in P):
#            print(n1, n2)
#
# for i in range(1000, len(P)):
#     for j in range(i, len(P)):
#         n1 = P[i]
#         n2 = P[j]
#         if ((n1 + n2) in P) and ((n2 - n1) in P):
#             print(n1, n2, i, j)  # 1560090.0 7042750.0 1020 2167
