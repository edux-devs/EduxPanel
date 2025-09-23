#!/usr/bin/env python3
#Autor: Eduardo

import random

try:
    from banner import banner
    from return_menu import return_menu
    from exiting import exiting
except:
    from functions.banner import banner  # type:ignore
    from functions.return_menu import return_menu  # type:ignore
    from functions.exiting import exiting  # type:ignore

def rg_dv(numeros):
    soma = sum(int(d) * p for d, p in zip(reversed(numeros), list(range(2, 10))))
    resto = soma % 11
    if resto == 10: return 'X'
    return str(resto)

def rg_forge():
    while True:
        banner()
        base = ''.join([str(random.randint(0, 9)) for _ in range(8)])  # 8 primeiros dígitos
        dv = rg_dv(base)
        rg = base + dv
        input_user = input('\033[1;32m~#\033[1;36m Gerar RG com Pontuação? (S/N)\n➤➤➤\033[0;37m ').strip().lower()
        if input_user in ['99', 'q']: return True
        print('\033[1;34m' + '─' * 44)
        if input_user in ['s', 'sim', 'y', 'yes']: print(f'\033[1;33m{"• RG gerado":<4} \033[0;37m▸ {rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8]}\033[0;32m (Válido)\033[0m\n', end='')
        else: print(f'\033[1;33m{"• RG gerado":<4} \033[0;37m▸ {rg}\033[0;32m (Válido)\033[0m\n', end='')
        if return_menu():return True

if __name__ == '__main__':
    try: rg_forge()
    except: exiting()  # type:ignore

