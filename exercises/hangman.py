gesucht = 'test'
abfrage_Buchstaben = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "ü"]
def reset():
    global gefunden, falsch_geraten, k
    gefunden = []
    falsch_geraten = []
    k=1
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
    for i in range(29):
        if inp == abfrage_Buchstaben[i]:
            return True
        return False
    # Ob der input valid ist.
def eingabe():
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        buchstabe = input('Buchstabe? ')
    return buchstabe.lower()
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
def play():
    reset()
    while not game_over():
        valid_input = eingabe()
        auswerten(valid_input)
        show()
def gewonnen():
    if k > 10:
        print("Sorry deine 10 Versuche sind um")
        return True
    else:
        for buchstabe in gesucht:
            if buchstabe not in gefunden:
                return False
        return True
    
    # Wird geprüft, ob die Buchstaben stimmen.
play()
