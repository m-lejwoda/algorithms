class Element:
    def __init__(self, pNazwisko):
        self.poprzedni = None
        self.nastepny = None
        self.nazwisko = pNazwisko

class ListaCykliczna:
    def __init__(self):
        self.poczatek = None
        self.ogon = None

    def dodaj_element(self,pNazwisko):
        element = Element(pNazwisko)
        if self.poczatek is None:
            self.poczatek = element
            self.ogon = element
            return
        self.ogon.nastepny = element
        self.ogon = element
        element.nastepny = self.poczatek


    def wypisz(self):
        tmp = self.poczatek
        index = 0
        while tmp is not None:
            print(tmp.nazwisko)
            tmp = tmp.nastepny
            index += 1
            if index == 15:
                break

lista_cyk = ListaCykliczna()
lista_cyk.dodaj_element("Nazwisko")
lista_cyk.dodaj_element("Nazwisko2")
lista_cyk.dodaj_element("Nazwisko3")
lista_cyk.dodaj_element("Nazwisko4")
lista_cyk.wypisz()
