# Ceļotājs CLI

## Par Projektu
Šis projekts ir CLI rīks, kas ļauj atrast nejaušu ceļojumu vietu Latvijas, Lietuvas un Igaunijas teritorijās.  
Ceļojuma galamērķi tiek ievākti no mājaslapas [ceļotājs.lv](https://www.celotajs.lv/lv/c/wrth), apstrādāti un izvadīti lietotāja terminālī.  
Lietotājs spēj izvēlēties kategorijas ar dažādiem apskates objektiem, un programma izvēlās nejaušu galamērķi no lietotāja izvēlētās kategorijas.
## Instalācijas pamācība
Lai varētu izmantot šo rīku, ir nepieciešamas:  
### Rīka pirmkods
Tas ir pieejams šajā GitHub repozitorijā. To var lejupielādēt kā `.zip` failu, vai noklonēt ar `https://github.com/millers-daniels-241RDB218/DatuStrukturuProjekts.git` komandu terminālī.
### Python versija, kas ir virs 3.10
Tā kā rīks izmanto `match` operatoru, kas tika pievienots 3.10 versijā. To var iegūt [šeit](https://www.python.org/)
### `requests` bibliotēka
Tā kā rīks sazinās ar internetu, ir nepieciešama šī bibliotēka.  
Lai to ieinstalētu, savā terminālī ieraksti:  
`pip install requests`
### `beautifulsoup4` bibliotēka
Tā kā tiek ievākts liels datu apjoms no mājaslapas `HTML` formā, lai to apstrādātu tiek izmantota bibliotēka `beautifulsoup4`.
Lai to ieinstalētu, savā terminālī ieraksti:  
`pip install beautifulsoup4`
### Rīka palaišana
Lai palaistu rīku, sava terminālī, kura ceļš ir rīka pirmkoda direktoriju, uz veikt komandu:  
`python ./main.py`
## Izmantotās datu struktūras
### Node:
**Node** implementācija ir ierakstā 'Node' objekta implementācija, kas sastāv no `value` un `next` laukiem, kas tiek izmantots `Stack` un `LinkedList` implementācijās.
Kā arī ir **NodeHT** implementācija, ar papildus lauku `key`, kas ir nepieciešams, lai mēs varētu izveidot `HashTable` struktūru.  
Šī implementācija ir atrodama `node.py` failā.
### Stack:
`Stack` tiek izmantots nesen skatīto objektu uzglabāšanai.
`stack.py` ir gan parasta `Stack`, gan ierobežota izmēra `FixedSizeStack` implementācija. 
`Stack` implementācijas ir atrodamas `stack.py` failā. 
### LinkedList:
`LinkedList` tiek izmantots sadaļā `Favorīti`, kur lietājs var saglabāt sevi interesējošos galapunktus.  
`LinkedList` implementācija ir atrodama `linkedlist.py` failā.
### HashTable:
`HashTable` tiek izmantots `Destination` objektu uzglabāšanai vienviet atmiņā.
Tas ir implementēts izmantojot `NodeHT` objektus.
`HashTable` implementācija ir atrodama `hashtable.py` failā
### Destination:
Šis ir mūsu pašveidots objekts, galapunktu uzglabāšanai un apstrādei.  
Šim objektam ir lauki:  
`url`, kas satur saiti uz noteikto galapunktu.  
`name`, kas satur galapunkta nosaukumu.  
`country`, kas satur galapunkta atrašanās valsti.  
Šis ir viens no galvenajiem objektiem, kas tiek izmantoti mūsu projektā.



## Izstrādātāji
[Elīza Anna Jansone - 241RDB013](https://github.com/ElizaAnna)  
[Daniels Millers - 241RDB218](https://github.com/millers-daniels-241RDB218)  
[Toms Graudums - 241RDB237](https://github.com/mmm-jogurts)   


