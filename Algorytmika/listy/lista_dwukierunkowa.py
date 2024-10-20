class Element:
    def __init__(self, pNazwisko, pWiek):
        self.nazwisko = pNazwisko
        self.wiek = pWiek
        self.nastepny=None
        self.poprzedni=None

class ListaDwukierunkowa:
    def __init__(self):
        self.glowa = None
        self.ogon = None

    def wstawElement(self, pNazwisko, pWiek):
        element = Element(pNazwisko, pWiek)
        if self.glowa is None:
            self.glowa = element
            self.ogon = element
            return
        else:
            tmp = self.ogon
            self.ogon.nastepny = element
            self.ogon = element
            element.poprzedni = tmp
            return
    def wypisz(self):
        tmp = self.glowa
        while tmp is not None:
            print(tmp.nazwisko)
            tmp = tmp.nastepny
    def sprawdz_przedostatni(self):
        print(self.ogon.poprzedni.nazwisko)
        tmp = self.ogon.poprzedni
        print(tmp.poprzedni.nazwisko)

    def usun_po_nazwisku(self, nazwisko):
        tmp = self.glowa
        while tmp is not None:
            if tmp.nazwisko == nazwisko:
                if tmp.poprzedni is None:
                    self.glowa = tmp.nastepny
                    break
                if tmp.nastepny is None:
                    self.ogon = tmp.poprzedni
                    self.ogon.nastepny = None
                    break
                # normalne usuniecie
                pop = tmp.poprzedni
                nas = tmp.nastepny
                tmp.poprzedni.nastepny= nas
                tmp.nastepny.poprzedni = pop
                break
            tmp = tmp.nastepny

    def usun_po_indexie(self, index):
        tmp = self.glowa
        ind = 0
        while tmp is not None:
            if index == ind:
                if tmp.poprzedni is None:
                    self.glowa = tmp.nastepny
                    break
                if tmp.nastepny is None:
                    self.ogon = tmp.poprzedni
                    self.ogon.nastepny = None
                    break
                # normalne usuniecie
                pop = tmp.poprzedni
                nas = tmp.nastepny
                tmp.poprzedni.nastepny = nas
                tmp.nastepny.poprzedni = pop
                break
            ind += 1
            tmp = tmp.nastepny
lista = ListaDwukierunkowa()
lista.wstawElement("kowalski", 12)
lista.wstawElement("Nowak", 34)
lista.wstawElement("Wisniewski", 14)
lista.wypisz()
# lista.usun_po_nazwisku("Wisniewski")
lista.usun_po_indexie(0)
print("---------------------")
lista.wypisz()
# lista.sprawdz_przedostatni()