# Задача 27
# Квадратичные простые числа
# Эйлер опубликовал свою замечательную квадратичную формулу:
#
# n2+n+41
# Оказалось, что согласно данной формуле можно получить 40 простых чисел,
# последовательно подставляя значения 0≤n≤39. Однако, при n=40, 402+40+41=40(40+1)+41 делится на 41 без остатка,
# и, очевидно, при n=41,412+41+41 делится на 41 без остатка.
#
# При помощи компьютеров была найдена невероятная формула n2−79n+1601, согласно которой можно получить 80 простых чисел
# для последовательных значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.
#
# Рассмотрим квадратичную формулу вида:
#
# n^2+an+b, где |a|<1000 и |b|≤1000
# n^2+3n+1
# где |n| является модулем (абсолютным значением) n.
# К примеру, |11|=11 и |−4|=4
# Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное
# количество простых чисел для последовательных значений n, начиная со значения n=0.

from math import sqrt


def is_simple(number):
    if number < 0:
        return False
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


B = []

for i in range(1, 1000):
    if is_simple(i):
        B.append(i)
max = 0

for a in range(1, 1000):
    for b in B:
        k = 0
        for n in range(1000):
            if is_simple(n * n + a * n + b) or is_simple(n * n - a * n + b):
                k += 1
            else:
                break
        if k > max:
            max = k
            print(a, b, a * b, k)
#29 251 7279 124  n^2 +- 29n + 251