# Задача 7
# 10001-е простое число
# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.
#
# Какое число является 10001-м простым числом?
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

i = 0
n = 0
while True:
    i +=1
    if is_normal(i):
        n+=1
        if n==10001:
            print(i)
            break


