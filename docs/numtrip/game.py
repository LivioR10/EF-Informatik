from random import randint 

spielfeldliste = [
    [4, 2, 2, 2, 2],
    [4, 8, 8, 2, 4],
    [2, 2, 8, 8, 8],
    [8, 8, 2, 8, 2],
    [4, 16, 16, 8, 4]
]

def liste_machen():
    for i in range(5):
        for k in range(31):
            print("━", end="")
        print()
        for j in range(5):
            x=5
            l_grösse = len(str(spielfeldliste[i][j]))
            string = str(spielfeldliste[i][j])
            if l_grösse == 3 or l_grösse == 1:
                print("|" + ((x-l_grösse)//2)*" " + string + ((x-l_grösse)//2)*" ", end="")
            else:
                print("|" + 2*" " + string + " ", end="")
        print("|")
    for k in range (31):
        print("━", end="")

liste_machen()