#!/usr/bin/env python3
#Autor: Eduardo

from sys import argv

try:
    from banner import banner
    from menu import menu
    from clear import clear
except:
    from functions.banner import banner #type:ignore
    from functions.menu import menu #type:ignore
    from functions.clear import clear #type:ignore

def banner_menu():
    try:
        clear()
        banner()
        menu()
    except Exception as e:
        print(f'Erro: {e}\nArquivo: {argv[0]}')
        exit()

if __name__ == '__main__':
    banner_menu()
    