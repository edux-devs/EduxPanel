#!/usr/bin/env python3
#Autor: Eduardo

import time
import requests

try:
    from banner import banner
    from return_menu import return_menu
    from read_input import read_input
    from exiting import exiting
except:
    from functions.banner import banner #type:ignore
    from functions.return_menu import return_menu #type:ignore
    from functions.read_input import read_input #type:ignore
    from functions.exiting import exiting #type:ignore

def ip_query():
    while True:
        for i in range(3):
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o IP a ser consultado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not input_user: continue
            #if not read_input('numeric', input_user.replace('.', '')): continue
            break
        else: return False
        req = requests.get(f'http://ip-api.com/json/{input_user}').json()
        print('\033[1;34m'+ '─' * 44)  
        for i in req.keys():
            print(f'\033[1;33m• {i.capitalize(): <11} \033[0;37m▸ {str(req[i])}')
            time.sleep(0.01)
        if return_menu(): return True

if __name__ == '__main__':
    try: ip_query()
    except: exiting()

# IP: 1.1.1.1
