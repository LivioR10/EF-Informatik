import sys
import zufallsworte as zufall

HANGMANS_RAW = r''' 18 Zeichen ergeben ein Bild...
                                         __________        __________        __________        __________        __________        __________        __________        __________        __________     
                       |                 |                 |/                |/        |       |/        |       |/        |       |/        |       |/        |       |/        |       |/        |    
                       |                 |                 |                 |                 |         O       |         O       |         O       |         O       |         O       |         O    
                       |                 |                 |                 |                 |                 |         |       |        -|       |        -|       |        -|-      |        -|-   
                       |                 |                 |                 |                 |                 |                 |                 |          \      |          \      |        / \   
                       |                 |                 |                 |                 |                 |                 |                 |                 |                 |  GAME OVER   
    _________         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______     
___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ 
'''.split('\n')[1:-1] # ohne erste und letzte Zeile

# enthält 11 ASCII-Bilder, für jeden Spiel-Zustand einen
HANGMANS = ['\n'.join([line[i : i + 18] for line in HANGMANS_RAW]) for i in range(0, 11 * 18, 18)]

def zufallswort_gen():
    global gesucht
    gesucht = zufall.zufallswoerter(1)[0]  
    return(gesucht)



def get_hangman(nr):
    return HANGMANS[nr]

def reset():
    global gefunden, falsch_geraten, k, count, doppelcheck
    gefunden = []
    falsch_geraten = []
    k=0
    count = 0
    doppelcheck = []

def show():
    print('Falsche Buchstaben:', falsch_geraten)
    print(10-k, "versuche überig")
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')
    # Zählt wie viele male man schon geraten hat. Und welche buchstaben man schon erraten hat. 

def is_valid(inp):
    if inp == "Exit":
        stopp()
    if inp.isalpha and len(inp) == 1 and inp not in doppelcheck:
        return True
    return False
    # Ob der input valid ist.

def stopp():
    sys.exit()

def eingabe():
    global valid_inp
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        print("Sorry nimm bitte etwas anderes!")
        buchstabe = input('Neuer Buchstabe? ')
    valid_inp = buchstabe.lower()
    doppelcheck.append(valid_inp)
    # Welcher Buchstabe und dann, wenn er valid ist gibt es den Buchstaben zurück in kleinformat.

def auswerten(valid_inp):
    global k
    if valid_inp in gesucht:
        gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)
        k+=1

    # Wenn der Buchstabe drinnen ist wird in der Liste gefunden der Buchstabe angehängt. Sonst wird er in der Liste falsch_geraten angehängt.
def game_over():
    return gewonnen()

def gewonnen():
    global valid_inp, count
    if k == 10:
        print("Sorry deine 10 Versuche sind um")
        print(gesucht, "war gesucht")
        return True
    else:
        neuer_string = "".join(gesucht)
        for inp in gesucht:
            suchen = valid_inp.find(inp)
            if suchen >= 0:
                count += 1
            elif count == len(gesucht):
                return True
            else:
                None

def play_again():
    abbruch = input("Möchtest du es noch einmal versuchen? (y für ja und n für nein)\n")
    if abbruch == "y":
        play()
    else:
        None

def play():
    reset()
    zufallswort_gen()
    eingabe()
    auswerten(valid_inp)
    show()
    print(get_hangman(k))
    while not game_over():
        eingabe()
        auswerten(valid_inp)
        show()
        print(get_hangman(k))
    play_again()
play()
