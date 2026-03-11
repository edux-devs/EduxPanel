#!/usr/bin/env python
#Autor: Eduardo

import time
import unicodedata
import os

try:
    from banner import banner
    from read_input import read_input
except:
    from functions.banner import banner #type:ignore
    from functions.read_input import read_input #type:ignore

funcoes_painel = {
    "Instagram": "Social",
    "Github": "Social",
    "Telegram": "Social",
    "TikTok": "Social"}
'''
    "Twiiter": "Social"
}'''


def social_menu():
    links = {'1':'https://github.com/Edux-Devs', '2': 'https://instagram.com/Edux.Devs', '3':'https://t.me/EduxDevs','4': 'https://tiktok.com/@Edux.Devs'}
    while True:
        banner()
        time.sleep(0.1)
        for i, nome in enumerate(sorted(funcoes_painel.keys(), key=lambda x: unicodedata.normalize('NFKD', x).encode('ASCII', 'ignore').decode('ASCII').lower()), 1):
            print(f'\033[1;33m{str(i).zfill(2)} \033[0;37m▸ {nome}')
            time.sleep(0.01)
        print('\033[1;34m' + '─' * 44)
        print('\033[1;32m~# \033[1;36mDigite o número da opção ➤ \033[0m', end='')
        option = input('').strip()
        time.sleep(1)
        if not option: continue
        if option.lower() in ['00', '0', '99', 'q']: return 0
        if not read_input('numeric', option): continue #type:ignore
        if option not in links: 
            print(' opção inválida!')
            time.sleep(1)
            continue
        os.system('xdg-open ' + links[option] + ' > /dev/null 2>&1')
        break

if __name__ == '__main__':
    social_menu()