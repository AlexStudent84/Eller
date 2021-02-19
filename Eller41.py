# Задача 41
# Пан-цифровое простое число
# Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до nиспользуется в нем ровно один раз.
# К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.
#
# Какое существует наибольшее n-значное пан-цифровое простое число?
from math import sqrt


def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


def is_pannumber(i):
    s = str(i)
    if len(s) < 10:
        A = list(range(1, len(s) + 1))
        for n in range(1, len(s) + 1):
            if i % 10 in A:
                A.remove(i % 10)
                i //= 10
            else:
                return False
        return True
    return False


for i in range(7999999,999999+1, -1):
    if is_simple(i) and is_pannumber(i):
        print(i)  # 7: 7652413
        break

