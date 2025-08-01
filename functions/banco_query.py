#!/usr/bin/env python3
#Autor: Eduardo

import requests
import time

try:
    from banner import banner
    from return_menu import return_menu #type:ignore
    from exiting import exiting
    from read_input import read_input
except:
    from functions.banner import banner #type:ignore
    from functions.return_menu import return_menu  #type:ignore
    from functions.exiting import exiting #type:ignore
    from functions.read_input import read_input #type:ignore

def banco_query():
    while True:
        for i in range(4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o COMPE a ser consultado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not input_user: continue
            if not read_input('numeric', input_user): continue
            break   
        req = requests.get(f'https://brasilapi.com.br/api/banks/v1/{input_user}').json()
        print('\033[1;34m'+ '─' * 44) 
        for i in req.keys():
            print(f'\033[1;33m• {i.capitalize(): <8} \033[0;37m▸ {str(req[i]): <31.30}')
            time.sleep(0.01)
        if return_menu(): return True 

if __name__ == '__main__':
    try: banco_query()
    except: exiting()

# Exemplo: 143