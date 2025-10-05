#!/usr/bin/env python3
# Autor: Eduardo

import requests  # type:ignore
import time
import subprocess
import socket
import atexit
import sys

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


# Globals gerenciados automaticamente ao importar
tor_process = None
SESSION = None
TOR_STARTED_BY_ME = False


def is_tor_running(host="127.0.0.1", port=9050, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return True
    except Exception:
        return False
    finally:
        try:
            s.close()
        except Exception:
            pass


def start_tor(wait_seconds=10):
    try:
        p = subprocess.Popen(['tor'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # aguarda Tor inicializar e abrir a porta
        time.sleep(wait_seconds)
        return p
    except FileNotFoundError:
        return None
    except Exception:
        return None


def init_tor_and_session(auto_start=True):
    global tor_process, SESSION, TOR_STARTED_BY_ME
    if SESSION is not None:
        return SESSION, TOR_STARTED_BY_ME
    if not is_tor_running():
        if auto_start:
            tor_process = start_tor()
            if tor_process is None:
                SESSION = requests.Session()
                TOR_STARTED_BY_ME = False
                return SESSION, TOR_STARTED_BY_ME
            else:
                for _ in range(10):
                    if is_tor_running():
                        break
                    time.sleep(1)
                else:
                    print("\033[1;31m[✖] Tor iniciou mas a porta 9050 não abriu a tempo.\033[0m")
                    SESSION = requests.Session()
                    TOR_STARTED_BY_ME = False
                    return SESSION, TOR_STARTED_BY_ME
                TOR_STARTED_BY_ME = True
                globals()['tor_process'] = tor_process
        else:
            print("\033[1;31m[✖] Tor não está rodando. Inicie-o antes de usar este módulo.\033[0m")
            SESSION = requests.Session()
            TOR_STARTED_BY_ME = False
            return SESSION, TOR_STARTED_BY_ME

    else:
        TOR_STARTED_BY_ME = False
    SESSION = requests.Session()
    SESSION.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    return SESSION, TOR_STARTED_BY_ME


def _cleanup_tor_on_exit():
    global tor_process, TOR_STARTED_BY_ME
    if TOR_STARTED_BY_ME and tor_process:
        try:
            tor_process.terminate()
            tor_process.wait(timeout=5)
        except Exception:
            try:
                tor_process.kill()
            except Exception:
                pass

atexit.register(_cleanup_tor_on_exit)
_session, _ = init_tor_and_session(auto_start=True)


def cpf_query():
    global SESSION
    if SESSION is None:
        SESSION, _ = init_tor_and_session(auto_start=False)

    while True:
        for i in range(0, 4):
            if i == 3:
                return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o CPF a ser consultado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']:
                return True
            if read_input('empty', input_user):
                continue
            if not read_input('numeric', input_user):
                continue
            break

        try:
            url = f'http://pevbdnjjibvsldgavub3opda2m7g36zc5zuaxbillw52jjjqoehghpyd.onion/cpf.php?token=abc&cpf={input_user}'
            req = SESSION.get(url, timeout=30)
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
        cpf_query()
    except KeyboardInterrupt:
        exiting()  # type:ignore
