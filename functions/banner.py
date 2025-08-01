#!/usr/bin/env python3
#Autor: Eduardo

import time
import socket
import datetime

try: from clear import clear
except: from functions.clear import clear #type:ignore

def get_local_ip():
    try: return socket.gethostbyname(socket.gethostname())
    except: return 'Indefinido'

def banner():
    versao = 'v1.0'
    data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    ip_local = get_local_ip()
    host = socket.gethostname()

    banner_print = [
        '\033[1;35m[:: EduxPanel ::] \033[1;37mInteligência em Comando',
        '\033[1;34m' + '─' * 44,
        f'\033[1;33m📦 {"Versão":<8} \033[0;37m▸ {versao}\033[0m',
        f'\033[1;33m🗓️  {"Data":<8} \033[0;37m▸ {data}\033[0m',
        f'\033[1;33m🌐 {"IP Local":<8} \033[0;37m▸ {ip_local}\033[0m',
        f'\033[1;33m💻 {"Host":<8} \033[0;37m▸ {host}\033[0m',
        '\033[1;34m' + '─' * 44,
    ]

    clear()
    for i in banner_print:
        print(i)
        time.sleep(0.01)
    
if __name__ == '__main__':
    banner()