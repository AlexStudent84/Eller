# Задача 50
# Сумма последовательных простых чисел
# Простое число 41 можно записать в виде суммы шести последовательных простых чисел:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# Это - самая длинная сумма последовательных простых чисел, в результате которой п
# олучается простое число меньше одной сотни.
#
# Самая длинная сумма последовательных простых чисел, в результате которой получ
# ается простое число меньше одной тысячи, содержит 21 слагаемое и равна 953.
#
# Какое из простых чисел меньше одного миллиона можно записать в виде суммы наибольшего ко
# личества последовательных простых чисел?


from math import sqrt


def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


Sim = []
A = []
B = []
C = []
for i in range(1, 1000000):
    if is_simple(i):
        if i > 1000000:
            break
        Sim.append(i)
for n in range(len(Sim) - 500):
    s = 0
    i = 0
    while s < 1000000:
        if s + Sim[n + i] >= 1000000:
            break
        s += Sim[n + i]
        i += 1
    A.append(s)
    B.append(i)
    C.append(n)
max = 0
max_i = 0
for i in range(len(A)):
    if is_simple(A[i]):
        if B[i] > max:
            max = B[i]
            max_i = i

print(A[max_i], B[max_i], Sim[C[max_i]], Sim[C[max_i] + 1], Sim[C[max_i] + 2], '...', Sim[C[max_i] + B[max_i] - 1],
      Sim[C[max_i] + B[max_i]])
# 997651 543 7 11 13 ... 3931 3943
