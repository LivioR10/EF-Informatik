gesucht = 'test'

def reset():
    global gefunden, falsch_geraten, k, count, doppelcheck
    gefunden = []
    falsch_geraten = []
    k=1
    count = 0
    doppelcheck = []
def show():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')
    # Zählt wie viele male man schon geraten hat. Und welche buchstaben man schon erraten hat. 
def is_valid(inp):
    if inp.isalpha and len(inp) == 1 and inp not in doppelcheck:
        return True
    return False
    # Ob der input valid ist.

def eingabe():
    global valid_inp
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        print("Sorry nimm bitte etwas anderes!")
        buchstabe = input('Neuer Buchstabe?')
    valid_inp = buchstabe.lower()
    doppelcheck.append(valid_inp)
    # Welcher Buchstabe und dann, wenn er valid ist gibt es den Buchstaben zurück in kleinformat.

def auswerten(valid_inp):
    global k
    k+=1
    if valid_inp in gesucht:
        gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)

    # Wenn der Buchstabe drinnen ist wird in der Liste gefunden der Buchstabe angehängt. Sonst wird er in der Liste falsch_geraten angehängt.
def game_over():
    return gewonnen()

def gewonnen():
    global valid_inp, count
    if k > 10:
        print("Sorry deine 10 Versuche sind um")
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
def play():
    reset()
    eingabe()
    auswerten(valid_inp)
    show()
    while not game_over():
        eingabe()
        auswerten(valid_inp)
        show()
play()
