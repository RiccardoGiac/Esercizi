#Riccardo Giacalone 19/04/24
#Esercizio funzione subtract

def subtract(x: int, y: int) -> int:
    return x - y

print(subtract(6,4))
print("-------------------------------------")

#Esercizio due: numero maggiore, minore o uguale a 5

def check_value(x: int) -> int:
    if x > 5:
        print(f"Il numero {x} è maggiore di 5")
    elif x == 5:
        print(f"Il numero {x} è uguale a 5")
    else:
        print(f"Il numero {x} è minore di 5")

check_value(4)
