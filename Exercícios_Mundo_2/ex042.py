#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#  >Equilátero: todos os lados iguais
#  >Isósceles: dois lados iguais
#  >Escaleno: todos os lados diferentes

print('Esse programa verifica se 3 retas formam um triângulo')
reta1 = float(input('Medida da primeira reta: '))
reta2 = float(input('Medida da segunda reta: '))
reta3 = float(input('Medida da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('Essas retas podem formar um triângulo\nTipo: ', end="")
    if reta1 == reta2 == reta3:
        print('EQUILÁTERO')
    elif reta1 == reta2 != reta3 or reta1 != reta2 == reta3 or reta1 == reta3 != reta2:
        print('ISÓSCELES')
    elif reta1 != reta2 != reta3 != reta1:
        print('ESCALENO')
else:
    print('Essas retas NÃO formam um triangulo')
