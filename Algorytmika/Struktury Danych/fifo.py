class FIFO:
    def __init__(self, pRozmiar):
        self._kolejka = list()
        # Właściwa kolekcja danych
        self._MaxElt = pRozmiar
        # Maksymalny rozmiar kolejki
        self._licznik=0
        # Bieżąca liczba elementów
        print("Tworzę kolejkę o pojemności " + str(self._MaxElt) )

    def wypisz(self, s):
        print(s)
        if self._licznik != 0:
            print(" Zawartość kolejki:[", end=" ")
        for x in self._kolejka:  # Wywołajmy iterator klasy 'list'
            print(x, end=" ")
        print("]")

    def wstaw(self, obj):# Dołóż tu ew. kontrolę poprawności operacji, kontrolę typu itp.
        if self._licznik < self._MaxElt: # Jest miejsce
            self._kolejka.append(obj)
            # Dołóż element NA KONIEC
            self._licznik=self._licznik+1
        else:
            print(f"* Gdzie się Pan {obj} wpycha? Tu obowiązuje lista kolejkowa! *")
    def obsluz(self):
        if self._licznik != 0:
            temp = self._kolejka.pop(0)

            # Ktoś stoi w kolejce...
            # Pobierz wartość Z PRZODU
            self._licznik = self._licznik - 1
            return temp
        else:
            print("** Kolejka pusta **")
    def pusta(self):
        # Czy kolejka jest pusta?
        return self._licznik==0

kolejka = FIFO(4)
kolejka.wstaw("Kowalska"), kolejka.wstaw("Fronczak"), kolejka.wstaw("Becki"),
kolejka.wstaw("Pigwa")
kolejka.wstaw("Cwaniak"), kolejka.wstaw("Spóźnialski") # Te dwie operacje już się nie
# powiodą!
kolejka.wypisz("1-Stan kolejki")
szczesliwiec=kolejka.obsluz()
print("Obsłużony został klient: " + str(szczesliwiec))
kolejka.wypisz("2-Stan kolejki")
print("Przyszedł Pan 'Spóźnialski'")
kolejka.wstaw("Spóźnialski")
kolejka.wypisz("3-Stan kolejki")
print("Ekspresowa obsługa całej kolejki przed zamknięciem sklepu!")
while not kolejka.pusta():
    k=kolejka.obsluz()
    print("Obsłużony został klient: " + str(k))
    print("Kolejka pusta, zamykamy sklep!")