#!/usr/bin/env python3
#Autor: Eduardo

import time

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

def cpf_checker():
      while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o CPF a ser validado\n➤➤➤\033[0;37m ').strip().replace('-', '').replace('.', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if read_input('empty', input_user): continue
            if not read_input('numeric', input_user): continue
            if not len(input_user) == 11:
                print('\033[1;33m O CPF é formado por 11 digitos númerico!')
                time.sleep(2)
                continue
            break
        soma = 0
        cpf = input_user
        input_user = str(input_user[0:9])
        num = 11
        for i in range(0, 9):
            num -= 1
            soma += int(input_user[i:i+1]) * num
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        input_user = input_user + str(soma)
        soma = 0
        num = 11
        for i in range(0, 10):
            soma += int(input_user[i:i+1]) * num
            num -= 1
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        input_user = input_user + str(soma)
        print('\033[1;34m'+ '─' * 44) 
        if input_user == cpf:
            print(f'\033[1;33m{"• CPF":<4} \033[0;37m▸ {input_user[0:2]}.{input_user[2:5]}.{input_user[5:8]}/{input_user[8:12]}-{input_user[12::]}\033[0;32m (Válido)\033[0m\n', end='')
        else:
            print(f'\033[1;33m{"• CPF":<4} \033[0;37m▸ {input_user[0:2]}.{input_user[2:5]}.{input_user[5:8]}/{input_user[8:12]}-{input_user[12::]}\033[0;31m (Inválido)\033[0m\n', end='')
        if return_menu(): return True

if __name__ == '__main__':
    try: cpf_checker()
    except: exiting()

# 000.000.001-91
