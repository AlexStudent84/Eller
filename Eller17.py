# Задача 17
# Счет букв в числительных
# Если записать числа от 1 до 5 английскими словами
# (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
#
# Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
#
#
# Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two)
# состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв.
# Использование "and" при записи чисел соответствует правилам британского английского.


A1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten'
         , "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
A10 =["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


def len_no_space(s:str):
    k = 0
    for i in range(len(s)):
        if s[i] != ' ':
            k +=1
    return k


sum = 0

for i in range(1,1000):
    s = ''
    old_i = i
    if i // 100 > 0:
        s += A1[i // 100 -1] + ' hundred'
        i %= 100


    if i >= 0 and i < 20:
        for n in range(1, 20):
            if i == n:
                if s != '':
                    s += ' and '+ A1[n-1]
                else:
                    s += A1[n-1]
                break
    else:
        if s != '':
            s += ' and'
        s += ' ' + A10[i//10]
        if i % 10 > 0:
            s += ' ' + A1[i % 10 -1]

    sum += len_no_space(s)
    print(old_i,': ',s ,'-> ',len_no_space(s))
# + one thousand = 11
sum += len_no_space('one thousand')
print(sum) #21124