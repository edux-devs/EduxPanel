#!/usr/bin/env python3
#Autor: Eduardo

try:
    from clear import clear
    from banner import banner
    from menu import menu
except:
    from functions.clear import clear #type:ignore
    from functions.banner import banner #type:ignore
    from functions.menu import menu #type:ignore

def bannerMenu():
    clear()
    banner()
    menu()

if __name__ == '__main__':
    bannerMenu()
