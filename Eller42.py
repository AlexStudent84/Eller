# Задача 42
# Закодированные треугольные числа
# n-й член последовательности треугольных чисел задается как tn = ½n(n+1). Таким образом, первые десять треугольных чисел:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Преобразовывая каждую букву в число, соответствующее ее порядковому номеру в алфавите, и складывая эти значения, мы по
# лучим числовое значение слова. Для примера, числовое значение слова SKY равно 19 + 11 + 25 = 55 = t10. Если числовое зна
# чение слова является треугольным числом, то мы назовем это слово треугольным словом.
#
# Используя words.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), 16 КБ текстовый файл, содержащий
# около двух тысяч часто используемых английских слов, определите, сколько в нем треугольных слов.


f = open('p042_words.txt', mode='r')
str = f.read()
A = []

start = 1
i = 0

while str.find('","', i) > 0:
    n = str.find('","', i)
    A.append(str[start:n])
    start = n + 3
    i += 1
while '' in A:
    A.remove('')

B = []
for i in range(len(A)):
    s = 0
    for n in range(len(A[i])):
        s += ord(A[i][n]) - 64
    B.append(s)

max = 0
max_i = 0
for i in range(len(B)):
    if B[i] > max:
        max = B[i]
        max_i  = i

C = []
n = 1
while (n*(n+1)/2) <= max:
    C.append(n*(n+1)/2)
    n += 1

k = 0
for i in range(len(B)):
    if B[i] in C:
        k +=1


print('treeangle words is: ',k)
print(A[max_i], max)
#
# treeangle words is:  162
# RESPONSIBILITY 192