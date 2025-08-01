#!/usr/bin/env python3
#Autor: Eduardo

import time
import requests

try:
    from banner import banner
    from read_input import read_input
    from return_menu import return_menu
    from exiting import exiting 
except:
    from functions.banner import banner #type:ignore
    from functions.read_input import read_input #type:ignore
    from functions.return_menu import return_menu #type:ignore
    from functions.exiting import exiting #type:ignore

ddd_siglas = {'11':'SP', '12':'SP', '13':'SP', '14':'SP', '15':'SP', '16':'SP', '17':'SP', '18':'SP', '19':'SP', '21':'RJ', '22':'RJ', '24':'RJ', '27':'ES', '28':'ES', '31':'MG', '32':'MG', '33':'MG', '34':'MG', '35':'MG', '37':'MG', '38':'MG', '41':'PR', '42':'PR', '43':'PR', '44':'PR', '45':'PR', '46':'PR', '47':'SC', '48':'SC', '49':'SC', '51':'RS', '53':'RS', '54':'RS', '55':'RS', '61':'DF', '62':'GO', '63':'TO', '64':'GO', '65':'MT', '66':'MT', '67':'MS', '68':'AC', '69':'RO', '71':'BA', '73':'BA', '74':'BA', '75':'BA', '77':'BA', '79':'SE', '81':'PE', '82':'AL', '83':'PB', '84':'RN', '85':'CE', '86':'PI', '87':'PE', '88':'CE', '89':'PI', '91':'PA', '92':'AM', '93':'PA', '94':'PA', '95':'RR', '96':'AP', '97':'AM', '98':'MA', '99':'MA'}
siglas_estados = {'AC':'Acre', 'AL':'Alagoas', 'AP':'Amapá', 'AM':'Amazonas', 'BA':'Bahia', 'CE':'Ceará', 'DF':'Distrito Federal', 'ES':'Espírito Santo', 'GO':'Goiás', 'MA':'Maranhão', 'MT':'Mato Grosso', 'MS':'Mato Grosso Do Sul', 'MG':'Minas Gerais', 'PA':'Pará', 'PB':'Paraíba', 'PR':'Paraná', 'PE':'Pernambuco', 'PI':'Piauí', 'RJ':'Rio de Janeiro', 'RN':'Rio Grande Do Norte', 'RS':'Rio Grande Do Sul', 'RO':'Rondônia', 'RR':'Roraima', 'SC':'Santa Catarina', 'SP':'São Paulo', 'SE':'Sergipe', 'TO':'Tocantins'}

def ddd_query():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;32m~#\033[1;36m Informe o DDD a ser consultado\n➤➤➤\033[0;37m ').strip().replace('0', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if read_input('empty', input_user): continue
            if read_input('numeric', input_user) != True: continue
            if len(input_user) != 2:
                print('\033[1;33m O cep é formado por 2 digitos númerico!')
                time.sleep(2)
                continue
            break
        req = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{input_user}').json()
        print('\033[1;34m'+ '─' * 44)
        for i in req.keys():
            print(f'\033[1;33m• {i.capitalize(): <8} \033[0;37m▸ {str(req[i]).replace("'", '').replace('[', '').replace(']', '')}')
            time.sleep(0.01)
        if return_menu(): return True

if __name__ == '__main__':
    try: ddd_query()
    except: exiting

# DDD: 11
