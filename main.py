import requests
from bs4 import BeautifulSoup
import os
import re
from destination import Destination
from hashtable import HashTable
from stack import FixedSizeStack


URL = "https://www.celotajs.lv/lv/" #Konstants, NEAIZTIKT

state = 'main'
previousState = ''
running = True
destinationHT = HashTable(20)
history = FixedSizeStack(5)

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clearTerminal()
while(running):
    match (state):
        #######################
        #      MAIN MENU      #
        #######################
        case 'main':
            print('1) Meklēt\n2) Nesen skatītie\n3) Favorīti\n4) Favorīti\n5) Iziet')
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
                    previousState = state
                    state = 'about'
                    clearTerminal()
                case 5:
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
                    url = URL + f'c/wrth/{state}/parks'
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
                    url = URL + f'c/wrth/{state}/trails'
                    state = 'searching'
                    clearTerminal()

                case 2:
                    previousState = state
                    url = URL + f'c/wrth/{state}/watchtower'
                    state = 'searching'
                    clearTerminal()

                case 3:
                    previousState = state
                    url = URL + f'c/wrth/{state}/places'
                    state = 'searching'
                    clearTerminal()

                case 4:
                    previousState = state
                    url = URL + f'c/wrth/{state}/animals'
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
                    url = URL + f'c/wrth/{state}/rocks'
                    state = 'searching'
                    clearTerminal()
                case 2:
                    previousState = state
                    url = URL + f'c/wrth/{state}/outcrops'
                    state = 'searching'
                    clearTerminal()
                case 3:
                    previousState = state
                    url = URL + f'c/wrth/{state}/springs'
                    state = 'searching'
                    clearTerminal()
                case 4:
                    previousState = state
                    url = URL + f'c/wrth/{state}/sinkholes'
                    state = 'searching'
                    clearTerminal()
                case 5:
                    previousState = state
                    url = URL + f'c/wrth/{state}/dunes'
                    state = 'searching'
                    clearTerminal()
                case 6:
                    previousState = state
                    url = URL + f'c/wrth/{state}/trees'
                    state = 'searching'
                    clearTerminal()
                case 7:
                    previousState = state
                    url = URL + f'c/wrth/{state}/waterfall'
                    state = 'searching'
                    clearTerminal()
                case 8:
                    previousState = state
                    url = URL + f'c/wrth/{state}/relief'
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
                    url = URL+f'c/wrth/{state}/lakes'
                    state = 'searching'
                    clearTerminal()
                case 2:
                    previousState = state
                    url = URL+f'c/wrth/{state}/seaside'
                    state = 'searching'
                    clearTerminal()
                case 3:
                    previousState = state
                    url = URL+f'c/wrth/{state}/forests'
                    state = 'searching'
                    clearTerminal()
                case 4:
                    previousState = state
                    url = URL+f'c/wrth/{state}/swamps'
                    state = 'searching'
                    clearTerminal()
                case 5:
                    previousState = state
                    url = URL+f'c/wrth/{state}/meadows'
                    state = 'searching'
                    clearTerminal()
                case 6:
                    previousState = state
                    url = URL+f'c/wrth/{state}/islands'
                    state = 'searching'
                    clearTerminal()
                case 7:
                    previousState = state
                    url = URL+f'c/wrth/{state}/rivers'
                    state = 'searching'
                    clearTerminal()
                case 8:
                    previousState = state
                    url = URL+f'c/wrth/{state}/territory'
                    state = 'searching'
                    clearTerminal()
                case 9:
                    previousState = state
                    url = URL+f'c/wrth/{state}/biotope'
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
                    url = URL + f'c/wrth/{state}/historical/sites'
                    state = 'searching'
                    clearTerminal()
                case 2:
                    previousState = state
                    url = URL + f'c/wrth/{state}/centre'
                    state = 'searching'
                    clearTerminal()
                case 3:
                    previousState = state
                    url = URL + f'c/wrth/{state}/castles/manors'
                    state = 'searching'
                    clearTerminal()
                case 4:
                    previousState = state
                    url = URL + f'c/wrth/{state}/churches'
                    state = 'searching'
                    clearTerminal()
                case 5:
                    previousState = state
                    url = URL + f'c/wrth/{state}/museums'
                    state = 'searching'
                    clearTerminal()
                case 6:
                    previousState = state
                    url = URL + f'c/wrth/{state}/remarkable/building'
                    state = 'searching'
                    clearTerminal()
                case 7:
                    previousState = state
                    url = URL + f'c/wrth/{state}/industrial'
                    state = 'searching'
                    clearTerminal()
                case 8:
                    previousState = state
                    url = URL + f'c/wrth/{state}/cognition'
                    state = 'searching'
                    clearTerminal()
                case 9:
                    previousState = state
                    url = URL + f'c/wrth/{state}/memorial'
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
            page = requests.get(url)
            if page.status_code == 200:
                print("Connected")
                page_contents = BeautifulSoup(page.content, "html.parser")
                celojumi = page_contents.find_all('tr', class_=['even','odd'])
                
                for section in celojumi:
                    for tag in section.find_all('td', class_="minimalCol alignCeter"):
                        tag.decompose()
                    for tag in section.find_all('div', style=['margin-top: .5em; margin-bottom: .2em;', 'margin-top: 5px; float: right; text-align: center;']):
                        tag.decompose()
                    for tag in section.find_all('div', class_='dotdotdot-txt'):
                        tag.decompose()
                        
                    for tag in section.find_all('div'):
                        a_tag = tag.find('a', href=True)
                        if a_tag:
                            url = a_tag['href']
                        div = tag.find('div', style="float: left;")
                        if div:
                            country = div.get_text(strip=True)
                        h3 = tag.find('h3')
                        if h3:
                            nosaukums = h3.get_text(strip=True)
                        newDest = Destination('/'+re.sub(r'(\.\./)+', '', url), country, nosaukums, 0)
                        destinationHT.add(newDest.url, newDest)
                    
            randomDest = destinationHT.randomElement()
            print(str(randomDest))
            history.push(randomDest)
            input()
            state = previousState
            clearTerminal()
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

        case 'about':
            print('Daniels Millers\t241RDB218\nToms Graudums\t241RDB237\nElīza Anna Jansone\t241RDB013\nLai aizietu atpakaļ uzspiediet jebkuru pogu!')
            input()
            state = previousState

        case 'stop':
            running = False