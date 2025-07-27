#!/usr/bin/env python3
#Autor: Eduardo

import requests
import time

try:
    from banner import banner
    from readInput import readInput
    from returnMenu import returnMenu
except:
    from functions.banner import banner #type:ignore
    from functions.readInput import readInput #type:ignore
    from functions.returnMenu import returnMenu #type:ignore

def bin():
    while True:
        for i in range(0, 3):
            banner()
            input_user = input('\033[1;34m Informe o BIN para a consulta⎇\033[1;36m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not input_user: continue
            if not input_user.isnumeric(): continue
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
        print('\033[1;34m╔═══════════════[ DADOS DO BIN ]══════════════╗')
        for i in req.keys():
            print(f'\033[1;34m║ • {i.capitalize(): <14}:\033[0;32m {str(req[i]): <26.25}\033[1;34m║')
            time.sleep(0.01)
        print('╚' + '═'* 45 + '╝')
        if returnMenu() == True: return True

if __name__ == '__main__':
    bin()