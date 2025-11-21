# Crie um programa que tenha a função "leiaInt()", que vai funcionar de forma semelhante à função "input()" do Python.
# Essa função fará a validação para aceitar apenas um valor numérico.
# Exemplo: n = leiaInt('Digite um n').

def leiaint(txt):
    from colorama import init, Fore, Style
    init(autoreset=True)
    while True:
        num = input(txt)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print(Style.BRIGHT + Fore.RED + 'ERRO! Digite um número inteiro válido.')
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
