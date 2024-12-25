from sterta import Sterta
tab=[40, 2, 1, 6, 18, 29, 29, 32, 23, 34, 91, 45, 6]
print(tab)
sterta=Sterta( len(tab))
for element in tab:
    sterta.wstaw(element)
for i in range(len(tab)-1, -1, -1):
    tab[i]= sterta.obsluz()
print(tab)