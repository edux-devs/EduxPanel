#!/usr/bin/env python3
#Autor: Eduardo

import requests
import time

try:
    from banner import banner
    from returnMenu import returnMenu #type:ignore
except:
    from functions.banner import banner #type:ignore
    from functions.returnMenu import returnMenu #type:ignore 

def cep():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[34m ~$ Informe o CEP para a consulta:\033[1;36m ').strip().replace('-', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if not input_user: continue
            if not input_user.isnumeric(): continue
            if len(input_user) != 8:
                print('\033[1;33m O cep é formado por 8 digitos númerico!')
                time.sleep(2)
                continue
            break               
        req = requests.get(f'https://viacep.com.br/ws/{input_user}/json/').json()
        print('\033[1;34m╔═════════════════════════════════════════════╗') 
        for i in req.keys():
            print(f'\033[1;34m║ • {i.capitalize(): <11}:\033[0;32m {str(req[i]): <28}\033[1;34m ║')
            time.sleep(0.01)
        print('╚' + '═'* 45 + '╝')
        if returnMenu() == True: return True

if __name__ == '__main__':
    cep()
