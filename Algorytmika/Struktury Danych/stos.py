class StosOgraniczony:
    def __init__(self, pRozmiar):
        self._stos = list()
        self._MaxElt=pRozmiar

    def zeruj(self):
        # Zerowanie stosu
        self._stos.clear()

    def wypisz(self, s):
        print(s)
        if self._stos!=None:
            print(" Zawartość stosu: [", end=" ")
            for x in self._stos:
                # Wywołajmy iterator klasy list()
                print(x, end=" ")
                print("]")

    def push(self, obj):
        print("Odkładam: ", str(obj))
        # Konwersja na postać tekstową
        if len(self._stos) < self._MaxElt:
            self._stos.append(obj)
            # Dokładamy kolejny element na koniec
        else:
            print("* POJEMNOŚĆ PRZEKROCZONA *")
    def pop(self):
        if len(self._stos_)>0:
            tmp=self._stos.pop()
            # Pobiera ostatni element
            return tmp


x=StosOgraniczony(2)
x.wypisz("Zawartość stosu")
x.push(2)
x.push('A')
x.push("małe co nieco")
x.wypisz("Zawartość stosu")