# Задача 60
# Объединение пары в простое число
# Простые числа 3, 7, 109 и 673 достаточно замечательны.
# Если взять любые два из них и объединить их в произвольном порядке,
# в результате всегда получится простое число. Например, взяв 7 и 109,
# получатся простые числа 7109 и 1097. Сумма этих четырех простых чисел,
# 792, представляет собой наименьшую сумму элементов множества из четырех простых чисел,
# обладающих данным свойством.
#
# Найдите наименьшую сумму элементов множества из 5 простых чисел,
# для которых объединение любых двух даст новое простое число.


from math import sqrt


def len_number(i):
    c = 0
    while i > 0:
        i //= 10
        c += 1
    return c


def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


def is_merg_number_is_simple(a, b):
    # print(a * (10 ** len_number(b)) + b)
    # print(b * (10 ** len_number(a)) + a)
    if is_simple(a * (10 ** len_number(b)) + b) and is_simple(b * (10 ** len_number(a)) + a):
        return True
    return False


def is_mergd_arr_is_simple(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if not is_merg_number_is_simple(A[i], A[j]):
                return False
    print(A)
    return True


A = []

for i in range(1, 8500):
    if is_simple(i):
        A.append(i)


for i1 in range(0, len(A)):
    for i2 in range(i1+1, len(A)):
        if is_merg_number_is_simple(A[i1],A[i2]):
            for i3 in range(i2+1, len(A)):
                if is_merg_number_is_simple(A[i2], A[i3]) and is_merg_number_is_simple(A[i1], A[i3]):
                    for i4 in range(i3+1, len(A)):
                        if is_merg_number_is_simple(A[i4], A[i1]) and is_merg_number_is_simple(A[i4], A[i2]) and is_merg_number_is_simple(A[i4], A[i3]):
                             for i5 in range(i4+1, len(A)):
                                B = []
                                B.append(A[i1])
                                B.append(A[i2])
                                B.append(A[i3])
                                B.append(A[i4])
                                B.append(A[i5])

                                if is_mergd_arr_is_simple(B):
                                    print(B)
# [13, 5197, 5701, 6733, 8389]