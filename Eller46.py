# Задача 46
# Другая проблема Гольдбаха
# Кристиан Гольдбах показал, что любое нечетное составное число можно записать в виде суммы простого числа и удвоенного квадрата.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# Оказалось, что данная гипотеза неверна.
#
# Каково наименьшее нечетное составное число, которое нельзя записать в виде суммы простого числа и удвоенного квадрата?

from math import sqrt

Sim = []


def is_sum_sim_and_sqr(i):
    for s in Sim:
        k = 1
        while s + 2 * k * k <= i:
            if s + 2 * k * k == i:
                print(i ,' = ',s ,' + 2',k,'^2 ( ', k*k,')')
                return True
            k += 1
    return False


def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


for i in range(1, 10000):
    if is_simple(i):
        Sim.append(i)

A = []

for i in range(1, 10000, 2):
    if i not in Sim:
        A.append(i)

i = 10
while i < len(A):
    if not is_sum_sim_and_sqr(A[i]):
        print('stop at: ',A[i])
        break
    i +=1

#stop at:  5777