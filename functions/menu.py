#!/usr/bin/env python3
#Autor: Eduardo

def menu():
    print("\033[34m╔═════════════════════════════════════════════╗\033[0m")
    print("\033[34m║\033[0m [01] - \033[1mConsultar CEP  \033[0m                      \033[34m║")
    print("\033[34m║\033[0m [02] - \033[1mConsultar IP  \033[0m                       \033[34m║")
    print("\033[34m║\033[0m [03] - \033[1mConsultar Banco \033[0m                     \033[34m║")
    print("\033[34m║\033[0m [04] - \033[1mConsultar Instagram \033[0m                 \033[34m║")
    print("\033[34m║\033[0m [05] - \033[1mConsultar DDD \033[0m                       \033[34m║")
    print("\033[34m║\033[0m                                             \033[34m║")
    print("\033[34m║\033[0m [99] - \033[1mSair do Painel  \033[0m                     \033[34m║")
    print("\033[34m╚═════════════════════════════════════════════╝\033[0m", end='')

if __name__ == '__main__':
    menu()
