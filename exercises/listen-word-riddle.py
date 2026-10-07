message=[12, 9, 19, 20, 0, 18, 9, 4, 4, 12, 5]
ALPHABET = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ausgabe=[]
for i in range(len(message)):
    ausgabe.append(ALPHABET[message[i]])
print(ausgabe)
