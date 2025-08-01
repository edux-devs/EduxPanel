#!/usr/bin/env python3
#Autor: Eduardo

import random

try:
    from banner import banner
    from return_menu import return_menu
    from exiting import exiting
except:
    from functions.banner import banner #type:ignore
    from functions.return_menu import return_menu #type:ignore
    from functions.exiting import exiting #type:ignore

def cpf_forge():
    while True:
        banner()
        soma = 0
        var = ''
        for i in range(0, 8): var = var + str(random.randint(0, 9))
        var = var + '8'
        #var = '435231910'
        num = 11
        for i in range(0, 9):
            num -= 1
            soma += int(var[i:i+1]) * num
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        var = var + str(soma)
        soma = 0
        num = 11
        for i in range(0, 10):
            soma += int(var[i:i+1]) * num
            num -= 1
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        var = var + str(soma)
        input_user = input('\033[1;32m~#\033[1;36m Gerar CPF com Pontuação? (S/N)\n➤➤➤\033[0;37m ').strip().replace('-', '')
        print('\033[1;34m'+ '─' * 44)
        if input_user.lower() in ['99', 'q']: return True
        if input_user.lower() in ['s', 'y', 'sim', 'yes']:
            print(f'\033[1;33m{"• CPF gerado":<4} \033[0;37m▸ {var[0:3]}.{var[3:6]}.{var[6:9]}-{var[9:11]}\033[0;32m (Válido)\033[0m\n', end='')
        else: 
            print(f'\033[1;33m{"• CPF gerado":<4} \033[0;37m▸ {var}\033[0;32m (Válido)\033[0m\n', end='')
        if return_menu(): return True

if __name__ == '__main__':
    try: cpf_forge()
    except: exiting() #type:ignore