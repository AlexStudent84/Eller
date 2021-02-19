# Задача 3
# Наибольший простой делитель
# Простые делители числа 13195 - это 5, 7, 13 и 29.
#
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
#
# Оригинал
# max = 0
# proc = 0
# for i in range(2, 600851475143 // 2):
#     if (i / 600851475143 * 100)//1 > proc:
#         proc = i / 600851475143 * 100
#         print(proc//1)
#     if (600851475143 % i) == 0:
#         f = True
#         # print(i)
#         for n in range(2, i // 2):
#             if (i % n) == 0:
#                 f = False
#                 break
#         if f:
#             max = i
# print(max, "=  max")

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


# print(600851475143 / 8462696833)
# print(600851475143 / 839)
# print(i)


start = 600851475143
#
# if is_normal(839):
#     print("71!!!!")

# start = 8462696833
i = 2
while start > i:
    if (start % i) == 0:
        if is_normal(start % i):
            start //= i
            print(i)

    i += 1
