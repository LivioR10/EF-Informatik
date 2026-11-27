def uhrzeit_umwandeln(text):
    try:
        text_l = text.split(":")
        if int(text[0:2]) == 24 and int(text[3:5]) == 00:
            return text_l
        if not text[0:2].isnumeric() or not text[3:5].isnumeric():
            raise ValueError("Feherhafte eingabe")
        if int(text_l[0]) > 23 or int(text_l[1]) > 59 or len(text_l) > 2:
            raise ValueError("Fehlerhafte eingabe")
        else:
            return text_l
    except:
        return ("Ist keine oder nicht im Richtigen Format eingegebne Zeit")
        
tests = ['07:45', '23:59', '00:00', '24:00', '12:60', 'zwölf', '12-30', '', '12:3a', '7:45', '12:30:00', ' 7:45']
for t in tests:
    print(f"'{t}' ->", uhrzeit_umwandeln(t))