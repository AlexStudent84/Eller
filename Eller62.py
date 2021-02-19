# Задача 62
# Кубические перестановки
# Можно найти перестановки куба 41063625 (345^3),
# чтобы получить еще два куба: 56623104 (384^3) и 66430125 (405^3).
# К слову, 41063625 является наименьшим кубом, для которого ровно три перестановки также являются кубами
#
# Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.
import itertools


def is_sqrt3(i):
    if sqrt3(i) % 1 == 0:
        return True
    return False


def sqrt3(i):
    return i ** (1 / 3) + 0.0000000000001


for i in range(1, 400):
    n = i ** 3
    k = 0
    A = []
    for j in itertools.permutations(str(n), len(str(n))):
        s = ''
        for c in j:
            s += c
        A.append(int(s))

    B = []
    for i1 in range(len(A)):
        if A[i1] != n:
            if A[i1] not in B:
                B.append(A[i1])
    A = B
    for j in A:
        if is_sqrt3(j):
            k += 1
    if k >= 2:
        print(i, ': ', k)
