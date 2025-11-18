#Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
print(f'Área da parede é {area:.1f}m², sendo necessários {area / 2:.0f}l de tinta')