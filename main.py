#!/usr/bin/env python3
import os
import sys
import importlib.util

sys.path.append(os.path.abspath("."))

def importar_funcoes(pasta):
    base_path = os.path.join(os.path.dirname(__file__), pasta)
    for arquivo in os.listdir(base_path):
        if arquivo.endswith(".py") and not arquivo.startswith("__"):
            caminho = os.path.join(base_path, arquivo)
            nome_modulo = arquivo[:-3]
            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)
            globals().update({k: v for k, v in vars(modulo).items() if not k.startswith("_")})

importar_funcoes("functions")

os.system('cls' if os.name == 'nt' else 'clear')

banner()
menu()
input_user = input("   >_Digite a opção: ")
