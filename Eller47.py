# Задача 47
# Различные простые множители
# Первые два последовательные числа, каждое из которых имеет два отличных друг от друга простых множителя:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# Первые три последовательные числа, каждое из которых имеет три отличных друг от друга простых множителя:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Найдите первые четыре последовательных числа, каждое из которых
# имеет четыре отличных друг от друга простых множителя. Каким будет первое число?
from math import sqrt


def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


Sim = []
A = []

for i in range(1, 150):
    if is_simple(i):
        Sim.append(i)

i1 = 0
i2 = 0
i3 = 0
i4 = 0


for i1 in range(len(Sim)-3):
    for i2 in range(i1+1,len(Sim)-2):
        for i3 in range(i2+1,len(Sim)-1):
#            for i4 in range(i3+1,len(Sim)):
#                if i1 != i2 and i1 != i3 and i1 != i4 and i2 != i3 and i2 != i4 and i3 != i4:
                A.append(Sim[i1] * Sim[i2] * Sim[i3])# * Sim[i4])

B = []
for i in A:
    if i not in B:
        B.append(i)

B.sort()

for i in range(len(B) - 2):
    if B[i] == B[i + 1] - 1 and B[i] == B[i + 2] - 2: #and B[i] == B[i + 3] - 3:   and B[i] == B[i+4]-4:
        print(B[i], B[i + 1], B[i + 2])
