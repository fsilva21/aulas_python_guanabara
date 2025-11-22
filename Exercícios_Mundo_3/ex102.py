# Crie um programa que tenha uma função "fatorial()" que receba dois parâmetros:
# O primeiro que indique o número a calcular.
# O outro chamado "show(por padrão =false)" que é um valor booleano, indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num=1,show=False):
    """
    -> Calcula o Fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) 'True' Mostra a conta. Padrão é False.
    :return: O valor final de um número fatorado
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            if c != 1:
                print(f'{c}',end=' x ')
            else:
                print(f'{c}',end=' = ')
        f *= c
    return f

print(fatorial(7,True))
help(fatorial)