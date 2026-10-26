from random import randint 

spielfeldliste = [
    [4, 2, 2, 2, 2],
    [4, 8, 8, 2, 4],
    [2, 2, 8, 8, 8],
    [32, 8, 2, 64, 2],
    [4, 128, 16, 8, 4]
]
farben ={
    2: "\033[42m",
    4: "\033[105m",
    8: "\033[45m",
    16: "\033[41m",
    32: "\033[46m",
    64: "\033[44m",
    128: "\033[48;5;17m",
    }
reset = "\033[0m"

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
            string = spielfeldliste[i][j]
            if l_grösse == 3 or l_grösse == 1:
                print("|" + farben[string] + ((x-l_grösse)//2)*" " + str(string) + ((x-l_grösse)//2)*" " + reset, end="")
            else:
                print("|" + farben[string] + 2*" " + str(string) + " " + reset , end="")
        print("|")
    print(4*" ", end="")
    for k in range (31):
        print("━", end="")

liste_machen()