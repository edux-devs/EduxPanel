#!/usr/bin/env python3
# Autor: Eduardo

import time
import sys

try:
    from clear import clear
    from banner import banner
    from return_menu import return_menu
    from read_input import read_input
    from exiting import exiting 
except:
    from functions.clear import clear #type:ignore
    from functions.banner import banner #type:ignore
    from functions.return_menu import return_menu #type:ignore
    from functions.read_input import read_input #type:ignore
    from functions.exiting import exiting #type:ignore

def checker(input_user):
    soma = 0
    for i, digito in enumerate(reversed(input_user)):
        n = int(digito)
        if i % 2 == 1:
            n *= 2
            n = n - 9 if n > 9 else n
        soma += n
    return soma % 10 == 0

def cartao_checker(input_user: str = None):
    if input_user is not None:
        input_user = ''.join(filter(str.isdigit, str(input_user)))
        if not input_user: return False
        if not read_input('numeric', input_user): return False
        if len(input_user) not in [13, 14, 15, 16]: return False
        return checker(input_user)
    
    while True:
        banner()
        try:
            input_user = input('\033[1;32m~#\033[1;36m Informe o número do cartão a ser validado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not read_input('numeric', input_user): continue
            input_user = ''.join(filter(str.isdigit, input_user))
            if not input_user: continue
            if len(input_user) not in [13, 14, 15, 16]:
                print('\033[1;31m❌ Quantidade de dígitos inválida!\033[0m')
                time.sleep(2)
                continue
            print('\033[1;34m' + '─' * 44) 
            if checker(input_user):
                print(f'\033[1;33m{"• Cartão":<8} \033[0;37m▸ \033[0;32mVálido\033[0m\n', end='')
            else:
                print(f'\033[1;33m{"• Cartão":<8} \033[0;37m▸ \033[0;31mInválido\033[0m\n', end='')    
        except Exception as e:
            print(e)
        if return_menu(): return True

if __name__ == '__main__':
    try:
        cartao_checker()
    except:
        exiting() #type:ignore

# 371449635398431
