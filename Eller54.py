class Cart:
    def __init__(self, s):  # s = 'AD'
        self.suit = s[1]
        # T J Q K A
        if s[0] == 'T':
            self.value = 10
            return
        if s[0] == 'J':
            self.value = 11
            return
        if s[0] == 'Q':
            self.value = 12
            return
        if s[0] == 'K':
            self.value = 13
            return
        if s[0] == 'A':
            self.value = 14
            return
        self.value = int(s[0])

    def __lt__(self, other):
        return self.value < other.value


class Hend:
    def __init__(self, s: str):
        self.cards = []
        self.combination = [0] * 8
        self.combination.append([0] * 5)
        A = s.split(' ')
        for x in A:
            self.cards.append(Cart(x))
        self.cards.sort()
        self.initCombination()

    def initCombination(self):
        # is strit
        stit = 0
        for i in range(len(self.cards) - 1):
            if self.cards[i].value == self.cards[i + 1].value - 1:
                stit += 1
        if stit == 4:
            self.combination[4] = self.cards[4].value

        # is flesh
        flesh = 0
        for x in self.cards:
            if self.cards[0].suit == x.suit:
                flesh += 1
        if flesh == 5:
            self.combination[3] = self.cards[4].value

        # is stit-flash
        if self.combination[3] > 0 and self.combination[4]:
            self.combination[0] = self.cards[4].value

        # kikers
        i = 0
        for x in self.cards:
            self.combination[8][i] = x.value
            i += 1

        # 4
        if self.cards[0].value == self.cards[3].value or self.cards[1].value == self.cards[4].value:
            self.combination[1] = self.cards[2].value

        # Trips
        if self.combination[1] == 0:
            if self.cards[0].value == self.cards[2].value or self.cards[1].value == self.cards[3].value or self.cards[
                2].value == self.cards[4].value:
                self.combination[5] = self.cards[2].value
        # Full
        if self.combination[5] > 0:
            if self.cards[0].value == self.cards[1].value and self.cards[0].value != self.combination[5]:
                self.combination[2] = self.cards[2].value
                self.combination[7] = self.cards[0].value

            if self.cards[3].value == self.cards[4].value and self.cards[3].value != self.combination[5]:
                self.combination[2] = self.cards[2].value
                self.combination[7] = self.cards[3].value

        # Pare
        pare = 0
        pos = 0
        if self.combination[1] == 0 and self.combination[5] == 0:
            for i in range(len(self.cards)-1):
                for j in range(i+1, len(self.cards)):
                    if self.cards[i].value == self.cards[j].value:
                        pare += 1
                        pos = i

            if pare == 1:
                self.combination[7] = self.cards[pos].value
            if pare == 2:
                if self.cards[0] == self.cards[1]:
                    self.combination[6] = self.cards[0].value
                else:
                    self.combination[6] = self.cards[1].value

                self.combination[7] = self.cards[pos].value

    def __str__(self):
        s = ''
        for i in range(len(self.cards)):
            s += str(self.cards[i].value) + self.cards[i].suit + ' '
        return s


f = open('p054_poker.txt', mode='r')

str1 = f.read()
A = []
B = []

A = str1.split('\n')
strhend1 = ''
strhend2 = ''

First_win = 0

for str1 in A:
    strhend1 = str1[0:14]
    strhend2 = str1[15:224]
    h1 = Hend(strhend1)
    h2 = Hend(strhend2)

    if h1.combination > h2.combination:
        First_win +=1
    if h1.combination == h2.combination:
        print("Drow!!!")

print(First_win,' from', len(A))
# First_win = 406