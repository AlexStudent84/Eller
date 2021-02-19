# Задача 45
# Треугольные, пятиугольные и шестиугольные
# Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:
#
# Треугольные	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Пятиугольные	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Шестиугольные	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Можно убедиться в том, что T285 = P165 = H143 = 40755.
#
# Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.

# Треугольные n(n+1)/2	= 1/2 * n*n - 1/2*n - T   a = 1/2  b = - 1/2   c = - T
# (−b + sqrt(b2 − 4ac)) / 2a

# Шестиугольные	 	Hn=n(2n−1) = 2*n*n - n - H  a = 2  b = - 1   c = - H
from math import sqrt


# Треугольные
def is_trienglenumber(i):
    if ((1/2 + sqrt(1/4 + 4 * 1/2 *i) ) ) % 1 == 0:
        return True
    return False

# Пятиугольные
def is_fiveenglenumber(i):
    if ((1 + sqrt(1 + 4 * 3 * 2*i)) / (2 * 3)) % 1 == 0:
        return True
    return False
# Шестиугольные
def is_sixeenglenumber(i):
    if i > 0:
        if ((1 + sqrt(1 + 4 * 2 * i)) / (2 * 2)) % 1 == 0:
            return True
    return False


for i in range(300000):
    if is_trienglenumber(i) and is_fiveenglenumber(i) and is_sixeenglenumber(i):
        print(i)

#40755