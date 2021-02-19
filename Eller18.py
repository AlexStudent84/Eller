# Найдите максимальную сумму пути от вершины до основания следующего треугольника:
import itertools

A = []
str = ""
A.append([75])
A.append([95, 64])
A.append([17, 47, 82])
A.append([18, 35, 87, 10])
A.append([20, 4, 82, 47, 65])
A.append([19, 1, 23, 75, 3, 34])
A.append([88, 2, 77, 73, 7, 63, 67])
A.append([99, 65, 4, 28, 6, 16, 70, 92])
A.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
A.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
A.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
A.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
A.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
A.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
A.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

B = []
for i in itertools.product('01', repeat=15):
    B.append(i)
pos = 0
max = 0
iter = 0
for item in B:
    s = A[0][0]
    c = 0
    for i in range(1, 15):
        if item[i] == '0':
            s += A[i][c]
        else:
            c += 1
            s += A[i][c]
    if s > max:
        max = s
        pos = iter

    iter += 1

print(max)
print(B[pos])
