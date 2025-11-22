# Dentro do pacote utilidades CeV que criamos no ex111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores monetários.

from utilidadesCeV import dado,moeda

preco = dado.leia_dinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 22)