def silnia2(x, tmp=1):

    if x == 0:
        return tmp
    else:
        return silnia2(x-1, x*tmp)

print(silnia2(3))
print(silnia2(4))