#184
class Element:
    def __init__(self, pDane=None, pNastepny=None):
        self.dane = pDane
        self.nastepny = pNastepny

class Lista:
    def __init__(self):
        self.glowa = None
        self.ogon = None
        self.dlugosc = 0

    def wstaw_sort(self, number: int):
        element = Element(number)
        if self.dlugosc == 0:
            self.glowa = element
            self.ogon = element
            self.dlugosc += 1
            return
        tmp = self.glowa
        pop = self.glowa
        index = 0
        while tmp is not None:
            if element.dane <= tmp.dane:
                if index == 0:
                    self.glowa = element
                    pop = element
                    pop.nastepny = tmp
                else:
                    pop.nastepny = element
                    element.nastepny = tmp

                return
            index += 1
            pop = tmp
            tmp = tmp.nastepny
        self.ogon.nastepny = element
        self.dlugosc += 1

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
    def zwroc_liste_elementow_bez_dlugosc(self):
        index = 0
        tmp = self.glowa
        if self.glowa is None:
            print(index)
            return
        while tmp is not None:
            tmp = tmp.nastepny
            index += 1
        print(index)
        return index

    def zwroc_k_ty_element(self, k):
        index = 0
        tmp = self.glowa
        if k >= self.dlugosc:
            print("Nie ma tyle elementów")
            return
        while tmp is not None:
            if index == k:
                print("na indexie {} znajduje sie liczba {}".format(k, tmp.dane))
                return tmp.dane
            tmp = tmp.nastepny
            index += 1
    def usun_k_ty_element(self, k):
        index = 0
        tmp = self.glowa
        pop = None
        if k >= self.dlugosc:
            print("Nie ma tyle elementów")
            return
        while tmp is not None:
            if index == k:
                #pierwszy element
                if self.glowa == tmp:
                    if tmp.nastepny is not None:
                        self.glowa = tmp.nastepny
                    else:
                        self.glowa = None
                    return
                #Koncowy element
                if self.ogon == tmp:
                    self.ogon = pop
                    pop.nastepny = None
                    return
                #srodkowy element
                pop.nastepny = tmp.nastepny
                return tmp.dane
            pop = tmp
            tmp = tmp.nastepny
            index += 1
    def usun_pierwszy(self):
        self.glowa = self.glowa.nastepny
        self.dlugosc -= 1
    def usun_ze_srodka(self, k):
        if k >= self.dlugosc:
            return None
        tmp = self.glowa
        pop = self.glowa
        index = 0
        while tmp is not None:
            if k == 0:
                if self.glowa is not None:
                    if self.glowa.nastepny is not None:
                        self.glowa = self.glowa.nastepny
                    else:
                        self.glowa = None
                return
            if index == k:
                if tmp.nastepny is not None:
                    pop.nastepny = tmp.nastepny
                else:
                    pop.nastepny = None
                return
            pop = tmp
            tmp = tmp.nastepny
            index += 1

l = Lista()
l.wstaw_na_koniec(5)
l.wstaw_na_koniec(6)
l.wstaw_na_koniec(7)
l.wypisz()
l.szukaj(8)
l.zwroc_liste_elementow_bez_dlugosc()
l.zwroc_k_ty_element(0)
l.usun_k_ty_element(2)
l.wypisz()
lista_sort = Lista()
lista_sort.wstaw_sort(5)
lista_sort.wstaw_sort(7)
lista_sort.wstaw_sort(4)
lista_sort.wstaw_sort(3)
lista_sort.wstaw_sort(10)
lista_sort.wstaw_sort(6)
lista_sort.wstaw_sort(18)
lista_sort.wstaw_sort(9)
lista_sort.wstaw_sort(1)
# lista_sort.usun_pierwszy()
lista_sort.usun_ze_srodka(2)
lista_sort.usun_ze_srodka(0)
lista_sort.usun_ze_srodka(3)
lista_sort.usun_ze_srodka(14)
print("wypisz")
lista_sort.wypisz()

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