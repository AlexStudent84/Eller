# Задача 34
# Факториалы цифр
# 145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
#
# Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
#
# Оригинал

A=[0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


for i in range(145,10000000000):
    s = 0
    old_i =i
    while (i // 10) > 0:
       s += A[(i % 10)]
       i //=10

    s += A[i]
    if s == old_i:
        print(old_i)