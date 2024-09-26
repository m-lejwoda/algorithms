def przeszukiwanie_binarne(tab, x, l,r):
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if x == tab[mid]:
            return x
        if x > tab[mid]:
            return przeszukiwanie_binarne(tab, x, mid + 1, r)
        else:
            return przeszukiwanie_binarne(tab, x, l, mid - 1)



tab = [1,2,6,18,20,23,29,32,34,39,40,49]
print(przeszukiwanie_binarne(tab, 6,0, len(tab)-1))
print(przeszukiwanie_binarne(tab, 7,0, len(tab)-1))