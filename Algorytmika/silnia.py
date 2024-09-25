def silnia(x):
    if(x==0):
        return 1
    else:
        return x * silnia(x-1)

print(silnia(5))