from random import randint 

spielfeldliste = [
    [4, 2, 2, 2, 2],
    [4, 8, 8, 2, 4],
    [2, 2, 8, 8, 8],
    [8, 8, 2, 8, 2],
    [4, 16, 16, 8, 4]
]

def liste_machen():
    print(4*" ", end="")
    for e in range(1, 6):
        print(3*" " + str(e) + 2*" ", end="")
    print()
    for i in range(5):
        print(4*" ",end="")
        for k in range(31):
            print("━", end="")
        print()
        print(str(i+1) + 3*" ", end="")
        for j in range(5):
            x=5
            l_grösse = len(str(spielfeldliste[i][j]))
            string = str(spielfeldliste[i][j])
            if l_grösse == 3 or l_grösse == 1:
                print("|" + ((x-l_grösse)//2)*" " + string + ((x-l_grösse)//2)*" ", end="")
            else:
                print("|" + 2*" " + string + " ", end="")
        print("|")
    print(4*" ", end="")
    for k in range (31):
        print("━", end="")

liste_machen()