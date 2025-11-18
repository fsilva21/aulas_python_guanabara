# DOCSTRINGS e help()
# def contador(i,f,p):
#     """
#     —> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     print('Fim!')
#
#
# contador(0,10,2)
# help(contador)

# PARÂMETROS OPCIONAIS
# def somar(a=0, b=0, c=0):
#     """
#     —> Faz a soma de três valores e mostra o resultado na tela
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
#
# somar(1,6)

# ESCOPO DE VARIÁVEIS
# def teste():
#     x=8 # Variável local
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
#
#
# n = 2 # Variável global
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}')

# def funcao(n2):
#     global n1 # Diz para o python que a variável local deverá se transformar na global
#     n1 = 4
#     n2 += 5
#     print(f'n1 local vale {n1} e n2 vale {n2} ')
#
#
# n1 = 2
# funcao(n1)
# print(f'n1 global vale {n1}')

# Retornando valores
# def somar(a=0, b=0, c=0):
#     """
#     —> Faz a soma de três valores e mostra o resultado na tela
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     """
#     s = a + b + c
#     return s
#
#
# r1 = somar(3,2,5)
# r2 = somar(2,2)
# r3 = somar(6)
#
# print(f'Os resultados foram {r1}, {r2}, {r3}')

# EXEMPLOS USANDO O "return"
# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#
#
# f1 = fatorial(6)
# f2 = fatorial(9)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')

# RETURN DE VALOR BOOLEANO
# def par(n=0):
#     """
#
#     :param n:
#     :return:
#     """
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
#
# num = int(input('Digite um número: '))
# if par(num):
#     print('É par!')
# else:
#     print('Não é par!')