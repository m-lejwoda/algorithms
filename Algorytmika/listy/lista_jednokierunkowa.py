#184

def sortuj(a, b):
    if a == None:
        return b
    if b == None:
        return a
    if a.dane <= b.dane:
        a.nastepny = sortuj(a.nastepny, b)
        return a
    else:
        b.nastepny = sortuj(b.nastepny, a)
        return b

class Element:
    def __init__(self, pDane=None, pNastepny=None):
        self.dane = pDane
        self.nastepny = pNastepny

class Lista:
    def __init__(self):
        self.glowa = None
        self.ogon = None
        self.dlugosc = 0

    def __add__(self, other):
        tmp_self = self.glowa
        tmp_other = other.glowa
        # pop = self.glowa
        while tmp_self is not None and tmp_other is not None:
            if tmp_other.dane <= tmp_self.dane:
                pop = tmp_other
                tmp_other = tmp_other.nastepny
                pop.nastepny = tmp_self

            else:
                tmp_self = tmp_self.nastepny
                # pop = tmp_self


    # def __add__(self, x2):
    #
    #     suma = Lista()
    #     q1 = self.glowa
    #     q2 = x2.glowa
    #     while q1 != None:
    #         suma.wstaw_sort(q1.dane)
    #         q1 = q1.nastepny
    #     while q2 != None:
    #         suma.wstaw_sort(q2.dane)
    #         q2 = q2.nastepny
    #     return suma

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
lista_sort2 = Lista()

# lista_sort.usun_pierwszy()
# lista_sort.usun_ze_srodka(2)
# lista_sort.usun_ze_srodka(0)
# lista_sort.usun_ze_srodka(3)
# lista_sort.usun_ze_srodka(14)
print("wypisz")

lista_sort.wypisz()
lista_sort2.wstaw_sort(5)
lista_sort2.wstaw_sort(6)
lista_sort2.wstaw_sort(1)
lista_sort2.wstaw_sort(2)
print("lista_sort")
lista_sort.wypisz()
print("lista_sort2")
lista_sort2.wypisz()
suma = Lista()
suma = lista_sort + lista_sort2
suma.wypisz()