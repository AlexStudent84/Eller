# Задача 62
# Кубические перестановки
# Можно найти перестановки куба 41063625 (345^3),
# чтобы получить еще два куба: 56623104 (384^3) и 66430125 (405^3).
# К слову, 41063625 является наименьшим кубом, для которого ровно три перестановки также являются кубами
#
# Найдите наименьший куб, для которого ровно пять перестановок также являются кубами.

def sqrt3(i):
    return i ** (1 / 3) + 0.0000000000001

def len_number(i):
    c = 0
    while i > 0:
        i //= 10
        c += 1
    return c


def is_permutation(a, b):
    A = []
    B = []
    while a > 0:
        A.append(a % 10)
        a //= 10
    A.sort()
    while b > 0:
        B.append(b % 10)
        b //= 10
    B.sort()
    if A == B:
        return True

    return False

A = []
B = []
n = 1
for i in range(1, 100001):
    k = i ** 3
    if len_number(k) == n:
        B.append(i * i * i)
    else:
        n = len_number(k)
        A.append(B)
        B = []

for i in range(7,len(A)):
    for i1 in range(len(A[i])):
        k = 0
        B.append(A[i][i1])
        for i2 in range(i1+1,len(A[i])):
            if is_permutation(A[i][i1], A[i][i2]):
                k +=1
                B.append(A[i][i2])

        if k > 4:
            print(sqrt3(B[0]),B)
        B = []

#5027 = 4
#10002 = 5 [1000600120008, 1006012008000, 1061208000000, 8001200060001, 8012006001000, 8120601000000]