class Sterta:
    def __init__(self, nMax):
        self._Licznik = 0
        self._sterta = [0 for x in range(nMax + 1)]

    def wstaw(self, x):
        self._Licznik = self._Licznik + 1
        self._sterta[self._Licznik] = x
        self.DoGory()

    def obsluz(self):
        x = self._sterta[1]
        self._sterta[1] = self._sterta[self._Licznik]
        self._Licznik = self._Licznik - 1
        self.NaDol()
        return x

    def DoGory(self):
        tmp = self._sterta[self._Licznik]
        n = self._Licznik
        while ((n != 1) and (self._sterta[n // 2] <= tmp)):
            self._sterta[n] = self._sterta[n // 2]
            n = n // 2
            self._sterta[n] = tmp

    def NaDol(self):
        i = 1
        while (True):
            p = 2 * i
            # Lewy potomek węzła 'i' to (p), prawy to (p+1)
            if p > self._Licznik:
                break
            if p + 1 <= self._Licznik:
                # Prawy potomek niekoniecznie musi istnieć!
                if self._sterta[p] < self._sterta[p + 1]:
                    p = p + 1
            # Przesuwamy się do następnego
            if (self._sterta[i] >= self._sterta[p]):
                break
            tmp = self._sterta[p]
            # Zamiana
            self._sterta[p] = self._sterta[i]
            self._sterta[i] = tmp
            i = p

    def wypisz(self, s):
        print(s)

        for i in range(1, (self._Licznik // 2) + 1):
            print(" Wierzchołek: " + str(self._sterta[i]), end=" ")
            print(" lewy potomek: " + str(self._sterta[2 * i]), end=" ")
            # Prawy potomek niekoniecznie musi istnieć!
            if 2 * i + 1 <= self._Licznik:
                print(" prawy potomek: " + str(self._sterta[2 * i + 1]), end=" ")
            print()  # Przejście do nowej linii po serii instrukcji print() zawierających end=" "

doctorsWho = {
    37:
        "William Hartnell", 41:
        "Patrick Troughton",
    26:
        "Jon Pertwee", 14:
        "Tom Baker", 19:
        "Peter Davison",
    99:
        "Colin Baker", 23:
        "Sylvester McCoy", 17:
        "Paul McGann",
    12:
        "Christopher Eccleston", 20:
        "David Tennant", 25:
        "Matt Smith",
    42:
        "Peter Capaldi", 13:
        "Jodie Whittaker"}
n = len(doctorsWho)
s1 = Sterta(n)
for key in doctorsWho:
    s1.wstaw(key)
s1.wypisz("Zawartość sterty (priorytety rankingu preferencji):")
print("Rozdanie nagród publiczności na podstawie preferencji:")
for i in range(1, n+1):
    x=s1.obsluz()
    print(f" Nagroda {i:9}, aktor: {doctorsWho[x]:20} (ranking preferencji {x})")
s1.wypisz("Sterta po obsłudze:")
