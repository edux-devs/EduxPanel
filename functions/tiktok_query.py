#!/usr/bin/env python3
# Autor: Eduardo

import time
import requests
import re
import json

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

def get_tiktok_profile(identifier):
    if re.match(r'^MS4wLjAB', identifier):
        url = f"https://www.tiktok.com/@{identifier}"
    else:
        url = f"https://www.tiktok.com/@{identifier}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"\033[1;31m[x] Erro {response.status_code}: Não foi possível acessar o perfil.")
            return None
        html = response.text

        info = {}

        # IDs
        match_id = re.search(r'"id":"([0-9]+)"', html)
        match_secuid = re.search(r'"secUid":"([A-Za-z0-9_-]+)"', html)
        info['id'] = match_id.group(1) if match_id else None
        info['secUid'] = match_secuid.group(1) if match_secuid else None

        # Username
        match_username = re.search(r'"uniqueId":"([A-Za-z0-9_.]+)"', html)
        info['username'] = match_username.group(1) if match_username else None

        # Nome de exibição
        match_nickname = re.search(r'"nickname":"([^"]+)"', html)
        info['display_name'] = match_nickname.group(1) if match_nickname else None

        # Avatar
        match_avatar = re.search(r'"avatarLarger":"([^"]+)"', html)
        info['avatar_url'] = match_avatar.group(1).encode('utf-8').decode('unicode_escape') if match_avatar else None

        # Bio / descrição
        match_bio = re.search(r'"signature":"([^"]+)"', html)
        info['bio'] = match_bio.group(1).encode('utf-8').decode('unicode_escape').encode('latin1').decode('utf-8') if match_bio else None

        # Seguidores, seguindo, curtidas, vídeos
        match_followers = re.search(r'"followerCount":(\d+)', html)
        match_following = re.search(r'"followingCount":(\d+)', html)
        match_hearts = re.search(r'"heartCount":(\d+)', html)
        match_videos = re.search(r'"videoCount":(\d+)', html)

        info['followers'] = int(match_followers.group(1)) if match_followers else None
        info['following'] = int(match_following.group(1)) if match_following else None
        info['hearts'] = int(match_hearts.group(1)) if match_hearts else None
        info['videos'] = int(match_videos.group(1)) if match_videos else None

        # Link externo na bio (se existir)
        match_biolink = re.search(r'"bioLink":"([^"]+)"', html)
        info['bio_link'] = match_biolink.group(1).encode('utf-8').decode('unicode_escape') if match_biolink else None

        return info

    except Exception as e:
        print(f"\033[1;31m[!] Falha na requisição: {e}")
        return None

def tiktok_query():
    while True:
        for _ in range(3):
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o username ou secUid do TikTok\n➤➤➤\033[0;37m ').strip()
            if input_user.lower() in ['99', 'q']: return True
            if not input_user: continue
            #if not read_input('tiktok_user', input_user): continue
            break
        else: return False

        profile_info = get_tiktok_profile(input_user)
        if not profile_info:
            time.sleep(2)
            continue

        print('\033[1;34m' + '─' * 44)
        for chave, valor in profile_info.items():
            print(f'\033[1;33m• {chave: <12} \033[0;37m▸ {str(valor)}')
            time.sleep(0.03)

        if return_menu(): return True

if __name__ == '__main__':
    try: tiktok_query()
    except: exiting()
