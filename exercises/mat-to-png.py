import png # Paket png importieren
faktor = int(input("Zoomfaktor?"))
smiley = [
    [000, 000, 000, 000, 000, 000],
    [000, 255, 000, 000, 255, 000],
    [000, 000, 000, 000, 000, 000],
    [000, 255, 000, 000, 255, 000],
    [000, 000, 255, 255, 000, 000],
    [000, 000, 000, 000, 000, 000]
]
smiley2 = [
    [000, 000, 000, 000, 000, 000],
    [000, 255, 000, 000, 255, 000],
    [000, 000, 000, 000, 000, 000],
    [000, 255, 000, 000, 255, 000],
    [000, 000, 255, 255, 000, 000],
    [000, 000, 000, 000, 000, 000]
]
multiplikation = 1
def verbreiterung(smiley):
    for z in range(6*multiplikation):
            k=0
            for i in range(6*multiplikation):
                smiley[z].insert(k, smiley2[z][i])
                k+=2
    return smiley, smiley2
def verdickerung(smiley):
    verbreiterung(smiley)
    k=0
    for z in range(3*multiplikation):
            smiley[k].insert(k, k)
            k+=2 
    return smiley

zoom=0
while zoom<faktor:
    verdickerung(smiley)
    multiplikation+=1
    zoom+=1

# Erzeuge ein Graustufen-Bild (0=Schwarz, 255=Weiss)    
png.from_array(smiley, 'L').save('small_smiley.png')