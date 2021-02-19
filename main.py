from math import sqrt

#
# def is_simple(number):
#     if number > 0:
#         for i in range(2, int(sqrt(number) // 1 + 1)):
#             if (number % i) == 0:
#                 return False
#     return True
#
# for n in range(124):
#     print(n*n + 29*n + 251 if is_simple(n*n + 29*n + 251) else n*n - 29*n + 251)
#
#

import itertools

A = []
41063625
i = 0
for j in itertools.permutations(str(345*345*345), len(str(345*345*345))):
    s = ''
    i += 1
    # print(j)
    for c in j:
        s += c
    if int(s) == 56623104:
        print(i)
    A.append(int(s))

for j in A:
    if j == 56623104:
        print('56623104!!!',j) #'5', '6', '6', '2', '3', '1', '0', '4'
    if j == 41063625:
        print('41063625!!!',j)


print(len(A))

#29 251 7279 124  n^2 +- 29n + 251