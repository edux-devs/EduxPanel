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

def cnpj_checker():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o CNPJ a ser validado\n➤➤➤\033[0;37m ').strip().replace('-', '').replace('/', '').replace('.', '')
            if input_user.lower() in ['99', 'q']: return True
            if read_input('empty', input_user): continue
            if not len(input_user) == 14:
                print('\033[1;33m O CNPJ é formado por 14 digitos númerico!')
                time.sleep(2)
                continue
            if not read_input('numeric', input_user): continue
            break
        soma = 0
        num = 6
        cnpj = input_user
        input_user = str(input_user[0:12])
        for i in range(0, 12):
            num -= 1
            if num < 2: num = 9
            soma += int(input_user[i:i+1]) * num
        if (soma % 11) < 2: input_user = input_user + '0'
        else: input_user = input_user + str(11 - (soma % 11))
        soma = 0 
        num = 6
        for i in range(0, 13):
            soma += int(input_user[i:i+1]) * num
            num -= 1
            if num < 2: num = 9
        if (soma % 11) < 2: input_user = input_user + '0'
        else: input_user = input_user + str(11 - (soma % 11))
        print('\033[1;34m'+ '─' * 44) 
        if input_user == cnpj:
            print(f'\033[1;33m{"• CNPJ":<4} \033[0;37m▸ {input_user[0:2]}.{input_user[2:5]}.{input_user[5:8]}/{input_user[8:12]}-{input_user[12::]}\033[0;32m (Válido)\033[0m\n', end='')
        else:
            print(f'\033[1;33m{"• CNPJ":<4} \033[0;37m▸ {input_user[0:2]}.{input_user[2:5]}.{input_user[5:8]}/{input_user[8:12]}-{input_user[12::]}\033[0;31m (Inválido)\033[0m\n', end='')
        if return_menu() == True: return True

if __name__ == '__main__':
    cnpj_checker()

# 00.000.000/0001-91

