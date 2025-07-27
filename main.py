#!/usr/bin/env python3
#Autor: Eduardo
#Versão 0.1.15

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

def main():
    func = {1:cep, 2:ip, 3:banco, 4:queryInstagram, 5:ddd, 6:bin, 7:validarCartao} # type: ignore
    while True:
        bannerMenu() # type: ignore
        option = input('\n\033[1;34m ~ $ Digite a opção⎇\033[1;36m ').strip()
        if not option: continue
        if option.lower() in ['00', '0', '99', 'q']: return 0
        if not readInput('numeric', option): continue #type:ignore
        if int(option) > 7: 
            print(' opção inválida!')
            time.sleep(1)
            continue
        str(func[int(option)]())

if __name__ == '__main__':    
    importar_funcoes("functions")
    try: main(), sair() #type:ignore
    except KeyboardInterrupt:
        print('\n\033[1;33m Programa interrompido pelo usuário')
        time.sleep(2)
        sair() #type:ignore
    except EOFError: 
        print('\n\033[1;33m Programa interrompido pelo usuário')
        time.sleep(2)
        sair() #type:ignore
else:
    print('Você não pode importar esse arquivo!')
    exit()