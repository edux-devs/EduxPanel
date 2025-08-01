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

def main():
    func = {1:banco_query, 2:bin_query, 3:cartao_checker, 4:cartao_query, 5:cep_query, 6:cnpj_checker, 7:cnpj_forge, 8:cnpj_query, 9:covid19_query, 10:cpf_checker, 11:cpf_forge, 12:ddd_query, 13:ddi_query, 14:instagram_query, 15:ip_query} # type: ignore
    while True:
        banner_menu() # type: ignore
        option = input().strip()
        if not option: continue
        if option.lower() in ['00', '0', '99', 'q']: return 0
        if not read_input('numeric', option): continue #type:ignore
        if 98 > int(option) > 18: 
            print(' opção inválida!')
            time.sleep(1)
            continue
        str(func[int(option)]())

if __name__ == '__main__': 
    if os.path.exists('.installed'):
        print("Execute o arquivo install.sh primeiro\n bash install.sh")
        sys.exit(0)    
    importar_funcoes("functions")
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