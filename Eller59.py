# Задача 59
# XOR шифровка
# Каждый символ в компьютере имеет уникальный код, предпочитаемым
# является стандарт ASCII (American Standard Code for Information
# Interchange - Американский стандартный код для обмена информацией).
# Для примера, A верхнего регистра = 65, звездочка (*) = 42, а k нижнего регистра = 107.
#
# Современный метод шифровки состоит в том, что берется текстовый файл, конвертируется
# в байты по ASCII, а потом над каждым байтом выполняется операция XOR с определенным значением,
# взятым из секретного ключа. Преимущество функции XOR состоит в том, что применяя тот же ключ к зашифрованному
# тексту, получается исходный; к примеру, 65 XOR 42 = 107, тогда 107 XOR 42 = 65.
#
# Для невзламываемого шифрования ключ должен быть такой же длины, что и сам текст,
# и ключ должен быть составлен из случайных байтов. Тогда, если пользователь хранит
# зашифрованное сообщение и ключ шифрования в разных местах, то без обеих "половинок"
# расшифровать сообщение просто невозможно.
#
# К сожалению, этот метод непрактичен для большинства пользователей, поэтому упрощенный
# метод использует в качестве ключа пароль. Если пароль короче текстового сообщения, что
# наиболее вероятно, то ключ циклично повторяется на протяжении всего сообщения. Идеальный
# пароль для этого метода достаточно длинный, чтобы быть надежным, но достаточно короткий,
# чтобы его можно было запомнить.
#
# Ваша задача была упрощена, так как пароль состоит из трех символов нижнего регистра. Используя
# cipher1.txt (щелкнуть правой кнопкой мыши и выбрать 'Save Link/Target As...'), содержащий зашифрованные коды ASCII,
# а также тот факт, что сообщение должно содержать распространенные английские слова, расшифруйте сообщение и найдите
# сумму всех значений ASCII в исходном тексте.


def xor_arr(A,B):
    C = []
    for i in range(len(A)):
        C.append(int(A[i]) ^ int(B[i]))
    return C

def arr_to_str(A):
    s = ''
    for i in range(len(A)):
        s += chr(A[i])
    return s

def start_hack(A):
    for i1 in range(97, 123):
        for i2 in range(97, 123):
            for i3 in range(97, 123):
                B = []
                s = ''
                for i in range(0, len(A), 3):
                    B.append(i1)
                    B.append(i2)
                    B.append(i3)
                C = xor_arr(A, B)
                s = arr_to_str(C)
                if s.find(' is ') > 0 and s.find(' a ') > 0:
                    # if s.find(' not ') > 0 and s.find(' is ') > 0 and s.find(' a ') > 0:
                    print(chr(i1) + chr(i2) + chr(i3))
                    print(s)
                    return s


f = open('p059_cipher.txt', mode='r')
str1 = f.read()
A = str1.split(',')
s = start_hack(A)
summ = 0
for i in range(len(s)):
    summ += ord(s[i])

print('summ =',summ)
# Key is = "exp"