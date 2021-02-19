# Задача 37
# Укорачиваемые простые числа
# Число 3797 обладает интересным свойством. Будучи само по себе простым числом, из него можно последовательно
# выбрасывать цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7.
# Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.
#
# Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево,
# так и слева направо, но числа при этом остаются простыми.
#
# ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.
#
# Оригинал


from math import sqrt


def is_simple(number):
    for i in range(2, int(sqrt(number) // 1 + 1)):
        if (number % i) == 0:
            return False
    return True


def is_totaly_simple(i):
    f = False
    if is_simple(i):
        f = True
        old_i = i
        max10 = 0
        # remove right end
        while i > 0:
            i //= 10
            max10 += 1
            if not is_simple(i):
                f = False
                break
        # remove left end
        if f:
            i = old_i
            for n in range(max10 - 1, 0, -1):
                i %= 10 ** n
                if not is_simple(i):
                    f = False
                    break
    return f


A = []

for i in range(1, 10000):
    if is_simple(i):
        A.append(i)
B = []

for i in A:
    for n in A:
        if is_totaly_simple(i + n) and i + n > 7:
            if i + n not in B:
                B.append(i + n)
                print(i, n, '=', i + n)
# print(B)

s = 0
c = 0
for i in A:
    if c == 11:
        break
    if is_totaly_simple(i) and i > 7:
        s += i
        print(i)
        c += 1
print(s) #573
