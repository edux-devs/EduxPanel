#!/usr/bin/env python3
#Autor: Eduardo

import os
import sys
import importlib.util
import requests # type: ignore
import time

#variables
#publicIp = requests.get('https://ifconfig.me').text

# importar arquivos
import os
import sys
import importlib.util

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

importar_funcoes("functions")

def ip():
    print('ip')
    time.sleep(10)

def main():
    func = {1:cep, 2:ip} # type: ignore
    while True:
        bannerMenu() # type: ignore
        option = input('\n\033[1;34m>_ Digite a opção: \033[1;36m').strip()
        if not option: continue
        if option.lower() == 'q': return 0
        if not option.isnumeric(): continue
        if int(option) == 99 or int(option) == 0: return 0
        if int(option) > 13:
            print(' option invalida!')
            time.sleep(1)
            continue
        str(func[int(option)]())

main()