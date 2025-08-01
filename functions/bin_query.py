#!/usr/bin/env python3
#Autor: Eduardo

import requests
import time

try:
    from banner import banner
    from read_input import read_input
    from return_menu import return_menu
    from exiting import exiting
except:
    from functions.banner import banner #type:ignore
    from functions.read_input import read_input #type:ignore
    from functions.return_menu import return_menu #type:ignore
    from functions.exiting import exiting #type:ignore

def bin_query():
    while True:
        for i in range(0, 3):
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o BIN a ser consultado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not input_user: continue
            if not read_input('numeric', input_user): continue
            if len(input_user) < 6:
                print('\033[1;33m O BIN é formado por 6 ou mais dígitos!')
                time.sleep(2)
                continue
            break
        try:
            req = requests.get(f'https://api.pagar.me/bin/v1/{input_user}').text
        except Exception as e:
            print(f'\n\033[1;31m Erro ao consultar BIN: {e}\033[0m')
            time.sleep(2)
            continue
        try: req = eval(req)
        except:
            print('\n\033[1;31m Erro ao processar resposta da API.\033[0m')
            time.sleep(2)
            continue
        print('\033[1;34m' + '─' * 44)
        for i in req.keys():
            print(f'\033[1;33m• {i.capitalize(): <14}\033[0;37m ▸ {str(req[i])}')
            time.sleep(0.01)
        if return_menu() == True: return True

if __name__ == '__main__':
    try:
        bin_query()
    except KeyboardInterrupt:
        exiting() #type:ignore    
    #BIN de exemplo: 516230
