#!/usr/bin/env python3
#Autor: Eduardo
#Versão 1.0.0

# importar arquivos
import os
import sys
import importlib.util
import time

#variables
# var = here

# função de import
sys.path.append(os.path.abspath("."))
def importar_funcoes(pasta):
    base_path = os.path.join(os.path.dirname(__file__), pasta)

    for arquivo in os.listdir(base_path):
        if arquivo.endswith(".py") and not arquivo.startswith("__"):
            caminho = os.path.join(base_path, arquivo)
            nome_modulo = f"{pasta}.{arquivo[:-3]}" 

            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            for nome, obj in vars(modulo).items():
                if callable(obj) and not nome.startswith("_"):
                    globals()[nome] = obj

def login():
    banner() #type:ignore
    print('\033[1;32m~# \033[1;36mDigite o nome de usuário ➤ \033[0m', end='')
    usern = input().strip()
    print('\033[1;32m~# \033[1;36mDigite a senha ➤ \033[0m', end='')
    passw = input().strip()

    if usern == "EduxDevs" and passw == "Eduardo":
        return True
    else:
        print('\033[1;32m~# \033[1;31mUsername ou Password incorreto!\033[0m')
        time.sleep(3)
        return False


def main():
    func = {1:banco_query, 2:bin_query, 3:cartao_checker, 4:cartao_query, 5:cep_query, 6:cnpj_checker, 7:cnpj_forge, 8:cnpj_query, 9:covid19_query, 10:cpf_checker, 11:cpf_forge, 12:cpf_query, 13:ddd_query, 14:ddi_query, 15:instagram_query, 16:ip_query, 17:rg_checker, 18:rg_forge, 19:tiktok_query} # type: ignore
    while True:
        banner_menu() # type: ignore
        option = input().strip()
        if not option: continue
        if option.lower() in ['00', '0', '99', 'q']: return 0
        if not read_input('numeric', option): continue #type:ignore
        if 98 > int(option) > 19: 
            print(' opção inválida!')
            time.sleep(1)
            continue
        str(func[int(option)]())

if __name__ == '__main__': 
    if not os.path.exists('.installed'):
        print("\033[1;33m[!] Execute o arquivo install.sh primeiro\n\033[1;36m~$ bash install.sh")
        sys.exit(0)    
    importar_funcoes("functions")
    try:
        for i in [0,1,2,3]:
            if i == 3: exit()
            if not login(): continue
            if login: break
    except: exiting() #type:ignore
    try: main(), exiting() #type:ignore
    except KeyboardInterrupt:
        print('\n\033[1;33m Programa interrompido pelo usuário')
        exiting() #type:ignore
    except EOFError: 
        print('\n\033[1;33m Programa interrompido pelo usuário')
        exiting() #type:ignore
else:
    print('Você não pode importar esse arquivo!')
    exiting() #type:ignore

