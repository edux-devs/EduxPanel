#!/usr/bin/env python
#Autor: Eduardo

import time
import unicodedata

funcoes_painel = {
    "Banco Info": "Info",
    "BIN Lookup": "Lookup",
    "Cartão Checker": "Checker",
    "Cartão Lookup": "Lookup",
    "CEP Lookup": "Lookup",
    "CNPJ Checker": "Checker",
    "CNPJ Forge": "Forge",
    "CNPJ Info": "Info",
    "CPF Checker": "Checker",
    "CPF Forge": "Forge",
    "Covid19 Info": "Info",
    "DDD Info": "Info",
    "DDI Info": "Info",
    "Instagram Info": "Info",
    "IP Lookup": "Lookup",}
'''
    "RG Checker": "Checker",
    "RG Forge": "Forge",
    "Telefone Básico Lookup": "Lookup"
}'''


def menu():
    time.sleep(0.1)
    for i, nome in enumerate(sorted(funcoes_painel.keys(), key=lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII').lower()), 1):
        print(f'\033[1;33m{str(i).zfill(2)} \033[0;37m▸ {nome}')
        time.sleep(0.01)

    print('\033[1;34m' + '─' * 44)
    print('\033[1;33m98 \033[0;37m▸ redes socias')
    print('\033[1;33m99 \033[0;37m▸ Sair')
    print('\033[1;34m' + '─' * 44)
    print('\033[1;32m~# \033[1;36mDigite o número da opção ➤ \033[0m', end='')

if __name__ == '__main__':
    menu()