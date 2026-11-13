def runden(wert):
    gerundet = round(wert * 2) / 2
    return gerundet


def schnitt(liste):
    summe = 0
    for note in liste:
        summe = summe + note
    return runden(summe / len(liste))


def auswerten(liste):
    liste.append(6)
    resultat = schnitt(liste)
    return resultat


noten = [4.5, 5, 3.5, 5.5]
resultat = 0
summe = 100
ergebnis = auswerten(noten)
print(noten)
print(resultat, summe, ergebnis)