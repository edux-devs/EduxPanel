#!/usr/bin/env python3
#Autor: Eduardo

import requests
import time

try:
    from banner import banner
    from returnMenu import returnMenu
except:
    from functions.banner import banner #type:ignore
    from functions.returnMenu import returnMenu  #type:ignore

def banco():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m~ $ Informe o codigo para a consulta⎇\033[1;36m ').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if not input_user: continue
            if not input_user.isnumeric(): continue
            break             
        req = requests.get(f'https://brasilapi.com.br/api/banks/v1/{input_user}').json()
        print('\033[1;34m╔'+ '═'* 45 + '╗') 
        for i in req.keys():
            print(f'\033[1;34m║ •{i.capitalize(): <8}:\033[0;32m {str(req[i]): <32.31} ║')
            time.sleep(0.01)
        print('╚' + '═'* 45 + '╝')
        if returnMenu() == True: return True

if __name__ == '__main__':
    banco()