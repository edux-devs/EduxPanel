#!/usr/bin/env python3
#Autor: Eduardo

import time

try:
    from clear import clear
    from banner import banner
    from returnMenu import returnMenu
except:
    from functions.clear import clear #type:ignore
    from functions.banner import banner #type:ignore
    from functions.returnMenu import returnMenu #type:ignore

def validarCartao():
    while True:
        clear()
        banner()
        try:
            input_user = input('\033[1;34m Informe o cartão a ser validado⎇\033[1;36m ')
            input_user = ''.join(filter(str.isdigit, input_user.strip()))
            if not input_user: continue

            if len(input_user) not in [13, 14, 15, 16]:
                print('\n\033[1;31m ❌ Quantidade de dígitos inválida!\033[0m')
                time.sleep(2)
                continue

            soma = 0
            for i, digito in enumerate(reversed(input_user)):
                n = int(digito)
                if i % 2 == 1:
                    n *= 2
                    n = n - 9 if n > 9 else n
                soma += n

            if soma % 10 == 0:
                print(f'\033[1;34m {"•Cartão":<8}: \033[0;32mVálido\033[0m\n')
                time.sleep(2)
            else:
                print(f'\033[1;34m {"•Cartão":<8}: \033[0;31mInválido\033[0m\n')
                time.sleep(2)
                continue
        except Exception as e:
            print(e)
        
        returnMenu()

if __name__ == '__main__':
    validarCartao()
    # Exemplo: 371449635398431	