# Задача 15
# Пути через таблицу
# Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
#
#
# Сколько существует таких маршрутов в сетке 20×20?
#
# Оригинал


# обязательно придется сделать 20 вниз и 20 вправо

import itertools

#str = '1111111111111111111100000000000000000000'
str = '1111100000'
#str = '1100'
A =[]

for i in itertools.permutations(str, len(str)):
    A.append(i)


new_list = []
[new_list.append(item) for item in A if item not in new_list]

print(len(new_list))
