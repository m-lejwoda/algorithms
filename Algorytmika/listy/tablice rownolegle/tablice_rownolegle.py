class RekordDanych:
    def __init__(self, pWiek, pZarobki):
        self.wiek = pWiek
        self.zarobki = pZarobki
...
class BazaTablicowa:
    def __init__(self, MaxTab):
        self.Licznik = 0
        self.Rozmiar = MaxTab
        self.tab = [RekordDanych() for x in range(MaxTab)]
        self.index_Nazwiska = [-1 for x in range(MaxTab+2)] # Lista indeksowa 1.
        self.index_Wiek= [-1 for x in range(MaxTab+2)] # Lista indeksowa 2.
        self.index_Zarobki = [-1 for x in range(MaxTab+2)] # Lista indeksowa 3.