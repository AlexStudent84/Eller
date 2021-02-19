# Задача 39
# Целые прямоугольные треугольники
# Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c},
# то существует ровно три решения для p = 120:
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# Какое значение p ≤ 1000 дает максимальное число решений?
#
# Оригина

# a*a + b*b = c*c
# a + b + c = p
# b = p - a - c
# a*a + (p - a - c) * (p - a - c) = c*c
# a*a + p*p - a*p - c*p -a*p +a*a + a*c - p*c + a*c + c*c = c * c
# 2a*a + p*p - 2a*p - 2p*c + 2a*c = 0
# (2a*a + p*p - 2a*p)/(2p* - 2a)   = c
from math import sqrt


max = 0
max_p = 0

for p in range(10, 1000):
    k = 0
    for a in range(1, p-2):
        c = (2*a*a + p*p - 2*a*p)/(2*p - 2*a)
        if c % 1 == 0:
            b = sqrt (c * c - a * a)
            if (a + b + c)  == p   and  b > 0:
                k +=1
                if k > max:
                    max = k
                    max_p = p
   #             print(a,b , c ,  ' = ', a + b + c)

print(max_p , max/2) #840 8.0
# 40 399.0 401.0  =  840.0
# 56 390.0 394.0  =  840.0
# 105 360.0 375.0  =  840.0
# 120 350.0 370.0  =  840.0
# 140 336.0 364.0  =  840.0
# 168 315.0 357.0  =  840.0
# 210 280.0 350.0  =  840.0
# 240 252.0 348.0  =  840.0
