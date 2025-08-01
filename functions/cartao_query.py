#!/usr/bin/env python3
#Autor: Eduardo

import requests
import time

try:
    from banner import banner
    from return_menu import return_menu #type:ignore
    from exiting import exiting
    from cartao_checker import cartao_checker
    from read_input import read_input
except:
    from functions.banner import banner #type:ignore
    from functions.return_menu import return_menu  #type:ignore
    from functions.exiting import exiting #type:ignore
    from functions.cartao_checker import cartao_checker #type:ignore
    from functions.read_input import read_input #type:ignore

def cartao_query():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o Cartão a ser consultado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if read_input('empty', input_user): continue
            if not read_input('numeric', input_user): continue
            if not cartao_checker(input_user): 
                print('\033[1;31m❌ Cartão inválido!\033[0m')  
                time.sleep(2)
                continue
            break
        try:           
            req = requests.get(f'https://api.pagar.me/bin/v1/{input_user}').text
            req = eval(req)
        except:
            print('')
        print('\033[1;34m'+ '─' * 44) 
        for i in req.keys():
            print(f'\033[1;33m• {i.capitalize(): <15} \033[0;37m▸ {str(req[i])}')
            time.sleep(0.01)
        try:
            req = requests.get(f'https://lookup.binlist.net/{input_user}').json()
            for i in req.keys():
                print(f'\033[1;33m• {i.capitalize(): <15} \033[0;37m▸ {str(req[i])}')
                time.sleep(0.01)
        except:
            pass
        if return_menu() == True: return True 

if __name__ == '__main__':
    try:
        cartao_query()
    except KeyboardInterrupt:
        exiting() #type:ignore

# 371449635398431
