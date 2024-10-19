class Element:
    def __init__(self, pDane=None, pNastepny=None):
        self.dane = pDane
        self.nastepny = pNastepny

class Lista:
    def __init__(self):
        self.glowa = None
        self.ogon = None
        self.dlugosc = 0
    def wstaw_na_koniec(self, number: int):
        e = Element(number)
        if self.glowa is None:
            self.glowa = e
        if self.ogon is not None:
            self.ogon.nastepny = e
        self.dlugosc += 1
        self.ogon = e

    def wypisz(self):
        tmp = self.glowa
        if tmp is None:
            print("Lista jest pusta")
            return
        while tmp is not None:
            print(tmp.dane, end=" ")
            tmp = tmp.nastepny
        print("\n")

    def szukaj(self, number):
        tmp = self.glowa
        index = 0
        while tmp is not None:
            if tmp.dane == number:
                print("Znaleziono {} na indexie {}".format(number, index))
                return
            tmp = tmp.nastepny
            index += 1
        print("W liscie nie ma takiego elementu")

l = Lista()
l.wstaw_na_koniec(5)
l.wstaw_na_koniec(6)
l.wstaw_na_koniec(7)
l.wypisz()
l.szukaj(8)
# l = Lista()
# q = Element(3)
# l.glowa = q
# l.ogon = q
# r = Element(5)
# q.nastepny = r
# l.ogon = r
# x=5
# adres_tmp=l.glowa
# while adres_tmp!= None:
#     if adres_tmp.dane==x:
#         print("Znalazłem poszukiwany element")
#         break
#     adres_tmp=adres_tmp.nastepny
#     if adres_tmp == None:
#         print("Nie znaleziono poszukiwanego elementu")