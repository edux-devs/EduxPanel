#!/usr/bin/env python3
#Autor: Eduardo

import time

def return_menu():
    lst = ['Continuar', 'Retorne ao menu principal', 'Sair do Painel']
    print('\033[1;34m─' * 44) 
    a = 0
    for i in lst:
        a += 1
        if a == 3: a = 0
        print(f'\033[1;33m0{a}\033[0;37m ▸ {str(i): <37.36}')
        time.sleep(0.01)
    print('\033[1;34m─' * 44) 
    input_user = input('\033[1;32m~#\033[1;36m Continue ou retornar ao menu principal\n➤➤➤\033[0;37m ').strip()
    if input_user.replace(' ', '') == '': return False
    elif input_user.lower() == 'q': return True
    elif input_user.isnumeric() == False: return False
    if int(input_user) == 0: exit()
    elif int(input_user) == 2: return True

if __name__ == '__main__':
    return_menu()