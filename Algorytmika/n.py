def N(n,p):
    if n==0:
        return 1
    else:
        return N(n-1,N(n-p,p))

print( "N(1,0)=", N(1,0))