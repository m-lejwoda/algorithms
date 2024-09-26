def algorytm_euklidesa(x,y):
    if x == y:
        return x
    if x > y:
        tmp = x - y
        return algorytm_euklidesa(tmp, y)
    else:
        tmp = y - x
        return algorytm_euklidesa(tmp, x)


print(algorytm_euklidesa(6,8))
print(algorytm_euklidesa(15,5))
print(algorytm_euklidesa(24,18))