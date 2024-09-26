def binary_func(num, tmp = ""):
    if num == 0:
        print(tmp)
    else:
        binary_func(num // 2, str(num % 2) + tmp)


binary_func(13)
binary_func(38)

def post_dw_dod(x, res=0, pos=0):
    if x>0:
        post_dw_dod( x//2, res + ((x%2) * pow(10, pos)), pos+1)
    else:
        print(res, end="")

post_dw_dod(13)
print("")
post_dw_dod(38)