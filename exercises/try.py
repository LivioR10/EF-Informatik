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
def smiley123(smiley, smiley2):
    for z in range((len(smiley2[0]))*multiplikation):
            k=0
            for i in range((len(smiley2[0]))*multiplikation):
                smiley[z].insert(k, smiley2[z][i])
                k+=2


    smiley2 = [
            [smiley[kir][zir] for zir in range(len(smiley[0]))] for kir in range(len(smiley))
            ]
    print(smiley2)
