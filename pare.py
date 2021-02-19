from math import sqrt


def is_simple(number):
    for i in range(3, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False

    return True


size = 10000

# A = list(range(1, size,2))
# A = []
# for i in range(1, size,2):
#     A.append(i)

pos = 0

for i in range(1, size,2):
    # print(i)
    if (is_simple(i)):
        if (is_simple(i + 2)):
            print(i - pos)
            pos = i

    # for j in range(i*i, size, i):
    #     if j in A:
    #         A.remove(j)
