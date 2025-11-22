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
    print('-'*30)
    print("RESUMO DO VALOR".center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metade do preço: \t{metade(n)}')
    print(f'{aum}% de aumento: \t{aumentar(n,aum)}')
    print(f'{red}% de redução: \t{diminuir(n,red)}')
    return '-'*30