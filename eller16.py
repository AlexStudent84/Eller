# Задача 16
# Сумма цифр степени
# 2^15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
#
# Какова сумма цифр числа 2^1000?
#
# Оригинал

n = 2 ** 1000

s = 0

while n > 0:
    s += n % 10
    n //= 10

print(s) #1366
