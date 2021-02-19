# Задача 10
# Сложение простых чисел
# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#
# Найдите сумму всех простых чисел меньше двух миллионов.
#
# Оригинал

def is_normal(number):
    start = number
    i = 2
    while start > i:
        if (start % i) == 0:
            return False
        else:
            start = number // i
        i += 1

    return True


s = 0
for i in range(2000000):
    if is_normal(i):
        s += i

print(s)
