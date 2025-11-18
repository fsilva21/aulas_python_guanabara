# Faça um programa que tenha uma função chamada "contador()", que receba três parâmetros: ínicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# - De 1 até 10, de 1 em 1
# - De 10 até 0, de 2 em 2
# - Uma contagem personalizada

from time import sleep

def contador(inicio,fim,passo):
    print('*-'*15)
    print(f'Contagem de {inicio} até {fim} de {passo * -1 if passo < 0 else passo} em {passo * -1 if passo < 0 else passo}')
    if passo == 0:
        passo += 1
    if inicio > fim and passo > 0:
        passo *= -1
    for valor in range(inicio,fim,passo):
        print(valor,end=' ')
        sleep(0.5)
        if valor + passo == fim:
            print(fim,end=' ')
            sleep(0.5)
    print('FIM!',end='')
    sleep(1)


# Programa Principal
print(flush=contador(1,10,1))
print(flush=contador(10,0,-2))
print('*-'*15)
print('Personalize a contagem!')
print()
print(flush=contador(inicio = int(input('Início: ')),fim = int(input('Fim: ')),passo = int(input('Passo: '))))
