#Riccardo Giacalone
#10/05/2024
import copy
"""
Scrivi una funzione che determina se un numero è 'magico'. 
Un numero è considerato magico se è divisibile per 4 ma non per 6.
"""
def numero_magico(num: int) -> bool:
    # cancella pass e scrivi il tuo codice
    if num % 4 == 0 and num % 6 != 0:
        return True
    return False

print("--------------------------")

"""
Scrivi una funzione che prenda un dizionario e un valore, e 
ritorni la prima chiave che corrisponde a quel valore, 
o None se il valore non è presente.
"""
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    # cancella pass e scrivi il tuo codice
    for key in dizionario:
        if dizionario[key] == valore:
            return key
        
print("--------------------------")

"""
Scrivi una funzione che elimini dalla lista dati certi elementi specificati 
in un dizionario. Il dizionario contiene elementi da rimuovere come 
chiavi e il numero di volte che devono essere rimossi come valori.
"""
def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    # cancella pass e scrivi il tuo codice
    for key in da_rimuovere:
        for i in lista:
            if key == i:
                while da_rimuovere[key]!= 0:
                    lista.remove(i)
                    da_rimuovere[key] -= 1
    return lista

print("--------------------------")

"""
Scrivi una funzione che prenda in input una lista di dizionari che 
rappresentano voti di studenti e aggrega i voti per studente in 
un nuovo dizionario.
"""
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    # cancella pass e scrivi il tuo codice
    new_dict : dict = {}
    
    for s in voti:
        nome = s["name"]
        voto = s["voto"]
        
        if nome in new_dict:
            new_dict[nome].append(voto)
        else:
            new_dict[nome] = [voto]  # ---> inizia a creare una lista se non è presente il nome in new dict

    return new_dict

"""
Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e 
restituisca un nuovo dizionario con solo i prodotti che hanno un 
prezzo superiore a 20, scontati del 10%
""" 
def filtra_e_mappa(prodotti: dict[str:float]) -> list[str:float]:
    # cancella pass e scrivi il tuo codice
    new_prodotti : dict = copy.copy(prodotti)
    
    for key in prodotti:

        if prodotti[key] < 20:
            new_prodotti.pop(key)
        else:
            new_prodotti[key] = new_prodotti[key] - (new_prodotti[key] * 10) / 100 

    return new_prodotti

print("--------------------------")

"""

PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, 
e-mail (facoltativo) e numero di telefono (facoltativo). 
La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il 
dizionario creato, il nome e cognome del contatto da aggiornare, 
e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe 
aggiornare il dizionario del contatto.

"""
def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    contatti: dict = {}
    contatti["nome"] = name
    contatti["email"] = email
    contatti["telefono"] = telefono
    return contatti



def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    # cancella pass e scrivi il tuo codice
    dictionary["nome"] = name
    if email != None:
        dictionary["email"] = email
    if telefono != None:
        dictionary["telefono"] = telefono
    return dictionary

contact = create_contact("Mario", email="mario@gmail.com",telefono=422424)
print(contact)
print(update_contact(contact,"Mario Rossi", telefono=4141222222))
        
        

    


    

        

            

        

        


        
            

