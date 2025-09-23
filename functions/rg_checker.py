#!/usr/bin/env python3
#Autor: Eduardo

import time

try:
    from banner import banner
    from read_input import read_input
    from return_menu import return_menu
    from exiting import exiting
    from rg_forge import rg_dv #type:ignore
except:
    from functions.banner import banner #type:ignore
    from functions.read_input import read_input #type:ignore
    from functions.return_menu import return_menu #type:ignore
    from functions.exiting import exiting #type:ignore
    from functions.rg_forge import rg_dv #type:ignore

def rg_checker():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o RG a ser validado\n➤➤➤\033[0;37m ').strip().replace('.', '').replace('-', '')
            if read_input('empty', input_user): continue
            if input_user.lower() in ['99','q']: return True
            if not input_user[:-1].isdigit() or (not input_user[-1].isdigit() and input_user[-1] != 'X'):
                print('\033[1;33m O RG deve conter apenas números e o dígito final pode ser "X"')
                time.sleep(2)
                continue
            if len(input_user) != 9:
                print('\033[1;33m O RG deve ter 9 caracteres (8 números + 1 dígito verificador)')
                time.sleep(2)
                continue
            break 
        rg = input_user
        input_user = input_user[:8] + rg_dv(''.join((input_user[:8])))
        print('\033[1;34m' + '─' * 44)
        if rg == input_user: print(f'\033[1;33m{"• RG":<4} \033[0;37m▸ {rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8-9]}\033[0;32m (Válido)\033[0m\n', end='')
        else: print(f'\033[1;33m{"• RG":<4} \033[0;37m▸ {rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8-9]}\033[0;31m (Inválido)\033[0m\n', end='')
        if return_menu(): return True

if __name__ == '__main__':
    try:
        rg_checker()
    except:
        exiting()

# RG: 000000019
