#!/usr/bin/env python3
#Autor: Eduardo

try: from banner import banner
except: from functions.banner import banner #type:ignore

def exiting():
    banner()
    print('\033[1;34m Agradeço por usar EduxPanel\n Até a próxima!')
    exit()

if __name__ == '__main__':
    exiting()