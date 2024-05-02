#Riccardo Giacalone
#Esercizi riepilogativi (quiz)
import copy
"""
La funzione dovrebbe determinare se un elemento è presente in una lista.
Un errore nell'implementazione porta a risultati inaspettati.
"""
def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if element in lst:
            return True
        return False

ls: list = [1, 2, 3]
print(find_element(ls,4))
print("---------------------------------------")

"""
Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni. 
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e l'elemento iniziale 
viene spostato alla fine della lista. Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore 
della lunghezza della lista.
"""
"""
La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.
"""
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers) 
    
numbers:list = [3,7,5,1]
print(calculate_average(numbers))
print("---------------------------------------")

"""
Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
La funzione ritorna "Accesso consentito" oppure "Accesso negato".
"""
def check_access(username: str, password: str, is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"

print("---------------------------------------")

"""
Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
"""    
def remove_duplicates(ls: list) -> list:
    ls1: list = copy.copy(ls)
    ls = list(set(ls))
    return ls 
print("---------------------------------------")

"""
Scrivi una funzione che, dato un numero intero, determina se è un "numero magico". Un numero magico è definito come un numero che contiene il numero 7.
"""
def is_magic_number(num: int) -> bool:
    if "7" in str(num):
        return True
    else:
        return False
print("---------------------------------------")

"""
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
"""
def check_parentheses(expression: str) -> bool:
    # cancella pass e scrivi il tuo codice
    ls1: list = []
    ls2: list = []
    for i in expression:
        if len(ls2) > len(ls1):
            return False
        if i == ")":
            ls2.append(i)
        elif i == "(":
            ls1.append(i)
        else:
            continue
    return True
print("---------------------------------------")

"""
Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
"""
def count_isolated(ls: list[int]) -> int:
    # cancella ... e definisci parametri e tipo di dato, successivamente cancella pass e scrivi il tuo codice
    ls1: list = []
    i: int = 0
    while i < len(ls):
        for e in ls:
            if i == 0 and e[i+1] != e[i]:
                ls1.append(i)
            elif i == len(ls)-1 and e[i-1] != e[i]:
                ls.append(i)
            elif e[i] != e[i-1] and e[i] != e[i+1]:
                ls.append(i)
            else:
                continue
    
    return len(ls1)