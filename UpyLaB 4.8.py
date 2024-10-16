from math import factorial as fac

def catalan(n):
    catalan_number = fac(2*n)//(fac((n+1))*fac(n))

    return int(catalan_number)

print(catalan(4))