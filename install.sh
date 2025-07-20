#!/bin/bash
clear

if [ -d ".git" ]; then
  echo -e "\033[34mAtualizando arquivos do repositório...\033[0m"
  git fetch origin &>/dev/null
  git reset --hard origin/main &>/dev/null
fi

function open_link {
  command -v xdg-open &>/dev/null && {
    xdg-open "$1"
    sleep 5
  }
}

echo "Abrindo perfis sociais..."
open_link "https://instagram.com/edux.dev" &>/dev/null
open_link "https://www.youtube.com/@edux-dev" &>/dev/null
open_link "https://tiktok.com/@edux.dev" &>/dev/null

if [[ -e /data/data/com.termux ]]; then
  PKG_MANAGER="pkg"
else
  PKG_MANAGER="sudo apt-get"
  if [[ $EUID -ne 0 ]]; then
    echo "Por favor, execute este script como root (sudo)."
    exit 1
  fi
fi

if ! command -v python3 &>/dev/null; then
  echo "Instalando Python3..."
  $PKG_MANAGER update -y &>/dev/null && yes "" | $PKG_MANAGER upgrade -y &>/dev/null
  $PKG_MANAGER install -y python3 &>/dev/null
  [[ "$PKG_MANAGER" == "pkg" ]] || $PKG_MANAGER install -y python3-pip &>/dev/null
fi

echo "Instalando os requisitos do programa..."
python3 -m pip install --upgrade pip &>/dev/null
if [[ -f requirements.txt ]]; then
  python3 -m pip install -r requirements.txt
else
  echo "Arquivo requirements.txt não encontrado."
fi

clear
echo -e "\033[32mExecutando o programa principal...\033[0m"
python3 main.py

