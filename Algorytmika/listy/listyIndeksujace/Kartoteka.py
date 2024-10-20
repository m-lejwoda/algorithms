class Osoba:
    def __init__(self, pNazwisko, pZarobek, pNastepny = None):
        self.nazwisko = pNazwisko
        self.zarobek = pZarobek
        self.nastepny = pNastepny
class Kartoteka:
    def __init__(self):
        self.glowa = None
        self.ogon = None
        self.dlugosc = 0

    def wstaw_na_koniec(self, pNazwisko, pZarobek):
        osoba = Osoba(pNazwisko, pZarobek)
        if self.glowa == None:
            self.glowa = osoba
            self.ogon = osoba
        else:
            self.ogon.nastepny = osoba
            self.ogon = osoba
        self.dlugosc = self.dlugosc + 1
        return osoba