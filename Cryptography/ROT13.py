message = input("Enter the message:" )
alph = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm')
abet = ('n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

for i in (message):
    while True:
        if i in (alph):
            position = alph.index(i)
            alph = abet
            pos = alph[position]
            print (pos)
        else:
            position1 = abet.index(i)
            abet = alph
            pos1 = abet[position1]
            print (pos1)


