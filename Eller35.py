# Задача 35
# Круговые простые числа
# Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются
# простыми числами: 197, 719 и 971.
#
# Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.
#
# Сколько существует круговых простых чисел меньше миллиона?
#
# Оригинал

import itertools


def is_normal(number):
    start = number
    i = 2
    while start > i:
        if (start % i) == 0:
            return False
  #      else:
  #          start = number // i
        i += 1
    return True


def number_to_digit_array(number):
    A = []
    while (number // 10) > 0:
        A.append(number % 10)
        number //= 10
    A.append(number)
    A.reverse()
    return A


for n in range(1,10000):
    if is_normal(n):
        s = str(n)
        A = []
        for i in itertools.permutations(s, len(s)):
            A.append(i)
        c = 0
        for i in range(len(A)):
            num = 0
            for k in range(len(A[i])):
                num += int(A[i][k]) * 10**(len(A[i]) - k - 1)
            if is_normal(num):
                c += 1
        if c == len(A):
            print(n)

# 113
# 131
# 199
# 311
# 337
# 373
# 733
# 919
# 991
