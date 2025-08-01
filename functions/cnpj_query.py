#!/usr/bin/env python3
#Autor: Eduardo

import requests
import time

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

def cnpj_query():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o CNPJ a ser consultado\n➤➤➤\033[0;37m ').strip().replace('-', '').replace('/', '').replace('.', '')
            if input_user.lower() in ['99', 'q']: return True
            if read_input('empty', input_user): continue
            if not read_input('numeric', input_user): continue
            if len(input_user) != 14:
                print('\033[1;33m O CNPJ é formado por 14 digitos númerico!')
                time.sleep(2)
                continue
            break               
        req = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/${input_user}').json()
        print('\033[1;34m'+ '─' * 44) 
        for i in req.keys():
            print(f'\033[1;33m• {i.capitalize(): <11} \033[0;37m▸ {str(req[i])}')
            time.sleep(0.01)
        if return_menu() == True: return True

if __name__ == '__main__':
    try:
        cnpj_query()
    except:
        exiting() #type:ignore

# 00.000.000/0001-91

