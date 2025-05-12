Source website: https://www.celotajs.lv/lv/c/wrth

Izmantojot 'requests' bibliotēku mēs savienojamies ar šo mājas lapu.  
No tās mēs savācam *linkus* uz pieejamajām kategorijām.  
No šīm kategorijām mēs dabujam galamērķus.  
Galamērķus mēs varam pārveidot par objektiem 'destination', kas varētu izskatīties šādi:  

- url - saite uz galamērķa mājaslapu 
- name - norāda galamērķa nosaukumu  
- country - norāda kurā valstī tas atrodas  
- categories[] - masīvs ar visām kategorijām, kur šis galamērķis ietilpts  

Datus mēs uzglabāsim HashTable struktūrās. Galapunktu_HT un Kategoriju_HT.  
Galapunkts_HT mēs saglabāsim visus 'destination' objektus un kā atslēgu priekš šī HashTable mēs izmantosism URL.  
Kategorija_HT mēs saglabāsim atsauces uz visiem objektiem, kas ir sastopami kādā kategorijā. Šim kā atslēgas mēs izmantosim kategorijas nosaukumu.  
Mēs varētu arī uztaisīt 'favorite' vai  'stared' sekciju, kas varētu būt LinkedList vai Doubly LinkedList, kur lietotājs var pievienot galamērķi.  
Also varam izmantot Stack priekš 'nesen skatītie' sekcijas.  

Lai nevajadzētu visu to uzturēt RAM atmiņā, mēs varam to izvadīt failā. Tas mums arī dotu iespēju saglabāt lietotāja datus.

Ja jums ir vēl kāda idea, droši sakat.

