#Desenvolva um programa que leia a distância de uma viagem em km
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens acima disso

dist = float(input('Qual a distância da sua viagem? '))
if dist > 200:
    preco_dist = float(dist * 0.45)
    print(f'Distância da viagem é de {dist:.1f}km e irá custar R${preco_dist:.2f}')
else:
    preco_dist = float(dist * 0.5)
    print(f'A distância da sua viagem é de {dist}km e irá custar R${preco_dist}')