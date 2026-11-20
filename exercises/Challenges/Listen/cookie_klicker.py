text = '''\
*-----
-*----
--*---
---*--
----*-
-----*\
'''
neu_text=""
ganze_linie = 0
for j in range(1, 7):
    for k in range(6):
        alt_text=text[ganze_linie+k]
        print(alt_text ,end="")
    for i in range(1, 7):
        neu_text=text[(j*6)-i]
        print(neu_text, end="")
    print()
    ganze_linie += 6