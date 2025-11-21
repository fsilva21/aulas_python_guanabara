def aumentar(n,a,f=True):
    n += (n * (a / 100))
    if f:
        return moeda(n)
    else:
        return n

def diminuir(n,d,f=True):
    n -= (n*(d / 100))
    if f:
        return moeda(n)
    else:
        return n

def dobro(n,f=True):
    n *= 2
    if f:
        return moeda(n)
    else:
        return n

def metade(n,f=True):
    n /= 2
    if f:
        return moeda(n)
    else:
        return n

def moeda(n):
    return f'R${n:.2f}'.replace(".",",")

def resumo(n,aum=0,red=0):
    res = str(f'{' '*7}{"RESUMO DO VALOR"}{' '*7}')
    print('-'*len(res))
    print(res)
    print('-'*len(res))
    print(f'{"Preço analisado:":<20}{moeda(n)}')
    print(f'{"Dobro do preço:":<20}{dobro(n)}')
    print(f'{"Metade do preço:":<20}{metade(n)}')
    print(f'{aum}{"% de aumento:":<18}{aumentar(n,aum)}')
    print(f'{red}{"% de redução:":<18}{diminuir(n,red)}')
    return '-'*len(res)