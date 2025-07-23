#!/usr/bin/env python3
#Autor: Eduardo

from os import system, name
from sys import argv

def clear():
    try:
        system('cls' if name == 'nt' else 'clear')
    except Exception as e:
        print(f'Erro: {e}\nArquivo: {argv[0]}')

if __name__ == '__main__':
    clear()
    