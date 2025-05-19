import requests
import os
from hashtable import HashTable

URL = "https://www.celotajs.lv/lv/c/wrth" #Konstants, NEAIZTIKT

url = URL

state = 'main'
running = True

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clearTerminal()
while(running):
    match (state):
        case 'main':
            print('Meklēt\nNesen skatīti\nFavorīti\nBeidzēt')
            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match (userInput):
                case 1:
                    state = 'search'
                    clearTerminal()
                case 2:
                    state = 'recent'
                    clearTerminal()
                case 3:
                    state = 'favorites'
                    clearTerminal()
                case 4:
                    state = 'stop'
                    clearTerminal()
                case _:
                    clearTerminal()

        case 'search':
            print('Dabas objekti\nBaltijas kult\nKulturas zīme\nAtpakaļ')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")
            
            match(userInput):
                case 1:
                    state = 'nature'
                    clearTerminal()
                case 2:
                    state = 'culture'
                    clearTerminal()
                case 3:
                    state = 'heritage'
                    url = url+ f'/{state}'
                    clearTerminal()
                case 4: 
                    state = 'main'
                    clearTerminal()
                case _:
                    clearTerminal()
                    
        case 'nature':
            print('Dabas vērošas vietas\nDabas pieminekļi\nDabas teritoriajs\nDabas parki, dārzi un dendrāji\natpakal')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")
            
            match(userInput):
                case 1:
                    state = 'nature/observation'
                    clearTerminal()
                case 2:
                    state = 'nature/sights'
                    clearTerminal()
                case 3:
                    state = 'nature/natural/areas'
                    
                    clearTerminal()
                case 4:
                    state = 'nature/parks'
                    url = url + f'/{state}'
                    clearTerminal()
                case 5: 
                    state = 'search'
                    clearTerminal()
                case _:
                    clearTerminal()
        case 'recent': 
            #display the stack ;d
            pass
        
        case 'favorite':
            #dosplay the linked list ;d
            pass

        case 'stop':
            running = False