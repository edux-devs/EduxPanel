#!/usr/bin/env python3
# Autor: Eduardo

import time
import instaloader  # type: ignore

try:
    from banner import banner
    from returnMenu import returnMenu
except ImportError:
    from functions.banner import banner  # type: ignore
    from functions.returnMenu import returnMenu  # type: ignore

def queryInstagram():
    while True:
        for tentativas in range(3):
            banner()
            input_user = input('\033[34m ~$ Informe o username ou ID para a consulta:\033[1;36m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not input_user: continue
            break

        try:
            time.sleep(3)
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, input_user)

            dados = {
                'ID': profile.userid,
                'Nome': profile.full_name,
                'Biografia': profile.biography,
                'Seguidores': profile.followers,
                'Seguindo': profile.followees,
                'Privado': profile.is_private,
                'Verificado': profile.is_verified,
                'URL': f'https://instagram.com/{profile.username}'
            }

            print('\n\033[1;34m╔' + '═' * 45 + '╗')
            print(f'║  \033[0;36mInformações de: @{profile.username:<26}\033[1;34m║')
            print('╠' + '═' * 45 + '╣')
        
            for chave, valor in dados.items():
                print(f'║ • {chave:<10}:\033[0;32m {str(valor).replace('\n', ''):<30.29}\033[1;34m║')
                time.sleep(0.03)

            print('╚' + '═' * 45 + '╝')

        except Exception as e:
            print(f'\n\033[31m[!] Erro ao consultar: {e}\033[0m')
            time.sleep(3)

        if returnMenu() == True:
            return True

if __name__ == '__main__':
    queryInstagram()
