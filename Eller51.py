# Задача 51
# Замена цифр в простом числе
# Меняя первую цифру числа *3 (двузначного числа, заканчивающегося
# цифрой 3), оказывается, что шесть из девяти возможных значений - 13, 23, 43, 53, 73 и 83 - являются простыми числами.
#
# При замене третьей и четвертой цифры числа 56**3 одинаковыми
# цифрами, получаются десять чисел, из которых семь - простые: 56003, 56113, 56333, 56443, 56663, 56773 и 56993.
# Число 56**3 является наименьшим числом, подставление цифр в которое дает именно семь простых чисел. Соответственно,
# число 56003, будучи первым из полученных простых чисел, является наименьшим простым числом,
# обладающим указанным свойством.
#
# Найдите наименьшее простое число, которое является одним из
# восьми простых чисел, полученных заменой части цифр (не обязательно соседних) одинаковыми цифрами.
#
# Оригинал
import copy
import itertools
from builtins import range

from math import sqrt


def listtoint(A):
    s = 0
    for i in range(len(A)):
        s = s + A[i] * 10 ** (len(A) - i - 1)
    return s


def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


size = 6

B = list([])
A = list([])
C = []
for i in itertools.product('0*', repeat=size):
    B.append(i)

# for i in range(len(B)):
#     for j in range(len(B[i])):
#         C.append(B[i][j])


for i in range(len(B)):
    C = []
    for j in range(len(B[i])):
        C.append(B[i][j])
    A.append(C)

B = A
# A = []
#
for i in range(len(B)):
    # A.append(B[i])
    D = []
    for j in range(size):
        if B[i][j] == '0':
            D.append(j)
    # print(D, B[i])
    if len(D) > 0:
        for n in range(1, 10 ** len(D)):
            C = []
            while n > 0:
                C.append(n % 10)
                n //= 10
            while len(C) < len(D):
                C.append(0)
            # print(C)
            for t in range(len(D)):
                B[i][D[t]] = C[t]
            C1 = []
            for k in range(size):
                C1.append(B[i][k])
            A.append(C1)

C = []
i = 0
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         print(A[i][j])

B = []

for i in range(len(A)):
    # print(A[i], end=' ')
    for n in range(10):
        C = []
        for j in range(len(A[i])):
            if A[i][j] == "*":
                C.append(n)
            else:
                C.append(A[i][j])
        U = []
        # for k in range(len(C)):
        #      U.append(C[k])
        U = C.copy()
        B.append(U)

        # print(C, end=' ')
    # print()

# print(A[1],B[1],B[2],B[3],B[4],B[5],B[6],B[7],B[8],B[9],B[10])

max = 0
max_i = 0

for i in range(len(A)):
    if '*' in A[i]:
        k = 0
        for n in range(10):
            if is_simple(listtoint(B[i * 10 + n])):
                k += 1
        if k >= max:
            max = k
            max_i = i
C = []
print(max, A[max_i])
for n in range(10):
    C.append(B[max_i * 10 + n])
    print(B[max_i * 10 + n], end=' ')

print()
for n in range(10):
    if not is_simple(listtoint(C[n])):
        print(C[n])


# print(len(A), len(B))
# 8 ['*', '*', '*', 1, 0, 9]
# [0, 0, 0, 1, 0, 9] [1, 1, 1, 1, 0, 9] [2, 2, 2, 1, 0, 9] [3, 3, 3, 1, 0, 9] [4, 4, 4, 1, 0, 9]
# [5, 5, 5, 1, 0, 9] [6, 6, 6, 1, 0, 9] [7, 7, 7, 1, 0, 9] [8, 8, 8, 1, 0, 9] [9, 9, 9, 1, 0, 9]
# not simple
# [3, 3, 3, 1, 0, 9]
# [9, 9, 9, 1, 0, 9]