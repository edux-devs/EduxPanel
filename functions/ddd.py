import time
import requests

try:
    from banner import banner
    from readInput import readInput #type:ignore
    from returnMenu import returnMenu
except:
    from functions.banner import banner #type:ignore
    from functions.readInput import readInput #type:ignore
    from functions.returnMenu import returnMenu #type:ignore

ddd_siglas = {'11':'SP', '12':'SP', '13':'SP', '14':'SP', '15':'SP', '16':'SP', '17':'SP', '18':'SP', '19':'SP', '21':'RJ', '22':'RJ', '24':'RJ', '27':'ES', '28':'ES', '31':'MG', '32':'MG', '33':'MG', '34':'MG', '35':'MG', '37':'MG', '38':'MG', '41':'PR', '42':'PR', '43':'PR', '44':'PR', '45':'PR', '46':'PR', '47':'SC', '48':'SC', '49':'SC', '51':'RS', '53':'RS', '54':'RS', '55':'RS', '61':'DF', '62':'GO', '63':'TO', '64':'GO', '65':'MT', '66':'MT', '67':'MS', '68':'AC', '69':'RO', '71':'BA', '73':'BA', '74':'BA', '75':'BA', '77':'BA', '79':'SE', '81':'PE', '82':'AL', '83':'PB', '84':'RN', '85':'CE', '86':'PI', '87':'PE', '88':'CE', '89':'PI', '91':'PA', '92':'AM', '93':'PA', '94':'PA', '95':'RR', '96':'AP', '97':'AM', '98':'MA', '99':'MA'}

def ddd():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m ~ $ Informe o DDD para a consulta ⎇\033[1;36m ').strip().replace('0', '')
            if input_user.lower() in ['99', 'q']: return True
            if readInput('empty', input_user): continue
            if readInput('numeric', input_user) != True: continue
            if len(input_user) != 2:
                print('\033[1;33m O número não corresponde ao um DDD existente!')
                time.sleep(2)
                continue
            break
        req = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <6}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if returnMenu() == True: return True

if __name__ == '__main__':
    ddd()