def leia_dinheiro(n):
    from colorama import init, Fore
    init(autoreset=True)
    while True:
        num = input(n)
        if not num.isnumeric():
            if ',' in num or '.' in num:
                num = num.replace(',','.')
                return float(num)
            print(Fore.RED + f'Erro "{num}" é um preço inválido')
        else:
            return float(num)
