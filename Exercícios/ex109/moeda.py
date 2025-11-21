def aumentar(n,a,f=False):
    n += (n * (a / 100))
    if f:
        return moeda(n)
    else:
        return n

def diminuir(n,a,f=False):
    n -= (n*(a / 100))
    if f:
        return moeda(n)
    else:
        return n

def dobro(n,f=False):
    n *= 2
    if f:
        return moeda(n)
    else:
        return n

def metade(n,f=False):
    n /= 2
    if f:
        return moeda(n)
    else:
        return n

def moeda(n):
    return f'R${n:.2f}'.replace(".",",")