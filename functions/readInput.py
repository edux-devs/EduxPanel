#!/usr/bin/env python
#Autor: Eduardo

import time
import re
import sys

def readInput(typ: str, x: str) -> bool:
    typ = typ.lower()
    match typ:
        case 'numeric':
            if x.isnumeric():
                return True
            print('\033[1;33m[!] Digite apenas números!\033[0m')

        case 'isalpha':
            if x.isalpha():
                return True
            print('\033[1;33m[!] Digite apenas letras!\033[0m')

        case 'isalnum':
            if x.isalnum():
                return True
            print('\033[1;33m[!] Digite apenas letras e números!\033[0m')

        case 'empty':
            if not x.strip():
                print('\033[1;33m[!] Digite alguma coisa!\033[0m')
                return True
            return False

        case 'instagram_user':
            if re.fullmatch(r"(?!.*\.\.)(?!\.)[a-zA-Z0-9._]{1,30}(?<!\.)", x):
                return True
            print('\033[1;33m[!] Username inválido. Use apenas letras, números, pontos ou underline. Máx 30 caracteres.\033[0m')

        case 'instagram_id':
            if x.isdigit() and 6 < len(x) < 25:  # IDs costumam ter mais de 6 e menos de 25 dígitos
                return True
            print('\033[1;33m[!] ID inválido. Deve conter apenas números.\033[0m')

        case _:
            print(f'\033[1;31m[!] Tipo de validação desconhecido: {typ}\033[0m')

    time.sleep(2)
    return False

if __name__ == '__main__':
    if len(sys.argv) > 2:
        if readInput(sys.argv[1], sys.argv[2]):
            print('True')
        else:
            print('Falsen')
    else:
        print('./readInput type $variavel')