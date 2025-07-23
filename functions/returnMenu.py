#!/usr/bin/env python3
#Autor: Eduardo

import time

def returnMenu():
    lst = ['Continuar', 'Retorne ao menu principal', 'Sair do Painel']
    print('\033[1;34m╔' + '═'*45 + '╗') 
    a = 0
    for i in lst:
        a += 1
        if a == 3: a = 00
        print(f'║ \033[1;32m[\033[m\033[1;36m0{a}\033[1;32m]\033[m - \033[1;36m{str(i): <37.36}║')
        time.sleep(0.01)
    print('╚' + '═'* 45 + '╝', end='')
    input_user = input('\n\033[1;34m ~ $ Continue ou retornar ao menu principal: \033[1;36m').strip()
    if input_user.replace(' ', '') == '': return False
    elif input_user.lower() == 'q': return True
    elif input_user.isnumeric() == False: return False
    if int(input_user) == 0: exit()
    elif int(input_user) == 2: return True

if __name__ == '__main__':
    returnMenu()