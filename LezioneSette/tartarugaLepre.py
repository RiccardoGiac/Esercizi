#Riccardo Giacalone
import random
#Dati
#Percorso: lista 70 quadrati
#Ogni azione avviene a intervalli di un secondo

#Tartaruga
# funzioni: Passo_veloce: (50% di prob): avanza 3 quadrati
#           Scivolata: (20% prob): arretra 6 quadrati(non sotto 1)
#           Passo lento: (30% prob): avanza 1 quadrato

#Lepre
#funzioni: Riposo(20%): non si muove
#          Grande balzo(20%): avanza di 9 quadrati
#          Grande scivolata(10%): arretra 12 quadrati
#          Piccolo balzo(30%): avanza 1 quadrato
#          Piccola scivolata(20%): arretra 2 quadrati    

percorso: list[str] = [" " for i in range(1,71)]


lepre: int = 1
tartaruga: int = 1
tempo: int = 0


def movimento_tartaruga(tartaruga:int)-> int:
    mov: int = random.randint(1,10)
    if mov <= 5:
        tartaruga += 3
        print(f"Passo veloce! +3 quadrati ({tartaruga})")
    if mov >=6 and mov <= 7 and tartaruga > 6:
        tartaruga -= 6
        print(f"Scivolata! -6 quadrati ({tartaruga})")
    elif mov >= 6 and mov <= 7 and tartaruga <= 6:
        tartaruga = 1
        print(f"Scivolata! torna al primo quadrato!")
    if mov >= 8 and mov <= 10:
        tartaruga += 1
        print(f"Passo lento! +1 quadrato ({tartaruga})")
    return tartaruga

def movimento_lepre(lepre: int):
    mov: int = random.randint(1,10)
    if mov == 1 and lepre > 12:
        lepre -= 12
        print(f"Grande Scivolata! -12 quadrati {lepre}")
    elif mov == 1 and lepre <= 12:
        lepre = 1
        print(f"Scivolata! Torna alla prima posizione")
    if mov > 1 and mov <= 3:
        print("Riposo! La lepre si mette a dormire e non avanza")
    if mov > 3 and mov <= 5:
        lepre += 9
        print(f"Grande balzo! +9 quadrati ({lepre})")
    if mov > 5 and mov <= 8:
        lepre += 1
        print(f"Piccolo balzo! +1 quadrato ({lepre})")
    if mov > 8 and mov <= 10 and lepre > 1:
        lepre -= 2
        print(f"Piccola scivolata! -1 quadrato")
    elif mov > 8 and mov <= 10 and lepre == 1:
        print(f"Piccola scivolata! Resta al primo quadrato!")
    return lepre

print("BANG!!!! AND THEY'RE OFF!!!")


while lepre <= len(percorso) and tartaruga <= len(percorso):

    
    
    print(f"Tempo: {tempo}\nLepre: ")
    lepre = movimento_lepre(lepre)
    print(f"\nTartaruga: ")
    tartaruga = movimento_tartaruga(tartaruga)
    
    tempo += 1
    if lepre < len(percorso) and tartaruga < len(percorso):
        if lepre == tartaruga:
            percorso[lepre] = "OUCH!!!"
        else:
            percorso[lepre] = "L"
            percorso[tartaruga] = "T"
        print(percorso)
        percorso[lepre] = " "
        percorso[tartaruga] = " "

if lepre > tartaruga:
    print("LA LEPRE HA VINTO!!!")
elif lepre < tartaruga:
    print("LA TARTARUGA HA VINTO!!!")
else:
    print("PAREGGIO!!!")



    