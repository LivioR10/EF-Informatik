def durchgehend(breite):
    for i in range(breite):
        print("*", end="")
    print()

def lücke(breite):
    print("*", end="")
    for i in range(breite-2):
        print(" ", end="")
    print("*")

def höhe(breite, anzahl):
    durchgehend(breite)
    for i in range(anzahl-2):
        lücke(breite)
    durchgehend(breite)
höhe(20, 6)

