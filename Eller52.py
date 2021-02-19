# Задача 52
# Кратные из переставленных цифр Body:
# Найдите такое наименьшее положительное
# целое число x, чтобы 2x, 3x, 4x, 5x и 6x
# состояли из одних и тех же цифр.


DIG = []


def create_dig(i):
    A = []
    while i > 0:
        if i % 10 not in A:
            A.append(i % 10)
        i //= 10
    return A


def check_dig(i, A):
    while i > 0:
        if i % 10 not in A:
            return False
        i //= 10
    return True

f = False
i = 0
while not f:
    i += 1
    DIG = []
    for k in range(2, 7):
        if k == 2:
            DIG = create_dig(i)
            # print(i, DIG)
        f = check_dig(i*k, DIG)
        if not f:
            break
    if f:
        print(i,":", DIG)
        for k in range(2, 7):
            print(i*k, end =" ")
        print()
# 142857 : [7, 5, 8, 2, 4, 1]
# 285714 428571 571428 714285 857142
