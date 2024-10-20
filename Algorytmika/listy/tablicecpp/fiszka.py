#203
class Fiszka:

    def __init__(self, pNazwisko="", pWiek=0):
        self.nazwisko = pNazwisko
        self.wiek = pWiek

class ListaTab:
    def __init__(self, MaxTab):
        self.tab= [ Fiszka() for x in range(MaxTab)]
        self.Licznik = 0
        self.Rozmiar=MaxTab

    def wypisz(self):

        for i in range(0, self.Licznik):
            print(f"[{self.tab[i].nazwisko}, {self.tab[i].wiek}]", end=" ")
            print()

    def szukaj(self, pNazwisko):
        for i in range(0, self.Licznik):
            if (self.tab[i].nazwisko == pNazwisko):
                return i
        return -1

    def usunOsobe(self, pNazwisko):
        k = self.szukaj(pNazwisko)

        if k >= 0:
            for i in range(k, self.Licznik):
                self.tab[i] = self.tab[i + 1]
        self.Licznik = self.Licznik - 1

    def wstawNaKoniec(self, pNazwisko, pWiek):
        if self.Rozmiar > self.Licznik + 1:
            self.tab[self.Licznik].wiek = pWiek
            self.tab[self.Licznik].nazwisko = pNazwisko
            self.Licznik += 1
        return -1

    def wstawNaPozycje(self, pNazwisko, pWiek, k):
        if k >= self.Rozmiar or self.Licznik >= self.Rozmiar:
            return -1

        nowa_osoba = Fiszka(pNazwisko, pWiek)

        for i in range(self.Licznik, k, -1):
            self.tab[i] = self.tab[i - 1]

        self.tab[k] = nowa_osoba

        self.Licznik += 1
        return 0

tab = ListaTab(10)

tab.wstawNaKoniec("sad",12)
tab.wstawNaKoniec("sad1",11)
tab.wstawNaKoniec("sad2",13)
tab.wstawNaKoniec("sad3",14)
tab.wstawNaKoniec("sad4",15)
tab.wstawNaKoniec("sad5",16)
tab.wypisz()
tab.wstawNaPozycje("sas",2814,2)
print("----------------------------------")
tab.wypisz()
