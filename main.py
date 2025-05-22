import requests
from bs4 import BeautifulSoup
import os
import re
from destination import Destination
from hashtable import HashTable
from stack import FixedSizeStack
from linkedlist import LinkedList


URL = "https://www.celotajs.lv/lv/" #Konstants, NEAIZTIKT

if not os.path.exists("saveData"):
    os.makedirs("saveData")

stack_path = os.path.join("saveData", "stack")
list_path = os.path.join("saveData", "linkedList")

if os.path.isfile(stack_path):
    history = FixedSizeStack.load(stack_path)
else:
    history = FixedSizeStack(6)

if os.path.isfile(stack_path):
    favourite = LinkedList.load(list_path)
else:
    favourite = LinkedList()

state = 'main'
previousState = ''
running = True
destinationHT = HashTable(20)

firstloop= True
repick = False

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clearTerminal()
while(running):
    match (state):
        #######################
        #      MAIN MENU      #
        #######################
        case 'main':
            print('1) Meklēt\n2) Nesen skatītie\n3) Favorīti\n4) Par izstrādātājiem\n5) Iziet')
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
                    url = URL + f'c/wrth/heritage'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    

                case 4: 
                    state = 'main'
                    clearTerminal()

                case _:
                    clearTerminal()

        #######################
        #     NATURE MENU     #
        #######################         
        case 'nature':
            print('1) Dabas vērošanas vietas\n2) Dabas pieminekļi\n3) Dabas teritorijas\n4) Dabas parki, dārzi un dendrāji\n5) Atpakaļ')

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
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    

                case 5: 
                    state = 'search'
                    clearTerminal()

                case _:
                    clearTerminal()
        
        case 'nature/observation':
            print('1) Dabas takas\n2) Skatu torņi\n3) Skatu vietas\n4) Dzīvnieku, putnu un augu vērošanas vietas\n5) Atpakaļ')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    url = URL + f'c/wrth/{state}/trails'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    

                case 2:
                    previousState = state
                    url = URL + f'c/wrth/{state}/watchtower'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    

                case 3:
                    previousState = state
                    url = URL + f'c/wrth/{state}/places'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    

                case 4:
                    previousState = state
                    url = URL + f'c/wrth/{state}/animals'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    

                case 5:
                    state = 'nature'
                    clearTerminal()

                case _:
                    clearTerminal()

        case 'nature/sights':
            print('1) Akmeņi\n2) Atsegumi\n3) Avoti\n4) Karsta kritenes\n5) Kāpas\n6) Koki\n7) Ūdenskritumi\n8) Reljefa fromas\n9) Atpakaļ')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    url = URL + f'c/wrth/{state}/rocks'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 2:
                    previousState = state
                    url = URL + f'c/wrth/{state}/outcrops'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 3:
                    previousState = state
                    url = URL + f'c/wrth/{state}/springs'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 4:
                    previousState = state
                    url = URL + f'c/wrth/{state}/sinkholes'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 5:
                    previousState = state
                    url = URL + f'c/wrth/{state}/dunes'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 6:
                    previousState = state
                    url = URL + f'c/wrth/{state}/trees'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 7:
                    previousState = state
                    url = URL + f'c/wrth/{state}/waterfall'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 8:
                    previousState = state
                    url = URL + f'c/wrth/{state}/relief'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 9:
                    state = 'nature'
                    clearTerminal()
                case _:
                    clearTerminal()


        case 'nature/natural/areas':
            print('1) Ezeri\n2) Jūras krasta posms\n3) Meži\n4) Purvi\n5) Pļavas\n6) Salas\n7) Upes\n8) Citas dabas teritorijas\n9) Biotopi\n10) Atpakaļ')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")

            match(userInput):
                case 1:
                    previousState = state
                    url = URL+f'c/wrth/{state}/lakes'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 2:
                    previousState = state
                    url = URL+f'c/wrth/{state}/seaside'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 3:
                    previousState = state
                    url = URL+f'c/wrth/{state}/forests'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 4:
                    previousState = state
                    url = URL+f'c/wrth/{state}/swamps'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 5:
                    previousState = state
                    url = URL+f'c/wrth/{state}/meadows'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 6:
                    previousState = state
                    url = URL+f'c/wrth/{state}/islands'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 7:
                    previousState = state
                    url = URL+f'c/wrth/{state}/rivers'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 8:
                    previousState = state
                    url = URL+f'c/wrth/{state}/territory'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                case 9:
                    previousState = state
                    url = URL+f'c/wrth/{state}/biotope'
                    clearTerminal()
                    print("Savienojas...")
                    firstloop = True
                    state = 'searching'
                    
                case 10:
                    state = 'nature'
                    clearTerminal()
                case _:
                    clearTerminal()


        #######################
        #    CULTURE MENU     #
        #######################
        case 'culture':
            print('1) Senās vēsturiskās vietas\n2) Vēsturiskie un mūsdienu centri\n3) Pilis un muižas\n4) Baznīcas\n5) Muzeji\n6) Ievērojamas celtnes\n7) Industriālais mantojums\n8) Izziņas vietas\n9) Piemiņas vietas\n10) Atpakaļ')

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
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 2:
                    previousState = state
                    url = URL + f'c/wrth/{state}/centre'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 3:
                    previousState = state
                    url = URL + f'c/wrth/{state}/castles/manors'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 4:
                    previousState = state
                    url = URL + f'c/wrth/{state}/churches'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 5:
                    previousState = state
                    url = URL + f'c/wrth/{state}/museums'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 6:
                    previousState = state
                    url = URL + f'c/wrth/{state}/remarkable/building'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 7:
                    previousState = state
                    url = URL + f'c/wrth/{state}/industrial'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 8:
                    previousState = state
                    url = URL + f'c/wrth/{state}/cognition'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
                    clearTerminal()
                case 9:
                    previousState = state
                    url = URL + f'c/wrth/{state}/memorial'
                    state = 'searching'
                    print("Savienojas...")
                    firstloop = True
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
            if firstloop:
                destinationHT.clear()
                try: 
                    page = requests.get(url)
                except requests.exceptions.Timeout:
                    print("Lapa pašlaik nav sasniedzama!")
                    print('Lai aizietu atpakaļ uzspiediet jebkuru pogu!')
                    input()
                    state = previousState

                if page.status_code == 200:
                    print("Apstrādā datus...")
                    page_contents = BeautifulSoup(page.content, "html.parser")
                    celojumi = page_contents.find_all('tr', class_=['even','odd'])

                    for section in celojumi:
                        for tag in section.find_all('td', class_="minimalCol alignCenter"):
                            tag.decompose()
                        for tag in section.find_all('div', style=['margin-top: .5em; margin-bottom: .2em;', 'margin-top: 5px; float: right; text-align: center;']):
                            tag.decompose()
                        for tag in section.find_all('div', class_='dotdotdot-txt'):
                            tag.decompose()

                        for tag in section.find_all('div'):
                            a_tag = tag.find('a', href=True)
                            if a_tag:
                                Desturl = a_tag['href']
                            div = tag.find('div', style="float: left;")
                            if div:
                                Destcountry = div.get_text(strip=True)
                            h3 = tag.find('h3')
                            if h3:
                                Destnosaukums = h3.get_text(strip=True)
                            newDest = Destination(URL +re.sub(r'(\.\./)+', '', Desturl), Destnosaukums, Destcountry)
                            destinationHT.add(newDest.url, newDest)
                repick = True
                firstloop = False
                clearTerminal()
            if repick:
                randomDest = destinationHT.randomElement()
                history.push(randomDest)
                repick = False
            print(str(randomDest))
            print('1) Pievienot favorītiem\n2) Cits galamērķis\n3) Atpakaļ')

            userInput = 0
            try:
                userInput = int(input())
            
            except (ValueError):
                print("notika kļūda, lūdzu ievadiet atkal\n")
            match (userInput):
                case 1:
                    if favourite.contains(randomDest):
                        clearTerminal()
                        print('Jau tika pievienots!')
                        continue
                    favourite.append(randomDest)
                    clearTerminal()
                    print('Pievienots favorītiem!')

                case 2:
                    repick = True
                    clearTerminal()
                    pass
                case 3:
                    state = previousState
                    clearTerminal()
                case _:
                    clearTerminal()
        case 'recent': 
            if history.is_empty():
                print("Nav iepriekš skatīti galamērķu!")
            else: 
                print(history)
            print('Lai aizietu atpakaļ uzspiediet jebkuru pogu!')
            input()
            state = previousState
            clearTerminal()
        
        case 'favorites':
            if favourite.empty():
                print("Nav neviena favorīta!")
            else:
                print(favourite)
            print('Lai aizietu atpakaļ uzspiediet jebkuru pogu!')
            input()
            state = previousState
            clearTerminal()
            
        case 'about':
            print('Daniels Millers\t\t241RDB218\nElīza Anna Jansone\t241RDB013\nToms Graudums\t\t241RDB237\nLai aizietu atpakaļ uzspiediet jebkuru pogu!')
            input()
            clearTerminal()
            state = previousState

        case 'stop':
            history.save(stack_path)
            favourite.save(list_path)
            running = False