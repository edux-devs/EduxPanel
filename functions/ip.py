#!/usr/bin/env python3
#Autor: Eduardo

import time
import requests

try:
    from banner import banner
    from returnMenu import returnMenu
except:
    from functions.banner import banner #type:ignore
    from functions.returnMenu import returnMenu #type:ignore

def ip():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m ~ $ Informe o ip para a consulta:\033[1;36m ').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if not input_user: continue
            '''
            for i in range(0, len(input_user)):
                if input_user[i] == '.':
                    if int(input_user[0:i-4]) > 255:
                        print('\033[1;33m O IP informado é falso!')
                        time.sleep(2)
            '''
            #if readInput(input_user, 'numeric') != True: continue
            break
        req = requests.get(f'http://ip-api.com/json/{input_user}').json()
        print('\033[1;34m╔'+ '═'* 45 + '╗') 
        for i in req.keys():
            print(f'\033[1;34m║ •{i.capitalize(): <11}:\033[0;32m {str(req[i]): <29.29} ║')
            time.sleep(0.01)
        print('╚' + '═'* 45 + '╝')
        if returnMenu() == True: return True
        # verifica se o ip é valido . 255

if __name__ == '__main__':
    ip()
