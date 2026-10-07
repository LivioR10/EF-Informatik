pzahlen = []
def Primzahlen():
    for i in range(1, 101):
        anz=0
        if i > 2:
            for j in range(1, 101):
                if i%j==0:
                    anz+=1
        if anz==2:
            pzahlen.append(i)
Primzahlen()
print(pzahlen)