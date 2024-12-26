class Wezel:
    def __init__(self, pKlucz=None):
        self.klucz = pKlucz
        self.lewy = None
        self.prawy = None

def MinWezel(start):
    tmp = start
    while (tmp.lewy != None): # Idziemy skrajnie na lewo!
        tmp = tmp.lewy
    return tmp

def usunWezel(wierzcholek, klucz):
    # Startujemy od węzła „wierzcholek”
    if wierzcholek == None:
        return wierzcholek
    if klucz < wierzcholek.klucz:
        # Idziemy na lewo
        wierzcholek.lewy = usunWezel(wierzcholek.lewy, klucz)
    elif (klucz > wierzcholek.klucz):
        # Idziemy na prawo
        wierzcholek.prawy = usunWezel(wierzcholek.prawy, klucz)
    else: # Usuwamy znaleziony wierzchołek
        if wierzcholek.lewy==None:
            # Wierzchołek z tylko jednym potomkiem
            temp = wierzcholek.prawy
            return temp
        elif wierzcholek.prawy==None:
            temp = wierzcholek.lewy
            return temp
        # Wierzchołek z dwoma potomkami => szukamy następcy kasowanego węzła,
        # który znajduje się w prawej gałęzi:
        temp = MinWezel(wierzcholek.prawy)
        # Kopiujemy zawartość następnika w miejsce usuwanego węzła (klucz i ew. inne atrybuty):
        wierzcholek.klucz = temp.klucz
        wierzcholek.prawy=usunWezel(wierzcholek.prawy,temp.klucz)# Usuwamy następnik
        # z podgałęzi
    return wierzcholek

class BST:
    def __init__(self):
        self.korzen = None

    def szukaj(self, x):
        # Zwraca węzeł o kluczu 'x' lub None
        if self.korzen == None:
            return None
        tmp = self.korzen
        while tmp.klucz != x:
            if x < tmp.klucz: # Kieruj się na lewo
                tmp = tmp.lewy
            else:
                tmp = tmp.prawy
            if tmp == None: # Brak potomka
                return None
        return tmp

    def wstaw(self, k):
        w = Wezel(k)
        if self.korzen == None:
            self.korzen = w
        else:
            tmp = self.korzen
            while True:
                rodzic = tmp
                if k < tmp.klucz:
                    tmp = tmp.lewy
                    if tmp == None:
                        rodzic.lewy = w
                        break
                else:
                    tmp = tmp.prawy
                    if tmp == None:
                        rodzic.prawy = w
                        break

    def Min(self):
        tmp = self.korzen
        while tmp.lewy != None:
            tmp = tmp.lewy
        return tmp

    def Max(self):
        tmp = self.korzen
        while tmp.prawy != None:
            tmp = tmp.prawy
        return tmp

    def preOrder(self, w):
        # Przejście „wzdłużne”
        if w != None:
            print("[", w.klucz, "]", end=" ")
            self.preOrder(w.lewy)
            self.preOrder(w.prawy)

    def inOrder(self, w):

        # Przejście „poprzeczne”
        if w != None:
            self.inOrder(w.lewy)
            print("[", w.klucz, "]", end=" ")
            self.inOrder(w.prawy)

    def postOrder(self, w):
        # Przejście „wsteczne”
        if w != None:
            self.postOrder(w.lewy)
            self.postOrder(w.prawy)
            print("[", w.klucz, "]", end=" ")

drzewo = BST()
for x in [19, 4, 25, 3, 12, 14, 8, 27, 26, 31]:
    drzewo.wstaw(x)
print(" Pre-order")
drzewo.preOrder(drzewo.korzen)
print("\n In-order")
drzewo.inOrder(drzewo.korzen)
print("\n Post-order")
drzewo.postOrder(drzewo.korzen)
# print("\nMin=", drzewo.Min(drzewo.korzen).klucz)
# print("Max=", drzewo.Max(drzewo.korzen).klucz)
print("\nUsuwam 12:")
print(drzewo.korzen.klucz)
drzewo.korzen = usunWezel(drzewo.korzen, 12)
print(drzewo.korzen.klucz)
print("Nowy In-order:")
drzewo.inOrder(drzewo.korzen)
for x in [3, 6, 25, 27]:
    res=drzewo.szukaj(x)
    if res!=None:
        print("Znalazłem ", res.klucz)
    else:
        print("Nie znaleziono ", x)