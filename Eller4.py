# Задача 4
# Наибольшее произведение-палиндром
# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
#
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
#
# Оригинал

def is_polendrom(number):
    n = str(number)
    for i in range(len(n)//2):
        if n[i] != n[len(n)-1-i]:
            return False
    return True


max = 0
n1_max = 0
n2_max = 0
for n1 in range(100, 1000):
    for n2 in range(100, 1000):
        if is_polendrom(n1 * n2):
            if n1 * n2 > max:
                max = n1 * n2
                n1_max = n1
                n2_max = n2
print(max)
print(n1_max)
print(n2_max)
