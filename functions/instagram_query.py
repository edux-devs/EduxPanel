#!/usr/bin/env python3
# Autor: Eduardo

import time
import instaloader  # type: ignore
import requests

try:
    from banner import banner
    from return_menu import return_menu
    from exiting import exiting
    from read_input import read_input
except ImportError:
    from functions.banner import banner  # type: ignore
    from functions.return_menu import return_menu  # type: ignore
    from functions.exiting import exiting #type:ignore
    from functions.read_input import read_input #type:ignore

def get_username_from_id(user_id):
    headers = {"User-Agent": "Instagram 155.0.0.37.107"}
    try:
        r = requests.get(f"https://i.instagram.com/api/v1/users/{user_id}/info/", headers=headers)
        if r.status_code == 200:
            return r.json()['user']['username']
        else:
            print(f"\033[1;31m[x] Erro {r.status_code}: Não foi possível obter o username.")
            return None
    except Exception as e:
        print(f"\033[1;31m[!] Falha na requisição: {e}")
        return None

def instagram_query():
    while True:
        for _ in range(3):
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o ID ou username a ser consultado\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not input_user: continue
            if input_user.isdigit():
                if not read_input('instagram_id', input_user): continue
                username = get_username_from_id(input_user)
                if not username:
                    time.sleep(2)
                    continue
                input_user = username
            if not read_input('instagram_user', input_user): continue
            break
        else: return False
        try:
            time.sleep(3)
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, input_user)
            dados = {
                'Username': profile.username,
                'ID': profile.userid,
                'Seguidores': profile.followers,
                'Seguindo': profile.followees,
                'Privado': profile.is_private,
                'Verificado': profile.is_verified,
                'Nome': profile.full_name,
                'Biografia': profile.biography,
                'URL': f'https://instagram.com/{profile.username}'
            }

            print('\033[1;34m' + '─' * 44)
            for chave, valor in dados.items():
                print(f'\033[1;33m• {chave: <10} \033[0;37m▸ {str(valor)}')
                time.sleep(0.03)

        except Exception as e:
            print(f'\n\033[31m[!] Erro ao consultar: {e}\033[0m')
            time.sleep(3)
        if return_menu(): return True

if __name__ == '__main__':
    try: instagram_query()
    except: exiting()
