from random import randint 
player_input = True
Buchstaben = [
    "A", "B", "C", "D", "E"
]
spielfeldliste = [
    [],
    [],
    [],
    [],
    []  
]
def wert():
    hoch = randint(1, 3)
    spielfeldliste
spielfeldliste = [
    [4, 2, 2, 2, 2],
    [4, 8, 8, 2, 4],
    [2, 2, 8, 8, 8],
    [32, 8, 2, 64, 2],
    [4, 8, 16, 8, 4]
]
farben ={
    2: "\033[42m",
    4: "\033[105m",
    8: "\033[45m",
    16: "\033[41m",
    32: "\033[46m",
    64: "\033[44m",
    128: "\033[48;5;17m",
    "   ": "\033[39m"
    }
reset = "\033[0m"

def zahlen_unten():
    print(4*" ", end="")
    for e in range(5):
        print(3*" " + str(Buchstaben[e]) + 2*" ", end="")
    print()

def querlinie():
    for k in range (31):
        print("━", end="")

def spielfeld_zeichnen():
    for i in range(5):
        print(4*" ",end="")
        querlinie()
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
    querlinie()
    print()
    zahlen_unten()

def auswerten(Koordinate):
    y_kor = int(Koordinate[1])
    x_kor = int(Buchstaben.index(Koordinate[0]))
    spielfeldliste[y_kor-1][x_kor] = "   "
def input_abfragen():
    global Koordinate
    Koordinate = input("Gib die Korrdinaten ein.(Z.B: A1) \nKoordinate: ")
def play():
    global Koordinate
    while player_input:
        input_abfragen()
        auswerten(Koordinate)
        spielfeld_zeichnen()
        print()
play()