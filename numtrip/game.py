from random import randint 
player_input = True
prüfung = True
kein_Alpha = 0
kein_Zahl = 0
zu_gross = 0
zu_lang = 0

Buchstaben = [
    "A", "B", "C", "D", "E"
]

spielfeldliste = []

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

def spielfeldgeneration():
    for j in range(5):
        spielfeldliste.append([])
        for i in range(5):
            hoch = randint(1, 3)
            spielfeldliste[-1].append(2**hoch)

def Exit(Koordinate):
    if Koordinate == "Exit" or Koordinate == "Stopp":
        return True
    return False

def zahlen_unten():
    print(4*" ", end="")
    for e in range(5):
        print(3*" " + str(Buchstaben[e]) + 2*" ", end="")
    print()

def querlinie():
    for k in range (31):
        print("━", end="")

def fehlermeldungen():
    global kein_Alpha, kein_Zahl, zu_gross, zu_lang
    rot = farben[16]
    if kein_Zahl == 1:
        print(rot + "Der zweite Teil ist keine Zahl" + reset)
    if kein_Alpha == 1:
        print(rot + "Der erste Teil ist kein Buchstabe" + reset)
    if zu_gross == 1:
        print(rot + "Sorry dieser Punkt befindet sich nicht im Spielfeld" + reset)
    if zu_lang == 1:
        print(rot + "Eine zu lange Koordinate. Bitte nur zwei Zeichen verwenden" + reset)
    kein_Alpha = 0
    kein_Zahl = 0
    zu_gross = 0
    zu_lang = 0

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

def erneute_frage():
    while True:
        Erneute_frage = input("Wolltest du " + Koordinate[0:2] + " eingeben?. Bitte ja oder nein eingeben\n")
        if Erneute_frage == "ja":
            return False
        elif Erneute_frage == "nein":
            raise ValueError("Zu lange Eingabe")
            return False
        else:
            return True
            print("Bitte gibt eine neue Antowrt ein")

def auswerten(Koordinate):
    global kein_Alpha, kein_Zahl, zu_gross, zu_lang
    while prüfung:
        try:
            unbearbeitet_y = int(Koordinate[1])
            gross = Koordinate[0].upper()
            unbearbetiet_x = int(Buchstaben.index(gross))
            if len(Koordinate) > 2:
                erneute_frage()
            x_kor = unbearbetiet_x
            y_kor = unbearbeitet_y
            spielfeldliste[y_kor-1][x_kor] = 3*" "
            if y_kor > 5:
                raise ValueError("zu grosse y_kor")
            return False
        except:
            rot = farben[16]
            if not Koordinate[0].isalpha():
                kein_Alpha = 1
            if not Koordinate[1].isnumeric():
                kein_Zahl = 1
            if Koordinate[1] > "5":
                zu_gross = 1
            if len(Koordinate) > 2:
                zu_lang = 1
            print(rot +"Bitte im Format (Buchstabe bis E, Zahl bis 5)" + reset)
            return False


def input_abfragen():
    global Koordinate
    Koordinate = input("Gib die Korrdinaten ein.(Z.B: A1) \nKoordinate: ")

def play():
    global Koordinate
    spielfeldgeneration()
    spielfeld_zeichnen()
    while player_input:
        input_abfragen()
        if Exit(Koordinate):
            break
        auswerten(Koordinate)
        spielfeld_zeichnen()
        print()
        fehlermeldungen()
play()