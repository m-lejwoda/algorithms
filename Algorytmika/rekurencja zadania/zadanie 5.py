def silnia_bez_rekurencji(x):
    if x == 0:
        return 1
    tmp = 1
    for i in range(1,x+1):
        tmp *= i
    return tmp
print(silnia_bez_rekurencji(5))
print(silnia_bez_rekurencji(1))
print(silnia_bez_rekurencji(0))
