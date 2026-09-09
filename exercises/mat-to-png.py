import png # Paket png importieren
faktor = int(input("Zoomfaktor?"))
smiley = [
    [000, 000, 000, 000, 000, 000],
    [000, 255, 000, 000, 255, 000], # [000, 000, 255, 255] [000, 000, 000, 000, 255, 255, 255, 255]
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
def verbreiterung(smiley, smiley2):
    for z in range((len(smiley2[0])-1)*multiplikation):
            k=0
            for i in range((len(smiley2[0])-1)*multiplikation):
                smiley[z].insert(k, smiley2[z][i])
                k+=2
    smiley = smiley2
    return smiley, smiley2
def verdickerung(smiley, smiley2):
    verbreiterung(smiley, smiley2)
    k=0
    for z in range(len(smiley)*multiplikation):
            smiley[z].insert(k, smiley2[z])
            k+=2 
    return smiley, smiley2

zoom=0
while zoom<faktor:
    verdickerung(smiley, smiley2)
    multiplikation+=1
    zoom+=1

# Erzeuge ein Graustufen-Bild (0=Schwarz, 255=Weiss)    
png.from_array(smiley, 'L').save('small_smiley.png')