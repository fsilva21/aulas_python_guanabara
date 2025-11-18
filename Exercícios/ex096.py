# Faça um programa que tenha uma função chamada "área()", que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área.

def área():
    largura = float(input('LARGURA (m): '))
    comprimento = float(input('COMPRIMENTO (m): '))
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento:.1f}m²')


print('  Controle de Terrenos')
print('-'*30)
área()