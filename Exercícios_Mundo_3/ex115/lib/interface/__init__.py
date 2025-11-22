def erro(error):
    from colorama import init, Fore, Style
    init(autoreset=True)
    return Style.BRIGHT + Fore.RED + error

def leiaint(txt):
    from time import sleep
    while True:
        try:
            num = int(input(txt))
        except KeyboardInterrupt:
            print(erro('\nUsuário preferiu ver o filme do pelé do que digitar esse número.'))
            return 3
        except Exception:
            print(erro('ERRO! Digite um número inteiro válido.'))
            sleep(2)
        else:
            return num


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    from colorama import init, Fore
    init(autoreset=True)
    c = 1
    for item in lista:
        print(Fore.YELLOW + f'{c}' '-', Fore.LIGHTBLUE_EX + f'{item}')
        c+=1
    print(linha())
    opc = leiaint(Fore.LIGHTMAGENTA_EX + 'Sua opção: ')
    return opc