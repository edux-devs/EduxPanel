#!/usr/bin/env python3
import os 
import functions.banner
import functions.menu #type:ignore

os.system('cls' if os.name == 'nt' else 'clear')
functions.banner
functions.menu
input_user = input("   >_Digite a opção: ")
