# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.

def leiaint(txt):
    from colorama import init, Fore, Style
    init(autoreset=True)
    num = 0
    while True:
        try:
            num = int(input(txt))
        except KeyboardInterrupt:
            print(Style.BRIGHT + Fore.RED + '\nUsuário preferiu ver o filme do pelé do que digitar esse número.')
            return num
        except Exception:
            print(Style.BRIGHT + Fore.RED + 'ERRO! Digite um número inteiro válido.')
        else:
            return num


def leiafloat(txt):
    from colorama import init, Fore, Style
    init(autoreset=True)
    num = 0
    while True:
        try:
            num = float(input(txt))
        except KeyboardInterrupt:
            print(Style.BRIGHT + Fore.RED + '\nUsuário preferiu ver o filme do pelé do que digitar esse número.')
            return num
        except Exception:
            print(Style.BRIGHT + Fore.RED + 'ERRO! Digite um número real válido.')
        else:
            return num


# num_int = leiaint('Digite um número inteiro: ')
# num_float = leiafloat('Digite um número Real: ')
# print(f'Você digitou o valor inteiro {num_int} e o real {num_float}')