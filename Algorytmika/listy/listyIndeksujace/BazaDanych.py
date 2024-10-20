from Algorytmika.listy.listyIndeksujace.Kartoteka import Kartoteka


class IndeksNazwisk:
    def __init__(self):
        self.ref = None
        self.nastepny = None

    def wypiszKolejne(self,s):
        tmp = self
        while tmp is not None:
            print("[", tmp.ref.nazwisko, " zarabia ", tmp.ref.zarobek, "]")
            tmp = tmp.nastepny
        print()

class IndeksZarobkow:
    def __init__(self):
        self.ref = None
        self.nastepny = None

    def wypiszKolejne(self,s):
        tmp = self
        while tmp is not None:
            print("[", tmp.ref.nazwisko, " zarabia ", tmp.ref.zarobek, "]")
            tmp = tmp.nastepny
        print()
class BazaDanych:
    def __init__(self):
        self.dane = Kartoteka()
        self.glowaZ = None
        self.ogonZ = None
        self.glowaN = None
        self.ogonN = None

    def wstawSort(self, nazwisko, zarobki):
        nowaref = self.dane.wstaw_na_koniec(nazwisko, zarobki)
        self.wstaw_sort_zarobki(nowaref)
        self.wstaw_sort_nazwisko(nowaref)

    def wstaw_sort_zarobki(self, nowaref):
        zar = nowaref.zarobek
        nowy = IndeksZarobkow()
        # Tworzymy nowy element na liście indeksu
        nowy.ref = nowaref

        # Poszukiwanie właściwej pozycji na wstawienie elementu:
        if self.glowaZ == None:
            # Lista pusta
            self.glowaZ = nowy
            self.ogonZ = nowy
            return

        # Pozwala na szybkie opuszczenie funkcji
        # Poszukiwanie miejsca na wstawienie:
        szukamy = True
        # Stan poszukiwania miejsca na wstawienie
        przed = None
        # 'przed' i 'po' określą miejsce wstawiania nowego elementu
        po = self.glowaZ

        while szukamy and (po is not None):
            if po.ref.zarobek >= zar:  # Kryterium sortowania (*)
                szukamy = False
                # Znaleźliśmy właściwe miejsce!
            else:
                # Szukamy dalej
                przed = po
                po = po.nastepny

        # Wstawiamy, analizując wartości zapamiętane w 'przed' i 'po'
        if przed == None:
            # Na początek listy
            self.glowaZ = nowy
            nowy.nastepny = po
        else:
            if po == None:
                # Na koniec listy
                przed.nastepny = nowy
                self.ogonZ = nowy
                # Nowy koniec listy!
            else:
                # Wstawiamy gdzieś w środku, „rozpinając” łańcuszek danych
                przed.nastepny = nowy
                nowy.nastepny = po


    def wypisz_zarobki(self):
        tmp = self.glowaZ
        while tmp is not None:
            print(tmp.ref.zarobek)
            tmp = tmp.nastepny

    def wypisz_nazwiska(self):
        tmp = self.glowaN
        while tmp is not None:
            print(tmp.ref.nazwisko)
            tmp = tmp.nastepny

    def wstaw_sort_nazwisko(self, nowaref):
        element = IndeksNazwisk()
        element.ref = nowaref

        # Na początek listy, jeśli jest pusta
        if self.glowaN is None:
            self.glowaN = element
            self.ogonN = element
            return

        # Przechodzimy przez listę, aby znaleźć odpowiednie miejsce do wstawienia
        tmp = self.glowaN
        pop = None

        while tmp is not None:
            # Wstawianie na początek, jeśli nowaref.nazwisko jest mniejsze lub równe aktualnemu
            if nowaref.nazwisko <= tmp.ref.nazwisko:
                element.nastepny = tmp
                if pop is None:
                    self.glowaN = element
                else:
                    pop.nastepny = element
                return

            # Ustawienie wskaźników na następną iterację
            pop = tmp
            tmp = tmp.nastepny

        # Wstawienie na końcu, jeśli nie znaleziono mniejszego elementu
        self.ogonN.nastepny = element
        self.ogonN = element



















