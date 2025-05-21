import requests
import os
from hashtable import HashTable
from stack import Stack

URL = "https://www.celotajs.lv/lv/c/wrth" #Konstants, NEAIZTIKT

url = URL

state = 'main'
previousState = ''
running = True
history = Stack()

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clearTerminal()
while(running):
    match (state):
        #######################
        #      MAIN MENU      #
        #######################
        case 'main':
            print('1) Meklēt\n2) Nesen skatītie\n3) Favorīti\n4) Iziet')
            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")
            

            match (userInput):
                case 1:
                    previousState = state
                    state = 'search'
                    clearTerminal()
                case 2:
                    previousState = state
                    state = 'recent'
                    clearTerminal()
                case 3:
                    previousState = state
                    state = 'favorites'
                    clearTerminal()
                case 4:
                    state = 'stop'
                    clearTerminal()
                case _:
                    clearTerminal()

        #######################
        #     SEARCH MENU     #
        #######################
        case 'search':
            print('1) Dabas objekti\n2) Baltijas kultūra\n3) Kulturas zīme "Latvijas mantojums"\n4) Atpakaļ')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    state = 'nature'
                    clearTerminal()

                case 2:
                    previousState = state
                    state = 'culture'
                    clearTerminal()

                case 3:
                    previousState = state
                    url = url+ f'/{state}/heritage'
                    state = 'searching'
                    clearTerminal()

                case 4: 
                    state = 'main'
                    clearTerminal()

                case _:
                    clearTerminal()

        #######################
        #     NATURE MENU     #
        #######################         
        case 'nature':
            print('1) Dabas vērošanas vietas\n2) Dabas pieminekļi\n3) Dabas teritorijas\n4) Dabas parki, dārzi un dendrāji\n5) Atpakal')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    state = 'nature/observation'
                    clearTerminal()

                case 2:
                    previousState = state
                    state = 'nature/sights'
                    clearTerminal()

                case 3:
                    previousState = state
                    state = 'nature/natural/areas'
                    clearTerminal()

                case 4:
                    previousState = state
                    url = url + f'/{state}/parks'
                    state = 'searching'
                    clearTerminal()

                case 5: 
                    state = 'search'
                    clearTerminal()

                case _:
                    clearTerminal()
        
        case 'nature/observation':
            print('1) Dabas takas\n2) Skatu torņi\n3) Skatu vietas\n4) Dzīvnieku, putnu un augu vērošanas vietas\n5) Atpakal')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    url = url + f'/{state}/trials'
                    state = 'searching'
                    clearTerminal()

                case 2:
                    previousState = state
                    url = url + f'/{state}/watchtower'
                    state = 'searching'
                    clearTerminal()

                case 3:
                    previousState = state
                    url = url + f'/{state}/places'
                    state = 'searching'
                    clearTerminal()

                case 4:
                    previousState = state
                    url = url + f'/{state}/animals'
                    state = 'searching'
                    clearTerminal()

                case 5:
                    state = 'nature'
                    clearTerminal()

                case _:
                    clearTerminal()

        case 'nature/sights':
            print('1) Akmeņi\n2) Atsegumi\n3) Avoti\n4) Karsta kritenes\n5) Kāpas\n6) Koki\n7) Ūdenskritumi\n8) Reljefa fromas\n9) Atpakal')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    url = URL + f'/{state}/rocks'
                    state = 'searching'
                    clearTerminal()
                case 2:
                    previousState = state
                    url = URL + f'/{state}/outcrops'
                    state = 'searching'
                    clearTerminal()
                case 3:
                    previousState = state
                    url = URL + f'/{state}/springs'
                    state = 'searching'
                    clearTerminal()
                case 4:
                    previousState = state
                    url = URL + f'/{state}/sinkholes'
                    state = 'searching'
                    clearTerminal()
                case 5:
                    previousState = state
                    url = URL + f'/{state}/dunes'
                    state = 'searching'
                    clearTerminal()
                case 6:
                    previousState = state
                    url = URL + f'/{state}/trees'
                    state = 'searching'
                    clearTerminal()
                case 7:
                    previousState = state
                    url = URL + f'/{state}/waterfalls'
                    state = 'searching'
                    clearTerminal()
                case 8:
                    previousState = state
                    url = URL + f'/{state}/relief'
                    state = 'searching'
                    clearTerminal()
                case 9:
                    state = 'nature'
                    clearTerminal()
                case _:
                    clearTerminal()


        case 'nature/natural/areas':
            print('1) Ezeri\n2) Jūras krasta posms\n3) Meži\n4) Purvi\n5) Pļavas\n6) Salas\n7) Upes\n8) Citas dabas teritorijas\n9) Biotopi\n10) Atpakal')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    url = URL+f'/{state}/lakes'
                    state = 'searching'
                    clearTerminal()
                case 2:
                    previousState = state
                    url = URL+f'/{state}/seaside'
                    state = 'searching'
                    clearTerminal()
                case 3:
                    previousState = state
                    url = URL+f'/{state}/forests'
                    state = 'searching'
                    clearTerminal()
                case 4:
                    previousState = state
                    url = URL+f'/{state}/swamps'
                    state = 'searching'
                    clearTerminal()
                case 5:
                    previousState = state
                    url = URL+f'/{state}/meadows'
                    state = 'searching'
                    clearTerminal()
                case 6:
                    previousState = state
                    url = URL+f'/{state}/islands'
                    state = 'searching'
                    clearTerminal()
                case 7:
                    previousState = state
                    url = URL+f'/{state}/rivers'
                    state = 'searching'
                    clearTerminal()
                case 8:
                    previousState = state
                    url = URL+f'/{state}/territory'
                    state = 'searching'
                    clearTerminal()
                case 9:
                    previousState = state
                    url = URL+f'/{state}/biotope'
                    state = 'searching'
                    clearTerminal()
                case 10:
                    state = 'nature'
                    clearTerminal()
                case _:
                    clearTerminal()


        #######################
        #    CULTURE MENU     #
        #######################
        case 'culture':
            print('1) Senās vēsturiskās vietas\n2) Vēsturiskie un mūsdienu centri\n3) Pilis un muižas\n4) Baznīcas\n5) Muzeji\n6) Ievērojamas celtnes\n7) Industriālais mantojums\n8) Izziņas vietas\n9) Piemiņas vietas\n10) Atpakal')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")
            
            match (userInput):
                case 1:
                    previousState = state
                    url = URL + f'/{state}/historical/sites'
                    state = 'searching'
                    clearTerminal()
                case 2:
                    previousState = state
                    url = URL + f'/{state}/centre'
                    state = 'searching'
                    clearTerminal()
                case 3:
                    previousState = state
                    url = URL + f'/{state}/castles/manors'
                    state = 'searching'
                    clearTerminal()
                case 4:
                    previousState = state
                    url = URL + f'/{state}/churches'
                    state = 'searching'
                    clearTerminal()
                case 5:
                    previousState = state
                    url = URL + f'/{state}/museums'
                    state = 'searching'
                    clearTerminal()
                case 6:
                    previousState = state
                    url = URL + f'/{state}/remarkable/building'
                    state = 'searching'
                    clearTerminal()
                case 7:
                    previousState = state
                    url = URL + f'/{state}/industrial'
                    state = 'searching'
                    clearTerminal()
                case 8:
                    previousState = state
                    url = URL + f'/{state}/cognition'
                    state = 'searching'
                    clearTerminal()
                case 9:
                    previousState = state
                    url = URL + f'/{state}/memorial'
                    state = 'searching'
                    clearTerminal()
                case 10:
                    state = 'search'
                    clearTerminal()
                case _:
                    clearTerminal()

        #######################
        #     OTHER MENUs     #
        #######################
        case 'searching':
            #you do the requesst thingy
            state = previousState
            pass
        case 'recent': 
            #Have the screen display the contents of the stack
            #Have options for:
            #Atpakaļ
            #un atkal iereakstot skaitli, lai displayo to galamērķi...
            pass
        
        case 'favorite':
            #dosplay the linked list ;d
            #tas pats, kas stack, burtiski
            pass

        case 'stop':
            running = False