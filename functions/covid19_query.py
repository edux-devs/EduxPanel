#!/usr/bin/env python3
#Autor: Eduardo

import time
import requests

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

def covid19_query():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe a sigla do estado a ser consultado\n➤➤➤\033[0;37m ')
            if input_user.lower() in ['99', 'q']: return True
            if read_input('empty', input_user): continue
            if not read_input('isalpha', input_user): continue
            break 
        req = requests.get(f'https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{input_user}').json()
        print('\033[1;34m'+ '─' * 44)
        for i in req.keys():
            print(f'\033[1;33m• {i.capitalize(): <8} \033[0;37m▸ {str(req[i])}')
            time.sleep(0.01)
        if return_menu(): return True

if __name__ == '__main__':
    try: covid19_query()
    except: exiting() 