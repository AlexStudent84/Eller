# Задача 57
# Приближения квадратного корня
# Можно убедиться в том, что квадратный корень из двух можно выразить в виде бесконечно длинной дроби.
#
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# Приблизив это выражение для первых четырех итераций, получим:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# Следующие три приближения: 99/70, 239/169 и 577/408, а восьмое приближение, 1393/985,
# является первым случаем, в котором количество цифр в числителе превышает количество цифр в знаменателе.
#
# У скольких дробей длина числителя больше длины знаменателя в первой тысяче приближений выражения?
#
# Оригинал

# 1 / (2 + 1/2) = 1 / ( 4/2 + 1/2 ) = 1 / ( 5/2 )

def len_number(i):
    c = 0
    while i > 0:
        i //= 10
        c += 1
    return c

a = 1
b = 2
res = 0
for n in range(1,1000):
    a = a + 2 * b
    a, b = b, a
    if len_number(a + b) > len_number(b):
        res +=1
print(res) #153
# print(a + b, '/', b)