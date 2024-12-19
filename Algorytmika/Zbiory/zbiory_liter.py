class ZbiorLitery:
    def __init__(self):
        self.zbior = [False for x in range(26)]


    def dodaj(self, c):
        i = do_indeksu(c)
        if i in range(26):
            self.zbior[i] = True
        else:
            print("[Błąd] Znak spoza dozwolonego alfabetu:", c, i)

    def __add__(self, x2):
        suma = ZbiorLitery()
        for i in range(26):
            suma.zbior[i] = self.zbior[i] or x2.zbior[i]
        return suma

    def usun(self, c):
        i = do_indeksu(c)
        print("Usuwam", c.upper())
        if i != -1 and self.zbior[i] == True:
            self.zbior[i] = False
        else:
            print(f"\n[Błąd] Znak nie należy do zbioru:", c)

    def wypisz(self, s):
        print(s, "= {", end=" ")
        for i in range(26):
            if self.zbior[i] == True:
                print(chr(i+65) + " ", end="")
        print("}\n")


def do_indeksu(c):
    if ((c >= 'A') and (c <= 'Z') or (c >= 'a') and (c <= 'z')):
        return ord(c.upper())-ord('A')
    else:
        return -1


z1=ZbiorLitery()
z2=ZbiorLitery()
z1.dodaj('A')
z1.dodaj('K')
z1.dodaj('K')
z1.dodaj('M')
z2.dodaj('B')
z2.dodaj('K')
z2.dodaj('R')
z1.wypisz("z1")
z2.wypisz("z2")
z1.usun('a')
z1.usun('X')
z1.wypisz("z1")
(z1+z2).wypisz("z1+z2")