from lib.interface import *
from lib.arquivo import *
from time import sleep

arquivo = 'cursoemvideo.txt'
if not arquivoexiste(arquivo):
    criararquivo(arquivo)
else:
    while True:
        cabecalho('SISTEMA DE CADASTRO')
        resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Programa'])
        if resposta == 1:
            lerarquivo(arquivo)
        elif resposta == 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            cadastrar(arquivo, nome, idade)
        elif resposta == 3:
            cabecalho('Saindo do programa...')
            sleep(2)
            break
        else:
            print(erro('Erro! Digite uma opção válida.'))
        sleep(2)

