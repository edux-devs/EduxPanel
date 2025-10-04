#!/usr/bin/env python3
# Autor: Eduardo

import requests #type:ignore
import time

try:
    from banner import banner
    from return_menu import return_menu
    from read_input import read_input
    from exiting import exiting
except:
    from functions.banner import banner  # type:ignore
    from functions.return_menu import return_menu  # type:ignore
    from functions.read_input import read_input  # type:ignore
    from functions.exiting import exiting  # type:ignore


def onion_query():
    session = requests.Session()
    # Configura proxy Tor (porta padrão: 9050)
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    while True:
        for i in range(0, 4):
            if i == 3:
                return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o CPF a ser consultado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if read_input('empty', input_user): continue
            if not read_input('numeric', input_user): continue
            break
        try:
            url = f'http://pevbdnjjibvsldgavub3opda2m7g36zc5zuaxbillw52jjjqoehghpyd.onion/cpf.php?token=abc&cpf={input_user}'
            req = session.get(url, timeout=30)
            req.raise_for_status()
            data = req.json()
            data = data[0]

            print('\033[1;34m' + '─' * 44)
            for key, value in data.items():
                print(f'\033[1;33m• {key.capitalize(): <11} \033[0;37m▸ {str(value)}')
                time.sleep(0.01)
        except requests.exceptions.RequestException as e:
            print(f"\033[1;31mErro na conexão: {e}\033[0m")
            time.sleep(2)
        except ValueError:
            print("\033[1;31mResposta inválida da API.\033[0m")
            time.sleep(2)

        if return_menu() is True:
            return True


if __name__ == '__main__':
    try:
        onion_query()
    except KeyboardInterrupt:
        exiting()  # type:ignore
