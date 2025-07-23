#!/usr/bin/env python3
#Autor: Eduardo

try: from clear import clear
except: from functions.clear import clear #type:ignore

def banner():
    clear()
    print("\033[34m   ⌬\033[33m  EduxPanel - Inteligência em Comando  \033[34m⌬")
    print("\033[34m╭─────────────────────────────────────────────╮")
    print("\033[34m│\033[33m  >_ Terminal Iniciado (2025)                \033[34m│")
    print("\033[34m│\033[33m  🧠 Mente Digital | ⚙️  Automação | 📡 Dados \033[34m│")
    print("╰─────────────────────────────────────────────╯\033[0m\n", end='')

if __name__ == '__main__':
    banner()    
