# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira as funções utilizadas nos desafios anteriores para o pacote moeda e mantenha tudo funcionando.

from utilidadesCeV import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 35, 22)
