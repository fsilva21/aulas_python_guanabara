# Adicione ao módulo moeda.py, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui

import moeda

preco = float(input('Digite o preço: R$'))
print(moeda.resumo(preco, 25, 40))