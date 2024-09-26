def suma_liczb(liczba,tmp = 0):
    if liczba > 0:
        return suma_liczb(liczba//10, tmp + liczba%10)
    else:
        return tmp
print(suma_liczb(478))
print(suma_liczb(24681))