def przeszukiwanie_binarne(tab, x, l,r):
    pass
    if x == tab[r//2]:
        print(r//2)
        return x
    if x > tab[r//2]:
        return przeszukiwanie_binarne(tab, x, r//2, r)
    if x < tab[r//2]:
        return przeszukiwanie_binarne(tab, x, l, r//2)



tab = [1,2,6,18,20,23,29,32,34,39,40,49]
przeszukiwanie_binarne(tab, 6,0, len(tab)-1)