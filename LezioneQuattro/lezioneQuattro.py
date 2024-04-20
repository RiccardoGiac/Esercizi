#Riccardo Giacalone 19/04/24
#Esercizio funzione subtract

def subtract(x: int, y: int):
    return x - y

print(subtract(6,4))
print("-------------------------------------")

#Esercizio due: numero maggiore, minore o uguale a 5

def check_value(x: int):
    if x > 5:
        print(f"Il numero {x} è maggiore di 5")
    elif x == 5:
        print(f"Il numero {x} è uguale a 5")
    else:
        print(f"Il numero {x} è minore di 5")

check_value(4)
print("-------------------------------------")

#Esercizio tre: stringa con numero caratteri minore, maggiore o uguale a 10

def check_length(x: str):
    if len(x) > 10:
       print(f"Il numero di caratteri di {x} è maggiore di 10") 
    elif len(x) == 10:
        print(f"Il numero di caratteri di {x} è uguale a 10")
    else:
        print(f"Il numero di caratteri di {x} è minore di 10")

check_length("ciao")
check_length("ciao benvenuto nel mio programma")
check_length("ciaocomeva")
print("-------------------------------------")

#Esercizio quattro: funzione che printa elementi di una lista di numeri con un for loop

def print_numbers(l: list):
    for n in l:
        print(n)

lista = [3,4,1]
print_numbers(lista)
print("-------------------------------------")

#Esercizio cinque(Mi sono accorto ora che dalle slide in realtà sono un esercizio in meno quindi questo è il 4)
#Funzione che prende una lista di numeri come parametri. Per ogni numero printa se è minore maggiore o uguale a 5

def check_each(l: list):
    for i in l:
        if i > 5:
            print(f"Il numero {i} è maggiore di 5")
        elif i < 5:
            print(f"Il numero {i} è minore di 5")
        else:
            print(f"Il numero {i} è uguale a 5")

lista : list = [1,6,5] 
check_each(lista) 
print("-------------------------------------")  




        
