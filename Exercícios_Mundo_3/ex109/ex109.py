# Modifique as funções criadas no ex107 para que elas aceitem um parâmetro a mais.
# O parâmetro informará se o valor retornado por elas vai ser ou não formatado pela função moeda() desenvolvido no ex 108

import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, False)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentar 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, False)}')