cpt = 0
def McCarthy(x):
    global cpt
    cpt = cpt + 1
    print("x", x)
    if x > 100:
        return x-10
    else:
        return McCarthy(McCarthy(x+11))

x = int(input("Enter a number: "))
print(f"McCarthy({x}) = {McCarthy(x)}")
if cpt ==1:
    print("Funkcja została wywołana raz")
else:
    print(f"Funkcja została wywołana {cpt} razy")
print("Do widzenia")
